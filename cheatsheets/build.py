"""Génère les fiches A4 (une par chapitre) à partir des sources Markdown de src/.

Usage :
    python cheatsheets/build.py              # toutes les fiches, puis le recueil
    python cheatsheets/build.py ch05 ch12    # seulement certaines (le recueil est mis à jour)
    python cheatsheets/build.py --png        # ajoute un aperçu PNG dans build/

Les fiches sont écrites dans pdf/chNN.pdf ; le recueil pdf/fiches-de-revision.pdf
les réunit toutes, avec un signet par chapitre.

Chaque fiche est rendue en HTML (template/style.css), avec le même corps de
texte de 7 pt pour toutes, puis imprimée en PDF par Edge ou Chrome sans
interface. Le script échoue si une fiche dépasse une page A4 ou si un texte du
PDF est composé sous 7 pt.
"""

from __future__ import annotations

import argparse
import html
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml
from markdown_it import MarkdownIt
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT / "pdf"
BUILD = ROOT / "build"
CSS = ROOT / "template" / "style.css"
COMBINED = OUT / "fiches-de-revision.pdf"

FONT_PT = 7.0
BOOK = "De l'assistant à l'agent"

BOX_CLASSES = {
    "à retenir": "retenir",
    "pièges": "pieges",
    "critères": "criteres",
}

FIT_SCRIPT = """
<script>
(function () {
  const main = document.querySelector('main');
  const root = document.documentElement;
  const overflows = () => main.scrollWidth > main.clientWidth + 1 || main.scrollHeight > main.clientHeight + 1;
  root.style.setProperty('--fs', '%(size)spt');
  document.title = 'FIT|%(size)s|' + (overflows() ? 'overflow' : 'ok');
})();
</script>
"""

md = MarkdownIt("commonmark", {"typographer": False}).enable("table")


def find_browser() -> str:
    candidates = [
        os.environ.get("CHEATSHEET_BROWSER"),
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        shutil.which("msedge"),
        shutil.which("microsoft-edge"),
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    for c in candidates:
        if c and Path(c).exists():
            return c
    sys.exit("Navigateur introuvable : définissez CHEATSHEET_BROWSER (Edge ou Chrome).")


def parse_source(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        sys.exit(f"{path.name} : en-tête YAML manquant")
    return yaml.safe_load(m.group(1)), m.group(2)


def french_spacing(fragment: str) -> str:
    """Espaces insécables avant : ; ? ! » et après «, hors <code> et <pre>."""
    parts = re.split(r"(<pre>.*?</pre>|<code>.*?</code>|<[^>]+>)", fragment, flags=re.S)
    for i, part in enumerate(parts):
        if part.startswith("<"):
            continue
        part = re.sub(r" ([:;?!»])", "\u00a0\\1", part)
        parts[i] = re.sub(r"« ", "«\u00a0", part)
    return "".join(parts)


def render_sections(body: str) -> str:
    chunks = re.split(r"^## +", body, flags=re.M)
    out = []
    if chunks[0].strip():
        out.append(f'<section>{md.render(chunks[0])}</section>')
    for chunk in chunks[1:]:
        heading, _, content = chunk.partition("\n")
        heading = heading.strip()
        cls = next((c for k, c in BOX_CLASSES.items() if heading.lower().startswith(k)), None)
        css = f' class="box {cls}"' if cls else ""
        out.append(
            f"<section{css}><h2>{md.renderInline(heading)}</h2>{md.render(content)}</section>"
        )
    return french_spacing("\n".join(out))


def build_html(meta: dict, body: str) -> str:
    num = meta["numero"]
    css = CSS.read_text(encoding="utf-8")
    return f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><title>Chapitre {num}</title>
<style>{css}</style></head>
<body><div class="page">
<header>
  <div class="num">{num}</div>
  <div class="titles">
    <div class="partie">{french_spacing(html.escape(meta['partie'], quote=False))}</div>
    <h1>{french_spacing(html.escape(meta['titre'], quote=False))}</h1>
  </div>
  <div class="meta">Source : {html.escape(meta['source'])}</div>
</header>
<main>
{render_sections(body)}
</main>
<footer><span>{BOOK} — fiche du chapitre {num}</span><span>Fiche de révision : condense le chapitre, ne le remplace pas</span></footer>
</div>
{FIT_SCRIPT % {'size': FONT_PT}}
</body></html>
"""


def run_browser(browser: str, args: list[str]) -> None:
    with tempfile.TemporaryDirectory() as profile:
        cmd = [
            browser,
            "--headless=new",
            "--disable-gpu",
            "--no-first-run",
            "--disable-extensions",
            f"--user-data-dir={profile}",
            *args,
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)


def min_font_size(reader: PdfReader) -> float:
    sizes: list[float] = []

    def visitor(text, cm, tm, font_dict, font_size):
        if not text.strip():
            return
        a, b, c, d = (tm[0] * cm[0] + tm[1] * cm[2], tm[0] * cm[1] + tm[1] * cm[3],
                      tm[2] * cm[0] + tm[3] * cm[2], tm[2] * cm[1] + tm[3] * cm[3])
        scale = math.sqrt(abs(a * d - b * c))
        sizes.append(font_size * scale)

    for page in reader.pages:
        page.extract_text(visitor_text=visitor)
    return min(sizes) if sizes else 0.0


def build_one(src: Path, browser: str, png: bool) -> list[str]:
    meta, body = parse_source(src)
    stem = src.stem
    html_path = BUILD / f"{stem}.html"
    html_path.write_text(build_html(meta, body), encoding="utf-8")
    pdf_path = OUT / f"{stem}.pdf"
    tmp_pdf = BUILD / f"{stem}.raw.pdf"
    run_browser(browser, ["--no-pdf-header-footer", f"--print-to-pdf={tmp_pdf}", html_path.as_uri()])

    reader = PdfReader(tmp_pdf)
    title = (reader.metadata or {}).get("/Title", "")
    errors = []
    fit = title.split("|") if title.startswith("FIT|") else ["", "?", "?"]
    if fit[2] != "ok":
        errors.append(f"contenu trop long pour une page à {FONT_PT} pt")
    if len(reader.pages) != 1:
        errors.append(f"{len(reader.pages)} pages au lieu d'une")
    box = reader.pages[0].mediabox
    if abs(float(box.width) - 595.3) > 2 or abs(float(box.height) - 841.9) > 2:
        errors.append(f"format {float(box.width):.0f}x{float(box.height):.0f} pt, pas A4")
    smallest = min_font_size(reader)
    if smallest < FONT_PT - 0.05:
        errors.append(f"texte à {smallest:.2f} pt (< {FONT_PT} pt)")

    writer = PdfWriter(clone_from=reader)
    writer.add_metadata({
        "/Title": f"{BOOK} — Fiche du chapitre {meta['numero']} : {meta['titre']}",
        "/Author": "ai-generated-books",
        "/Subject": meta["partie"],
    })
    with open(pdf_path, "wb") as fh:
        writer.write(fh)
    tmp_pdf.unlink()

    if png:
        run_browser(browser, ["--hide-scrollbars", "--window-size=794,1123",
                              f"--screenshot={BUILD / (stem + '.png')}", html_path.as_uri()])

    status = "OK " if not errors else "ERR"
    print(f"{status} {stem}: corps {fit[1]} pt, plus petit texte {smallest:.2f} pt, "
          f"{len(reader.pages)} page(s)" + ("" if not errors else " — " + "; ".join(errors)))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("chapitres", nargs="*", help="ex. ch01 ch12 (défaut : tous)")
    parser.add_argument("--png", action="store_true", help="produit aussi un aperçu PNG dans build/")
    args = parser.parse_args()

    BUILD.mkdir(exist_ok=True)
    OUT.mkdir(exist_ok=True)
    sources = sorted(SRC.glob("ch*.md"))
    if args.chapitres:
        wanted = set(args.chapitres)
        sources = [s for s in sources if s.stem.split("-")[0] in wanted or s.stem in wanted]
    if not sources:
        sys.exit("Aucune source trouvée.")

    browser = find_browser()
    failures = sum(bool(build_one(s, browser, args.png)) for s in sources)
    print(f"{len(sources) - failures}/{len(sources)} fiche(s) conformes.")
    if not failures:
        build_combined()
    return 1 if failures else 0


def build_combined() -> None:
    """Réunit toutes les fiches de pdf/ dans un seul PDF, avec un signet par chapitre."""
    writer = PdfWriter()
    count = 0
    for src in sorted(SRC.glob("ch*.md")):
        pdf = OUT / f"{src.stem}.pdf"
        if not pdf.exists():
            continue
        meta, _ = parse_source(src)
        writer.append(str(pdf), outline_item=f"Chapitre {meta['numero']} — {meta['titre']}")
        count += 1
    writer.add_metadata({"/Title": f"{BOOK} — Fiches de révision", "/Author": "ai-generated-books"})
    with open(COMBINED, "wb") as fh:
        writer.write(fh)
    print(f"Recueil : {COMBINED.relative_to(ROOT.parent)} ({count} page(s)).")


if __name__ == "__main__":
    sys.exit(main())
