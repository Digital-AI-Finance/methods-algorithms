# Prompt Log: 2026-03-20 22:00 — RL Five New Charts

## Request
Create 5 new chart.py files for the RL lecture with strict single-axes, single-figure constraints, FancyBboxPatch/FancyArrowPatch diagrams, chart_style import pattern.

## Charts Created

| # | Directory | Description |
|---|-----------|-------------|
| 1 | `20_rl_taxonomy_tree` | Tree diagram of RL method families; Q-Learning/DQN/PPO highlighted MLORANGE |
| 2 | `21_sarsa_vs_qlearning_cliff` | 4×12 cliff-walk gridworld; SARSA safe path (MLBLUE) vs Q-Learning cliff-hugging (MLORANGE) |
| 3 | `22_actor_critic_architecture` | Actor-Critic architecture box diagram with feedback arrow from Advantage to Actor |
| 4 | `23_offline_vs_online_rl` | Left/right zone split with bidirectional arrows vs one-way dataset arrow, finance annotation |
| 5 | `24_bandit_to_mdp_progression` | Horizontal 3-zone flow: Multi-Armed Bandit → Contextual Bandit → Full MDP |

## Outcome
All 5 chart.py files executed without errors. All 5 chart.pdf files confirmed present.
One cosmetic UserWarning in chart 2 (mpatches.Patch color override) — does not affect output.
