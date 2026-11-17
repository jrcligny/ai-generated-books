# Annexe A — Réaliser les ateliers

Cette annexe décrit ce dont vous avez besoin pour réaliser les ateliers du livre : le dépôt compagnon et ce qu'il fournit, le contrat d'interface que respecte votre agent, la trace minimale que laisse chaque tour, et la manière dont les tests de bout en bout vérifient le critère de réussite de chaque atelier.

## Les ateliers et le dépôt compagnon

À partir du chapitre 3, chaque chapitre comporte un atelier qui fait évoluer l'agent du fil rouge. Le texte de l'atelier expose la décision prise pour cet agent et ce qu'elle coûte. À vous ensuite de la réaliser : vous construisez votre propre agent, atelier après atelier, en appliquant le choix retenu. Aucun corrigé n'est fourni.

Dans le livre, l'expression **dépôt compagnon** désigne le dépôt de code qui accompagne les ateliers. Il ne contient pas l'agent ; il fournit tout ce qui l'entoure :

- une application de gestion simulée, qui expose les commandes, les achats et les factures du fil rouge, avec leurs rôles, leurs droits et deux organisations distinctes ;
- une application de recherche documentaire, dont la documentation est rangée dans de simples fichiers texte, utilisée à partir du chapitre 13 ;
- un proxy par lequel passent tous les appels aux modèles, qui garde la clé d'accès hors de votre agent et permet de travailler avec un modèle simulé avant de disposer d'un modèle réel ;
- une coquille d'agent, qui offre l'interface de conversation, l'accès au modèle par le proxy et l'écriture des traces, mais ni la boucle ni le *system prompt* ;
- un serveur d'outils *MCP* vide, que vous compléterez au chapitre 7 ;
- un dossier de tests de bout en bout par atelier.

Le livre ne prescrit aucun modèle : ceux que vous utiliserez sont accessibles par le proxy.

## Le contrat d'interface

Pour que les tests puissent conduire n'importe quel agent, le vôtre respecte un contrat d'interface minimal, identique pour tous les ateliers.

- **Ouvrir une conversation.** L'agent accepte la création d'une conversation pour un utilisateur donné, avec son rôle et son organisation, et lui attribue un identifiant.
- **Conduire un tour.** Pour chaque message reçu dans une conversation, l'agent transmet sa réponse en continu, sous la forme d'une suite d'événements : des fragments de texte, puis un événement de fin qui indique si le tour a abouti. Un événement d'erreur signale un échec.
- **Garder le fil.** Les messages suivants réutilisent l'identifiant de la conversation, et l'agent rejoue l'historique dans l'entrée du modèle.
- **Laisser une trace.** Chaque tour produit un enregistrement : les identifiants de la conversation et du tour, l'horodatage, l'entrée remise au modèle (consignes, historique, nouveau message), le modèle appelé, le nombre de *tokens*, la durée et la raison de l'arrêt, le texte produit et les outils appelés. Aucun secret n'y figure.

D'autres événements, comme les étapes en cours, une demande de confirmation, les sources ou une mention ajoutée sous la réponse, font partie du contrat ; ils restent inutilisés jusqu'à l'atelier qui en a besoin. La coquille fournit l'ossature de ce contrat, et vous écrivez ce qui détermine le comportement de l'agent.

Cette **trace minimale** vous servira dès le chapitre 6, puis au chapitre 10, pour observer les trajectoires de l'agent et mesurer son contexte. Le chapitre 16 la transforme en trace de bout en bout, aux données sensibles masquées.

## Le critère de réussite

Chaque atelier se termine par un critère de réussite vérifiable. Les tests de bout en bout du dépôt compagnon le mettent à l'épreuve, et ils sont rangés dans un dossier par atelier ; l'atelier du chapitre 8, qui réunit quatre décisions, est découpé en quatre ateliers, de 8a à 8d. Le tableau A-1 indique le dossier de chaque atelier, dans l'ordre des chapitres ; les numéros des dossiers ne suivent pas toujours ceux des chapitres. Tant que vous n'avez pas réalisé un atelier, ses tests échouent : c'est attendu, et non un défaut d'installation. Vous pouvez lancer les tests d'un atelier seul, ou avec ceux des ateliers précédents pour vérifier que rien n'a régressé.

*Tableau A-1 — Les ateliers et leurs dossiers de tests*

| Chapitre | Atelier | Dossier de tests du dépôt compagnon |
|---|---|---|
| 3 | Le *system prompt* | *workshops/03-system-prompt/tests/* |
| 4 | Le premier outil | *workshops/04-first-tool/tests/* |
| 5 | Les outils de lecture | *workshops/05-read-tools/tests/* |
| 6 | La boucle agentique | *workshops/06-agent-loop/tests/* |
| 7 | Le serveur d'outils *MCP* | *workshops/09-mcp/tests/* |
| 8a à 8d | L'identité, les écritures, les regroupements, le confinement | *workshops/10a-identity/tests/*, *workshops/10b-writes/tests/*, *workshops/10c-groupings/tests/*, *workshops/10d-sandboxing/tests/* |
| 9 | L'état de conversation | *workshops/08-context-compaction/tests/* |
| 10 | La découverte progressive | *workshops/07-progressive-disclosure/tests/* |
| 11 | La compaction | *workshops/08-context-compaction/tests/* |
| 12 | La mémoire persistante | *workshops/12-long-term-memory/tests/* |
| 13 | La recherche documentaire | *workshops/13-document-search/tests/* |
| 14 | Les *skills* | *workshops/14-skills/tests/* |
| 15 | Lire sans obéir | *workshops/15-read-without-obeying/tests/* |
| 16 | Les traces et l'évaluation | *workshops/17-evaluation/tests/* |
| 17 | Les pannes | *workshops/18-failures/tests/* |
| 18 | La spécification d'un contrôle | *workshops/19-specification/tests/* |

Ce qui se vérifie par programme l'est : l'état de l'application simulée, le contenu de la trace, les droits appliqués. Lorsqu'un critère porte sur la qualité d'une réponse, comme un refus justifié ou une limite annoncée, un modèle juge l'apprécie selon une grille écrite. L'agent ne répondant pas deux fois de la même manière, ces appréciations portent sur plusieurs exécutions. Le chapitre 16 explique pourquoi cette combinaison s'impose.

> **Point clé**
>
> Le critère de réussite et ses tests disent ce que votre agent doit faire, pas comment l'écrire. Un test qui passe établit que le critère est atteint sur les cas essayés, rien de plus.
