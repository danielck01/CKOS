from __future__ import annotations

import base64
import json
import mimetypes
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from PIL import Image, ImageDraw, ImageOps

from providers.mock import _draw_copy, _font


API_URL = "https://openrouter.ai/api/v1/chat/completions"


def render_slide(
    *,
    slide: dict,
    brand: dict,
    provider_cfg: dict | None = None,
    output_path: Path,
    run_date: str,
    tema: str,
) -> None:
    cfg = provider_cfg or {}
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY nao definido no ambiente")

    payload = _build_payload(slide=slide, brand=brand, cfg=cfg, tema=tema, run_date=run_date)
    response = _post_json(payload=payload, api_key=api_key, cfg=cfg)
    image_url = _first_image_url(response)
    image_bytes = _read_image_url(image_url, cfg=cfg)
    _write_png(
        image_bytes=image_bytes,
        output_path=output_path,
        brand=brand,
        cfg=cfg,
        slide=slide,
        run_date=run_date,
    )


def _build_payload(*, slide: dict, brand: dict, cfg: dict, tema: str, run_date: str) -> dict:
    model = cfg.get("image_model") or "google/gemini-3.1-flash-image-preview"
    modalities = cfg.get("modalities") or cfg.get("image_modalities") or ["image", "text"]
    image_config = cfg.get("image_config") or {}

    prompt = _build_prompt(slide=slide, brand=brand, cfg=cfg, tema=tema, run_date=run_date)
    content = [{"type": "text", "text": prompt}]
    content.extend(_image_content_entries(slide=slide))

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": content}],
        "modalities": modalities,
        "stream": False,
    }

    if image_config:
        payload["image_config"] = image_config

    seed = cfg.get("seed")
    if seed is not None:
        payload["seed"] = seed

    return payload


def _build_prompt(*, slide: dict, brand: dict, cfg: dict, tema: str, run_date: str) -> str:
    text_lines = "\n".join(f"- {item}" for item in slide.get("text", []))
    prompt = slide.get("prompt") or slide.get("visual_brief") or ""
    if cfg.get("local_text_overlay", True):
        prompt = slide.get("visual_brief") or prompt
        return (
            f"{prompt}\n\n"
            "=== TEXT RENDERING OVERRIDE ===\n"
            "Generate only the visual/background image. Do not render visible words, "
            "letters, captions, signatures, brand bars, watermarks, slide numbers, "
            "UI labels, or typography. The local runner will add exact text after "
            "generation.\n\n"
            "The copy below is semantic context only. Never draw it:\n"
            f"{text_lines}\n\n"
            f"Theme: {tema}\n"
            f"Brand colors to respect visually: primary {brand.get('brand_color_primary')}, "
            f"dark {brand.get('brand_color_dark')}, light {brand.get('brand_color_light')}\n"
        )

    allowed_visible_text = _allowed_visible_text(slide=slide, brand=brand, run_date=run_date)
    return (
        f"{prompt}\n\n"
        "=== RUNNER CONTRACT ===\n"
        f"Date: {run_date}\n"
        f"Theme: {tema}\n"
        f"Brand: {brand.get('brand_name')} ({brand.get('brand_handle')})\n"
        f"Brand colors: primary {brand.get('brand_color_primary')}, "
        f"dark {brand.get('brand_color_dark')}, light {brand.get('brand_color_light')}\n"
        "Render all slide text exactly as listed below. Do not paraphrase.\n"
        f"{text_lines}\n\n"
        "=== VISIBLE TEXT ALLOWLIST ===\n"
        "Only render these visible text strings. Do not render labels, implementation notes, "
        "font sizes, opacity notes, px values, markdown labels, or instruction words.\n"
        f"{allowed_visible_text}\n\n"
        "Forbidden visible text examples: DETAIL SIGNATURE, TYPOGRAPHY LOCK, 12px, 55%, "
        "opacidade, signature, prompt, visual brief, RUNNER CONTRACT.\n"
    )


def _allowed_visible_text(*, slide: dict, brand: dict, run_date: str) -> str:
    visible = [str(item) for item in slide.get("text", [])]
    if int(slide.get("n", 0)) == 1:
        visible.append(f"POR {brand.get('brand_name')} | {brand.get('brand_handle')} | {run_date[:4]}")
    if int(slide.get("n", 0)) == 9 and not brand.get("brand_has_logo", False):
        visible.append(str(brand.get("brand_name")))
    visible.append(f"{run_date.replace('-', '.')} · {brand.get('brand_handle')}")
    return "\n".join(f"- {item}" for item in visible if item)


def _image_content_entries(*, slide: dict) -> list[dict]:
    entries = []
    for image_ref in slide.get("input_images", []) + slide.get("reference_images", []):
        entries.append(
            {
                "type": "image_url",
                "image_url": {"url": _to_image_url(image_ref)},
            }
        )
    return entries


def _to_image_url(image_ref: str | dict) -> str:
    if isinstance(image_ref, dict):
        image_ref = image_ref.get("url") or image_ref.get("path")
    if not image_ref:
        raise ValueError("Referencia de imagem vazia")

    parsed = urlparse(str(image_ref))
    if parsed.scheme in {"http", "https", "data"}:
        return str(image_ref)

    path = Path(str(image_ref)).expanduser()
    if not path.exists():
        raise FileNotFoundError(f"Imagem de referencia nao encontrada: {path}")

    mime_type = mimetypes.guess_type(path.name)[0] or "image/png"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def _post_json(*, payload: dict, api_key: str, cfg: dict) -> dict:
    body = json.dumps(payload).encode("utf-8")
    request = Request(
        API_URL,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": cfg.get("http_referer", "https://ckos.local"),
            "X-Title": cfg.get("x_title", "CKOS Carroussel Sandbox"),
        },
    )

    timeout = int(cfg.get("timeout_seconds", 180))
    try:
        with urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        message = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenRouter HTTP {exc.code}: {message}") from exc
    except URLError as exc:
        raise RuntimeError(f"Falha de rede OpenRouter: {exc.reason}") from exc


def _first_image_url(response: dict) -> str:
    choices = response.get("choices") or []
    if not choices:
        raise RuntimeError(f"OpenRouter nao retornou choices: {response}")

    message = choices[0].get("message") or {}
    images = message.get("images") or []
    if not images:
        content = message.get("content", "")
        raise RuntimeError(f"OpenRouter nao retornou message.images. Conteudo: {content!r}")

    image_url = images[0].get("image_url") or {}
    url = image_url.get("url")
    if not url:
        raise RuntimeError(f"Imagem sem image_url.url: {images[0]}")
    return url


def _read_image_url(image_url: str, *, cfg: dict) -> bytes:
    if image_url.startswith("data:"):
        return _decode_data_url(image_url)

    parsed = urlparse(image_url)
    if parsed.scheme not in {"http", "https"}:
        raise ValueError(f"Formato de imagem nao suportado: {image_url[:40]}")

    timeout = int(cfg.get("timeout_seconds", 180))
    with urlopen(image_url, timeout=timeout) as response:
        return response.read()


def _decode_data_url(data_url: str) -> bytes:
    header, _, payload = data_url.partition(",")
    if ";base64" not in header or not payload:
        raise ValueError("Data URL de imagem invalida")
    return base64.b64decode(payload)


def _write_png(*, image_bytes: bytes, output_path: Path, brand: dict, cfg: dict, slide: dict, run_date: str) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = output_path.with_suffix(".provider-output.tmp")
    temp_path.write_bytes(image_bytes)

    try:
        with Image.open(temp_path) as image:
            image = image.convert("RGB")
            if cfg.get("normalize_output", True):
                image = _normalize_image(image=image, brand=brand, cfg=cfg)
            if cfg.get("local_text_overlay", True):
                image = _overlay_local_text(image=image, slide=slide, brand=brand, run_date=run_date)
            image.save(output_path, format="PNG")
    finally:
        temp_path.unlink(missing_ok=True)


def _normalize_image(*, image: Image.Image, brand: dict, cfg: dict) -> Image.Image:
    width = int(cfg.get("target_width", 810))
    height = int(cfg.get("target_height", 1080))
    bg = _hex_to_rgb(brand.get("brand_color_light", "#F1ECE3"))

    contained = ImageOps.contain(image, (width, height), method=Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (width, height), bg)
    left = (width - contained.width) // 2
    top = (height - contained.height) // 2
    canvas.paste(contained, (left, top))
    return canvas


def _overlay_local_text(*, image: Image.Image, slide: dict, brand: dict, run_date: str) -> Image.Image:
    canvas = image.convert("RGBA")
    bg = _hex_to_rgb(brand.get("brand_color_light", "#F1ECE3"))
    fg = _hex_to_rgb(brand.get("brand_color_dark", "#1B1411"))
    accent = _hex_to_rgb(brand.get("brand_color_primary", "#EC5E26"))

    panel = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    panel_draw = ImageDraw.Draw(panel)
    panel_draw.rounded_rectangle((34, 132, canvas.width - 34, 952), radius=18, fill=(*bg, 244))
    canvas = Image.alpha_composite(canvas, panel)

    draw = ImageDraw.Draw(canvas)
    text_parts = [str(item) for item in slide.get("text", [])]
    if int(slide.get("n", 0)) == 9 and not brand.get("brand_has_logo", False):
        text_parts = [str(brand.get("brand_name", ""))] + text_parts

    if int(slide.get("n", 0)) == 1:
        brand_bar = f"POR {brand.get('brand_name')} | {brand.get('brand_handle')} | {run_date[:4]}"
        _draw_chip_text(draw=draw, xy=(54, 42), text=brand_bar, font=_font(24), fg=fg, bg=bg)

    _draw_copy(draw, text_parts, fg, accent)
    _draw_chip_text(
        draw=draw,
        xy=(54, 994),
        text=f"{run_date.replace('-', '.')} · {brand.get('brand_handle')}",
        font=_font(22),
        fg=fg,
        bg=bg,
    )
    return canvas.convert("RGB")


def _draw_chip_text(
    *,
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font,
    fg: tuple[int, int, int],
    bg: tuple[int, int, int],
) -> None:
    x, y = xy
    bbox = draw.textbbox((x, y), text, font=font)
    pad_x = 10
    pad_y = 6
    rect = (bbox[0] - pad_x, bbox[1] - pad_y, bbox[2] + pad_x, bbox[3] + pad_y)
    draw.rounded_rectangle(rect, radius=8, fill=(*bg, 232))
    draw.text((x, y), text, fill=fg, font=font)


def _hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.strip().lstrip("#")
    return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))
