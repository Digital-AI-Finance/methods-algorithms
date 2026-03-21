# Prompt: Ultra deep improvement of RL lecture (RALPLAN)

**Time:** 2026-03-20 21:18
**Action:** RALPLAN iterative planning (Planner + Critic)
**Iterations:** 3 (REJECT 24/35 → REJECT 32/35 → OKAY 34/35)

## Request
User requested `/ralplan ultra deep improvement of the RL lecture`

## What Was Done
- Read all 6 L06 RL-related lecture files (overview, deepdive, L06b_simple, L06e_modern, rl_full, rl_mini)
- Spawned Planner agent with comprehensive context
- Planner created 33-TODO plan across 7 phases
- Critic rejected (iteration 1): 5 critical issues - budget blown, subplot violation, stale counts, ambiguity, empty phase
- Planner revised: fixed all 5 critical + 6 minor issues
- Critic rejected (iteration 2): 1 critical - Embeddings frame count was 19 not 18, budget off by 1
- Fixed directly: demoted SARSA to appendix-only, corrected all running totals
- Critic approved (iteration 3): 34/35, 2 cosmetic issues only

## Plan Summary (33 TODOs, 7 phases)
- **5 new charts**: RL taxonomy tree, SARSA cliff-walking, Actor-Critic architecture, offline vs online RL, bandit-to-MDP progression
- **Deepdive overhaul**: +4 new slides (RL roadmap, bandits, bandits-to-MDP, taxonomy+AC/PPO) -3 merges = net +1 → 45 main + 10 appendix = 55
- **L06e enhancements**: +2 slides (offline RL, FinRL framework), XKCD dedup
- **L06_rl_full consolidation**: repositioned as standalone RL lecture with full PPO math
- **Cross-file**: notation audit, AGENTS.md update, manifest update

## Plan Location
`.omc/plans/rl-lecture-ultra-deep.md` (revision 3, Critic-approved)
