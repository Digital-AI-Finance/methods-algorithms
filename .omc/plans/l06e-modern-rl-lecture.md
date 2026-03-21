# Plan: L06e Modern RL Visual Lecture

**File:** `slides/L06_Embeddings_RL/L06e_modern_rl_simple.tex`
**Arc:** Single-topic (compressed, ~10 slides)
**Mirror of:** L06d_modern_embeddings_simple.tex (11 slides)

---

## Context

### Original Request
Create a ~10 slide formula-free visual lecture about RL as used TODAY (Gymnasium, Stable-Baselines3, PPO, RLHF, sim-to-real). More technical than L06b (classic Q-learning basics) but still ultra simple. Mirrors L06d (modern embeddings) but for RL.

### Relationship to L06b
L06b covers the "what is RL" basics: agent-environment loop, Q-learning, reward curves, explore/exploit, policy viz, and a pseudocode recipe. L06e picks up where L06b leaves off: "OK, you understand RL basics -- here is how people actually DO RL in 2025."

### Positioning Statement
L06b = "What is RL?" (classic, conceptual)
L06e = "How do people USE RL today?" (modern, practical)

This mirrors the embeddings pair:
L06a = "What are embeddings?" (Word2Vec, GloVe)
L06d = "How do people USE embeddings today?" (sentence-transformers, RAG, vector DBs)

---

## Work Objectives

### Core Objective
Create `L06e_modern_rl_simple.tex` -- an 11-slide formula-free visual lecture on modern RL tooling and applications.

### Deliverables
1. `slides/L06_Embeddings_RL/L06e_modern_rl_simple.tex` (11 slides)
2. `slides/L06_Embeddings_RL/15_ppo_training_curve/chart.py` + `chart.pdf` (NEW chart)
3. Compiled `L06e_modern_rl_simple.pdf`

### Definition of Done
- 11 slides (title + 9 content + closing)
- Zero `$$` display math
- `\bottomnote{}` on every content slide (>= 10)
- 2 TikZ comics (opening problem + closing)
- 2-3 charts (mix of reused + new)
- XKCD bookends (opening + closing)
- 0 Overfull warnings
- Compiles clean with pdflatex

---

## Guardrails

### MUST Have
- Zero overlap with L06b content (no agent-environment loop, no Q-learning, no basic reward curves, no explore/exploit, no pseudocode recipe)
- Gymnasium, Stable-Baselines3, PPO mentioned by name
- RLHF explained in plain English
- Real Python code snippet (from stable_baselines3 import PPO)
- Sim-to-real concept explained
- Finance application beyond L06b (not just "trading, portfolio, order execution" again)

### MUST NOT Have
- Display math (`$$`)
- Any chart already used in L06b (03_rl_loop, 04_q_learning_grid, 05_reward_curves, 06_policy_viz, top10_09_epsilon_greedy)
- Q-learning explanation (already in L06b)
- Basic RL loop explanation (already in L06b)
- Epsilon-greedy explanation (already in L06b)
- More than 3 bullets per chart slide

---

## Slide-by-Slide Plan

### Slide 1: Title Page
- `\begin{frame}[plain]\titlepage\end{frame}`
- Title: "Modern Reinforcement Learning: A Practical Guide"
- Subtitle: "How to Use RL in 2025 with Gymnasium, PPO, and RLHF"

### Slide 2: XKCD Opening
- Image: `images/2173_trained_a_neural_net.png`
- Framing: "You know what RL is (L06b). Now: how do practitioners actually USE it today?"
- Three preview bullets: Deep RL libraries, PPO as the workhorse, RLHF for LLMs
- `\bottomnote{XKCD \#2173 by Randall Munroe (CC BY-NC 2.5)}`

### Slide 3: TikZ Comic C1 -- "The Scale Problem"
- Stick figure looking at a tiny grid (3x3, like L06b) vs a massive grid (implied 1000x1000)
- Speech bubble: "Q-tables don't scale! I need neural networks."
- Message: Classic RL stores a table. Modern RL uses neural networks to handle huge state spaces.
- `\bottomnote{A chess board has ~10^{44} possible states. No table can store that. Neural networks generalize.}`
- Max 25 lines TikZ, scale=0.8

### Slide 4: From Tables to Neural Networks
- Two-column comparison (red/green blocks):
  - Left (red): "Classic RL (L06b)" -- Q-table, small state spaces, tabular lookup
  - Right (green): "Modern RL (Today)" -- Neural network, huge state spaces, generalization
- Key insight highlight: "Replace the table with a neural network = Deep RL"
- `\bottomnote{DQN (2015) was the breakthrough: a neural network that plays Atari games from raw pixels.}`

### Slide 5: CHART -- DQN Architecture
- Reuse: `09_dqn_architecture/chart.pdf` (available, NOT in L06b)
- Width: 0.60\textwidth
- 3 bullets: State goes in, neural network processes, Q-values come out
- `\bottomnote{DQN = Deep Q-Network. DeepMind used this to beat human experts at 49 Atari games (2015).}`

### Slide 6: The Modern RL Stack
- Comparison table (5 rows):
  - Environments: Gymnasium (successor to OpenAI Gym)
  - Algorithms: Stable-Baselines3 (PPO, SAC, DQN pre-built)
  - Training: GPU-accelerated (thousands of episodes/second)
  - Monitoring: Weights & Biases, TensorBoard
  - Deployment: ONNX export, sim-to-real transfer
- `\bottomnote{pip install gymnasium stable-baselines3. That is all you need to start training RL agents today.}`

### Slide 7: CHART -- PPO Training Curve (NEW)
- NEW chart: `15_ppo_training_curve/chart.py`
- Shows PPO training on CartPole-v1: episode reward over 50k timesteps
- Actual Stable-Baselines3 training data (or realistic synthetic curve showing PPO's characteristic stable learning)
- 3 bullets: PPO learns fast, stable updates (no catastrophic drops), the default choice in 2025
- `\bottomnote{PPO = Proximal Policy Optimization (Schulman et al., 2017). Used by OpenAI, DeepMind, and most RL practitioners.}`

### Slide 8: RLHF -- How ChatGPT Learned to Be Helpful
- Text slide with 3-step numbered list:
  1. Train a base LLM on text (supervised)
  2. Humans rank outputs (which response is better?)
  3. RL (PPO!) fine-tunes the LLM to match human preferences
- Block: "RLHF = Reinforcement Learning from Human Feedback"
- highlight: "The same PPO from Slide 7 is used to align ChatGPT"
- `\bottomnote{InstructGPT paper (Ouyang et al., 2022) introduced RLHF for language models. Now standard for all frontier LLMs.}`

### Slide 9: Sim-to-Real + Applications
- CHART reuse: `13_walkforward_timeline/chart.pdf` (available, NOT in L06b)
- Width: 0.55\textwidth with side text column
- Side text: Modern RL trains in simulation, validates with walk-forward, deploys to real markets
- 3 bullets: Game AI (AlphaGo, OpenAI Five), Robotics (sim-to-real transfer), Finance (walk-forward validated trading)
- `\bottomnote{Sim-to-real: train millions of episodes in simulation (free, fast, safe), then fine-tune on real data.}`

### Slide 10: Try It Yourself -- Five Lines of Python
- Code block (texttt, not lstlisting):
  ```
  from stable_baselines3 import PPO
  import gymnasium as gym

  env = gym.make("CartPole-v1")
  model = PPO("MlpPolicy", env)
  model.learn(total_timesteps=50_000)
  ```
- highlight: "Five lines. That is a complete RL training pipeline."
- `\bottomnote{pip install stable-baselines3[extra]. CartPole is the "Hello World" of RL. Try LunarLander-v3 next!}`

### Slide 11: TikZ Comic C2 + XKCD Closing
- Small TikZ: stick figure confidently at a control panel with a neural network icon, speech bubble "PPO, deploy!"
- 3 key takeaways (numbered):
  1. Modern RL uses neural networks, not tables (Deep RL)
  2. PPO is the workhorse algorithm; RLHF uses it to align LLMs
  3. Gymnasium + Stable-Baselines3 = 5 lines to a trained agent
- `\bottomnote{XKCD \#1838 by Randall Munroe (CC BY-NC 2.5). Next: try the RL notebook to train your own PPO agent!}`
- Include XKCD image: `images/1838_machine_learning.png`

---

## Chart Allocation

| Slide | Chart | Source | Status |
|-------|-------|--------|--------|
| 5 | `09_dqn_architecture/chart.pdf` | Existing | Ready (NOT in L06b) |
| 7 | `15_ppo_training_curve/chart.pdf` | NEW | Must create |
| 9 | `13_walkforward_timeline/chart.pdf` | Existing | Ready (NOT in L06b) |

### New Chart: 15_ppo_training_curve

**Purpose:** Show PPO learning curve on CartPole-v1 -- smooth, stable ascent to ~500 reward.

**Implementation:**
- Create `slides/L06_Embeddings_RL/15_ppo_training_curve/chart.py`
- Generate realistic PPO training curve (smoothed episode rewards over 50k timesteps)
- Use synthetic data that matches real PPO CartPole behavior: starts ~20, reaches ~500 by 30k steps, stays there
- Standard rcParams (figsize 10x6, dpi 150, font.size 14)
- ML color palette: main curve in MLBLUE, rolling average in MLPURPLE
- Shaded region for variance
- Title: "PPO Training on CartPole-v1"
- X-axis: "Timestep (thousands)", Y-axis: "Episode Reward"
- Annotation: "Solved!" near the 500 threshold line
- Save to `chart.pdf` in same directory

**Why synthetic:** Avoids requiring stable-baselines3 as a build dependency. The curve shape is well-documented and reproducible.

---

## TikZ Comic Descriptions

### Comic C1 (Slide 3): "The Scale Problem"
- Left: tiny 3x3 grid with arrows (like L06b's Q-learning grid, but tiny and labeled "9 states")
- Right: massive implied grid represented by a large rectangle with "..." and "1,000,000+ states"
- Stick figure in the middle looking overwhelmed
- Speech bubble: "Tables don't scale!"
- Arrow pointing to a neural network icon (circle-layer-circle) labeled "Solution: Deep RL"
- Max 25 lines, scale=0.8

### Comic C2 (Slide 11): "The Expert Deployer"
- Stick figure at a control panel (rectangle with circles for buttons)
- Screen showing a simple neural network icon (3 circles connected)
- Speech bubble: "PPO, deploy!"
- Small star/sparkle effects around the screen
- Max 20 lines, scale=0.7

---

## Implementation Steps

### TODO 1: Create new chart directory and chart.py
- Create `slides/L06_Embeddings_RL/15_ppo_training_curve/`
- Write `chart.py` following chart template rules
- Run `python chart.py` to generate `chart.pdf`
- Acceptance: chart.pdf exists, shows smooth PPO training curve, correct rcParams

### TODO 2: Create L06e_modern_rl_simple.tex
- Copy preamble from L06b lines 1-107
- Update title/subtitle for L06e
- Write all 11 slides per the slide-by-slide plan above
- Acceptance: File exists, 11 frames, 0 display math, bottomnote on every content slide

### TODO 3: Compile and verify
- Run `pdflatex -interaction=nonstopmode L06e_modern_rl_simple.tex`
- Check for Overfull warnings: `grep -c "Overfull" *.log` must be 0
- Verify frame count: `grep -c "begin{frame" L06e_modern_rl_simple.tex` = 11
- Verify chart count: `grep -c "chart.pdf" L06e_modern_rl_simple.tex` = 3
- Verify bottomnote count: `grep -c "bottomnote" L06e_modern_rl_simple.tex` >= 10
- Verify zero display math: `grep -c '\$\$' L06e_modern_rl_simple.tex` = 0
- Verify TikZ count: `grep -c "begin{tikzpicture}" L06e_modern_rl_simple.tex` >= 2
- Move aux files: `mkdir -p temp && mv *.aux *.log *.nav *.out *.snm *.toc temp/`

### TODO 4: Update manifest.json
- Add L06e entry to the L06 topic section
- Status: complete

---

## Commit Strategy

Single commit after all TODOs pass:
```
Add L06e modern RL visual lecture (11 slides, formula-free)

New formula-free visual lecture covering modern RL tooling: Gymnasium,
Stable-Baselines3, PPO, RLHF, and sim-to-real. Includes 1 new chart
(PPO training curve) and reuses 2 existing charts. Mirrors L06d
(modern embeddings) as the practical complement to L06b (RL basics).
```

---

## Verification Commands

```bash
cd slides/L06_Embeddings_RL

# Build new chart
python 15_ppo_training_curve/chart.py

# Compile
pdflatex -interaction=nonstopmode L06e_modern_rl_simple.tex

# All checks
grep -c "begin{frame" L06e_modern_rl_simple.tex           # expect: 11
grep -c "chart.pdf" L06e_modern_rl_simple.tex              # expect: 3
grep -c "bottomnote" L06e_modern_rl_simple.tex             # expect: >= 10
grep -c '\$\$' L06e_modern_rl_simple.tex                   # expect: 0
grep -c "begin{tikzpicture}" L06e_modern_rl_simple.tex     # expect: >= 2
grep -c "Overfull" temp/L06e_modern_rl_simple.log          # expect: 0

# Move aux files
mkdir -p temp && mv *.aux *.log *.nav *.out *.snm *.toc temp/ 2>/dev/null
```

---

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| TikZ comic exceeds 25 lines | Medium | Overfull vbox | Pre-count lines during writing; use scale=0.7 if tight |
| XKCD images reused from L06b/L06d | Low | Acceptable if framing text differs (skill allows this) | Use different framing text and different layout |
| PPO chart looks too similar to L06b reward_curves | Medium | Confusion | Distinct styling: add "Solved!" annotation, use timesteps not episodes, add variance shading |
| Slide 8 (RLHF) too text-heavy | Medium | Overflow | Use numbered list (not bullets), keep to 3 items, use block environment |
| Walk-forward chart on Slide 9 needs context | Low | Student confusion | Side text column explains why walk-forward matters for RL deployment |

---

## Content Overlap Check

| Topic | L06b Covers | L06e Covers | Overlap? |
|-------|-------------|-------------|----------|
| Agent-environment loop | Yes (chart + explanation) | No | Clean |
| Q-learning | Yes (chart + grid) | No (mentioned only as "classic") | Clean |
| Reward curves | Yes (chart) | Different chart (PPO-specific) | Clean |
| Explore/exploit | Yes (chart + explanation) | No | Clean |
| Policy visualization | Yes (chart) | No | Clean |
| DQN architecture | No | Yes (chart) | Clean |
| PPO | No | Yes (new chart + explanation) | Clean |
| RLHF | No | Yes (text slide) | Clean |
| Gymnasium | Mentioned in bottomnote only | Yes (full slide) | Clean |
| Stable-Baselines3 | No | Yes (code + explanation) | Clean |
| Sim-to-real | 1 bullet in gotchas | Yes (full treatment with chart) | Minimal, acceptable |
| Finance apps | Generic (trading, portfolio, execution) | Specific (walk-forward validated) | Complementary |
| Python code | Pseudocode recipe | Real library code (SB3) | Different |
