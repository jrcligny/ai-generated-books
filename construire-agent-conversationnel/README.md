# De l'assistant à l'agent : anatomie d'un agent conversationnel

Cette publication rassemble la préface, les dix-sept chapitres du livre, répartis en cinq parties, une conclusion, une annexe consacrée aux ateliers et le glossaire bilingue de fin d'ouvrage, à raison d'un document par chapitre. Chaque partie s'ouvre sur une courte présentation, apporte une notion structurante et la matérialise dans l'évolution de l'agent de démonstration, le fil rouge fictif introduit au chapitre 3.

Les ateliers se réalisent avec le dépôt compagnon, [jrcligny/workshops-build-conversational-agent](https://github.com/jrcligny/workshops-build-conversational-agent), présenté à l'annexe A : il fournit les applications de test, une coquille d'agent et les tests de bout en bout de chaque atelier, mais aucun corrigé. Les modèles y sont hébergés dans Azure OpenAI et appelés par l'intermédiaire de son proxy ; le livre ne prescrit aucun modèle.

- [Préface](00-preface.md)

## Partie I — Comprendre le modèle et construire un assistant outillé

- [Ouverture de la partie I](01-partie1.md)
- [Chapitre 1 — Situer l'IA générative et fixer le vocabulaire de l'agent](02-ch01.md)
- [Chapitre 2 — Comment un LLM génère du texte, et ce que cela impose à la conception](03-ch02.md)
- [Chapitre 3 — Construire un assistant autour du modèle : rôles, consignes et harness](04-ch03.md)
- [Chapitre 4 — Donner un outil à l'assistant : le modèle demande, le harness exécute](05-ch04.md)

## Partie II — Faire agir l'agent : boucle, outils et droits

- [Ouverture de la partie II](06-partie2.md)
- [Chapitre 5 — Passer de l'assistant à l'agent : la boucle agentique](07-ch05.md)
- [Chapitre 6 — Concevoir des outils qu'un modèle sait utiliser : contrat, erreurs et protocole MCP](08-ch06.md)
- [Chapitre 7 — Encadrer les actions de l'agent : droits, validation humaine et confinement](09-ch07.md)

## Partie III — Maîtriser le contexte d'une longue conversation

- [Ouverture de la partie III](10-partie3.md)
- [Chapitre 8 — Conserver ce que la conversation a établi : mémoire de travail et état de conversation](11-ch08.md)
- [Chapitre 9 — Ne charger dans le contexte que ce qui sert : la divulgation progressive](12-ch09.md)
- [Chapitre 10 — Réduire le contexte d'une longue conversation : la compaction](13-ch10.md)

## Partie IV — Enrichir le contexte : souvenirs, documents, procédures et contenus tiers

- [Ouverture de la partie IV](14-partie4.md)
- [Chapitre 11 — Mémoriser d'une conversation à l'autre : la mémoire persistante](15-ch11.md)
- [Chapitre 12 — Répondre à partir de documents : la génération augmentée par récupération](16-ch12.md)
- [Chapitre 13 — Charger des procédures à la demande : les skills](17-ch13.md)
- [Chapitre 14 — Protéger l'agent contre l'injection de prompt](18-ch14.md)

## Partie V — Évaluer l'agent et le maintenir en service

- [Ouverture de la partie V](19-partie5.md)
- [Chapitre 15 — Observer et évaluer un agent non déterministe](20-ch15.md)
- [Chapitre 16 — Résister aux pannes et aux changements des dépendances](21-ch16.md)
- [Chapitre 17 — Construire le harness avec un agent de programmation](22-ch17.md)

## Conclusion

- [Conclusion — Les principes qui restent valables quand les modèles changent](23-conclusion.md)

## Annexe et glossaire

- [Annexe A — Réaliser les ateliers](24-annexe-ateliers.md)
- [Glossaire français-anglais](25-glossaire.md)

[Retour à la liste des livres](../README.md)
