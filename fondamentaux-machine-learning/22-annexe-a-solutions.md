# Annexe A. Solutions des exercices

Cette annexe reprend les exercices dans l'ordre des chapitres. Les questions de compréhension n'y figurent pas : leur réponse est dans le chapitre. Les chapitres 4 à 16 seront ajoutés ici quand ils seront rédigés.

## Chapitre 1

### Exercice 1

Prédire une durée. La cible est la durée, une grandeur. Trois variables possibles, pourvu qu'elles soient connues avant la fin de cette durée : une mesure de charge déjà observée, une taille déjà connue, un compte déjà écrit. Le régime est la régression.

Dire si un événement aura lieu. La cible est une classe à deux valeurs. Trois variables possibles : des mesures antérieures à l'événement, un compteur déjà incrémenté, une catégorie déjà enregistrée. Le régime est la classification. Une variable qui ne s'écrit qu'une fois l'événement constaté est une fuite, pas une variable.

Grouper des objets qui se ressemblent. Il n'y a pas de cible. Les variables sont les mesures qui décrivent chaque objet au moment où l'on groupe. Le régime est non supervisé. Le Chapitre 14 construit ce type de modèle. Le cadrage reste : grouper pour quelle décision, et avec quelles mesures vraiment disponibles.

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
