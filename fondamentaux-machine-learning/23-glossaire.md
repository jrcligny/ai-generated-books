# Glossaire français-anglais

Le Tableau G-1 rassemble les termes introduits en italique dans les parties I et II, avec l'anglais et le chapitre de la première occurrence. Les parties suivantes ajouteront leurs entrées.

*Tableau G-1. Termes des parties I et II*

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| apprentissage automatique | *machine learning* | Ajustement des paramètres d'un modèle à partir d'exemples | 1 |
| apprentissage non supervisé | *unsupervised learning* | Recherche d'une structure sans cible | 1 |
| apprentissage par renforcement | *reinforcement learning* | Ajustement d'une politique à partir d'une récompense, non enseigné dans ce livre | 1 |
| apprentissage supervisé | *supervised learning* | Apprentissage d'une fonction des variables vers une cible | 1 |
| arrêt anticipé | *early stopping* | Arrêt de la descente à l'époque où la validation est la meilleure | 8 |
| biais | *bias* | Erreur due à une forme trop pauvre pour la relation. Distinct du biais entre groupes | 5 |
| cible | *target* | Réponse que le modèle doit produire | 1 |
| classification | *classification* | Prédiction d'une classe | 1 |
| coefficient | *weight* | Facteur d'une variable dans la somme pondérée | 2 |
| courbe d'apprentissage | *learning curve* | Erreurs d'entraînement et de cas nouveaux, selon la taille du jeu | 5 |
| courbe précision-rappel | *precision-recall curve* | Précision contre rappel quand le seuil parcourt les scores | 7 |
| courbe ROC | *ROC curve* | Rappel contre taux de faux positifs quand le seuil parcourt les scores | 7 |
| coût | *loss* | Mesure de ce que le modèle est puni d'avoir raté | 3 |
| décalage | *intercept* | Prédiction quand toutes les variables valent zéro | 2 |
| descente de gradient | *gradient descent* | Suite de pas dans le sens opposé à la pente du coût | 3 |
| descente de gradient stochastique | *stochastic gradient descent* | Descente dont chaque pas estime la pente sur un seul exemple | 3 |
| encodage one-hot | *one-hot encoding* | Une colonne par modalité, valant 1 si l'exemple la porte | 4 |
| ensemble d'entraînement | *training set* | Lignes qui ajustent les paramètres | 7 |
| ensemble de test | *test set* | Lignes tenues jusqu'à la mesure finale | 7 |
| ensemble de validation | *validation set* | Lignes qui servent aux choix autres que les paramètres | 7 |
| époque | *epoch* | Un passage sur l'ensemble du jeu d'entraînement | 3 |
| erreur quadratique moyenne | *mean squared error* | Moyenne des carrés des écarts entre prédiction et cible | 3 |
| exemple | *example* | Une situation passée, décrite par des variables et, s'il y a lieu, une cible | 1 |
| F1 | *F1 score* | Moyenne harmonique de la précision et du rappel | 7 |
| faux négatif | *false negative* | Cas positif annoncé négatif | 7 |
| faux positif | *false positive* | Cas négatif annoncé positif | 7 |
| forme close | *closed form* | Solution calculée directement, sans recherche itérative | 2 |
| frontière de décision | *decision boundary* | Lieu où le score égale le seuil de décision | 6 |
| fuite | *leakage* | Information utilisée à l'entraînement qui n'existera pas au moment de prédire | 1 |
| généralisation | *generalization* | Qualité d'une prédiction sur un exemple que le modèle n'a pas vu | 1 |
| gradient | *gradient* | Pente du coût par rapport aux paramètres | 3 |
| imputation | *imputation* | Remplacement d'une case vide par une valeur apprise sur l'entraînement | 4 |
| logit | *logit* | Somme pondérée associée à une classe, avant sigmoïde ou softmax | 6 |
| lot | *batch* | Ensemble de tous les exemples servant à estimer une pente | 3 |
| matrice de confusion | *confusion matrix* | Comptes des quatre issues d'une classification à deux classes | 7 |
| mini-lot | *mini-batch* | Sous-ensemble d'exemples servant à estimer une pente | 3 |
| modèle | *model* | Fonction dont les paramètres ont été ajustés sur des exemples | 1 |
| paramètre | *parameter* | Nombre que l'entraînement ajuste | 1 |
| pas d'apprentissage | *learning rate* | Longueur du pas de descente | 3 |
| pénalité | *penalty* | Terme ajouté au coût pour freiner les coefficients | 8 |
| perte logarithmique | *log loss* | Coût d'une probabilité annoncée pour une classe, sévère si la confiance est fausse | 6 |
| précision | *precision* | Part de vrais positifs parmi les cas annoncés positifs | 7 |
| prédiction | *prediction* | Valeur produite par le modèle pour un exemple | 1 |
| rappel | *recall* | Part des positifs réels que le modèle a retrouvés | 7 |
| régression | *regression* | Prédiction d'une grandeur | 1 |
| régression linéaire | *linear regression* | Modèle dont la prédiction est une somme pondérée, plus un décalage | 2 |
| régression logistique | *logistic regression* | Somme pondérée passée dans une sigmoïde, pour une classe | 6 |
| régression polynomiale | *polynomial regression* | Régression linéaire sur les puissances d'une variable | 5 |
| régularisation | *regularization* | Frein sur la liberté du modèle : pénalité ou arrêt | 8 |
| régularisation L1 | *lasso* | Pénalité sur la somme des valeurs absolues des coefficients | 8 |
| régularisation L2 | *ridge* | Pénalité sur la somme des carrés des coefficients | 8 |
| sigmoïde | *sigmoid* | Fonction qui ramène une somme dans l'intervalle entre 0 et 1 | 6 |
| softmax | *softmax* | Transformation de plusieurs logits en probabilités de somme 1 | 6 |
| sous-apprentissage | *underfitting* | Erreurs hautes des deux côtés, forme trop pauvre | 5 |
| standardisation | *standardization* | Centrage et réduction par la moyenne et l'écart-type de l'entraînement | 4 |
| surapprentissage | *overfitting* | Erreur d'entraînement basse et erreur sur des cas nouveaux haute | 5 |
| température | *temperature* | Diviseur des logits avant le softmax, qui concentre ou aplatit | 6 |
| variable | *feature* | Information décrivant un exemple, lue par le modèle | 1 |
| variance | *variance* | Part de l'erreur due à une forme trop sensible au jeu vu | 5 |
