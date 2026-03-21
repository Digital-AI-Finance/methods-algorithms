# Ultra Deep Improvement: RL Lecture (L06)

**Plan Created:** 2026-03-20
**Scope:** Comprehensive overhaul of all 5 RL-related lecture files + charts
**Estimated Complexity:** HIGH (45+ TODOs across ~15 files)

---

## Context

### Original Request
Ultra deep improvement of the Reinforcement Learning content in L06, covering all 5 RL-related lecture files, 19 RL charts, and the full pedagogical arc from beginner to advanced.

### Current State Inventory

**5 RL Lecture Files:**
| File | Slides | Level | RL Coverage |
|------|--------|-------|-------------|
| `L06_overview.tex` | 24 (6 RL) | Overview | Agent loop, Q-learning intuition, finance table |
| `L06_deepdive.tex` | 52 (18 RL main + 6 RL appendix) | Deepdive | MDP, Bellman, TD, Q-learning algo+worked example, DQN, trading, walk-forward |
| `L06b_rl_simple.tex` | 17 | Beginner visual | RL loop, grid Q-learning, rewards, explore/exploit, gotchas, reward shaping |
| `L06e_modern_rl_simple.tex` | 11 | Modern visual | Scale problem, DQN, PPO, RLHF, modern stack, 5-line Python |
| `L06_rl_full.tex` | 25 | Full standalone | MDP, Bellman, Q-learning, exploration, DQN, trading/portfolio/execution, challenges |

**19 RL Charts:**
Core (7): 03_rl_loop, 04_q_learning_grid, 05_reward_curves, 06_policy_viz, 09_dqn_architecture, 12_epsilon_decay, 13_walkforward_timeline
Extended (4): 15_ppo_training_curve, 18_rlhf_pipeline, 19_reward_shaping_trading
Top10 (8): top10_09_epsilon_greedy, top10_14_qvalue_convergence, top10_15_state_action_heatmap, top10_16_bandit_regret, top10_17_td_learning_update, top10_19_gridworld_trajectory, top10_20_reward_shaping

### Research Findings (from file analysis)

**Critical Gaps Identified:**
1. No multi-armed bandits entry point (bandits appear in chart top10_16 but never in slides)
2. No model-based vs model-free taxonomy slide
3. No Actor-Critic / A2C explanation (only a 3-bullet mention in appendix A9)
4. No offline RL content (critical for finance where online learning is expensive)
5. No FinRL framework coverage (despite being cited in references)
6. No safe/constrained RL for finance (regulatory compliance)
7. No Decision Transformer / sequence-modeling RL perspective
8. PPO only in L06e with no math; deepdive appendix gives 3 bullets only
9. RLHF only in L06e; missing from deepdive entirely

**Pedagogical Weaknesses:**
1. L06_rl_full.tex duplicates 80% of deepdive RL content with worse quality -- needs consolidation or differentiation
2. L06b and L06e share the XKCD #1838 opening comic (L06e also uses #2173 as closing of L06b's opening)
3. No "RL in One Picture" conceptual slide before formulas
4. No Key Terms slide in deepdive (L06_rl_full has one, deepdive doesn't)
5. MVF protocol not followed for Bellman equation in deepdive (jumps from definition to formula)
6. No worked example for policy gradient / PPO (only for Q-learning)
7. Missing "aha moment" for why discount factor matters (only bottomnote "gamma close to 1 = far-sighted")
8. Epsilon-greedy introduced in deepdive slide 24 but chart 12 (epsilon decay) is at slide 29 -- 5 slides apart
9. Walk-forward validation (slide 32-33) is orphaned from the reward design section (slide 31)
10. No "RL Taxonomy Tree" showing relationships between methods

**Structural Issues:**
1. L06_rl_full.tex is largely redundant with deepdive RL section + L06b + L06e combined
2. Content across 5 files has significant overlap with inconsistent depth
3. Deepdive appendix A9 (Policy Gradient) is a 1-slide stub covering REINFORCE, Actor-Critic, PPO in 3 bullets
4. Bandit regret chart exists (top10_16) but bandits are never introduced in any lecture file
5. State-action heatmap chart (top10_15) exists but only used in top10 deck, not in any main lecture
6. TD learning update chart (top10_17) exists but not used in deepdive despite having a TD learning slide

**Chart Improvement Opportunities:**
1. Several RL charts not used in any main lecture file (top10_14, top10_15, top10_16, top10_17, top10_19)
2. No chart for model-based vs model-free comparison
3. No chart for Actor-Critic architecture
4. No chart for offline RL concept
5. No chart for RL taxonomy/method family tree
6. No chart for SARSA vs Q-learning cliff-walking (only text description in appendix A7)

---

## Work Objectives

### Core Objective
Transform the RL content from a decent introduction into a comprehensive, pedagogically excellent MSc-level treatment that covers modern RL, has clear progression across difficulty levels, eliminates redundancy, and deeply integrates finance applications.

### Deliverables
1. Restructured deepdive RL section with 8-10 new/improved slides
2. Enhanced L06e_modern_rl with Actor-Critic, offline RL, and FinRL content
3. 5-7 new charts filling visualization gaps
4. Consolidated/differentiated L06_rl_full.tex
5. Fixed pedagogical flow issues in all files
6. All files compile clean (0 errors, 0 Overfull)

### Definition of Done
- All RL formulas follow MVF protocol (Motivate-Visualize-Formalize)
- Bandits, Actor-Critic, PPO, offline RL, and FinRL are properly covered
- No redundant content across the 5 files (each has clear purpose)
- All existing RL charts integrated into at least one main lecture
- 5+ new charts created for gap topics
- Every frame has `\bottomnote{}`
- Question-based frame titles throughout
- Finance running example (trading agent) threaded through deepdive

---

## Guardrails

### Must Have
- Bellman equation with full MVF treatment
- Multi-armed bandits as RL entry point
- Model-free taxonomy: value-based (Q-learning, DQN) vs policy-based (REINFORCE, PPO) vs Actor-Critic
- Offline RL slide with finance motivation
- FinRL framework mention with practical guidance
- SARSA vs Q-learning cliff-walking chart
- RL taxonomy visualization
- PPO with actual math in deepdive (not just L06e bullet points)
- All frames compile clean

### Must NOT Have
- Content above MSc level (no measure-theoretic RL, no convergence rate analysis beyond Robbins-Monro)
- More than 55 slides in deepdive total (currently 52)
- Breaking changes to existing chart.py APIs
- New dependencies beyond standard (numpy, matplotlib, scikit-learn, scipy)
- Removal of existing correctly-functioning content

---

## Task Flow and Dependencies

```
Phase 1: Structural Analysis & Content Planning (no file changes)
  |
Phase 2: New Charts (independent, parallelizable)
  |
Phase 3: Deepdive RL Section Overhaul (depends on Phase 2 charts)
  |
Phase 4: L06e Modern RL Enhancement (depends on Phase 2 charts)
  |
Phase 5: L06_rl_full Consolidation (depends on Phases 3-4)
  |
Phase 6: L06b & L06_overview Polish (depends on Phase 3)
  |
Phase 7: Verification & Compilation
```

---

## Detailed TODOs

### PHASE 2: New Charts (5 new charts)

**TODO-01: Create `20_rl_taxonomy_tree/chart.py`** [P1, Medium]
- Visualization: Tree diagram showing RL method families
  - Root: RL Methods
  - Branch 1: Model-Free -> Value-Based (Q-learning, DQN, Double DQN) | Policy-Based (REINFORCE, PPO, TRPO) | Actor-Critic (A2C, A3C, SAC)
  - Branch 2: Model-Based (Dyna, MBPO, MuZero)
  - Highlight the methods taught in this course in orange
- Style: figsize=(10,6), use chart_style.py, ML color palette
- Output: chart.pdf in same directory
- Acceptance: Tree renders cleanly, all method names legible, course-covered methods highlighted

**TODO-02: Create `21_sarsa_vs_qlearning_cliff/chart.py`** [P1, Medium]
- Visualization: Classic cliff-walking example
  - 4x12 grid with cliff along bottom edge
  - Two paths overlaid: SARSA safe path (blue, goes inland) vs Q-learning optimal path (orange, hugs cliff edge)
  - Start at bottom-left, goal at bottom-right
  - Cliff cells colored red, reward annotations
- Style: figsize=(10,6), chart_style.py
- Acceptance: Both paths clearly distinguishable, cliff cells visible, legend identifies SARSA vs Q-learning

**TODO-03: Create `22_actor_critic_architecture/chart.py`** [P1, Medium]
- Visualization: Architecture diagram showing Actor-Critic structure
  - Shared state input
  - Actor branch: state -> policy pi(a|s) -> action selection
  - Critic branch: state -> V(s) -> advantage computation -> actor update
  - Environment feedback loop
  - Labels: "Actor (policy)", "Critic (value)", "Advantage = Q - V"
- Style: figsize=(10,6), chart_style.py, box-and-arrow diagram style matching 09_dqn_architecture
- Acceptance: Clear separation of actor/critic, data flow arrows, labels readable

**TODO-04: Create `23_offline_vs_online_rl/chart.py`** [P2, Small]
- Visualization: Side-by-side comparison
  - Left: Online RL loop (agent <-> environment, live interaction)
  - Right: Offline RL (static dataset -> agent learns, no interaction)
  - Center: Finance motivation text ("Live trading data is expensive and risky")
  - Arrows showing data flow differences
- Style: figsize=(10,6), chart_style.py
- Acceptance: Clear visual distinction between online and offline paradigms

**TODO-05: Create `24_bandit_to_mdp_progression/chart.py`** [P2, Medium]
- Visualization: 3-panel progression showing complexity increase
  - Panel 1: Multi-armed bandit (one state, k arms with reward distributions)
  - Panel 2: Contextual bandit (state -> action -> reward, no transitions)
  - Panel 3: Full MDP (state -> action -> next state -> reward, transitions matter)
  - Arrows between panels labeled "Add states", "Add transitions"
- Style: figsize=(10,6), chart_style.py
- Acceptance: Clear progression, each panel self-contained, arrows connecting panels

### PHASE 3: Deepdive RL Section Overhaul (L06_deepdive.tex)

**TODO-06: Add "RL in One Picture" slide before MDP formalism** [P1, Medium]
- Location: Insert after current slide 18 (embeddings finance example), before slide 19 (RL framework)
- Content: Conceptual overview slide with TikZ showing the full RL landscape:
  - Central: Agent-Environment loop
  - Surrounding labels: "What we'll cover: Bandits -> Q-learning -> DQN -> Policy Gradient"
  - Finance context: "Running example: training a trading agent"
- Must have: `\bottomnote{}`, question-based title ("What Does the RL Landscape Look Like?")
- Acceptance: Provides roadmap before diving into formulas; mentions all topics

**TODO-07: Add Multi-Armed Bandits entry point slide** [P1, Medium]
- Location: Insert after "RL in One Picture", before MDP slide
- Content:
  - "What If There's Only One State?" -- bandits as simplest RL
  - k-armed bandit: pull arm -> get reward, goal = maximize total reward
  - Connect to top10_16_bandit_regret chart
  - Finance analogy: "Which of k trading strategies to allocate capital to?"
  - Motivate: "Bandits are RL with no state transitions -- the simplest case"
- Must have: MVF protocol (motivate with finance, visualize with chart, formalize regret)
- Acceptance: Bandit framed as gateway to full RL; chart integrated; finance example clear

**TODO-08: Add Bandits-to-MDP progression slide** [P1, Small]
- Location: After bandits slide, before MDP
- Content: Use chart 24_bandit_to_mdp_progression
  - "From Bandits to MDPs: Adding Complexity One Step at a Time"
  - Bandit (no states) -> Contextual bandit (states but no transitions) -> Full MDP
  - "The MDP adds state transitions -- now the future depends on your actions"
- Acceptance: Clear logical bridge from bandits to MDP; chart integrated

**TODO-09: Improve Bellman Equation slide with MVF protocol** [P1, Medium]
- Location: Current deepdive slide 22
- Changes:
  - Add MOTIVATE block: "Why do we need a recursive equation? Because evaluating a policy directly requires summing infinite futures"
  - Add VISUALIZE: Small TikZ tree showing one-step lookahead (s -> a -> s' with r and gamma labels)
  - Keep FORMALIZE: existing Bellman equation
  - Improve worked example: make it a 3-state trading scenario (not abstract A/B/C)
    - State: "Cash" -> buy -> "Holding" (reward = -commission) -> sell -> "Cash" (reward = +profit)
- Acceptance: MVF structure visible; trading example; TikZ tree

**TODO-10: Add RL Taxonomy slide using new chart** [P1, Small]
- Location: After DQN section (current slide 36), before Practice
- Content:
  - "Where Does Each Method Fit?" -- use chart 20_rl_taxonomy_tree
  - Brief 2-bullet annotation: "Value-based: learn Q-values (this lecture). Policy-based: learn actions directly (appendix)."
  - "Actor-Critic: best of both worlds (next)"
- Acceptance: Chart integrated; student can locate each method in the taxonomy

**TODO-11: Add Actor-Critic slide in deepdive main body** [P1, Medium]
- Location: After RL taxonomy slide
- Content: Promote from 3-bullet appendix stub to proper treatment
  - Use chart 22_actor_critic_architecture
  - "Why Combine Value and Policy Methods?"
  - Actor: learns policy pi(a|s) directly
  - Critic: learns V(s) to reduce variance
  - Advantage: A(s,a) = Q(s,a) - V(s) tells actor "was this action better or worse than average?"
  - Finance: "Actor decides trades, Critic evaluates portfolio value"
  - Key formula: Policy gradient with advantage (move from appendix A9 to here, simplified)
- Must have: MVF treatment, `\bottomnote{}`
- Acceptance: Actor-Critic explained at MSc level with chart; advantage function motivated

**TODO-12: Add PPO slide with actual math in deepdive** [P2, Medium]
- Location: After Actor-Critic slide
- Content:
  - "How Does PPO Prevent Catastrophic Updates?"
  - Clipped surrogate objective (the key PPO formula):
    $L^{CLIP}(\theta) = \mathbb{E}[\min(r_t(\theta) A_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) A_t)]$
  - where $r_t(\theta) = \pi_\theta(a_t|s_t) / \pi_{\theta_{old}}(a_t|s_t)$
  - Intuition: "Don't change the policy too much in one step"
  - Connect to L06e PPO training curve chart (15_ppo_training_curve)
  - Finance: "PPO's stability matters for live trading -- no sudden strategy flips"
- Must have: MVF protocol, `\bottomnote{}`
- Acceptance: PPO objective fully formalized; clipping explained; chart referenced

**TODO-13: Add SARSA vs Q-learning comparison slide** [P2, Medium]
- Location: Replace or enhance appendix A7
- Content:
  - Move from appendix to main body (after exploration section, before trading)
  - Use new chart 21_sarsa_vs_qlearning_cliff
  - "On-Policy vs Off-Policy: Does Exploration Risk Matter?"
  - SARSA formula vs Q-learning formula side-by-side
  - Cliff-walking visualization showing different learned paths
  - Finance: "SARSA accounts for execution risk; Q-learning optimizes assuming perfect execution"
- Acceptance: Chart integrated; on-policy vs off-policy distinction clear; finance relevance shown

**TODO-14: Integrate unused top10 charts into deepdive** [P2, Small]
- Charts to integrate:
  - top10_14_qvalue_convergence: Add to Q-learning section as supporting visual
  - top10_15_state_action_heatmap: Add to Q-values visualization slide (slide 27) or nearby
  - top10_17_td_learning_update: Add to TD learning slide (slide 23)
- For each: either add as a companion slide or integrate into existing two-column layout
- Acceptance: Each chart appears in at least one main lecture file

**TODO-15: Add discount factor "aha moment" slide** [P3, Small]
- Location: After Return and Value Functions (current deepdive slide 21)
- Content: "What Happens When Gamma Changes?"
  - TikZ or small table showing same 5-step reward sequence with gamma=0.1, 0.5, 0.9, 0.99
  - Compute G_0 for each, show dramatic difference
  - Finance: "gamma=0.99: patient long-term investor. gamma=0.5: day trader who ignores next week"
  - Visual: bar chart showing G_0 values at different gammas
- Acceptance: Student intuitively understands gamma's effect; finance analogy clear

### PHASE 4: L06e Modern RL Enhancement

**TODO-16: Add Offline RL slide to L06e** [P1, Medium]
- Location: After RLHF slide (current slide 8b)
- Content:
  - "What If You Can't Explore? Offline RL"
  - Use chart 23_offline_vs_online_rl
  - Finance motivation: "Live trading exploration is expensive. Offline RL learns from historical trade logs."
  - Key approaches: Conservative Q-Learning (CQL), Decision Transformer
  - Simple comparison table: Online (explore freely) vs Offline (fixed dataset, no new data)
  - Bottom line: "Offline RL is the most finance-relevant frontier"
- Must have: `\bottomnote{}`, no display math (L06e is formula-free)
- Acceptance: Offline RL concept clear; finance motivation strong; stays formula-free

**TODO-17: Add FinRL Framework slide to L06e** [P2, Small]
- Location: After Offline RL slide
- Content:
  - "FinRL: A Ready-Made Framework for Financial RL"
  - What it provides: pre-built trading environments (stock, crypto, portfolio)
  - Code snippet: 5 lines to train a PPO trading agent with FinRL
  - Key advantage: handles data download, feature engineering, backtesting
  - Link: github.com/AI4Finance-Foundation/FinRL
- Must have: `\bottomnote{}` with citation (Liu et al., 2021)
- Acceptance: Practical resource students can use; code snippet works conceptually

**TODO-18: Add Actor-Critic visual explanation to L06e** [P2, Small]
- Location: Before PPO slide (between DQN and PPO)
- Content: Formula-free explanation of Actor-Critic
  - TikZ comic: Two stick figures -- one choosing actions (Actor), one evaluating (Critic)
  - "The Actor tries things. The Critic judges. Together they learn faster."
  - Why it matters: "PPO is an Actor-Critic method -- you need this to understand PPO"
- Must have: TikZ comic, `\bottomnote{}`
- Acceptance: Bridges DQN -> PPO conceptual gap in L06e

**TODO-19: Differentiate L06e XKCD comics from L06b** [P3, Small]
- Problem: L06e opens with XKCD #2173 (same as L06b closing), L06b opens with #1838
- Fix: Find a different XKCD for L06e opening, or create a TikZ comic instead
- Options:
  - Use XKCD #2048 "Curve Fitting" (relevant to RL overfitting)
  - Or create a TikZ comic showing "From Q-Tables to Neural Networks" progression
- Acceptance: L06b and L06e no longer share the same XKCD; each has unique opening

### PHASE 5: L06_rl_full.tex Consolidation

**TODO-20: Differentiate L06_rl_full.tex purpose** [P1, Large]
- Problem: L06_rl_full duplicates ~80% of deepdive RL section content
- Decision: Reposition as the "RL-Only Standalone Lecture" for when RL is taught separately from Embeddings
- Changes needed:
  - Add a note at top of file: "Standalone RL lecture for use when taught separately from Embeddings"
  - Add bandits entry point (matching deepdive TODO-07)
  - Add Actor-Critic and PPO slides (matching deepdive TODOs 11-12, but self-contained)
  - Add offline RL slide (matching L06e TODO-16, but with formulas)
  - Remove course-wrap-up slide (slide 24 -- this only makes sense in the combined L06 context)
  - Add RL taxonomy chart (matching deepdive TODO-10)
- Acceptance: L06_rl_full is a coherent standalone RL lecture that doesn't require Embeddings context

**TODO-21: Update L06_rl_full learning objectives** [P2, Small]
- Current LOs are Bloom's 4-5 but miss Actor-Critic, PPO, offline RL
- New LOs:
  1. Formalize sequential decisions as MDPs and solve with Q-learning
  2. Derive the Bellman equation and analyze convergence conditions
  3. Evaluate model-free RL methods (Q-learning vs SARSA vs PPO) for trading applications
  4. Critique RL trading strategies accounting for transaction costs, non-stationarity, and offline constraints
- Acceptance: LOs reflect expanded scope; Bloom's 4-5 maintained

### PHASE 6: L06b & L06_overview Polish

**TODO-22: Add bandit teaser to L06b** [P3, Small]
- Location: After "What Makes RL Different?" slide (slide 5)
- Content: 1 slide introducing multi-armed bandit as the simplest RL problem
  - TikZ comic: stick figure facing 3 slot machines
  - "Which machine pays the most? You can only find out by trying."
  - No math, purely visual
- Acceptance: L06b introduces bandits as RL gateway; consistent with deepdive

**TODO-23: Add RL taxonomy teaser to L06_overview** [P3, Small]
- Location: After "How Does an Agent Learn from Rewards?" (current slide 14)
- Content: Brief 1-slide mention: "Beyond Q-learning: the RL family"
  - Simple 3-item list: Value-based (today), Policy-based (PPO in L06e), Actor-Critic (deepdive)
  - "Q-learning is just the beginning -- see the deepdive for the full picture"
- Acceptance: Overview sets up deepdive content; no formulas

**TODO-24: Fix L06_overview RL slide count** [P3, Small]
- Current: 6 RL slides (13-18) in a 24-slide combined lecture
- Issue: RL gets less than half the slides despite equal billing
- Fix: This is acceptable given that L06_overview covers both topics and detailed RL is in deepdive. No action unless other changes push it above budget.
- Acceptance: Slide count verified as appropriate; no change needed unless budget allows

### PHASE 7: Cross-File Consistency & Integration

**TODO-25: Ensure consistent RL notation across all 5 files** [P1, Medium]
- Audit all files for:
  - Q-function notation: $Q(s,a)$ vs $Q^*(s,a)$ vs $Q^\pi(s,a)$ used consistently
  - Reward notation: $r_t$ vs $R_t$ vs $R_{t+1}$ -- pick one convention
  - Policy notation: $\pi(a|s)$ vs $\pi(s)$ used correctly (stochastic vs deterministic)
  - Discount factor: $\gamma$ used consistently (not $\delta$ or other symbols)
  - Learning rate: $\alpha$ in all files (deepdive already fixed beta for epsilon decay)
- Acceptance: Same symbol means the same thing across all 5 files

**TODO-26: Update AGENTS.md with new chart inventory** [P2, Small]
- Add new charts (20-24) to the chart table in AGENTS.md
- Update slide counts for modified files
- Add note about file purposes:
  - L06_overview: Combined overview (Embeddings + RL)
  - L06_deepdive: Combined deep dive with full RL theory
  - L06b: Beginner visual RL guide (no math)
  - L06e: Modern RL practical guide (no math)
  - L06_rl_full: Standalone RL lecture (for separate RL sessions)
- Acceptance: AGENTS.md accurately reflects current state

**TODO-27: Update manifest.json with new charts** [P2, Small]
- Add entries for charts 20-24 with status "in_progress"
- Update any changed chart references
- Acceptance: manifest.json matches filesystem reality

**TODO-28: Add references for new content** [P2, Small]
- New references needed in deepdive:
  - Levine et al. (2020) for offline RL
  - Chen et al. (2021) for Decision Transformer
  - Konda & Tsitsiklis (2003) for Actor-Critic convergence
  - Liu et al. (2021) for FinRL (already in references, verify)
- Acceptance: All new content has proper citations; references slide updated

### PHASE 8: Verification

**TODO-29: Compile all 5 RL files** [P1, Small]
- Run pdflatex on:
  - L06_overview.tex
  - L06_deepdive.tex
  - L06b_rl_simple.tex
  - L06e_modern_rl_simple.tex
  - L06_rl_full.tex
- Check for: 0 errors, 0 Overfull hbox warnings
- Acceptance: All 5 PDFs generated clean

**TODO-30: Build all new charts** [P1, Small]
- Run python on:
  - 20_rl_taxonomy_tree/chart.py
  - 21_sarsa_vs_qlearning_cliff/chart.py
  - 22_actor_critic_architecture/chart.py
  - 23_offline_vs_online_rl/chart.py
  - 24_bandit_to_mdp_progression/chart.py
- Check each generates chart.pdf without errors
- Acceptance: All 5 chart.pdf files exist and render correctly

**TODO-31: Verify bottomnote coverage** [P1, Small]
- Grep all 5 files for frames missing `\bottomnote{}`
- Fix any gaps
- Acceptance: Every `\begin{frame}` has a corresponding `\bottomnote{}`

**TODO-32: Verify question-based frame titles** [P2, Small]
- Audit all new/modified frames for question-based titles
- Fix any declarative titles (e.g., "RL Taxonomy" -> "Where Does Each Method Fit?")
- Acceptance: 90%+ of frames have question-based titles (exceptions: title slides, chart-only slides)

**TODO-33: Final slide count verification** [P1, Small]
- Verify:
  - L06_overview: ~24-26 slides (acceptable range)
  - L06_deepdive: ~52-55 slides total (main + appendix)
  - L06b: ~17-19 slides
  - L06e: ~13-15 slides (was 11, adding 2-3)
  - L06_rl_full: ~28-30 slides (was 25, adding 3-5)
- Acceptance: No file exceeds budget; all files within acceptable range

---

## Commit Strategy

| Commit | Content | Files |
|--------|---------|-------|
| 1 | New RL charts (TODO 01-05) | 5 new chart.py + chart.pdf |
| 2 | Deepdive RL section overhaul (TODO 06-15) | L06_deepdive.tex |
| 3 | L06e modern RL enhancements (TODO 16-19) | L06e_modern_rl_simple.tex |
| 4 | L06_rl_full consolidation (TODO 20-21) | L06_rl_full.tex |
| 5 | L06b and overview polish (TODO 22-24) | L06b_rl_simple.tex, L06_overview.tex |
| 6 | Cross-file consistency + metadata (TODO 25-28) | All 5 .tex, AGENTS.md, manifest.json |
| 7 | Verification and compilation (TODO 29-33) | Compilation artifacts |

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Deepdive exceeds 55-slide budget | Medium | Medium | Move PPO math to appendix if needed; keep Actor-Critic in main |
| New charts fail to generate | Low | Medium | Use proven chart_style.py patterns from existing charts |
| LaTeX Overfull hbox after adding content | Medium | Low | Use `\small` or split slides; test after each addition |
| L06_rl_full still feels redundant | Medium | Low | Clear file-header comment explaining standalone purpose |
| Offline RL too advanced for MSc | Low | Medium | Keep at conceptual level (CQL name-drop, not math) |
| XKCD replacement for L06e unavailable | Low | Low | Fall back to TikZ comic instead |
| Notation inconsistency across files | Medium | Medium | Audit in dedicated pass (TODO-25) |

---

## Priority Summary

| Priority | Count | Focus |
|----------|-------|-------|
| P1 (Critical) | 16 | Core charts, MVF fixes, taxonomy, Actor-Critic, notation, compilation |
| P2 (Important) | 12 | PPO math, SARSA cliff, offline RL, FinRL, metadata, references |
| P3 (Nice-to-have) | 5 | Bandit teasers in simple files, discount factor aha, XKCD dedup, overview count |

---

## Success Criteria

1. **Content Completeness**: Bandits, Actor-Critic, PPO (with math), Offline RL, FinRL all covered
2. **Pedagogical Flow**: Clear progression from bandits -> Q-learning -> DQN -> Actor-Critic -> PPO
3. **MVF Compliance**: All RL formulas have Motivate-Visualize-Formalize treatment
4. **Chart Integration**: All 19 existing + 5 new charts used in at least one main lecture
5. **Zero Redundancy**: Each of the 5 files has a documented, distinct purpose
6. **Compilation**: All 5 files compile with 0 errors, 0 Overfull
7. **Notation**: Consistent symbols across all 5 files
8. **Finance Integration**: Trading running example threads through deepdive; FinRL practical guidance in L06e
