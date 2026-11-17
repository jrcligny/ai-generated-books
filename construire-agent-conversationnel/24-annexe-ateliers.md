# Annexe A — Réaliser les ateliers

Cette annexe décrit ce dont vous avez besoin pour réaliser les ateliers du livre : le dépôt compagnon et ce qu'il fournit, son installation, le contrat d'interface que respecte votre agent, la trace minimale que laisse chaque tour, et la manière dont les tests de bout en bout vérifient le critère de réussite de chaque atelier.

## Les ateliers et le dépôt compagnon

À partir du chapitre 3, chaque chapitre comporte un atelier qui fait évoluer l'agent du fil rouge. Le texte de l'atelier expose la décision prise pour cet agent et ce qu'elle coûte. À vous ensuite de la réaliser : vous construisez votre propre agent, atelier après atelier, en appliquant le choix retenu. Aucun corrigé n'est fourni.

Dans le livre, l'expression **dépôt compagnon** désigne le dépôt de code qui accompagne les ateliers, publié à l'adresse *https://github.com/jrcligny/workshops-build-conversational-agent*. Il ne contient pas l'agent ; il fournit tout ce qui l'entoure :

- une application de gestion simulée, qui expose les commandes, les achats et les factures du fil rouge, avec leurs rôles, leurs droits et deux organisations distinctes ;
- une application de recherche documentaire, dont la documentation est rangée dans de simples fichiers texte, utilisée à partir du chapitre 12 ;
- un proxy par lequel passent tous les appels aux modèles, qui garde la clé d'accès hors de votre agent et permet de travailler avec un modèle simulé avant de disposer d'un modèle réel ;
- une coquille d'agent, qui offre l'interface de conversation, l'accès au modèle par le proxy et l'écriture des traces, mais ni la boucle ni le *system prompt* ;
- un serveur d'outils MCP vide, que vous compléterez au chapitre 6 ;
- un dossier de tests de bout en bout par atelier, accompagné d'un guide en français.

Le livre ne prescrit aucun modèle : ceux que vous utiliserez sont accessibles par le proxy.

## Installer le dépôt et lancer les tests

Le dépôt compagnon cible d'abord Windows, et fonctionne aussi sous Linux et macOS. Il demande Python 3.13, de préférence installé depuis *python.org* ou par l'outil uv, et le gestionnaire de projets Python uv. Le fichier *docs/installation.md* du dépôt détaille l'installation pour chaque système et le diagnostic des erreurs les plus fréquentes.

Les commandes se lancent depuis la racine du dépôt. Sous Windows, dans PowerShell, la préparation tient en quelques lignes, présentées dans l'exemple A-1.

*Exemple A-1 — Installer le dépôt compagnon*

```powershell
git clone https://github.com/jrcligny/workshops-build-conversational-agent.git
cd workshops-build-conversational-agent
uv python install 3.13
uv sync --project tooling/cli --locked --python 3.13
uv sync --project tooling/cli --group tests --locked --python 3.13
Copy-Item .env.example .env
python start.py
```

La commande `python start.py` démarre les applications de test, le proxy et l'interface de conversation, accessible à l'adresse *http://127.0.0.1:8080*. Par défaut, le fichier *.env* règle le proxy sur un modèle simulé, qui suffit pour commencer l'atelier du chapitre 3. À partir de l'atelier du chapitre 4, l'agent doit choisir lui-même ses outils, ce que le modèle simulé ne fait pas : passez alors en mode réel en renseignant dans *.env* l'accès à un modèle hébergé dans Azure OpenAI. Le guide *GETTING_STARTED.md* du dépôt indique les variables à définir.

Chaque atelier se manipule avec la commande `workshop` du dépôt, désigné par le numéro de son chapitre, qui est aussi celui de son dossier (tableau A-1). L'exemple A-2 en montre les trois usages.

*Exemple A-2 — Afficher un atelier et lancer ses tests*

```powershell
# Afficher le guide de l'atelier du chapitre 9
uv run --project tooling/cli workshop start 09
# Lancer les tests de bout en bout de cet atelier
uv run --project tooling/cli workshop check 09
# Lancer aussi les tests des ateliers des chapitres précédents
uv run --project tooling/cli workshop check 09 --non-regression
```

## Le contrat d'interface

Pour que les tests puissent conduire n'importe quel agent, le vôtre respecte un contrat d'interface minimal, identique pour tous les ateliers. Le chapitre 3 l'introduit ; en voici les quatre obligations.

- **Ouvrir une conversation** : l'agent accepte la création d'une conversation pour un utilisateur donné, avec son rôle et son organisation, et lui attribue un identifiant.
- **Conduire un tour** : pour chaque message reçu dans une conversation, l'agent transmet sa réponse en continu, sous la forme d'une suite d'événements, faite de fragments de texte puis d'un événement de fin qui indique si le tour a abouti. Un événement d'erreur signale un échec.
- **Garder le fil** : les messages suivants réutilisent l'identifiant de la conversation, et l'agent rejoue l'historique dans l'entrée du modèle.
- **Laisser une trace** : chaque tour produit un enregistrement qui contient les identifiants de la conversation et du tour, l'horodatage, l'entrée remise au modèle (consignes, historique, nouveau message), le modèle appelé, le nombre de *tokens*, la durée et la raison de l'arrêt, le texte produit et les outils appelés. Aucun secret n'y figure.

D'autres événements, comme les étapes en cours, une demande de confirmation, les sources ou une mention ajoutée sous la réponse, font partie du contrat ; ils restent inutilisés jusqu'à l'atelier qui en a besoin. La coquille fournit l'ossature de ce contrat, et vous écrivez ce qui détermine le comportement de l'agent.

Cette **trace minimale** vous servira dès le chapitre 5, puis au chapitre 9, pour observer les trajectoires de l'agent et mesurer son contexte. Le chapitre 15 la transforme en trace de bout en bout, aux données sensibles masquées.

## Les tests de bout en bout et le critère de réussite

Chaque atelier se termine par un critère de réussite vérifiable. Les tests de bout en bout du dépôt compagnon le mettent à l'épreuve, et ils sont rangés dans un dossier par atelier, qui porte le numéro du chapitre. Le chapitre 8 n'a pas d'atelier : l'état de conversation qu'il décrit est construit dans celui du chapitre 10. Le tableau A-1 indique le dossier de chaque atelier.

Les ateliers des chapitres 5, 6 et 7 réunissent plusieurs décisions, que vous réalisez en étapes successives sur un même scénario. Chaque étape a ses propres tests, et l'option `--etape` les lance seuls, par exemple `workshop check 07 --etape identite` ; sans cette option, la commande vérifie le critère de réussite entier.

Tant que vous n'avez pas réalisé un atelier, ses tests échouent : c'est attendu, et non un défaut d'installation. Vous pouvez lancer les tests d'un atelier seul, ou vérifier avec l'option `--non-regression` que rien n'a régressé dans les ateliers des chapitres précédents.

Les guides de plusieurs ateliers vous demandent aussi d'écrire le parcours d'évaluation du cas limite qu'ils introduisent, dans le dossier *my-agent/routes/* du dépôt compagnon. L'atelier du chapitre 15 consolide ces parcours en un jeu complet.

Un atelier facultatif, hors du parcours, construit l'option écartée au chapitre 11 : une mémoire de préférences que l'utilisateur peut consulter, corriger et effacer. Son dossier, *workshops/bonus-preference-memory/*, n'est pas lancé par l'option `--non-regression`.

*Tableau A-1 — Les ateliers et leurs dossiers de tests*

| Chapitre | Atelier | Dossier de tests du dépôt compagnon |
|---|---|---|
| 3 | Le *system prompt* | *workshops/03-system-prompt/tests/* |
| 4 | Le premier outil | *workshops/04-first-tool/tests/* |
| 5 | Les outils de lecture et la boucle agentique | *workshops/05-agent-loop/tests/* |
| 6 | Le serveur d'outils MCP et les regroupements | *workshops/06-mcp-server/tests/* |
| 7 | L'identité, les écritures et le confinement | *workshops/07-acting-rights/tests/* |
| 9 | La divulgation progressive | *workshops/09-progressive-disclosure/tests/* |
| 10 | L'état de conversation et la compaction | *workshops/10-context-compaction/tests/* |
| 11 | La mémoire persistante | *workshops/11-no-memory/tests/* |
| 12 | La recherche documentaire | *workshops/12-document-search/tests/* |
| 13 | Les *skills* | *workshops/13-skills/tests/* |
| 14 | La défense contre l'injection de prompt | *workshops/14-read-without-obeying/tests/* |
| 15 | Les traces et l'évaluation | *workshops/15-evaluation/tests/* |
| 16 | Les pannes | *workshops/16-failures/tests/* |
| 17 | La spécification d'un contrôle | *workshops/17-specification/tests/* |

Ce qui se vérifie par programme l'est : l'état de l'application simulée, le contenu de la trace, les droits appliqués. Lorsqu'un critère porte sur la qualité d'une réponse, comme un refus justifié ou une limite annoncée, un modèle juge l'apprécie selon une grille écrite. L'agent ne répondant pas deux fois de la même manière, ces appréciations portent sur plusieurs exécutions. Le chapitre 15 explique pourquoi cette combinaison s'impose.

> **Point clé**
>
> Le critère de réussite et ses tests disent ce que votre agent doit faire, pas comment l'écrire. Un test qui passe établit que le critère est atteint sur les cas essayés, rien de plus.
