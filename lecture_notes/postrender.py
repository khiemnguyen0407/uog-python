"""Quarto post-render script.

After Quarto has built the lecture notes, file every output into its own folder
and repair the "Other Formats" link in the HTML pages:

    lecture_notes/html/<name>.html   (link to ../pdf/<name>.pdf)
    lecture_notes/pdf/<name>.pdf
"""
import os
from pathlib import Path

root = Path.cwd()                       # Quarto runs this script from the project folder
html_dir, pdf_dir = root / "html", root / "pdf"

outputs = os.environ.get("QUARTO_PROJECT_OUTPUT_FILES", "").splitlines()

for name in outputs:
    path = root / name
    if not path.exists():
        continue

    if path.suffix == ".html":
        html_dir.mkdir(exist_ok=True)
        text = path.read_text(encoding="utf-8")
        # Quarto links to the PDF in the same folder; point it at the pdf folder instead.
        text = text.replace(f"href=\"{path.stem}.pdf\"", f"href=\"../pdf/{path.stem}.pdf\"")
        (html_dir / path.name).write_text(text, encoding="utf-8")
        path.unlink()
        print(f"  html/{path.name}")

    elif path.suffix == ".pdf":
        pdf_dir.mkdir(exist_ok=True)
        os.replace(path, pdf_dir / path.name)     # overwrites an older version, on every system
        print(f"  pdf/{path.name}")
