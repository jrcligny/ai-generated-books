# Fiches de révision A4 — « De l'assistant à l'agent »

Ce dossier contient une fiche de révision A4 par chapitre du livre [De l'assistant à l'agent](../construire-agent-conversationnel/README.md). Chaque fiche condense son chapitre sur une seule page : définitions, règles de conception, pièges, critères et extraits de code clés. Toutes les fiches sont composées avec le même corps de texte, 7 pt. Elles servent à réviser et ne remplacent pas le chapitre.

## Contenu du dossier

| Chemin | Rôle |
|---|---|
| `src/chNN.md` | Source de la fiche du chapitre NN : en-tête YAML et corps Markdown |
| `template/style.css` | Gabarit A4 sur trois colonnes, avec les encadrés colorés |
| `build.py` | Générateur : Markdown → HTML → PDF, avec vérifications |
| `pdf/chNN.pdf` | Fiches produites, une page A4 chacune |
| `pdf/fiches-de-revision.pdf` | Recueil de toutes les fiches, avec un signet par chapitre |
| `build/` | Fichiers intermédiaires HTML et aperçus PNG, non versionnés |

## Régénérer les fiches

Prérequis : Python 3.10 ou plus récent, avec les paquets `markdown-it-py`, `PyYAML` et `pypdf`, et Microsoft Edge ou Google Chrome. Si le navigateur n'est pas trouvé, indiquez son chemin dans la variable d'environnement `CHEATSHEET_BROWSER`.

```powershell
pip install markdown-it-py PyYAML pypdf
python cheatsheets/build.py            # toutes les fiches
python cheatsheets/build.py ch05 ch12  # seulement certaines fiches
python cheatsheets/build.py --png      # ajoute un aperçu PNG dans build/
```

Pour chaque fiche, le script :

1. assemble le HTML à partir de la source et du gabarit, avec un corps de texte de 7 pt ;
2. imprime le PDF avec le navigateur sans interface ;
3. vérifie le PDF : contenu entièrement visible, une seule page, au format A4, sans texte composé sous 7 pt.

Le script affiche une ligne `OK` ou `ERR` par fiche et se termine en erreur si une fiche n'est pas conforme. Si toutes les fiches générées sont conformes, il reconstruit ensuite le recueil `pdf/fiches-de-revision.pdf` à partir de toutes les fiches présentes dans `pdf/`. Une fiche trop longue doit être condensée dans sa source : la taille du texte est la même pour toutes les fiches et ne varie pas.

## Écrire une source

```markdown
---
numero: 5
titre: "Passer de l'assistant à l'agent : la boucle agentique"
partie: "Partie II — Faire agir l'agent : boucle, outils et droits"
source: "07-ch05.md"
---

## Une section thématique
- **Terme** : définition…

## À retenir
…
```

Chaque titre `##` ouvre un bloc. Les blocs dont le titre commence par « À retenir », « Pièges » ou « Critères » deviennent des encadrés colorés ; les autres restent des sections ordinaires. Les tableaux, listes, code en ligne et blocs de code Markdown sont acceptés. Le générateur ajoute les espaces insécables de la typographie française.
