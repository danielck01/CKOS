from __future__ import annotations

from dataclasses import dataclass
from datetime import date as date_type
from pathlib import Path

from utils.config import load_json


@dataclass(frozen=True)
class StatePaths:
    date: str
    state_dir: Path
    output_dir: Path
    slides_dir: Path
    render_requests: Path
    logs: Path


def default_date() -> str:
    return date_type.today().isoformat()


def resolve_state_paths(root: Path, run_date: str) -> StatePaths:
    state_dir = root / "state" / run_date
    output_dir = root / "output" / run_date
    slides_dir = state_dir / "slides"

    return StatePaths(
        date=run_date,
        state_dir=state_dir,
        output_dir=output_dir,
        slides_dir=slides_dir,
        render_requests=state_dir / "render-requests.json",
        logs=state_dir / "logs.txt",
    )


def ensure_output_dirs(paths: StatePaths) -> None:
    paths.slides_dir.mkdir(parents=True, exist_ok=True)
    paths.output_dir.mkdir(parents=True, exist_ok=True)


def load_render_requests(paths: StatePaths) -> list[dict]:
    payload = load_json(paths.render_requests)
    slides = payload.get("slides")
    if not isinstance(slides, list):
        raise ValueError(f"Campo 'slides' ausente ou invalido em {paths.render_requests}")
    return slides

