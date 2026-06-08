from __future__ import annotations

from pathlib import Path
from textwrap import wrap
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont


WIDTH = 810
HEIGHT = 1080
MARGIN_X = 64
HEADER_Y = 44
BODY_TOP = 190
FOOTER_Y = 1012
BODY_BOTTOM = 925

ROLE_BY_SLIDE = {
    1: "Capa",
    2: "Hook",
    3: "Mecanismo P1",
    4: "Mecanismo P2",
    5: "Prova",
    6: "Virada",
    7: "Aplicacao",
    8: "Direcao",
    9: "Assinatura + CTA",
}


def render_slide(
    *,
    slide: dict,
    brand: dict,
    provider_cfg: dict | None = None,
    output_path: Path,
    run_date: str,
    tema: str,
    provider_label: str = "MOCK",
) -> None:
    aspect_ratio = slide.get("aspect_ratio", "3:4")
    if aspect_ratio != "3:4":
        raise ValueError(f"Slide {slide.get('n')} usa aspect_ratio={aspect_ratio}; esperado 3:4")

    n = int(slide["n"])
    text_parts = slide.get("text")
    if not isinstance(text_parts, list) or not text_parts:
        raise ValueError(f"Slide {n} nao possui text[] valido")

    bg = _hex_to_rgb(brand.get("brand_color_light", "#F1ECE3"))
    fg = _hex_to_rgb(brand.get("brand_color_dark", "#1B1411"))
    accent = _hex_to_rgb(brand.get("brand_color_primary", "#EC5E26"))

    image = Image.new("RGB", (WIDTH, HEIGHT), bg)
    draw = ImageDraw.Draw(image)

    _draw_paper_grain(draw, bg)
    _draw_frame(draw, accent)

    role = ROLE_BY_SLIDE.get(n, "Slide")
    header = f"Slide {n} - {role} | {provider_label} | {run_date}"
    footer = f"{run_date.replace('-', '.')} | {brand.get('brand_handle', '@teste')}"

    header_font = _font(28, bold=True)
    footer_font = _font(22)

    draw.text((MARGIN_X, HEADER_Y), header, fill=fg, font=header_font)
    _draw_footer(draw, footer, fg, footer_font)
    _draw_tema(draw, tema, fg)
    _draw_copy(draw, text_parts, fg, accent)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path, format="PNG")


def _draw_copy(draw: ImageDraw.ImageDraw, text_parts: list[str], fg: tuple[int, int, int], accent: tuple[int, int, int]) -> None:
    title = str(text_parts[0])
    body_parts = [str(item) for item in text_parts[1:]]

    for title_size, body_size in _font_size_candidates():
        title_font = _font(title_size, bold=True)
        body_font = _font(body_size)
        title_lines = _wrap_to_width(draw, title, title_font, WIDTH - (MARGIN_X * 2))
        body_lines_by_part = [
            _wrap_to_width(draw, part, body_font, WIDTH - (MARGIN_X * 2))
            for part in body_parts
        ]

        title_h = _line_height(title_font)
        body_h = _line_height(body_font)
        total_h = (len(title_lines) * title_h) + 24
        for lines in body_lines_by_part:
            total_h += len(lines) * body_h + 28

        if total_h <= BODY_BOTTOM - BODY_TOP:
            break
    else:
        title_font = _font(34, bold=True)
        body_font = _font(25)
        title_lines = _wrap_to_width(draw, title, title_font, WIDTH - (MARGIN_X * 2))
        body_lines_by_part = [
            _wrap_to_width(draw, part, body_font, WIDTH - (MARGIN_X * 2))
            for part in body_parts
        ]
        title_h = _line_height(title_font)
        body_h = _line_height(body_font)

    y = BODY_TOP
    for line in title_lines:
        draw.text((MARGIN_X, y), line, fill=accent, font=title_font)
        y += title_h

    y += 28
    for index, lines in enumerate(body_lines_by_part):
        for line in lines:
            draw.text((MARGIN_X, y), line, fill=fg, font=body_font)
            y += body_h
        if index != len(body_lines_by_part) - 1:
            y += 30


def _draw_footer(draw: ImageDraw.ImageDraw, footer: str, fg: tuple[int, int, int], font: ImageFont.ImageFont) -> None:
    muted = _blend(fg, (241, 236, 227), 0.55)
    draw.text((MARGIN_X, FOOTER_Y), footer, fill=muted, font=font)


def _draw_tema(draw: ImageDraw.ImageDraw, tema: str, fg: tuple[int, int, int]) -> None:
    if not tema:
        return
    font = _font(18)
    muted = _blend(fg, (241, 236, 227), 0.45)
    label = "tema: " + tema
    lines = _wrap_to_width(draw, label, font, WIDTH - (MARGIN_X * 2))
    y = 122
    for line in lines[:2]:
        draw.text((MARGIN_X, y), line, fill=muted, font=font)
        y += _line_height(font)


def _draw_frame(draw: ImageDraw.ImageDraw, accent: tuple[int, int, int]) -> None:
    draw.rectangle((28, 28, WIDTH - 29, HEIGHT - 29), outline=_blend(accent, (241, 236, 227), 0.65), width=3)
    draw.rectangle((MARGIN_X, 102, MARGIN_X + 72, 110), fill=accent)


def _draw_paper_grain(draw: ImageDraw.ImageDraw, bg: tuple[int, int, int]) -> None:
    # Deterministic light texture so the placeholder is not visually flat.
    grain = _blend((0, 0, 0), bg, 0.04)
    for y in range(0, HEIGHT, 18):
        draw.line((0, y, WIDTH, y), fill=grain, width=1)


def _font_size_candidates() -> Iterable[tuple[int, int]]:
    candidates = [
        (60, 38),
        (56, 36),
        (52, 34),
        (48, 32),
        (44, 30),
        (40, 28),
        (36, 26),
    ]
    yield from candidates


def _wrap_to_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    words = text.split()
    if not words:
        return [""]

    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if draw.textlength(candidate, font=font) <= max_width:
            current = candidate
            continue

        if current:
            lines.append(current)
            current = ""

        if draw.textlength(word, font=font) <= max_width:
            current = word
        else:
            chunks = _break_long_word(draw, word, font, max_width)
            lines.extend(chunks[:-1])
            current = chunks[-1]

    if current:
        lines.append(current)
    return lines


def _break_long_word(draw: ImageDraw.ImageDraw, word: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    chunks: list[str] = []
    current = ""
    for char in word:
        candidate = current + char
        if draw.textlength(candidate, font=font) <= max_width:
            current = candidate
            continue
        if current:
            chunks.append(current)
        current = char
    if current:
        chunks.append(current)
    return chunks or [word]


def _font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    names = [
        "arialbd.ttf" if bold else "arial.ttf",
        "segoeuib.ttf" if bold else "segoeui.ttf",
        "calibrib.ttf" if bold else "calibri.ttf",
        "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf",
    ]
    for name in names:
        try:
            return ImageFont.truetype(name, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def _line_height(font: ImageFont.ImageFont) -> int:
    bbox = font.getbbox("Ag")
    return (bbox[3] - bbox[1]) + 12


def _hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.strip().lstrip("#")
    if len(value) != 6:
        raise ValueError(f"Cor invalida: #{value}")
    return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))


def _blend(fg: tuple[int, int, int], bg: tuple[int, int, int], alpha: float) -> tuple[int, int, int]:
    return tuple(round((fg_part * alpha) + (bg_part * (1 - alpha))) for fg_part, bg_part in zip(fg, bg))
