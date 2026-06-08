from __future__ import annotations

import argparse
import shutil
import time
from datetime import datetime
from pathlib import Path
from typing import Callable

from utils.config import load_brand, load_render_provider, load_tema
from utils.state import default_date, ensure_output_dirs, load_render_requests, resolve_state_paths


RenderFn = Callable[..., None]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Carroussel sandbox Teste 0 runner")
    parser.add_argument("--date", default=default_date(), help="Data do estado, no formato YYYY-MM-DD")
    parser.add_argument("--slide", type=int, choices=range(1, 10), help="Re-renderiza apenas um slide (1-9)")
    parser.add_argument("--tema", help="Override do tema lido de input/tema.txt")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parent

    started_at = datetime.now().astimezone()
    start_perf = time.perf_counter()
    log_lines = [f"START {started_at.isoformat(timespec='seconds')}"]

    paths = resolve_state_paths(root, args.date)
    ensure_output_dirs(paths)

    brand = load_brand(root)
    provider_cfg = load_render_provider(root)
    tema = load_tema(root, args.tema)
    slides = load_render_requests(paths)

    provider_name = provider_cfg.get("provider")
    render_slide = load_provider(provider_name)

    selected = [slide for slide in slides if args.slide is None or int(slide.get("n", 0)) == args.slide]
    if args.slide is not None and not selected:
        raise ValueError(f"Slide {args.slide} nao encontrado em {paths.render_requests}")

    ok_count = 0
    fail_count = 0

    for slide in selected:
        slide_start = time.perf_counter()
        slide_n = int(slide["n"])
        filename = f"slide-{slide_n:02d}.png"
        state_path = paths.slides_dir / filename
        output_path = paths.output_dir / filename
        try:
            render_slide(
                slide=slide,
                brand=brand,
                provider_cfg=provider_cfg,
                output_path=state_path,
                run_date=args.date,
                tema=tema,
            )
            shutil.copy2(state_path, output_path)
        except Exception as exc:
            fail_count += 1
            elapsed_ms = round((time.perf_counter() - slide_start) * 1000)
            log_lines.append(f"FAIL slide-{slide_n:02d} ({exc}; {elapsed_ms}ms)")
            continue

        ok_count += 1
        elapsed_ms = round((time.perf_counter() - slide_start) * 1000)
        log_lines.append(f"OK slide-{slide_n:02d} ({elapsed_ms}ms)")

    total_ms = round((time.perf_counter() - start_perf) * 1000)
    log_lines.append(f"TOTAL {total_ms}ms")
    log_lines.append(_summary(ok_count, fail_count))
    paths.logs.write_text("\n".join(log_lines) + "\n", encoding="utf-8")

    print("\n".join(log_lines))
    return 0 if fail_count == 0 else 1


def load_provider(provider_name: str | None) -> RenderFn:
    if provider_name == "mock":
        from providers.mock import render_slide

        return render_slide
    if provider_name == "mock_html":
        from providers.mock_html import render_slide

        return render_slide
    if provider_name == "openrouter":
        from providers.openrouter import render_slide

        return render_slide
    raise ValueError(f"Provider desconhecido: {provider_name}")


def _summary(ok_count: int, fail_count: int) -> str:
    if fail_count == 0:
        return f"SUMMARY {ok_count}/{ok_count} OK"

    total = ok_count + fail_count
    plural = "falhas" if fail_count != 1 else "falha"
    return f"SUMMARY {ok_count}/{total} OK - {fail_count} {plural}"


if __name__ == "__main__":
    raise SystemExit(main())
