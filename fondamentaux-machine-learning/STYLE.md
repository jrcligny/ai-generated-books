# Conventions — Fondamentaux du Machine Learning

Ce fichier résume les règles du [guide de style O'Reilly](https://oreillymedia.github.io/production-resources/styleguide/) applicables à ce livre, et dit où le français s'en écarte. Le guide fait foi. En cas de trou, l'ordre du guide est : sa word list, puis le *Chicago Manual of Style* (18e éd.), puis le Merriam-Webster. Les choix propres à ce livre sont en fin de fichier.

Pages liées utilisées : le guide lui-même (word list incluse), [Production Resources](https://oreillymedia.github.io/production-resources/), les admonitions du [gabarit Word](https://oreillymedia.github.io/production-resources/word/) (Note, NoteTip, NoteWarning) et d'[HTMLBook](https://oreillymedia.github.io/HTMLBook/) (`data-type` note, tip, warning, et aussi caution et important). Ce livre n'emploie que Note, Tip et Warning, les trois types nommés dans le guide.

Ce fichier ne s'impose pas à l'autre livre du dépôt.

## Voix

Ton d'un collègue expérimenté qui s'adresse à quelqu'un d'intelligent et neuf sur ce point. Deuxième personne, verbes actifs, contractions naturelles du français parlé professionnel (« c'est », « n'est »). Le « vous » reste stable dans un paragraphe.

Le livre a été écrit avec l'aide d'outils d'IA générative : la préface le dit. Un échange avec un assistant, s'il apparaît, va dans une citation, invite et réponse séparées, le texte du modèle repris tel quel. Un fragment de code produit par un modèle va dans un bloc de code, lui aussi repris tel quel.

La finalité de chaque partie et de chaque chapitre apparaît de façon implicite dans son introduction, sans rubrique dédiée. L'ouverture de partie dit à quoi servira le mécanisme, en le reliant aux chapitres qui suivent. Les paragraphes qui ouvrent un chapitre, avant « Objectifs », font de même pour les notions du chapitre. Pas de titre, pas d'encadré, pas de liste d'usages. La section « Ce que ça change en pratique », en fin de chapitre, reste le lieu du levier concret.

## Titres

Un titre ne contient ni gras, ni italique, ni chasse fixe. Un sigle très courant pour le lecteur (API) peut rester en sigle ; les autres s'écrivent en toutes lettres.

Un titre est suivi d'un paragraphe de texte. Pas d'encadré, pas d'autre titre, immédiatement dessous. On n'empile pas deux encadrés, ni un encadré et un aparté.

Le guide met les titres de niveau A et B en *title case* anglais, et le niveau C en casse de phrase. **Adaptation.** Le français ne met pas de capitale à chaque mot lexical. Tous les titres de ce livre sont en casse de phrase : capitale initiale, puis minuscules, sauf nom propre et mot qui suit un point. Après un deux-points, le guide et l'usage français concordent : minuscule.

Le titre de chapitre s'écrit avec un point, pas un tiret cadratin :

```markdown
# Chapitre 2. La régression linéaire : une somme pondérée
```

Les titres `##` et `###` suivent la même casse. C'est le point où ce livre se sépare de la *title case* du guide, et rejoint la casse déjà en usage dans l'autre livre du dépôt.

## Renvois

Tout élément numéroté est annoncé dans le texte avant d'apparaître, par son numéro : « la Figure 2-1 », « le Tableau 7-1 », « l'Exemple 3-1 », « le Chapitre 4 ». Le numéro prend un trait d'union, pas un tiret demi-cadratin.

On n'écrit pas « ci-dessous », « ci-dessus », « la figure suivante », ni une introduction par deux-points (« comme le montre la figure : »). Si l'on ne peut pas donner le numéro, « précédente » ou « suivante ».

**Écart avec l'autre livre.** Il met « la figure 1-1 » et « le chapitre 4 » en minuscules. Ce livre met la capitale du guide sur le mot qui porte le numéro.

## Figures, tableaux, exemples

Légende en casse de phrase, sans point final. Le numéro est suivi d'un point, selon le guide (`Figure 1-1. Légende`), pas d'un tiret cadratin.

Dans le Markdown, la légende est une ligne en italique, immédiatement au-dessus de l'élément. C'est un repère de manuscrit : en production, elle devient le titre de figure, de tableau ou d'exemple, pas un paragraphe italique du corps.

```markdown
La Figure 2-1 montre les deux nuages.

*Figure 2-1. Coefficients avant et après mise à l'échelle*
```

Même forme pour `Tableau 1-1.` et `Exemple 3-1.`. Les têtes de colonnes sont en casse de phrase. Un exemple numéroté n'est pas introduit par un deux-points. Un bloc de code non numéroté l'est.

Les mots dans un schéma prennent une capitale au premier mot seulement, sans point final, sauf nom propre.

## Encadrés

Trois types, ceux du guide et du gabarit Word. Le nom du type reste en anglais : c'est l'identifiant de production (HTMLBook `data-type`). Le titre personnalisé, s'il y en a un, est facultatif et, en français, en casse de phrase.

| Type | Quand |
|---|---|
| Note | Précision utile qui n'est pas le fil de la phrase. |
| Tip | Geste recommandé, raccourci, réglage par défaut. |
| Warning | Risque coûteux : fuite, chiffre faux, donnée perdue, seuil pris pour une vérité. |

```markdown
Le pas se règle sur la courbe, pas au jugé.

> **Warning**
>
> Un pas trop grand fait diverger le coût. Le chapitre 4 montre le rôle de l'échelle.
```

Pas d'encadré « Point clé », « Attention » ni « Pour aller plus loin » : ces libellés sont ceux de l'autre livre, pas ceux du guide. Une idée à retenir va dans le texte ou dans « Ce qu'il faut retenir ». Un développement facultatif (forme matricielle, précision sur AdamW) est un aparté, pas un quatrième type d'encadré :

```markdown
> **Encadré. Forme matricielle**
>
> Texte que l'on peut sauter sans perdre le fil.
```

On n'empile pas deux encadrés, ni un encadré et un aparté.

## Listes

Trois listes : à puces (énumération), numérotée (ordre ou étapes), de définitions (terme, puis définition). Chaque item commence par une capitale. On ne relie pas les items par des virgules ni par « et ».

Si aucun item n'est une phrase complète, pas de point final. Si un item est une phrase complète, tous les items de la liste prennent un point, y compris les fragments.

Une puce qui est un terme suivi de sa définition devient une liste de définitions, pas une puce.

## Typographie du français

Là où le guide décrit l'anglais, ce livre suit la typographie française.

| Guide (anglais) | Ce livre |
|---|---|
| Guillemets courbes “ ”, virgule et point à l'intérieur | Guillemets « » avec espaces insécables. La ponctuation française reste dehors, avec son espace insécable devant `:` `;` `!` `?`. |
| Tiret cadratin collé, sans espaces | Tiret cadratin avec espaces, comme dans l'autre livre : `mot — mot`. |
| Virgule de série (*a, b, and c*) | Pas de virgule avant « et » ou « ou ». |
| *Title case* des titres A et B | Casse de phrase. Voir plus haut. |
| *data is* | « Les données » au pluriel. |
| *email* | « Courriel » dans la prose. Une adresse est en italique. |

Le guide et le français concordent sur la minuscule après un deux-points dans le corps du texte.

Les nombres de zéro à neuf s'écrivent en toutes lettres, les suivants en chiffres, sauf si les deux se côtoient dans la même phrase (alors tous en chiffres). Le symbole `%` est collé au chiffre. Un moins est un tiret demi-cadratin, pas un trait d'union. Les opérateurs en ligne prennent des espaces : `1 + 1 = 2`.

## Caractères

| Élément | Caractère |
|---|---|
| Première occurrence d'un terme technique | Italique, pas de gras. L'anglais suit entre parenthèses, en italique. Le glossaire reprend ces termes. |
| Emphase | Italique. Pas de gras pour appuyer. |
| Nom de fichier, chemin, URL, adresse | Italique |
| Code, identifiant, commande, paramètre, valeur | Chasse fixe |
| Texte que le lecteur doit saisir | Chasse fixe gras |
| Paramètre remplaçable dans une syntaxe | Chasse fixe italique |
| Bibliothèque ou produit (scikit-learn, NumPy, XGBoost) | Romain, casse d'usage |
| Code SQL réservé | Chasse fixe en capitales |

**Écart avec l'autre livre.** Il met le terme en gras à l'endroit de la définition. Ce livre le met en italique, comme le guide.

Les listings visent 81 caractères, largeur du corps pour le format Animal 7 × 9 du guide. Indentation par espaces. Langage indiqué sur la balise du bloc. Commentaires en français, identifiants en anglais. La sortie réellement obtenue suit le listing.

## Renvois bibliographiques

Système auteur-date, l'un des deux systèmes de Chicago acceptés par le guide, et celui de l'autre livre. Auteur et année dans le texte. Jusqu'à deux auteurs nommés ; au-delà, le premier suivi de « et al. ». Notice en fin de chapitre : la note contient le texte cité, pas une URL seule. Un DOI ou une URL est ancré à un intitulé descriptif, pas au mot « ici ».

## Langue inclusive

Le guide écarte le vocabulaire genré sans besoin, violent ou lié à une couleur prise pour une qualité. Dans ce livre : liste d'autorisation et liste de refus, pas *blacklist* ni *whitelist* ; primaire et réplique, pas *master* et *slave*. Pas de « trivial », « évidemment », « il suffit de ».

## Mots retenus pour ce livre

Graphies du guide, quand le mot reste en anglais, et équivalent français de la prose.

| Prose française | Anglais, graphie du guide |
|---|---|
| apprentissage automatique | *machine learning*, sans trait d'union |
| apprentissage profond | *deep learning*, sans trait d'union |
| jeu de données | *dataset* (une seule graphie si l'anglais apparaît) |
| module d'extension | *plug-in* |
| code source ouvert | *open source* (pas de forme verbale) |
| arrière-plan, interface | *backend*, *frontend* |
| nom de fichier | *filename* |

Les sigles API et IA s'emploient sans développement dès la première fois : le guide le permet pour les sigles courants du lectorat, et ce sont ceux de ce lecteur.
