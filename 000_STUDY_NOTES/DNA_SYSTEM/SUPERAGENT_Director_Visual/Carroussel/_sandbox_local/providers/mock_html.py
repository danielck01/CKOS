from __future__ import annotations

from pathlib import Path


def render_slide(
    *,
    slide: dict,
    brand: dict,
    provider_cfg: dict | None = None,
    output_path: Path,
    run_date: str,
    tema: str,
    provider_label: str = "MOCK_HTML",
) -> None:
    """Gera um HTML placeholder sem dependência de PIL."""
    n = int(slide["n"])
    text_parts = slide.get("text", [])
    if not isinstance(text_parts, list) or not text_parts:
        raise ValueError(f"Slide {n} nao possui text[] valido")

    bg = brand.get("brand_color_light", "#F1ECE3")
    fg = brand.get("brand_color_dark", "#1B1411")
    accent = brand.get("brand_color_primary", "#EC5E26")

    html = _build_html(
        n=n,
        text_parts=text_parts,
        bg=bg,
        fg=fg,
        accent=accent,
        tema=tema,
        run_date=run_date,
        brand=brand,
        provider_label=provider_label,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Salva como HTML mas com extensão .png para compatibilidade com o runner
    # O runner espera .png, mas vamos gerar .html e depois renomear
    html_path = output_path.with_suffix(".html")
    html_path.write_text(html, encoding="utf-8")
    
    # Cria um arquivo .png vazio como placeholder (o runner espera .png)
    output_path.write_text(f"HTML placeholder: {html_path.name}", encoding="utf-8")


def _build_html(
    *,
    n: int,
    text_parts: list[str],
    bg: str,
    fg: str,
    accent: str,
    tema: str,
    run_date: str,
    brand: dict,
    provider_label: str,
) -> str:
    role = {
        1: "Capa",
        2: "Hook",
        3: "Mecanismo P1",
        4: "Mecanismo P2",
        5: "Prova",
        6: "Virada",
        7: "Aplicacao",
        8: "Direcao",
        9: "Assinatura + CTA",
    }.get(n, "Slide")

    brand_name = brand.get("brand_name", "Teste Local")
    brand_handle = brand.get("brand_handle", "@teste")

    text_html = "\n".join(f"<p>{part}</p>" for part in text_parts)

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Slide {n} - {role}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: {bg};
            color: {fg};
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }}
        .container {{
            width: 810px;
            max-width: 90%;
            padding: 40px;
            border: 3px solid {accent};
            background-color: {bg};
            border-radius: 8px;
        }}
        .header {{
            font-size: 18px;
            margin-bottom: 20px;
            color: {fg};
            opacity: 0.7;
        }}
        .role {{
            font-size: 24px;
            font-weight: bold;
            color: {accent};
            margin-bottom: 30px;
        }}
        .text {{
            font-size: 28px;
            line-height: 1.6;
            margin-bottom: 20px;
        }}
        .text p:first-child {{
            color: {accent};
            font-weight: bold;
            font-size: 36px;
        }}
        .footer {{
            margin-top: 40px;
            font-size: 16px;
            color: {fg};
            opacity: 0.6;
        }}
        .tema {{
            font-size: 14px;
            color: {fg};
            opacity: 0.5;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">{provider_label} | {run_date}</div>
        <div class="role">Slide {n} - {role}</div>
        <div class="tema">tema: {tema}</div>
        <div class="text">
            {text_html}
        </div>
        <div class="footer">
            {run_date.replace('-', '.')} · {brand_handle}<br>
            POR {brand_name} | {brand_handle} | {run_date[:4]}
        </div>
    </div>
</body>
</html>
"""
