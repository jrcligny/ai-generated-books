# Préface

Ce livre apprend à construire un modèle. Pas à en appeler un déjà entraîné : à décider ce qu'il doit prédire, à écrire la forme de cette prédiction, à trouver ses paramètres, et à reconnaître quand le calcul a échoué.

La partie I le fait sur une table numérique propre. La suite élargit le geste : préparer des données réelles, mesurer sans se tromper, contraindre, choisir entre plusieurs familles de modèles, calibrer une probabilité, mettre en service, puis représenter.

## À qui s'adresse ce livre

Vous êtes ingénieur logiciel. Vous écrivez du Python, vous appelez des API, vous mettez des systèmes en production. Vous n'avez pas suivi de cursus d'apprentissage automatique. Vous voulez comprendre pourquoi un modèle que vous entraînez fonctionne, ou pourquoi il échoue, assez pour choisir le levier suivant.

Avoir déjà utilisé un grand modèle de langage ou un agent aide à reconnaître certains mécanismes quand ils reviennent. Ce n'est pas le sujet du livre. Le sujet est le modèle que vous construisez vous-même.

Il vous faut savoir lire un court programme Python et manipuler un tableau de nombres. Aucune analyse, aucune algèbre linéaire. Quand une formule matricielle apparaît, elle est dans un aparté : vous pouvez la passer.

## Organisation

Quatre parties, seize chapitres. Chacun consomme le précédent.

- La partie I, « Ajuster un modèle » (Chapitres 1 à 3), pose la décision, la somme pondérée, et la descente qui trouve les paramètres, sur une table encore propre.
- La partie II, « Préparer, diagnostiquer, contraindre » (Chapitres 4 à 8), rend une table utilisable, montre l'échec d'un modèle trop pauvre ou trop riche, passe à une classe, mesure, puis limite.
- La partie III, « Choisir un modèle et s'y fier » (Chapitres 9 à 13), entraîne des arbres et un boosting, cherche les réglages, calibre une probabilité, met en service, et mesure un écart entre groupes.
- La partie IV, « Structure et représentations » (Chapitres 14 à 16), groupe et compresse sans étiquette, associe un vecteur à un objet, et calcule ce vecteur par un réseau.

La lecture est linéaire. L'annexe A donne les solutions des exercices. Le glossaire donne l'anglais des termes introduits en italique.

## Exemples, code, conventions

Les exemples sont des jeux synthétiques, ou des jeux livrés avec scikit-learn. Aucune application fictive ne se poursuit d'un chapitre à l'autre. Chaque chapitre se termine par « Ce que ça change en pratique » : le levier sur un modèle que vous construisez, et le cas où ce levier ne s'applique pas.

Les listings ont été exécutés avec Python 3.12, NumPy 2.5.5 et scikit-learn 1.9.1. Quand le hasard intervient, la graine est fixée (`random_state=0` ou une graine explicite). Sur une autre version, un arrondi peut bouger à la dernière décimale affichée. Le raisonnement, lui, ne dépend pas de cette décimale.

Les listings affichent les décimales avec un point, comme Python. La prose utilise la virgule. `1.99` dans une sortie et 1,99 dans une phrase sont le même nombre.

Les conventions typographiques, les encadrés Note, Tip et Warning, et les légendes sont celles décrites dans *STYLE.md*, à la racine de ce livre. Elles suivent le guide de style O'Reilly, avec les adaptations nécessaires au français.

## Comment ce livre a été écrit

Ce livre a été rédigé avec l'aide d'outils d'IA générative. Le plan, le choix des exemples et les relectures relèvent de son auteur. Les formules sont accompagnées du calcul qui permet de les refaire. Les sorties de code reproduites sous les listings sont celles obtenues en exécutant ces listings.
