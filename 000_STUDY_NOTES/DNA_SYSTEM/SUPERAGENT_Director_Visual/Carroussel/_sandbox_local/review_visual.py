from __future__ import annotations

import argparse
import base64
import json
import os
import time
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from utils.config import load_json
from utils.state import default_date, resolve_state_paths


API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_REVIEW_MODEL = "google/gemini-3.5-flash"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="AI visual review for generated carousel slides")
    parser.add_argument("--date", default=default_date(), help="State date, YYYY-MM-DD")
    parser.add_argument("--slide", type=int, choices=range(1, 10), help="Review one slide only")
    parser.add_argument("--model", default=DEFAULT_REVIEW_MODEL, help="OpenRouter vision model")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY nao definido no ambiente")

    root = Path(__file__).resolve().parent
    paths = resolve_state_paths(root, args.date)
    requests_payload = load_json(paths.render_requests)
    slides = requests_payload.get("slides", [])
    selected = [slide for slide in slides if args.slide is None or int(slide["n"]) == args.slide]

    started_at = datetime.now().astimezone().isoformat(timespec="seconds")
    review_items = []

    for slide in selected:
        slide_n = int(slide["n"])
        image_path = paths.output_dir / f"slide-{slide_n:02d}.png"
        if not image_path.exists():
            raise FileNotFoundError(f"Slide nao encontrado: {image_path}")

        started = time.perf_counter()
        review_text = review_slide(
            api_key=api_key,
            model=args.model,
            slide=slide,
            image_path=image_path,
        )
        elapsed_ms = round((time.perf_counter() - started) * 1000)
        review_items.append(
            {
                "slide": slide_n,
                "image": str(image_path.relative_to(root)).replace("\\", "/"),
                "elapsed_ms": elapsed_ms,
                "review": review_text,
            }
        )
        print(f"OK review slide-{slide_n:02d} ({elapsed_ms}ms)")

    report = {
        "started_at": started_at,
        "date": args.date,
        "model": args.model,
        "items": review_items,
    }
    report_path = paths.state_dir / "visual-review.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown_report(paths.state_dir / "visual-review.md", report)
    print(f"WROTE {report_path}")
    return 0


def review_slide(*, api_key: str, model: str, slide: dict, image_path: Path) -> str:
    expected_text = "\n".join(f"- {item}" for item in slide.get("text", []))
    prompt = (
        "You are a PMO visual QA reviewer for an Instagram carousel.\n"
        "Inspect the attached slide image and compare it against the expected copy.\n"
        "Return concise Portuguese notes with these fields:\n"
        "STATUS: APPROVE, REVIEW, or FAIL\n"
        "COPY: exact / minor issue / major issue\n"
        "LEGIBILITY: pass / issue\n"
        "VISUAL: pass / issue\n"
        "NOTES: one short paragraph\n\n"
        "Expected copy:\n"
        f"{expected_text}\n"
    )

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_to_data_url(image_path)}},
                ],
            }
        ],
        "modalities": ["text"],
        "stream": False,
    }
    response = post_json(payload=payload, api_key=api_key)
    choices = response.get("choices") or []
    if not choices:
        raise RuntimeError(f"OpenRouter nao retornou choices: {response}")
    message = choices[0].get("message") or {}
    content = message.get("content")
    if not content:
        raise RuntimeError(f"OpenRouter nao retornou content: {response}")
    return content


def image_to_data_url(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def post_json(*, payload: dict, api_key: str) -> dict:
    request = Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://ckos.local",
            "X-Title": "CKOS Carroussel Visual Review",
        },
    )
    try:
        with urlopen(request, timeout=180) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        message = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenRouter HTTP {exc.code}: {message}") from exc
    except URLError as exc:
        raise RuntimeError(f"Falha de rede OpenRouter: {exc.reason}") from exc


def write_markdown_report(path: Path, report: dict) -> None:
    lines = [
        "# Visual Review",
        "",
        f"- date: {report['date']}",
        f"- model: {report['model']}",
        f"- started_at: {report['started_at']}",
        "",
    ]
    for item in report["items"]:
        lines.extend(
            [
                f"## Slide {item['slide']:02d}",
                "",
                f"- image: `{item['image']}`",
                f"- elapsed_ms: {item['elapsed_ms']}",
                "",
                item["review"].strip(),
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
