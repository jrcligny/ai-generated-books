# Annexe A. Solutions des exercices

Cette annexe reprend les exercices dans l'ordre des chapitres. Les questions de compréhension n'y figurent pas : leur réponse est dans le chapitre. Les exercices des chapitres 1 à 8 figurent ici. Ceux des chapitres 9 à 26 seront ajoutés quand ces chapitres seront rédigés.

## Chapitre 1

### Exercice 1

Prédire une durée. La cible est la durée, une grandeur. Trois variables possibles, pourvu qu'elles soient connues avant la fin de cette durée : une mesure de charge déjà observée, une taille déjà connue, un compte déjà écrit. Le régime est la régression.

Dire si un événement aura lieu. La cible est une classe à deux valeurs. Trois variables possibles : des mesures antérieures à l'événement, un compteur déjà incrémenté, une catégorie déjà enregistrée. Le régime est la classification. Une variable qui ne s'écrit qu'une fois l'événement constaté est une fuite, pas une variable.

Grouper des objets qui se ressemblent. Il n'y a pas de cible. Les variables sont les mesures qui décrivent chaque objet au moment où l'on groupe. Le régime est non supervisé. Le Chapitre 12 construit ce type de modèle. Le cadrage reste : grouper pour quelle décision, et avec quelles mesures vraiment disponibles.

### Exercice 2

Pour une ligne nouvelle, « Durée connue » et « Volume connu » sont utilisables : le Tableau 1-1 les présente comme déjà mesurées. « Résultat » est la cible. Elle est vide au moment de prédire, puisqu'on la cherche. « Commentaire rédigé après » n'existe qu'une fois le résultat connu. « Fuite » vaut deux fois « Résultat ». La retirer du fichier sans retirer « Résultat » ne change rien à l'inverse : retirer « Résultat » et garder « Fuite » laisse la cible dans le modèle, sous un autre nom. L'Exemple 1-1 le montre sur la deuxième ligne, où la fuite vaut 2,0 parce que le résultat vaut 1.

### Exercice 3

Pour un modèle ajusté sur une table, l'exemple est une ligne. La cible est la colonne que l'on a désignée. Une fuite est une autre colonne calculée à partir de cette cible, ou remplie seulement après elle.

Pour un modèle de langage qui poursuit un texte, l'exemple est un morceau de texte, et la cible est la suite de ce morceau. Il n'y a pas une colonne nommée « réponse ». Une fuite, au sens de ce chapitre, apparaît quand on évalue le modèle sur un texte qu'il a déjà vu à l'entraînement, ou quand la consigne contient la réponse que l'on prétend mesurer. L'objet appris n'est pas le même : une fonction d'une ligne vers une case, contre une fonction qui prolonge une séquence. Le geste de cadrage est le même : qu'est-ce qui est connu au moment de la prédiction, et qu'est-ce qui est la réponse.

## Chapitre 2

### Exercice 1

Sur x, w = 1,99 et b = 0,95. Sur x₂ = 100 x, le produit w x doit rester le même, donc le coefficient devient 1,99 / 100 = 0,0199. Le décalage ne change pas : la hauteur de la droite, quand la variable d'origine vaut zéro, est la même. 1,99 n'est pas « plus important » que 0,0199. Les deux disent la même hausse de la prédiction pour la même situation, écrite dans une unité cent fois plus grande. Comparer les coefficients bruts compare les unités. L'Exemple 2-3 montre le même phénomène sur deux variables à la fois : le second coefficient est divisé par 100, et les prédictions ne bougent que d'un arrondi.

### Exercice 2

Les x valent 1, 2, 3, 4, 5. Leur moyenne est 3. Les y valent 2,8, 5,1, 6,7, 9,4, 10,6. Leur somme est 34,6, leur moyenne est 6,92.

Écarts de x à 3 : −2, −1, 0, 1, 2. Écarts de y à 6,92 : −4,12, −1,82, −0,22, 2,48, 3,68.

Produits : 8,24, 1,82, 0, 2,48, 7,36. Somme : 19,9.

Carrés des écarts de x : 4, 1, 0, 1, 4. Somme : 10.

w = 19,9 / 10 = 1,99. b = 6,92 − 1,99 × 3 = 6,92 − 5,97 = 0,95.

Au point moyen, x = 3, la droite donne 0,95 + 1,99 × 3 = 6,92, qui est ȳ. Elle passe par (3 ; 6,92), comme la forme close le garantit. L'Exemple 2-1 affiche les mêmes 1,99 et 0,95.

### Exercice 3

Deux endroits reviennent souvent. Le premier est une tête linéaire en bout de modèle : les x sont des variables déjà préparées, ou des activations d'une couche, et les w sont les coefficients de cette tête. La prédiction, ou le logit avant une fonction de score, est b + w x. Le Chapitre 6 reprendra le logit.

Le second est toute régression que vous posez comme ligne de base avant un modèle plus lourd. Les x sont les colonnes numériques, les w sont `coef_`. Si vous n'en entraînez pas vous-même, une combinaison linéaire à l'intérieur d'un réseau, une couche qui multiplie un vecteur par des poids, est encore cette somme. Dans les deux cas, le signe de w se lit dans l'unité de x. L'Exemple 2-3 a montré qu'une unité cent fois plus grande divise w par cent.

## Chapitre 3

### Exercice 1

Les cibles sont 4, 7 et 10. Les prédictions sont 4, 10 et 10.

Écarts : 4 − 4 = 0, 10 − 7 = 3, 10 − 10 = 0.

Carrés : 0, 9 et 0.

Erreur quadratique moyenne : (0 + 9 + 0) / 3 = 3.

Le deuxième point contribue pour 9, les deux autres pour 0. C'est lui qui tire le gradient. Une descente déplacera les paramètres d'abord pour rapprocher 10 de 7, parce que le coût ne voit que ce carré.

### Exercice 2

Deux cents lignes tiennent en mémoire et se parcourent vite. Le lot complet est lisible : une mise à jour par époque, une courbe lisse. Vous vérifiez que le coût baisse sans être multiplié d'un pas à l'autre.

Deux millions de lignes se traitent par mini-lots. Un lot complet ferait une seule mise à jour très chère par époque. Vous regardez le coût moyen sur une époque, pas le coût d'un mini-lot isolé, qui tremble.

Cinquante millions de lignes que vous ne chargez pas d'un bloc imposent le même mini-lot, lu au fil de l'eau, ou la descente stochastique si même un petit lot est inutilement lourd. La courbe stochastique tremble davantage. Vous la lissez sur plusieurs centaines de pas avant de conclure qu'elle explose ou qu'elle stagne. Dans les trois cas, le critère n'est pas la mode : c'est le nombre de mises à jour par passage, et le bruit que vous acceptez sur la pente.

### Exercice 3

Un coût multiplié par dix à chaque pas est le régime η = 0,09 du Tableau 3-1, ou l'Exemple 3-5 quand l'échelle est en cause. Raccourcissez le pas. Si les variables ont des unités très différentes, ramenez-les à une échelle commune, ce que fera le Chapitre 4, plutôt que de compenser par un pas minuscule fragile.

Un coût qui passe de 55,89 à 53,28 est le pas 0,001 du même tableau. La direction est bonne, la longueur est courte. Allongez le pas, ou poursuivez si vous avez vérifié que la baisse continue et que vous avez le temps.

Un coût qui descend vers 45, remonte vers 59 et redescend vers 45 est la descente stochastique de l'Exemple 3-4, qui oscille autour du plancher de 44,59. Le régime est bruité parce que chaque pas ne voit qu'un exemple. Passez à un mini-lot plus grand si le tremblement vous empêche de lire la courbe. Raccourcir un peu le pas calme aussi l'oscillation. Ce n'est pas une explosion : le coût ne part pas vers l'infini.

Ces trois formes se lisent de la même façon sur le journal d'un ajustement fin. Le nom du modèle change. La pente, le pas et le bruit du lot, non.

## Chapitre 4

### Exercice 1

Les quatre valeurs d'entraînement sont 2, 4, 6 et 8. Leur moyenne est 5. C'est elle qui impute la case vide. La cinquième valeur, 80, est tenue à l'écart : la mêler donne (2 + 4 + 6 + 8 + 80) / 5 = 20. Le trou est alors bouché par 20, dans une colonne dont les cas d'apprentissage vivent entre 2 et 8. Le modèle apprend un centre qui n'existera pas à l'appel, quand ce 80 sera absent. L'Exemple 4-1 montre le même écart, 3,0 contre 22,4.

### Exercice 2

« Milieu » devient la ligne (0, 1, 0) si l'ordre des colonnes est bas, milieu, haut. « Bas » devient (1, 0, 0). Aucune colonne n'est plus grande qu'une autre. Remplacer les modalités par 0, 1 et 2 invente un ordre et des écarts égaux : le coefficient unique traiterait « haut » comme deux fois « milieu ». L'Exemple 4-2 montre le même principe sur « a », « b » et « c ».

### Exercice 3

Après standardisation, 1,875 et 1,898 sont du même ordre : un écart-type de chaque variable déplace la prédiction d'environ 1,9. On peut conclure que les deux effets, mesurés dans leur propre dispersion, se valent. Avant, 1,945 contre 0,020 comparait des unités. Le second coefficient était petit parce que la variable était dispersée sur une échelle d'environ 100, pas parce que son effet était négligeable.

## Chapitre 5

### Exercice 1

0,40 et 0,42 : les deux erreurs sont hautes et proches. C'est un sous-apprentissage, forme trop pauvre, comme le degré 1 de l'Exemple 5-1.

0,05 et 0,40 : l'entraînement est bas, les cas nouveaux sont hauts. C'est un surapprentissage.

0,35 et 0,33 : les deux erreurs se tiennent. Le modèle ne fait pas mieux sur les cas vus que sur les autres. Si ce niveau est trop haut pour la tâche, la forme est trop pauvre.

0,02 et 1,20 : surapprentissage net, comme le degré 12 dont l'erreur tenue à l'écart valait 1,480 pour une erreur d'entraînement de 0,086.

### Exercice 2

L'erreur vue passe de 0,30 à 0,04 et l'erreur tenue à l'écart de 0,32 à 0,55. Le modèle colle aux exemples et se dégrade ailleurs. Le levier est une contrainte, ou des exemples nouveaux si la forme est déjà la bonne et que la variance domine. Une forme plus riche aggraverait l'écart : c'est le degré 12 ajouté au degré 3.

### Exercice 3

Pour un degré très haut, l'erreur d'entraînement part de presque 0 quand il y a à peine plus de points que de coefficients, et reste basse. L'erreur tenue à l'écart part de très haut, comme les 30 730 de l'Exemple 5-2 à 12 points, puis redescend quand les points deviennent nombreux, sans forcément rattraper une forme juste. Le degré 1, sur le même dessin, garde les deux erreurs hautes : les points supplémentaires ne créent pas le coude qui manque.

## Chapitre 6

### Exercice 1

−0,55 et 1,03 ne sont pas des fréquences. Un seuil à 0,5 reste un nombre que l'on peut comparer, mais le score n'a pas le sens d'une part des cas, et rien n'empêche la droite d'annoncer « moins que impossible » ou « plus que certain ». La sigmoïde ramène toute somme dans l'intervalle ouvert entre 0 et 1. L'Exemple 6-1 est cette droite. L'Exemple 6-2 est la somme bornée.

### Exercice 2

En (1, 0), la somme vaut 2,684 × 1 + 1,269 × 0 − 2,151 = 0,533. Elle est positive, donc du côté où la sigmoïde dépasse 0,5. Au seuil 0,5, la classe estimée est 1.

### Exercice 3

Pour une vraie classe 0, la perte vaut −log(1 − p). À 0,99 elle vaut 4,605. À 0,6 elle vaut 0,916. Le tort presque sûr coûte environ cinq fois plus. L'Exemple 6-4 montre qu'à température 0,5 le premier logit pèse 0,831, et qu'à température 2 il ne pèse plus que 0,409. C'est 0,5 qui concentre la masse.

## Chapitre 7

### Exercice 1

Le découpage aléatoire met des instants postérieurs dans l'entraînement et des instants antérieurs dans le test : 198 d'un côté, 4 de l'autre, et 97,3 % des lignes d'entraînement après le début du test. Un découpage par ordre du temps interdit ce mélange : tout l'entraînement est avant tout le test. Le modèle n'a pas pour autant une colonne qui contient la cible. Il a seulement appris sur des moments qui ne seraient pas encore observés. C'est une fuite de protocole, pas une copie de la réponse.

### Exercice 2

Il faut retirer la copie, pas seulement la colonne qui porte le nom de la cible. L'Exemple 7-2 passe de 0,600 à 1,000 dès qu'une colonne vaut exactement la classe. Une colonne calculée à partir d'elle, comme la colonne « Fuite » du Chapitre 1, laisse le même 1. On retire toute colonne qui ne serait pas connue le jour de la prédiction.

### Exercice 3

Le Tableau 7-1 a une précision de 1 et un rappel de 0,250. Si l'alerte à tort coûte dix fois plus cher, on regarde d'abord la précision : elle est déjà maximale, le seuil 0,5 est prudent. Si le cas manqué coûte dix fois plus cher, on regarde le rappel : 0,250 veut dire que neuf positifs sur douze sont manqués. On baisse le seuil sur la validation, pour annoncer « positif » plus souvent, et l'on accepte des faux positifs. On ne règle pas ce seuil sur le test.

### Exercice 4

On retire le texte qui figurait déjà dans les cinq consignes. Le garder dans l'évaluation finale, c'est l'Exemple 7-2 : le chiffre mesure une reconnaissance, pas une généralisation. Les trois textes nouveaux restent le test. Les cinq du réglage restent la validation.

## Chapitre 8

### Exercice 1

L1 a le plus de chances de poser des zéros exacts sur les cinq positions nulles : la pénalité est linéaire, et la descente peut abandonner une variable. L2 va surtout rapetisser les trois coefficients non nuls, 3, −2 et 1,5, et laisser des miettes là où la vérité est 0. L'Exemple 8-1, sur un jeu de cette forme, montre L2 encore à −0,14 et 0,14 sur des positions nulles, et L1 à zéro sur ces positions, au signe d'arrondi près.

### Exercice 2

On garde l'époque 15 : la validation y vaut 3,295, contre 4,696 au début, 3,498 à l'époque 5, et 3,510 à l'époque 59. L'époque 59 est un surapprentissage parce que l'entraînement a continué de baisser, jusqu'à 0,023, pendant que la validation remontait. C'est le degré 12 du Chapitre 5, lu sur le nombre de pas.

### Exercice 3

La copie de la cible de l'Exemple 7-2 porte la justesse à 1. Rapetisser son coefficient, ou s'arrêter plus tôt, ne la rend pas inconnue le jour de l'appel. Il faut retirer la colonne. La régularisation freine une forme trop libre. Elle ne répare pas une fuite.

