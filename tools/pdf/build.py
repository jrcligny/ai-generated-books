"""Assemble le livre en un seul PDF : pandoc -> HTML -> Edge headless (puppeteer) -> PDF.

Deux passes : la première sert à repérer la page de chaque partie / chapitre,
la seconde injecte ces numéros dans la table des matières.

Usage : python build.py [dossier_du_livre] [sortie.pdf]
"""
import html, json, re, subprocess, sys, unicodedata
from pathlib import Path
import pypandoc
from pypdf import PdfReader

BUILD = Path(__file__).resolve().parent
BOOK = Path(sys.argv[1]) if len(sys.argv) > 1 else BUILD.parents[1] / "construire-agent-conversationnel"
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else BUILD / "de-l-assistant-a-l-agent.pdf"
README = (BOOK / "README.md").read_text(encoding="utf-8")
TITLE, SUBTITLE = "De l'assistant à l'agent", "Anatomie d'un agent conversationnel"

files = re.findall(r"^- \[[^\]]+\]\((\d\d-[^)]+\.md)\)", README, re.M)
assert len(files) == 26, files

chunks, toc = [], []
for i, name in enumerate(files):
    body = pypandoc.convert_file(
        str(BOOK / name), "html5", format="markdown-smart+autolink_bare_uris",
        extra_args=["--section-divs", f"--id-prefix=f{i:02d}-", "--wrap=none"],
    )
    kind = "part" if "partie" in name else "chap"
    m = re.search(r'<section id="([^"]+)" class="level1">\s*<h1>(.*?)</h1>', body, re.S)
    assert m, name
    body = body.replace('class="level1"', f'class="level1 {kind}"', 1)
    if " — " in m.group(2):
        label, title = m.group(2).split(" — ", 1)
        body = body.replace(f"<h1>{m.group(2)}</h1>",
                            f'<h1><span class="label">{label}</span><span class="sep"> — </span>{title}</h1>', 1)
    toc.append({"id": m.group(1), "html": m.group(2), "kind": kind,
                "text": html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))})
    chunks.append(body)

mermaid_js = (BUILD / "node_modules/mermaid/dist/mermaid.min.js").as_uri()
SCRIPT = f'<script src="{mermaid_js}"></script><script src="calib.js"></script>'


def render(pages):
    items = "\n".join(
        f'<li class="{t["kind"]}"><a class="lbl" href="#{t["id"]}">{t["html"]}</a>'
        f'<span class="dots"></span><a class="pg" href="#{t["id"]}">{pages.get(t["id"], "00")}</a></li>'
        for t in toc)
    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>{TITLE} — {SUBTITLE}</title><link rel="stylesheet" href="style.css"></head><body>
<div class="title-page"><div class="t1">{TITLE}</div><div class="t2">{SUBTITLE}</div>
<div class="t3">Préface, cinq parties, dix-sept chapitres, conclusion, annexe et glossaire</div></div>
<nav id="toc"><h1>Table des matières</h1><ul>{items}</ul></nav>
{''.join(chunks)}
{SCRIPT}</body></html>"""


def build(pages, pdf):
    src = BUILD / "book.html"
    src.write_text(render(pages).replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    subprocess.run(["node", str(BUILD / "print.js"), str(src), str(pdf)], check=True)


def norm(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s).replace("—", " ")).strip().casefold()


def locate(pdf):
    texts = [norm(p.extract_text() or "") for p in PdfReader(str(pdf)).pages]
    pages, start = {}, 0
    for t in toc:
        head = norm(t["text"])[:40]
        for n in range(start, len(texts)):
            if texts[n].startswith(head):
                pages[t["id"]] = n + 1
                start = n + 1
                break
        else:
            raise SystemExit(f"Titre introuvable en tête de page : {t['text']}")
    return pages


tmp = BUILD / "pass1.pdf"
build({}, tmp)
pages = locate(tmp)
build(pages, OUT)
assert locate(OUT) == pages, "la pagination a changé entre les deux passes"
(BUILD / "pages.json").write_text(json.dumps(
    [{"titre": t["text"], "page": pages[t["id"]]} for t in toc], ensure_ascii=False, indent=1), encoding="utf-8")
print("OK", OUT, len(PdfReader(str(OUT)).pages), "pages")


