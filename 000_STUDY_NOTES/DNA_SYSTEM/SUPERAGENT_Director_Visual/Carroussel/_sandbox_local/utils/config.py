from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_brand(root: Path) -> dict[str, Any]:
    return load_json(root / "config" / "brand.json")


def load_render_provider(root: Path) -> dict[str, Any]:
    return load_json(root / "config" / "render-provider.json")


def load_tema(root: Path, override: str | None = None) -> str:
    if override is not None:
        return override.strip()

    tema_path = root / "input" / "tema.txt"
    return tema_path.read_text(encoding="utf-8").strip()

