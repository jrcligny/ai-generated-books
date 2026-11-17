# Préface

Un LLM rédige. Un assistant répond à ce qu'on lui demande. Un agent décide de ce qu'il fait ensuite, appelle des outils et finit par agir sur une application. Ce livre décrit ce qui sépare ces trois systèmes, et surtout ce qu'il faut construire autour du modèle pour que le troisième reste utile, sûr et vérifiable.

Il suit un seul exemple du début à la fin : l'assistant d'une application de gestion des commandes, des achats et des factures, qui devient peu à peu un agent. Chaque chapitre part d'une difficulté rencontrée par cet agent, en tire une notion, puis montre la décision de conception qu'elle impose.

## À qui s'adresse ce livre

Ce livre s'adresse aux développeurs, architectes et responsables techniques qui doivent concevoir, intégrer ou faire évoluer un agent conversationnel dans une application métier. Il convient aussi à qui doit juger un tel projet sans l'écrire : il explique ce que coûte chaque choix et ce qu'il laisse incertain.

Aucune connaissance préalable de l'apprentissage automatique n'est nécessaire : les chapitres 1 et 2 posent ce qu'il faut savoir des modèles. Il vous sera utile d'avoir déjà écrit un programme qui appelle un service web et manipule des données au format JSON. Les ateliers demandent de savoir programmer en Python.

## Organisation du livre

Le livre compte dix-sept chapitres, répartis en cinq parties. Chaque partie s'ouvre sur une courte présentation de la question qu'elle traite.

- La **partie I**, « Fondations : du modèle à l'assistant outillé » (chapitres 1 à 4), situe l'IA générative, explique comment un modèle produit du texte, puis construit un assistant et lui donne un premier outil.
- La **partie II**, « Agir : la boucle, les outils et le droit d'agir » (chapitres 5 à 7), fait de l'assistant un agent : la boucle qui enchaîne les décisions, des outils conçus pour un lecteur qui est un modèle, et les règles qui encadrent les actions.
- La **partie III**, « Garder le contexte utile » (chapitres 8 à 10), traite ce que l'agent tient à part, ce qu'il laisse entrer dans le contexte et ce qu'il en retire quand la conversation dure.
- La **partie IV**, « Ce que l'agent lit » (chapitres 11 à 14), examine ce que l'agent peut remettre dans le contexte : souvenirs, documents, procédures, et contenus écrits par des tiers.
- La **partie V**, « Éprouver et maintenir » (chapitres 15 à 17), montre comment observer et évaluer l'agent, le faire tenir quand une dépendance fait défaut, et confier une partie de sa construction à un agent de programmation.

La conclusion rassemble les principes qui restent valables quand les modèles changent. L'annexe A explique comment réaliser les ateliers, et le glossaire donne l'équivalent anglais de chaque terme.

Les chapitres se lisent dans l'ordre : chacun suppose les notions et l'agent des précédents.

## Les ateliers et le dépôt compagnon

À partir du chapitre 3, chaque chapitre, sauf le chapitre 8, se termine par un atelier. L'atelier expose la décision prise pour l'agent du fil rouge, les options écartées, ce que coûte le choix retenu et le critère de réussite qui permet de le vérifier. À vous ensuite de le réaliser : vous construisez votre propre agent, atelier après atelier.

Le dépôt compagnon, *https://github.com/jrcligny/workshops-build-conversational-agent*, fournit tout ce qui entoure l'agent : les applications de test, une coquille d'agent et les tests de bout en bout de chaque atelier, mais aucun corrigé. L'annexe A explique comment l'installer et lancer les tests.

Si vous réalisez les ateliers avec l'aide d'un agent de programmation, lisez d'abord le chapitre 17 : il explique ce qu'on peut lui confier et comment garder la main sur ce qu'il produit.

## Conventions

Ce livre emploie les conventions typographiques suivantes.

- **Gras** : un terme à l'endroit où il est défini. Le glossaire reprend ces termes.
- *Italique* : les mots étrangers, comme *harness* ou *token*, les chemins de fichiers et les adresses web. Les sigles restent en romain.
- « Guillemets » : les noms des outils et des *skills* de l'agent, comme l'outil « résoudre un nom ».
- `Police à chasse fixe` : le code et les messages échangés avec un modèle, dans les exemples numérotés.

Quatre sortes d'encadrés ponctuent le texte.

> **Point clé**
>
> L'idée à retenir d'une section.

Les avertissements signalent une erreur fréquente ou coûteuse.

> **Attention**
>
> Un piège de conception, et ce qu'il entraîne.

Les retours de terrain rapportent des pratiques observées sur des projets d'agents en production. Ils ne s'appuient pas sur une étude publiée : lisez-les comme des retours d'expérience, à confronter à votre contexte.

> **Sur le terrain**
>
> Une pratique, et la situation qui la justifie.

Enfin, certains encadrés approfondissent un point hors du fil principal ; vous pouvez les passer en première lecture.

> **Pour aller plus loin**
>
> Un mécanisme, une mesure ou une référence complémentaire.

Le domaine évolue vite, et toutes les affirmations n'ont pas le même appui. Le livre distingue trois degrés : ce qui est **établi**, par la recherche publiée ou par la spécification d'un protocole ; ce qui relève de la **pratique courante**, répandue sans être démontrée ; et ce qui reste une **zone d'incertitude**, sur laquelle les travaux et les praticiens ne s'accordent pas. Les encadrés « Zone d'incertitude » signalent ces dernières.

Les références sont données à la fin de chaque chapitre, sous la forme auteur et année dans le texte.

## Comment ce livre a été écrit

Ce livre a été rédigé avec l'aide d'outils d'IA générative. Son plan, ses choix de contenu et ses relectures relèvent de son auteur. Les faits rapportés s'appuient sur les références citées ; les encadrés « Sur le terrain » rapportent des pratiques et non des résultats mesurés.
