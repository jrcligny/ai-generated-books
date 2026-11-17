# Génération du PDF du livre

Ce dossier assemble les fichiers de [`construire-agent-conversationnel/`](../../construire-agent-conversationnel/README.md) en un seul PDF. L'ordre des fichiers est celui du README du livre. Le PDF contient une page de titre, une table des matières paginée et des signets. Chaque partie et chaque chapitre commencent sur une nouvelle page.

Chaîne : pandoc (Markdown → HTML) → navigateur Chromium sans interface, piloté par Puppeteer (HTML → PDF). Le script lance deux passes : la première repère la page de chaque titre, la seconde injecte ces numéros dans la table des matières.

## Prérequis

- Python 3.10 ou plus. Le paquet `pypandoc_binary` embarque pandoc, il n'y a rien d'autre à installer.
- Node.js 18 ou plus.
- Microsoft Edge ou Google Chrome. Le script cherche les emplacements usuels ; sinon, indiquez le chemin de l'exécutable dans la variable `BROWSER_PATH`.

Installation, une seule fois, depuis ce dossier :

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
npm install
```

Sous Linux ou macOS, remplacez `.\.venv\Scripts\python` par `.venv/bin/python`.

## Génération

```powershell
.\.venv\Scripts\python build.py
```

Le PDF est écrit dans `tools/pdf/de-l-assistant-a-l-agent.pdf`, un fichier ignoré par Git. Pour changer le dossier du livre ou le fichier produit, passez-les en arguments : `build.py <dossier_du_livre> <sortie.pdf>`.

## Fichiers

| Fichier | Rôle |
|---|---|
| `build.py` | Assemble les fichiers dans l'ordre du README, construit la table des matières et lance les deux passes. |
| `style.css` | Mise en page inspirée du format O'Reilly : 7 × 9,19 in, texte en 9,5 pt, code en 8 pt. |
| `calib.js` | Rendu des schémas Mermaid. Chaque schéma est calibré pour tenir dans la largeur du texte et sur 3,6 in de haut au plus. Les légendes restent sur la même page que leur figure, leur exemple ou leur tableau. |
| `print.js` | Impression en PDF avec Puppeteer : numéros de page, signets, PDF balisé. |

## Limites connues

- Les schémas larges orientés de gauche à droite (figures 3-1, 6-x, 7-x, 9-1, 15-1) et la figure 12-1, très haute, sont fortement réduits : leur texte descend vers 4 pt. Pour les rendre lisibles, il faudrait raccourcir leurs libellés ou revoir leur disposition dans le manuscrit.
- Mermaid ignore `direction LR` dans les sous-graphes : la figure 12-1 sort en vertical.
- `build.py` vérifie qu'il trouve 26 fichiers dans le README du livre. Si vous ajoutez ou retirez un fichier, mettez ce contrôle à jour.
