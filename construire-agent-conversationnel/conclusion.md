# Conclusion — Synthèse et ouverture

Dans cette conclusion, vous verrez l'anatomie de l'agent du fil rouge rassemblée en une page, selon les cinq notions qui ont structuré les parties du livre. Vous retrouverez les principes qui ont guidé ses choix, vous distinguerez ce qui est établi de ce qui relève de la pratique courante ou reste incertain, puis vous parcourrez les questions ouvertes et quelques pistes de lecture.

## Une question courte, relue une dernière fois

Une comptable écrit à l'agent : « Pourquoi la facture de ce fournisseur est-elle bloquée ? », en donnant sa référence. Le modèle du chapitre 2, laissé seul devant cette phrase, la prolongerait par un texte plausible, sans savoir de quelle facture il s'agit.

Dans l'agent du fil rouge, la même phrase déclenche un tour entier. Le modèle charge le *skill* de contrôle des factures, puis demande la lecture de la facture, de la commande et de la réception qui s'y rattachent. Chaque appel s'exécute avec les droits de la comptable et renvoie un résultat borné ; si la règle de blocage est documentée, un passage en est cité avec sa source. Le tour laisse une trace, et aucune écriture n'est possible sans que la comptable la confirme. La qualité de la réponse dépend du modèle et de tout ce qui l'entoure.

## L'anatomie en une page

Le tableau C-1 rassemble ce que chaque partie du livre a donné à l'agent du fil rouge.

*Tableau C-1 — L'anatomie de l'agent en une page*

| Partie | Notion | Ce que l'agent en a reçu | Chapitres |
|---|---|---|---|
| I — Fondations | Le modèle produit des propositions ; le *harness* gère la conversation et l'exécution | *System prompt* court, historique tenu par le programme, outils décrits au modèle et exécutés par le *harness* | 1 à 4 |
| II — De l'assistant à l'agent | Choix de l'étape suivante dans une boucle contrôlée, contexte limité, état de la tâche | Boucle bornée, visible et interruptible ; résultats bornés et déclarés, détail à la demande ; compaction de l'historique ; mémoire de travail | 5 à 8 |
| III — Capacité | Les capacités effectives tiennent aux opérations exposées, à leur contrat et à l'autorisation réelle | Outils servis par un protocole standard ; droits de l'utilisateur ; écritures en trois temps | 9 et 10 |
| IV — Connaissances | Ce que le modèle utilise dépend de ce que le *harness* remet dans son contexte, avec provenance et confiance | Aucune mémoire entre conversations ; recherche documentaire sourcée ; *skills* versionnés ; contenus externes non fiables | 12 à 15 |
| V — Le *harness* | Une consigne influence ; des contrôles, des traces et des parcours répétés rendent le système vérifiable | Traces et parcours répétés ; repli et livraison indépendante ; contrôles spécifiés et relus | 17 à 19 |

Ce découpage est une convention. Des synthèses académiques décrivent plutôt un agent par un modèle entouré de modules de mémoire, de planification et d'action (Wang et al., 2023a), ou par ses mémoires, son espace d'actions et sa procédure de décision (Sumers et al., 2023).

## Les principes qui traversent le livre

La sortie du modèle est un texte sans effet par lui-même, que le *harness* lit avant de décider de ce qu'il en fait. Le chapitre 4 l'a posé pour les appels d'outils, les ateliers suivants l'ont étendu aux droits, aux écritures et aux contenus lus : une consigne est suivie souvent, à un degré qu'il faut mesurer, un contrôle s'applique à chaque exécution.

Ce que le modèle lit se compose et se pèse d'après ce qu'il apporte à la décision suivante, avec sa provenance et la confiance qu'on peut lui accorder. L'autonomie se décide par famille de demandes : le fil rouge laisse le modèle enchaîner les lectures et lui retire la décision d'écrire. Un argumentaire contre le développement d'agents pleinement autonomes soutient que les risques pour les personnes augmentent avec le contrôle cédé au système (Mitchell et al., 2025).

La conception suppose que le modèle se trompera parfois, ou sera détourné par un contenu lu, et borne ce qui peut s'ensuivre par l'architecture. Le comportement se mesure sur des parcours répétés, rejoués à chaque changement, y compris lorsque le service de modèle évolue sans action du concepteur (Chen et al., 2023a). Enfin, chaque composant a été ajouté en réponse à une difficulté constatée ; une étude de systèmes en production rapporte que les agents qu'elle décrit reposent sur des approches simples et contrôlables (Pan et al., 2025).

## Établi, pratique courante, zone d'incertitude

Le tableau C-2 classe les limites rencontrées au fil du livre, notamment au chapitre 18, selon trois niveaux de certitude.

*Tableau C-2 — Les limites selon leur niveau de certitude*

| Limite | Établi | Pratique courante | Zone d'incertitude |
|---|---|---|---|
| Fiabilité | Une même demande peut suivre des trajectoires différentes | Contrôles du *harness*, autonomie bornée, parcours répétés | La constance atteignable pour un cas d'usage |
| Tâches longues | Une erreur précoce se propage aux cycles suivants | Tours courts, étapes fixées par un *skill*, résultats partiels annoncés | Le rythme des progrès hors des tâches mesurées |
| Coût et latence | Le coût croît avec les cycles et la longueur du contexte | Limites de cycles, de durée et de budget ; étapes visibles | Le délai acceptable pour une demande donnée |
| Dépendances | Un service de modèle peut changer sans action du concepteur | Parcours revérifiés, modèle de repli | La durée de vie d'un comportement ou d'un protocole |
| Démonstration et usage | Une exécution réussie ne renseigne pas sur les cas non essayés | Jeu de parcours avec cas limites | La part des prototypes qui deviennent des capacités maintenues |
| Confiance | La fluidité d'une réponse ne renseigne pas sur sa justesse | Sources affichées, limites dites, confirmation des écritures | Les moyens d'obtenir un recours approprié |

> **Attention — Zone d'incertitude**
>
> Les capacités des modèles changeront probablement. Des travaux mesurent leur progression sur des tâches logicielles, et leurs auteurs discutent eux-mêmes la validité de ces résultats hors du cadre étudié (Kwa et al., 2025). Certaines précautions pourraient alors peser moins ; les protocoles, les *skills* et le mot *harness* lui-même évolueront sans doute. Les questions de droits, d'attribution des actions et de décision humaine sur ce qui est difficile à défaire paraissent tenir à la structure d'un agent plutôt qu'au niveau des modèles. Rien, dans les travaux cités, ne permet de dire quels contrôles deviendront superflus.

La conduite prudente consiste à consigner la raison de chaque précaution, puis à la réexaminer à partir de mesures faites sur son propre système.

## Les questions ouvertes

La sécurité reste sans réponse complète : dans les travaux cités au chapitre 15, les défenses examinées ont été contournées par des attaques adaptées à chacune (Nasr et al., 2025), et les schémas de conception qui agissent par l'architecture ont un coût en utilité (Beurer-Kellner et al., 2025). La gestion de ce que l'agent retient demeure empirique (chapitres 8 et 12). Évaluer sur le sens suppose une référence ou un juge, et un évaluateur produit par un modèle demande lui-même une validation humaine (Shankar et al., 2024).

D'autres questions touchent les personnes. La présentation de l'incertitude influe sur le recours à une aide automatique, dans une tâche éloignée de la gestion (Cao et al., 2024). Le maintien des compétences, chez les utilisateurs comme chez les équipes qui font écrire leur *harness* par un outil, s'appuie sur des constats faits sur l'automatisation industrielle (Bainbridge, 1983), dont la transposition est une hypothèse. La frontière entre ce que les fournisseurs de modèles intègrent et ce que l'équipe construit elle-même est enfin en mouvement.

## Pour aller plus loin

Ces lectures ont toutes été citées dans le livre ; leurs résultats chiffrés vieillissent.

- **Décrire un agent.** Wang et al. (2023a), Sumers et al. (2023) et l'article qui fait alterner raisonnement et action (Yao et al., 2022).
- **Contexte, outils et protocole.** Une synthèse sur l'ingénierie du contexte (Mei et al., 2025) et un état des lieux du *Model Context Protocol* (*MCP*) et de ses menaces (Hou et al., 2025).
- **Sécurité.** L'étude d'applications compromises par injection indirecte (Greshake et al., 2023), Beurer-Kellner et al. (2025) et Nasr et al. (2025).
- **Évaluation et production.** Un banc d'essai de service client avec outils et règles (Yao et al., 2024), une analyse des pratiques d'évaluation (Kapoor et al., 2024), Pan et al. (2025) et une étude par entretiens sur l'intégration d'assistants à des produits (Parnin et al., 2023).
- **Usage responsable.** Mitchell et al. (2025) et Bainbridge (1983).

## Ce qu'il faut retenir

- Un agent réunit un modèle, une boucle, un contexte, une mémoire de travail, des outils et des *skills*, dans un *harness* qui compose, exécute, contrôle et trace.
- Une consigne influence le modèle ; une règle qui doit tenir à chaque exécution est confiée au *harness*.
- L'autonomie se décide par famille de demandes ; dans le fil rouge, toute écriture est confirmée par une personne.
- Le comportement se mesure sur des parcours répétés et se revérifie à chaque changement.
- Les précautions liées au niveau des modèles évolueront probablement ; les questions de droits, de responsabilité et de vérification devraient subsister, sans que cela soit acquis.

## Références

- Bainbridge, L. (1983). *Ironies of Automation*. Automatica, 19(6), 775-779.
- Beurer-Kellner, L., Buesser, B., Creţu, A.-M., et al. (2025). *Design Patterns for Securing LLM Agents against Prompt Injections*. arXiv:2506.08837.
- Cao, S., Liu, A., et Huang, C.-M. (2024). *Designing for Appropriate Reliance: The Roles of AI Uncertainty Presentation, Initial User Decision, and User Demographics in AI-Assisted Decision-Making*. arXiv:2401.05612.
- Chen, L., Zaharia, M., et Zou, J. (2023a). *How is ChatGPT's behavior changing over time?*. arXiv:2307.09009.
- Greshake, K., Abdelnabi, S., Mishra, S., et al. (2023). *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*. arXiv:2302.12173.
- Hou, X., Zhao, Y., Wang, S., et Wang, H. (2025). *Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions*. arXiv:2503.23278.
- Kapoor, S., Stroebl, B., Siegel, Z. S., et al. (2024). *AI Agents That Matter*. arXiv:2407.01502.
- Kwa, T., West, B., Becker, J., et al. (2025). *Measuring AI Ability to Complete Long Software Tasks*. arXiv:2503.14499.
- Mei, L., Yao, J., Ge, Y., et al. (2025). *A Survey of Context Engineering for Large Language Models*. arXiv:2507.13334.
- Mitchell, M., Ghosh, A., Luccioni, A. S., et Pistilli, G. (2025). *Fully Autonomous AI Agents Should Not be Developed*. arXiv:2502.02649.
- Nasr, M., Carlini, N., Sitawarin, C., et al. (2025). *The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against Llm Jailbreaks and Prompt Injections*. arXiv:2510.09023.
- Pan, M. Z., Arabzadeh, N., Cogo, R., et al. (2025). *Measuring Agents in Production*. arXiv:2512.04123.
- Parnin, C., Soares, G., Pandita, R., et al. (2023). *Building Your Own Product Copilot: Challenges, Opportunities, and Needs*. arXiv:2312.14231.
- Shankar, S., Zamfirescu-Pereira, J. D., Hartmann, B., et al. (2024). *Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences*. arXiv:2404.12272.
- Sumers, T. R., Yao, S., Narasimhan, K., et Griffiths, T. L. (2023). *Cognitive Architectures for Language Agents*. arXiv:2309.02427.
- Wang, L., Ma, C., Feng, X., et al. (2023a). *A Survey on Large Language Model based Autonomous Agents*. arXiv:2308.11432.
- Yao, S., Shinn, N., Razavi, P., et Narasimhan, K. (2024). *τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains*. arXiv:2406.12045.
- Yao, S., Zhao, J., Yu, D., et al. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv:2210.03629.
