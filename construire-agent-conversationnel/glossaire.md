# Glossaire français-anglais

Chaque entrée donne le terme tel que le livre l'emploie, son équivalent anglais, une définition courte et le chapitre où il est introduit. Lorsque le livre conserve le terme anglais comme terme d'usage, l'entrée est classée à ce terme, en italique, et un renvoi figure à l'équivalent français quand le livre en donne un. Un tiret (« — ») dans la colonne anglaise signale un terme propre à l'ouvrage, sans équivalent anglais établi ; l'index anglais-français, en fin de glossaire, permet la recherche inverse.

## A

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| accumulation d'erreurs | *compounding errors* | Forme d'échec de la boucle : une erreur commise tôt dans le tour reste sans correction, et les étapes suivantes s'exécutent correctement sur une base fausse. | chap. 5 |
| agent | *agent* | Système dans lequel le modèle décide lui-même de l'étape suivante : quel outil appeler, avec quoi, s'il faut continuer et quand la tâche est terminée. Ce critère est une convention du livre. | chap. 1 et 5 |
| agent conversationnel | *conversational agent* | Agent qui travaille dans un dialogue : une personne attend sa réponse, peut l'interrompre, préciser sa demande ou changer d'avis, et l'agent peut à son tour poser une question. | chap. 5 |
| agent de programmation | *coding agent* | → voir *coding agent* | chap. 17 |
| ajustement fin | *fine-tuning* | Entraînement complémentaire par lequel on adapte un modèle pré-entraîné à une tâche particulière. | chap. 1 |
| appel d'outil | *tool calling*, *function calling* | Capacité d'un modèle, entraîné à cet usage, à décider quand appeler un outil, lequel, et avec quels arguments. | chap. 4 |
| apprentissage automatique | *machine learning* | → voir *machine learning* | chap. 1 |
| apprentissage en contexte | *in-context learning* | Capacité d'un modèle à accomplir une tâche décrite dans le texte d'entrée par une consigne et quelques exemples ; ses paramètres ne changent pas, et l'adaptation ne dure que le temps de l'appel. | chap. 1 |
| apprentissage profond | *deep learning* | → voir *deep learning* | chap. 1 |
| assistant | *assistant* | Modèle de langage placé dans une boucle de conversation, avec des consignes et éventuellement des outils ; il répond à ce que l'utilisateur demande, tour après tour. | chap. 1 et 3 |
| avec état | *stateful* | Se dit d'un échange dans lequel le serveur ouvre une session et y conserve des informations auxquelles les requêtes suivantes se rapportent. | chap. 6 |

## B

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| boucle agentique | *agentic loop* | Boucle qui répète un cycle en trois temps (observer, décider, agir) jusqu'à ce que le modèle rédige une réponse au lieu de demander un appel d'outil. | chap. 5 |
| boucle conversationnelle | *conversation loop* | Organisation dans laquelle le programme conserve la liste des messages échangés et la soumet en entier au modèle à chaque tour, ce qui permet de tenir compte des échanges précédents. | chap. 3 |

## C

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| cache | *cache* | Mécanisme qui conserve un résultat pour éviter de le recalculer ; sa clé comprend l'organisation et l'utilisateur chaque fois que le contenu dépend de leurs droits. | chap. 7 |
| catalogue de *skills* | *skill catalog* | Ensemble des *skills* sortis du *system prompt* et versionnés ; le modèle en lit le sommaire et charge à la demande ceux dont l'utilisateur peut se servir. | chap. 13 |
| chaîne de pensée | *chain of thought* | Pratique qui amène le modèle à écrire son raisonnement avant sa conclusion. | chap. 5 |
| *chatbot* | *chatbot* | Programme de dialogue. Le mot ne dit rien de la technique employée : un *chatbot* peut suivre un arbre de décision écrit à la main, sans modèle de langage. | chap. 1 |
| clé d'idempotence | *idempotency key* | Identifiant unique associé à une soumission et reconnu par le système cible, de sorte qu'une répétition soit ignorée. | chap. 16 |
| client | *client* | Dans le protocole *MCP*, composant de l'hôte qui entretient la liaison avec un serveur donné ; l'hôte crée un client par serveur. | chap. 6 |
| cloisonnement | *data isolation* | Séparation imposée par le programme pour que la mémoire, les caches et les données d'un utilisateur ou d'une organisation n'atteignent pas un autre utilisateur ou une autre organisation. | chap. 11 |
| *coding agent* | *coding agent* | Agent dont la tâche consiste à modifier un projet logiciel ; ses outils lisent et modifient des fichiers, lancent des commandes et exécutent des vérifications. Équivalent français : agent de programmation. | chap. 17 |
| combinaison dangereuse | — | Réunion, dans un même agent, de l'accès à des données privées, de l'exposition à un contenu non fiable et de la capacité à communiquer vers l'extérieur ; elle forme un chemin complet pour faire sortir une information du système. | chap. 14 |
| compaction | *compaction* | Réduction de l'historique d'une conversation longue, par troncature, élagage des résultats d'outils ou résumé ; elle oblige à choisir les informations qui restent disponibles. Le fil rouge compacte la conversation par résumé, au-delà d'un seuil, en conservant à l'identique les messages de l'utilisateur et l'état de conversation. | chap. 10 |
| compte de service | *service account* | Compte technique dont on dote un serveur pour interroger l'application ; pourvu de droits étendus, il oblige le serveur à vérifier lui-même ce que chaque utilisateur a le droit de voir. | chap. 7 |
| condition d'arrêt | *stopping condition* | Situation qui met fin à la boucle : arrêt décidé par le modèle, imposé par le programme ou demandé par l'utilisateur. | chap. 5 |
| consignes | *instructions* | Textes par lesquels le concepteur oriente le comportement du modèle, portés notamment par le *system prompt* ; le modèle a appris à leur accorder du poids, sans que leur respect soit assuré à chaque exécution. | chap. 3 |
| contenu non fiable | *untrusted content* | Tout texte qu'un tiers a pu écrire ou modifier et que l'agent est amené à lire : document, page, message, champ de commentaire, description d'outil. | chap. 14 |
| contexte | *context* | Ce que l'on place dans la fenêtre de contexte ; pour produire un *token*, le modèle s'appuie sur ce contenu et sur ses paramètres. | chap. 2 |
| contexte composé | — | Ce que le *harness* assemble et envoie au modèle à un cycle donné : consignes, partie retenue de l'historique, résultats d'outils et éléments tenus à part. | chap. 8 |
| continuum d'autonomie | — | Échelle propre à ce livre, en cinq positions, qui décrit la part de décision confiée au modèle, depuis le modèle qui rédige jusqu'au modèle qui agit sur la durée. | chap. 5 |
| contrat d'interface | *interface contract* | Ensemble minimal de comportements que l'agent du lecteur respecte pour que les tests du dépôt compagnon puissent le conduire : ouvrir une conversation, conduire un tour, garder le fil, laisser une trace. | annexe A |
| convention de nommage | *naming convention* | Règle qui préfixe chaque outil par son domaine ; elle évite les collisions de noms lorsque des catalogues sont réunis et aide le modèle à situer l'outil. | chap. 6 |
| cycle | — | Une exécution de la boucle agentique : le modèle observe l'état courant et décide, puis le programme agit. | chap. 5 |

## D

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| *deep learning* | *deep learning* | Sous-ensemble du *machine learning* qui emploie des réseaux de neurones composés de nombreuses couches, capables d'apprendre eux-mêmes les représentations utiles à partir de données brutes. Équivalent français : apprentissage profond. | chap. 1 |
| défenses en profondeur | *defense in depth* | Démarche de conception qui part de l'hypothèse que le modèle sera parfois détourné et cherche à borner ce qui en résulte : limiter, isoler, confirmer, tracer. | chap. 14 |
| définition d'outil | *tool definition* | Nom, description et paramètres d'un outil, transmis au modèle à chaque appel ; le modèle ne voit rien d'autre de l'outil. | chap. 4 |
| demande d'appel d'outil | *tool call* | Sortie du modèle qui indique le nom d'un outil et les valeurs de ses paramètres ; elle n'a aucun effet par elle-même, et c'est le programme qui décide de l'exécuter. | chap. 4 |
| dépôt compagnon | *companion repository* | Dépôt de code qui accompagne les ateliers : applications de test, proxy vers les modèles, coquille d'agent et tests de bout en bout par atelier ; il ne contient pas l'agent. | chap. 3, annexe A |
| dérive d'objectif | *goal drift* | Forme d'échec de la boucle : au fil des étapes, le modèle s'éloigne de la demande initiale. | chap. 5 |
| divulgation progressive | *progressive disclosure* | Principe qui consiste à rendre les informations accessibles au moment où elles deviennent utiles : un sommaire d'abord, puis le détail à la demande. | chap. 9 |
| dossier de conception | *design document* | Document qui reprend, pour chaque atelier du livre, la décision posée, le choix retenu et le coût accepté ; il ne contient aucun programme. | chap. 17 |

## E

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| échantillonnage | *sampling* | Tirage au hasard du *token* suivant parmi les plus plausibles de la distribution calculée par le modèle. | chap. 2 |
| échantillonnage par noyau | *nucleus sampling*, *top-p* | Réglage de décodage qui restreint le tirage au plus petit ensemble de *tokens* dont la probabilité cumulée atteint un seuil donné. | chap. 2 |
| élagage des résultats d'outils | — | Réduction de l'historique qui conserve la trace des appels et remplace les anciens résultats volumineux par une mention abrégée. | chap. 10 |
| enchaînement prédéfini | *workflow* | → voir *workflow* | chap. 5 |
| état de conversation | *conversation state* | Petit ensemble d'informations structurées que le programme conserve à côté de l'historique, met à jour à partir des résultats d'outils et replace à l'identique dans le contexte à chaque cycle ; moyen le plus direct de réaliser la mémoire de travail. | chap. 8 |
| excès de zèle | — | Forme d'échec de la boucle : le modèle fait davantage que ce qui était demandé ; ce travers devient un risque dès qu'il existe des outils d'écriture. | chap. 5 |

## F

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| factualité | *factuality* | Conformité d'un texte aux faits établis ; inventer une référence, une date ou un montant est un défaut de factualité. | chap. 2 |
| fatigue d'approbation | *approval fatigue* | Risque qui apparaît lorsque les demandes de confirmation sont fréquentes : l'utilisateur peut en venir à les accepter sans les lire. | chap. 7 |
| fenêtre de contexte | *context window* | Longueur maximale de la séquence soumise au modèle ; elle se mesure en *tokens* et dépend du modèle. | chap. 2 |
| fidélité | *faithfulness* | Conformité d'un texte à la consigne et au contexte fourni ; faire dire à un document ce qu'il ne dit pas est un défaut de fidélité. | chap. 2 |
| fil rouge | — | Cas fictif qui accompagne le livre depuis le chapitre 3 : l'agent d'une application de gestion, construit atelier après atelier. | chap. 3 |

## G

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| garde-fou | *guardrail* | Contrôle qui encadre ce que l'agent peut faire, comme la confirmation par l'utilisateur, la limitation des droits ou les limites imposées à la boucle. | chap. 4 |
| génération augmentée par récupération | *retrieval-augmented generation*, *RAG* | Principe qui combine ce que le modèle a appris dans ses paramètres avec une mémoire externe interrogée au moment de répondre : on y recherche les passages les plus proches de la question et on les fournit au modèle avec celle-ci. | chap. 4 et 12 |
| génération autorégressive | *autoregressive generation* | Mode de génération dans lequel chaque *token* produit devient une entrée pour les suivants. | chap. 2 |
| grand modèle de langage | *large language model*, *LLM* | Modèle de fondation dont la matière est le texte. Le livre emploie couramment le sigle *LLM*. | chap. 1 |

## H

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| hallucination | *hallucination* | Suite plausible produite par le modèle, mais infidèle à la réalité ou aux sources fournies. | chap. 2 |
| hallucination extrinsèque | *extrinsic hallucination* | Hallucination dans laquelle le texte produit avance quelque chose que la source fournie ne permet ni de confirmer ni d'infirmer. | chap. 2 |
| hallucination intrinsèque | *intrinsic hallucination* | Hallucination dans laquelle le texte produit contredit la source fournie au modèle. | chap. 2 |
| *harness* | *harness* | Ensemble de ce qui entoure le modèle pour en faire un assistant, puis un agent, utilisable : le code qui l'appelle, compose son contexte, exécute ses demandes d'appel d'outil, applique les limites et les permissions, conserve l'état de la conversation et enregistre ce qui s'est passé. Nommé au chapitre 3, le livre l'appelle souvent simplement « le programme ». | chap. 3 |
| historique | *conversation history* | Liste des messages échangés, que le programme conserve et renvoie au modèle ; elle s'allonge à chaque tour. | chap. 3 |
| hôte | *host* | Dans le protocole *MCP*, application construite autour du modèle ; elle conduit la conversation et coordonne ses clients. | chap. 6 |

## I

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| IA générative | *generative AI* | Famille de modèles capables de produire de nouveaux contenus ; celle dont traite le livre repose entièrement sur le *deep learning*. | chap. 1 |
| IA symbolique | *symbolic AI* | Approche de l'IA qui repose sur des connaissances écrites explicitement : des règles, des faits, des procédures de raisonnement. | chap. 1 |
| identifiant d'appel | *tool call ID* | Identifiant que porte chaque demande d'appel d'outil et que reprend le message qui en contient le résultat ; il permet de rapprocher chaque résultat de sa demande. | chap. 4 |
| indexation | *indexing* | Étape qui a lieu avant toute conversation et transforme les documents en une structure que l'on peut interroger rapidement. | chap. 12 |
| ingénierie du contexte | *context engineering* | Travail d'assemblage, à chaque cycle, de ce que le modèle lit : ce qui y entre et sous quelle forme, puis ce qui en est retiré ou résumé lorsque la conversation s'allonge. | chap. 9 |
| injection de *prompt* | *prompt injection* | Fait d'introduire dans l'entrée du modèle un texte conçu pour détourner son comportement de ce que le concepteur et l'utilisateur attendaient. | chap. 14 |
| injection de *prompt* indirecte | *indirect prompt injection* | Injection dans laquelle un tiers place le texte hostile dans un contenu que l'agent lira plus tard : un document, une page, un message, un champ de commentaire, la description d'un outil. | chap. 4 |
| injection directe | *direct prompt injection* | Injection dans laquelle l'utilisateur écrit lui-même dans la conversation un message destiné à faire abandonner au modèle les consignes du concepteur. | chap. 14 |
| intelligence artificielle | *artificial intelligence* | Au sens le plus large, ensemble des techniques qui font accomplir à une machine des tâches que l'on associe à l'intelligence humaine. | chap. 1 |

## J

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| jeton d'authentification | *authentication token* | Secret dont la possession donne un accès au nom d'une identité ; il reste hors du contexte du modèle. Sans rapport avec le *token*, unité de texte. | chap. 7 |
| journal | *log* | Enregistrement des événements d'un composant ; il se distingue de la trace, rattachée à un tour. | chap. 15 |

## L

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| limite d'affichage | — | Borne sur le nombre de lignes qu'un outil renvoie au modèle ; elle protège la fenêtre de contexte, et le résultat signale qu'il est partiel, indique le total et le moyen d'obtenir la suite. | chap. 9 |
| limite de budget | *budget limit* | Plafond de la consommation d'un tour, mesurée en *tokens* lus et produits ou dans l'unité de facturation du service. | chap. 7 |
| limite de cycles | — | Nombre maximal de cycles qu'un tour peut compter ; imposée par le programme, elle sert de garde-fou. | chap. 5 |
| limite de durée | *time limit* | Borne de temps appliquée au tour entier et à chaque appel d'outil, afin qu'un outil bloqué n'immobilise pas la boucle. | chap. 7 |
| liste d'autorisation | *allowlist* | Liste qui énumère les destinations réseau permises ; toute autre destination est refusée. | chap. 7 |
| *LLM* | *LLM* | → voir grand modèle de langage | chap. 1 |

## M

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| *machine learning* | *machine learning* | Ensemble de techniques dans lesquelles un algorithme ajuste les paramètres d'un modèle à partir d'exemples, afin de reproduire la relation observée dans ces exemples. Équivalent français : apprentissage automatique. | chap. 1 |
| *MCP* | *MCP* | → voir *Model Context Protocol* | chap. 6 |
| mémoire de travail | *working memory* | Dans ce livre, sous-ensemble des informations dont l'agent a besoin pour mener la tâche en cours, que le *harness* place délibérément à sa portée à chaque cycle, quelle que soit la place qui reste dans la fenêtre de contexte. | chap. 8 |
| mémoire persistante | *persistent memory*, souvent *long-term memory* | Informations enregistrées hors de la fenêtre de contexte, pendant une conversation ou après elle, et relues lors d'une conversation ultérieure. | chap. 11 |
| message | *message* | Élément de la séquence soumise au modèle, attribué à un rôle. | chap. 3 |
| message système | *system prompt* | → voir *system prompt* | chap. 3 |
| métrique | *metric* | Mesure agrégée sur un grand nombre de tours ; elle se distingue de la trace, qui décrit un seul tour. | chap. 15 |
| *Model Context Protocol* | *Model Context Protocol*, *MCP* | Protocole ouvert, abrégé en *MCP*, qui normalise la manière dont une application construite autour d'un modèle de langage découvre et utilise des capacités fournies par d'autres programmes. | chap. 6 |
| modèle | *model* | Composant qui transforme un texte d'entrée en texte de sortie ; il ne conserve rien d'un appel à l'autre et n'agit pas par lui-même. | chap. 1 |
| modèle de fondation | *foundation model* | Modèle entraîné sur des données larges, à grande échelle, et adaptable à un vaste éventail de tâches en aval. | chap. 1 |
| modèle de langage | *language model* | Modèle génératif qui apprend à prolonger une séquence de texte. | chap. 1 |
| modèle de *prompt* | *prompt template* | Dans le protocole *MCP*, trame d'instructions réutilisable pour une tâche donnée, qu'un serveur expose et dont l'emploi revient le plus souvent à l'utilisateur. | chap. 6 |
| modèle discriminatif | *discriminative model* | Modèle qui reçoit une entrée et prédit une étiquette ou une valeur. | chap. 1 |
| modèle génératif | *generative model* | Modèle qui apprend la distribution des données elles-mêmes et peut produire de nouveaux exemples qui ressemblent à ceux qu'il a vus. | chap. 1 |
| modèle juge | *LLM-as-a-judge* | Modèle auquel on confie le jugement d'une réponse, en lui fournissant la demande, la réponse de référence, la réponse obtenue et des critères. | chap. 15 |
| moindre privilège (principe du) | *least privilege* | Principe selon lequel chaque programme et chaque utilisateur opère avec l'ensemble de droits le plus réduit qui lui permette d'accomplir sa tâche. | chap. 7 |

## N

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| non-déterminisme | *non-determinism* | Propriété d'un système dans lequel des appels identiques peuvent donner des textes différents, parce que le décodage comporte un tirage aléatoire. | chap. 2 |

## O

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| outil | *tool* | Opération que le programme exécute à la demande du modèle ; elle est décrite par un nom, une description et des paramètres, et renvoie un résultat sous forme de texte. | chap. 4 |
| outil d'écriture | *write tool* | Outil qui modifie l'état d'un système : créer une demande, valider une facture, envoyer un message. | chap. 4 |
| outil de lecture | *read tool* | Outil qui obtient une information sans rien modifier : consulter une commande, chercher un produit, lire un document. | chap. 4 |
| outil générique | *generic tool* | Outil qui interroge une source de données quelconque : le modèle indique la source, les filtres, les champs souhaités, le tri et un éventuel agrégat. | chap. 6 |
| outil spécialisé | *specialized tool* | Outil qui répond à une question métier ; il a peu de paramètres, et sa logique est écrite par le concepteur. | chap. 6 |

## P

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| parcours métier | — | Parcours d'évaluation tiré des métiers servis par l'agent : il décrit une situation de départ, les messages de l'utilisateur et ce qui est attendu. | chap. 15 |
| passage | *chunk* | Fragment d'un document, découpé lors de l'indexation, que la recherche peut retrouver et remettre au modèle. | chap. 12 |
| plafond de récupération | — | Borne sur le nombre de lignes qu'un outil va chercher ; elle protège le système interrogé, et lorsqu'elle est atteinte le total annoncé est un minimum. | chap. 9 |
| préchargement | *preloading* | Chargement d'un *skill* indiqué par l'application avant le premier appel au modèle ; il épargne un cycle mais suppose un signal fiable de la tâche en cours. | chap. 13 |
| préparer, valider, soumettre | — | Organisation en trois temps d'une action qui modifie un système : l'agent construit un brouillon sans effet, l'utilisateur le confirme sur un récapitulatif, puis le *harness* le soumet. | chap. 7 |
| *prompt* | *prompt* | Texte d'entrée soumis au modèle. | chap. 1 |
| *prompt engineering* | *prompt engineering* | Art de rédiger des consignes efficaces. | chap. 9 |

## R

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| *RAG* | *RAG* | → voir génération augmentée par récupération | chap. 4 et 12 |
| rappel | *recall* | Parmi les *k* premiers résultats d'une recherche, part des questions pour lesquelles un passage attendu y figure. | chap. 12 |
| recherche hybride | *hybrid search* | Recherche qui exécute une recherche lexicale et une recherche sémantique, puis fusionne leurs classements. | chap. 12 |
| recherche lexicale | *lexical search* | Recherche qui compare les mots de la question à ceux des passages ; précise sur les termes exacts, elle échoue lorsque la question et le passage n'emploient pas les mêmes mots. | chap. 12 |
| recherche sémantique | *semantic search* | Recherche des passages dont la représentation vectorielle est proche de celle de la question ; elle retrouve un passage pertinent même s'il n'emploie aucun des mots de la question. | chap. 12 |
| reclassement | *reranking* | Second examen, plus coûteux, d'un petit nombre de passages candidats, pour les ordonner selon leur pertinence. | chap. 12 |
| rejeu | *replay* | Mode d'évaluation dans lequel l'outil renvoie une réponse enregistrée lors d'une exécution antérieure, ce qui permet d'observer le comportement de l'agent à données constantes. | chap. 15 |
| repli | *fallback* | Fait d'adresser la requête à une autre ressource, autre point d'accès ou autre modèle, lorsque la première fait défaut. | chap. 16 |
| représentations vectorielles | *embeddings* | Vecteurs qu'un modèle dédié produit à partir de textes, de telle sorte que deux textes de sens voisin aient des vecteurs voisins. | chap. 12 |
| résolution de noms | *name resolution* | Étape confiée à un outil : il reçoit un nom et le type d'objet recherché, effectue la comparaison approchée dans le programme et renvoie les candidats avec leur identifiant. | chap. 6 |
| ressource | *resource* | Dans le protocole *MCP*, données qu'un serveur propose à la lecture pour enrichir le contexte ; leur emploi est décidé par l'hôte. | chap. 6 |
| résumé | *summarization* | Réduction de l'historique dans laquelle un modèle rédige une version plus courte de la partie ancienne, que le programme substitue aux échanges concernés. | chap. 10 |
| révélation progressive des outils | — | Pratique qui ne présente un outil au modèle que lorsque le *skill* qui en décrit l'usage est chargé. | chap. 13 |
| rôle | *role* | Attribut d'un message, qui indique ce qu'il porte : consignes du concepteur (système), texte de la personne (utilisateur), réponse du modèle (assistant) ou résultat d'un outil (outil). | chap. 3 |

## S

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| *sandbox* | *sandbox* | Environnement d'exécution dont les accès sont déclarés à l'avance : dossiers lisibles et inscriptibles, destinations réseau joignables, variables de configuration visibles, mémoire et temps de calcul disponibles. | chap. 7 |
| *sandboxing* | *sandboxing* | Exécution des outils dans une *sandbox* ; ce qui n'a pas été accordé est refusé par le système qui héberge l'exécution. | chap. 7 |
| sans état | *stateless* | Se dit d'un modèle qui ne conserve rien d'un appel à l'autre. Au chapitre 6, se dit aussi d'un échange dans lequel chaque requête porte tout ce qui est nécessaire à son traitement. | chap. 2 |
| secret | *secret* | Information dont la possession donne un accès : mot de passe, clé de service, jeton d'authentification, chaîne de connexion. | chap. 7 |
| serveur | *server* | Dans le protocole *MCP*, programme qui fournit des capacités : il annonce ce qu'il sait faire et exécute ce qu'on lui demande. | chap. 6 |
| serveur d'outils | *tool server* | Programme distinct de celui de l'agent, joint par un protocole standard, dans lequel les outils s'exécutent. | chap. 6 |
| *skill* | *skill* | Savoir-faire nommé que l'agent peut charger au cours d'une conversation ; il se compose d'une description, d'instructions et de ressources éventuelles. | chap. 13 |
| stratégie de décodage | *decoding strategy* | Manière de tirer un *token* de la distribution de probabilité calculée par le modèle ; c'est un réglage de celui qui appelle le modèle. | chap. 2 |
| *system prompt* | *system prompt* | Texte que le concepteur place en tête de chaque conversation pour orienter le comportement de l'assistant. Équivalent français : message système. | chap. 3 |

## T

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| température | *temperature* | Réglage de décodage qui resserre ou étale la distribution : basse, elle favorise fortement les *tokens* les plus probables ; élevée, elle laisse leur chance aux autres. | chap. 2 |
| *token* | *token* | Fragment de texte issu d'un vocabulaire fixe, établi avant l'entraînement : mot entier, partie de mot ou caractère. C'est l'unité de travail du modèle. | chap. 2 |
| tour | *turn* | Ensemble des cycles qui séparent la demande de l'utilisateur de la réponse finale. | chap. 5 |
| trace | *trace* | Enregistrement structuré de ce qui s'est produit au cours d'un tour, rattaché à un identifiant unique. | chap. 15 |
| trace minimale | — | Enregistrement que laisse chaque tour de l'agent dès le premier atelier, pour observer ses trajectoires et mesurer son contexte. | chap. 3, annexe A |
| trajectoire | *trajectory* | Suite des décisions prises et des résultats obtenus au cours d'un tour. | chap. 5 |
| Transformer | *Transformer* | Architecture de réseau de neurones, introduite pour la traduction automatique, qui s'appuie sur un mécanisme d'attention mettant en relation les éléments d'une séquence. | chap. 1 |
| transmission en continu | *streaming* | Envoi de la réponse à l'interface à mesure qu'elle est produite. | chap. 3 |
| traversée de répertoires | *path traversal* | Situation dans laquelle un chemin construit à partir d'une valeur que le serveur ne maîtrise pas sort du périmètre de fichiers prévu. | chap. 7 |
| troncature | *truncation* | Réduction de l'historique qui retire les messages les plus anciens. Se dit aussi d'un résultat d'outil dont une partie seulement est renvoyée. | chap. 9, 10 |

## V

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| validation des paramètres | *parameter validation* | Vérification, avant toute exécution, de chaque demande d'appel contre le schéma formel qui décrit les paramètres de l'outil. | chap. 4 |
| validation humaine | *human-in-the-loop* | Suspension d'une action jusqu'à la décision d'une personne. | chap. 7 |

## W

| Terme français | Terme anglais | Définition | Chapitre |
|---|---|---|---|
| *workflow* | *workflow* | Organisation dans laquelle le concepteur a prévu le chemin : le programme appelle le modèle à des points précis, pour des tâches délimitées, et sa logique détermine l'étape à exécuter ensuite. Équivalent français : enchaînement prédéfini. | chap. 5 |

## Index anglais-français

| English term | Terme français |
|---|---|
| *agent* | agent |
| *agentic loop* | boucle agentique |
| *allowlist* | liste d'autorisation |
| *approval fatigue* | fatigue d'approbation |
| *artificial intelligence* | intelligence artificielle |
| *assistant* | assistant |
| *authentication token* | jeton d'authentification |
| *autoregressive generation* | génération autorégressive |
| *budget limit* | limite de budget |
| *cache* | cache |
| *chain of thought* | chaîne de pensée |
| *chatbot* | *chatbot* |
| *chunk* | passage |
| *client* | client |
| *coding agent* | *coding agent* |
| *compaction* | compaction |
| *companion repository* | dépôt compagnon |
| *compounding errors* | accumulation d'erreurs |
| *context* | contexte |
| *context engineering* | ingénierie du contexte |
| *context window* | fenêtre de contexte |
| *conversation history* | historique |
| *conversation loop* | boucle conversationnelle |
| *conversation state* | état de conversation |
| *conversational agent* | agent conversationnel |
| *data isolation* | cloisonnement |
| *decoding strategy* | stratégie de décodage |
| *deep learning* | *deep learning* |
| *defense in depth* | défenses en profondeur |
| *design document* | dossier de conception |
| *direct prompt injection* | injection directe |
| *discriminative model* | modèle discriminatif |
| *embeddings* | représentations vectorielles |
| *extrinsic hallucination* | hallucination extrinsèque |
| *factuality* | factualité |
| *faithfulness* | fidélité |
| *fallback* | repli |
| *fine-tuning* | ajustement fin |
| *foundation model* | modèle de fondation |
| *function calling* | appel d'outil |
| *generative AI* | IA générative |
| *generative model* | modèle génératif |
| *generic tool* | outil générique |
| *goal drift* | dérive d'objectif |
| *guardrail* | garde-fou |
| *hallucination* | hallucination |
| *harness* | *harness* |
| *host* | hôte |
| *human-in-the-loop* | validation humaine |
| *hybrid search* | recherche hybride |
| *idempotency key* | clé d'idempotence |
| *in-context learning* | apprentissage en contexte |
| *indexing* | indexation |
| *indirect prompt injection* | injection de *prompt* indirecte |
| *instructions* | consignes |
| *interface contract* | contrat d'interface |
| *intrinsic hallucination* | hallucination intrinsèque |
| *language model* | modèle de langage |
| *large language model* | grand modèle de langage |
| *least privilege* | moindre privilège (principe du) |
| *lexical search* | recherche lexicale |
| *LLM* | grand modèle de langage |
| *LLM-as-a-judge* | modèle juge |
| *log* | journal |
| *long-term memory* | mémoire persistante |
| *machine learning* | *machine learning* |
| *MCP* | *Model Context Protocol* |
| *message* | message |
| *metric* | métrique |
| *model* | modèle |
| *Model Context Protocol* | *Model Context Protocol* |
| *name resolution* | résolution de noms |
| *naming convention* | convention de nommage |
| *non-determinism* | non-déterminisme |
| *nucleus sampling* | échantillonnage par noyau |
| *parameter validation* | validation des paramètres |
| *path traversal* | traversée de répertoires |
| *persistent memory* | mémoire persistante |
| *preloading* | préchargement |
| *progressive disclosure* | divulgation progressive |
| *prompt* | *prompt* |
| *prompt engineering* | *prompt engineering* |
| *prompt injection* | injection de *prompt* |
| *prompt template* | modèle de *prompt* |
| *RAG* | génération augmentée par récupération |
| *read tool* | outil de lecture |
| *recall* | rappel |
| *replay* | rejeu |
| *reranking* | reclassement |
| *resource* | ressource |
| *retrieval-augmented generation* | génération augmentée par récupération |
| *role* | rôle |
| *sampling* | échantillonnage |
| *sandbox* | *sandbox* |
| *sandboxing* | *sandboxing* |
| *secret* | secret |
| *semantic search* | recherche sémantique |
| *server* | serveur |
| *service account* | compte de service |
| *skill* | *skill* |
| *skill catalog* | catalogue de *skills* |
| *specialized tool* | outil spécialisé |
| *stateful* | avec état |
| *stateless* | sans état |
| *stopping condition* | condition d'arrêt |
| *streaming* | transmission en continu |
| *summarization* | résumé |
| *symbolic AI* | IA symbolique |
| *system prompt* | *system prompt* |
| *temperature* | température |
| *time limit* | limite de durée |
| *token* | *token* |
| *tool* | outil |
| *tool call* | demande d'appel d'outil |
| *tool call ID* | identifiant d'appel |
| *tool calling* | appel d'outil |
| *tool definition* | définition d'outil |
| *tool server* | serveur d'outils |
| *top-p* | échantillonnage par noyau |
| *trace* | trace |
| *trajectory* | trajectoire |
| *Transformer* | Transformer |
| *truncation* | troncature |
| *turn* | tour |
| *untrusted content* | contenu non fiable |
| *workflow* | *workflow* |
| *working memory* | mémoire de travail |
| *write tool* | outil d'écriture |
