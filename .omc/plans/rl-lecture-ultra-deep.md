# Ultra Deep Improvement: RL Lecture (L06)

**Plan Created:** 2026-03-20
**Plan Revision:** 3 (Critic iteration 2 feedback: Embeddings frame count fix)
**Scope:** Comprehensive overhaul of all 5 RL-related lecture files + charts
**Estimated Complexity:** HIGH (33 TODOs across ~15 files)

---

## Context

### Original Request
Ultra deep improvement of the Reinforcement Learning content in L06, covering all 5 RL-related lecture files, 19 RL charts, and the full pedagogical arc from beginner to advanced.

### Current State Inventory (VERIFIED)

**6 RL-Related Lecture Files:**
| File | Frames (verified) | Split | Level | RL Coverage |
|------|--------------------|-------|-------|-------------|
| `L06_overview.tex` | **25** | 25 main, 0 appendix | Overview | Agent loop, Q-learning intuition, finance table |
| `L06_deepdive.tex` | **54** | **44 main + 10 appendix** | Deepdive | MDP, Bellman, TD, Q-learning algo+worked example, DQN, trading, walk-forward |
| `L06b_rl_simple.tex` | **19** | 19 main | Beginner visual | RL loop, grid Q-learning, rewards, explore/exploit, gotchas, reward shaping |
| `L06e_modern_rl_simple.tex` | **12** | 12 main | Modern visual | Scale problem, DQN, PPO, RLHF, modern stack, 5-line Python |
| `L06_rl_full.tex` | **25** | 25 main | Full standalone | MDP, Bellman, Q-learning, exploration, DQN, trading/portfolio/execution, challenges |
| `L06_rl_mini.tex` | **10** | 10 main | Quick reference | Condensed RL overview |

**23 RL-Related Charts (verified from filesystem):**
Core (7): 03_rl_loop, 04_q_learning_grid, 05_reward_curves, 06_policy_viz, 09_dqn_architecture, 12_epsilon_decay, 13_walkforward_timeline
Extended (4): 15_ppo_training_curve, 16_finbert_sentiment_bars, 17_static_vs_contextual_embedding, 18_rlhf_pipeline, 19_reward_shaping_trading
Top10 (8): top10_09_epsilon_greedy, top10_14_qvalue_convergence, top10_15_state_action_heatmap, top10_16_bandit_regret, top10_17_td_learning_update, top10_19_gridworld_trajectory, top10_20_reward_shaping

Note: Charts 16_finbert_sentiment_bars and 17_static_vs_contextual_embedding are embeddings charts, not RL. The RL chart count is 21.

**XKCD Comic Situation (verified):**
- L06b opens with XKCD #1838, closes with XKCD #2173
- L06e opens with XKCD #2173, closes with XKCD #1838
- Both comics appear in BOTH files (swapped opening/closing positions)

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
2. L06b and L06e swap the same two XKCD comics (#1838, #2173) for opening/closing -- both appear in both files
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
2. Content across 5+ files has significant overlap with inconsistent depth
3. Deepdive appendix A9 (Policy Gradient) is a 1-slide stub covering REINFORCE, Actor-Critic, PPO in 3 bullets
4. Bandit regret chart exists (top10_16) but bandits are never introduced in any lecture file
5. State-action heatmap chart (top10_15) exists but only used in top10 deck, not in any main lecture
6. TD learning update chart (top10_17) exists but not used in deepdive despite having a TD learning slide
7. L06_rl_mini.tex exists (10 frames) but was not in original inventory

**Chart Improvement Opportunities:**
1. Several RL charts not used in any main lecture file (top10_14, top10_15, top10_16, top10_17, top10_19)
2. No chart for model-based vs model-free comparison
3. No chart for Actor-Critic architecture
4. No chart for offline RL concept
5. No chart for RL taxonomy/method family tree
6. No chart for SARSA vs Q-learning cliff-walking (only text description in appendix A7)

**Current Chart Density:**
- Deepdive: 11 charts in 44 main body slides = 1:4.0 ratio (on target)
- Adding 5 new charts + 8 new main slides would be 16:52 = 1:3.25 (slightly chart-heavy but acceptable)

---

## Work Objectives

### Core Objective
Transform the RL content from a decent introduction into a comprehensive, pedagogically excellent MSc-level treatment that covers modern RL, has clear progression across difficulty levels, eliminates redundancy, and deeply integrates finance applications.

### Deliverables
1. Restructured deepdive RL section with 4 new main body slides (net, within budget)
2. Enhanced L06e_modern_rl with offline RL and FinRL content
3. 5 new charts filling visualization gaps
4. Consolidated/differentiated L06_rl_full.tex
5. Fixed pedagogical flow issues in all files
6. All files compile clean (0 errors, 0 Overfull)

### Definition of Done
- All RL formulas follow MVF protocol (Motivate-Visualize-Formalize)
- Bandits, Actor-Critic, PPO, offline RL, and FinRL are properly covered
- No redundant content across the 6 files (each has clear purpose)
- All existing RL charts integrated into at least one main lecture
- 5 new charts created for gap topics
- Every frame has `\bottomnote{}`
- Question-based frame titles throughout
- Finance running example (trading agent) threaded through deepdive
- Deepdive total does NOT exceed 55 frames

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
- All frames compile clean
- Deepdive total <= 55 frames (44 main + 10 appendix currently; 19 Embeddings + 25 RL; budget for +1 net main body)

### Must NOT Have
- Content above MSc level (no measure-theoretic RL, no convergence rate analysis beyond Robbins-Monro)
- More than 55 slides in deepdive total (currently 54)
- Breaking changes to existing chart.py APIs
- New dependencies beyond standard (numpy, matplotlib, scikit-learn, scipy)
- Removal of existing correctly-functioning content

---

## Architect Questions (Addressed)

**Q1: Should some new content go to L06_rl_full instead of deepdive to avoid budget overflow?**

**A: Yes.** The PPO math (full clipped objective formula) will go into L06_rl_full only, NOT the deepdive. The deepdive will get a concise Actor-Critic + "PPO: the key idea" treatment on a SINGLE combined slide, not separate slides. L06_rl_full is the place for full PPO math since it's the standalone deep RL lecture.

**Q2: After promoting A7/A9 to main body, what replaces them in appendix?**

**A: Nothing replaces them. They stay as-is.** We are NOT promoting appendix content to main body. Instead:
- A7 (SARSA vs Q-learning) STAYS in the appendix. The new main body SARSA slide is a separate, lighter treatment with the cliff-walking chart. A7 remains as the detailed formula comparison for advanced students.
- A9 (Policy Gradient Methods) STAYS in the appendix as-is. The new main body Actor-Critic slide provides the visual/intuitive treatment; A9 remains for students who want the REINFORCE formula.
- Net appendix change: 0 slides added, 0 removed. Appendix stays at 10.

**Q3: Should PPO math stay in appendix rather than main body?**

**A: PPO math goes to L06_rl_full, not deepdive at all.** The deepdive main body gets a combined Actor-Critic/PPO intuition slide (no display math beyond the advantage formula). PPO's clipped objective is placed in L06_rl_full (the standalone lecture) where there is ample room. This keeps the deepdive within budget.

---

## Deepdive Slide Budget (CRITICAL)

### Current State: 44 main + 10 appendix = 54 total
### Budget Limit: 55 total (hard cap from CLAUDE.md: 35-45 main + 7-10 appendix)

The current 44 main is at the ceiling of the 35-45 range. Embeddings section = 19 frames (including slide 16b Polysemy), RL section = 25 frames. We have room for exactly **+1 net main body frame**.

### Slide-by-Slide Accounting

| Change | Slides | Running Total (main) | Description |
|--------|--------|---------------------|-------------|
| **Current state** | -- | **44 main** | Verified baseline |
| TODO-06: RL in One Picture | +1 | 45 | New slide after embeddings section, before RL framework |
| TODO-07: Multi-Armed Bandits | +1 | 46 | New slide before MDP |
| TODO-08: Bandits-to-MDP (chart) | +1 | 47 | New slide with progression chart |
| TODO-09: Bellman MVF improvement | 0 | 47 | Modify existing slide 22 in-place |
| TODO-10: RL Taxonomy + Actor-Critic/PPO combo | +1 | 48 | Single combined slide: taxonomy chart + Actor-Critic/PPO intuition |
| **Offset: merge References into one slide** | -1 | 47 | Merge "References: RL and Finance" into "References: Embeddings" (one combined references slide) |
| **Offset: merge Hands-on + Decision Framework** | -1 | 46 | Combine slides 37-38 into one Practice slide |
| **Offset: merge Walk-Forward + Trading Policy** | -1 | 45 | Merge walk-forward content into trading/backtesting slide (currently slides 32-33, merge into one) |
| **Final main body** | -- | **45 main** | +1 net from baseline (4 added, 3 merged). Embeddings=19, RL=26. |
| **Appendix (unchanged)** | -- | **10 appendix** | A1-A10 all stay |
| **TOTAL** | -- | **55** | Exactly at budget cap |

### What About TODO-14 (integrating top10 charts) and TODO-15 (discount factor)?

- **TODO-14** (integrate top10 charts): These are added to EXISTING slides as `\includegraphics` on slides that already have related content. No new frames needed.
- **TODO-15** (discount factor "aha moment"): **DROPPED** to stay within budget. The discount factor is adequately covered in the existing Return/Value Functions slide with the bottomnote. Not worth a full frame.

### Final Deepdive Structure Summary

| Section | Frames | Notes |
|---------|--------|-------|
| Embeddings (slides 1-18 incl. 16b) | 19 | Unchanged (includes Polysemy Visualization 16b) |
| RL in One Picture (new) | 1 | NEW: roadmap slide |
| Bandits intro (new) | 1 | NEW: bandits as simplest RL |
| Bandits-to-MDP (new) | 1 | NEW: progression chart |
| MDP through DQN (slides 19-36, renumbered) | 18 | Existing, Bellman improved in-place |
| RL Taxonomy + Actor-Critic/PPO (new) | 1 | NEW: combined taxonomy + intuition |
| Practice + Summary (merged) | 3 | Was 5, now 3 after merges |
| References (merged) | 1 | Was 2, now 1 combined |
| **Main body total** | **45** | +1 from baseline 44 (4 added, 3 merged) |
| Appendix A1-A10 | 10 | Unchanged |
| **GRAND TOTAL** | **55** | At budget cap |

---

## Task Flow and Dependencies

```
Phase 1: New Charts (independent, parallelizable)
  TODO-01 through TODO-05 (5 new chart.py files)
  |
Phase 2: Deepdive RL Section Overhaul (depends on Phase 1 charts)
  TODO-06 through TODO-14 (slide additions, merges, chart integrations)
  |
Phase 3: L06e Modern RL Enhancement (depends on Phase 1 charts)
  TODO-15 through TODO-18 (new slides, XKCD fix)
  |
Phase 4: L06_rl_full Consolidation (depends on Phases 2-3)
  TODO-19 through TODO-20 (differentiate, add PPO math, update LOs)
  |
Phase 5: L06b & L06_overview Polish (depends on Phase 2)
  TODO-21 through TODO-23 (bandit teaser, taxonomy teaser, rl_mini mention)
  |
Phase 6: Cross-File Consistency & Integration
  TODO-24 through TODO-27 (notation audit, AGENTS.md, manifest, references)
  |
Phase 7: Verification & Compilation
  TODO-28 through TODO-33 (compile, build charts, bottomnote/title audit, slide counts)
```

Note: Phase 1 was "Structural Analysis" in v1 but had no TODOs. The analysis work is captured in the Context section above. Phase numbering now starts at 1 = Charts.

---

## Detailed TODOs

### PHASE 1: New Charts (5 new charts)

**TODO-01: Create `20_rl_taxonomy_tree/chart.py`** [P1, Medium]
- Visualization: Tree diagram showing RL method families (single figure, NO subplots)
  - Root: RL Methods
  - Branch 1: Model-Free -> Value-Based (Q-learning, DQN, Double DQN) | Policy-Based (REINFORCE, PPO, TRPO) | Actor-Critic (A2C, A3C, SAC)
  - Branch 2: Model-Based (Dyna, MBPO, MuZero)
  - Highlight the methods taught in this course in MLOrange
- Implementation: Use matplotlib annotations/patches for tree layout (NOT networkx). Single axes, single figure.
- Style: figsize=(10,6), use chart_style.py, ML color palette
- Output: chart.pdf in same directory
- Acceptance: Tree renders cleanly on single axes, all method names legible, course-covered methods highlighted

**TODO-02: Create `21_sarsa_vs_qlearning_cliff/chart.py`** [P1, Medium]
- Visualization: Classic cliff-walking example (single figure, NO subplots)
  - 4x12 grid with cliff along bottom edge
  - Two paths overlaid: SARSA safe path (MLBlue, goes inland) vs Q-learning optimal path (MLOrange, hugs cliff edge)
  - Start at bottom-left, goal at bottom-right
  - Cliff cells colored MLRed, reward annotations
- Implementation: Single axes with grid drawn via patches/rectangles. Paths as line overlays.
- Style: figsize=(10,6), chart_style.py
- Acceptance: Both paths clearly distinguishable, cliff cells visible, legend identifies SARSA vs Q-learning

**TODO-03: Create `22_actor_critic_architecture/chart.py`** [P1, Medium]
- Visualization: Architecture diagram showing Actor-Critic structure (single figure, NO subplots)
  - Shared state input at top
  - Actor branch: state -> policy pi(a|s) -> action selection
  - Critic branch: state -> V(s) -> advantage computation -> actor update
  - Environment feedback loop at bottom
  - Labels: "Actor (policy)", "Critic (value)", "Advantage = Q - V"
- Implementation: Box-and-arrow diagram using matplotlib patches and FancyArrowPatch. Single axes. Style matching 09_dqn_architecture.
- Style: figsize=(10,6), chart_style.py
- Acceptance: Clear separation of actor/critic, data flow arrows, labels readable

**TODO-04: Create `23_offline_vs_online_rl/chart.py`** [P2, Small]
- Visualization: Side-by-side comparison on a SINGLE axes (NO subplots, NO plt.subplot)
  - Left zone: Online RL loop (agent <-> environment, live interaction)
  - Right zone: Offline RL (static dataset -> agent learns, no interaction)
  - Center divider line with label "vs"
  - Finance motivation text at bottom ("Live trading data is expensive and risky")
- Implementation: Single axes divided into zones using annotations, patches, and arrows. NOT separate subplot panels.
- Style: figsize=(10,6), chart_style.py
- Acceptance: Clear visual distinction between online and offline paradigms on single axes

**TODO-05: Create `24_bandit_to_mdp_progression/chart.py`** [P2, Medium]
- Visualization: Single-axes horizontal flow diagram (NOT subplots, NOT plt.subplot)
  - Three connected zones arranged left-to-right on ONE axes:
    - Zone 1: Multi-armed bandit (one state circle, k arms radiating out with reward labels)
    - Zone 2: Contextual bandit (state -> action -> reward, no transitions)
    - Zone 3: Full MDP (state -> action -> next state -> reward, transition arrows)
  - Large arrows between zones labeled "Add states", "Add transitions"
- Implementation: All drawn on a SINGLE matplotlib axes using patches, annotations, and FancyArrowPatch. This is a connected diagram, not three separate panels.
- Style: figsize=(10,6), chart_style.py
- Acceptance: Clear progression, zones visually distinct via background shading, arrows connecting zones

### PHASE 2: Deepdive RL Section Overhaul (L06_deepdive.tex)

**TODO-06: Add "RL in One Picture" slide before MDP formalism** [P1, Medium]
- Location: Insert after current slide 18 (embeddings finance example), before slide 19 (RL framework)
- Content: Conceptual overview slide with TikZ showing the full RL landscape:
  - Central: Agent-Environment loop
  - Surrounding labels: "What we'll cover: Bandits -> Q-learning -> DQN -> Actor-Critic"
  - Finance context: "Running example: training a trading agent"
- Must have: `\bottomnote{}`, question-based title ("What Does the RL Landscape Look Like?")
- Budget impact: +1 main body frame
- Acceptance: Provides roadmap before diving into formulas; mentions all topics

**TODO-07: Add Multi-Armed Bandits entry point slide** [P1, Medium]
- Location: Insert after "RL in One Picture", before MDP slide
- Content:
  - "What If There's Only One State?" -- bandits as simplest RL
  - k-armed bandit: pull arm -> get reward, goal = maximize total reward
  - Connect to top10_16_bandit_regret chart via `\includegraphics`
  - Finance analogy: "Which of k trading strategies to allocate capital to?"
  - Motivate: "Bandits are RL with no state transitions -- the simplest case"
- Must have: MVF protocol (motivate with finance, visualize with chart, formalize regret)
- Budget impact: +1 main body frame
- Acceptance: Bandit framed as gateway to full RL; chart integrated; finance example clear

**TODO-08: Add Bandits-to-MDP progression slide** [P1, Small]
- Location: After bandits slide, before MDP
- Content: Use chart 24_bandit_to_mdp_progression
  - "From Bandits to MDPs: Adding Complexity One Step at a Time"
  - Bandit (no states) -> Contextual bandit (states but no transitions) -> Full MDP
  - "The MDP adds state transitions -- now the future depends on your actions"
- Budget impact: +1 main body frame
- Acceptance: Clear logical bridge from bandits to MDP; chart integrated

**TODO-09: Improve Bellman Equation slide with MVF protocol** [P1, Medium]
- Location: Current deepdive slide 22 (modify in-place, NO new frame)
- Changes:
  - Add MOTIVATE block: "Why do we need a recursive equation? Because evaluating a policy directly requires summing infinite futures"
  - Add VISUALIZE: Small TikZ tree showing one-step lookahead (s -> a -> s' with r and gamma labels)
  - Keep FORMALIZE: existing Bellman equation
  - Improve worked example: make it a 3-state trading scenario (not abstract A/B/C)
    - State: "Cash" -> buy -> "Holding" (reward = -commission) -> sell -> "Cash" (reward = +profit)
- Budget impact: 0 (in-place modification)
- Acceptance: MVF structure visible; trading example; TikZ tree

**TODO-10: Add combined RL Taxonomy + Actor-Critic/PPO intuition slide** [P1, Medium]
- Location: After DQN section (current slide 36), before Practice section
- Content: SINGLE slide with two-column layout:
  - Left column: RL taxonomy chart (20_rl_taxonomy_tree) at 0.45\textwidth
  - Right column: 4-bullet summary:
    - "Value-based: learn Q-values (Q-learning, DQN) -- this lecture"
    - "Policy-based: learn actions directly (REINFORCE, PPO)"
    - "Actor-Critic: Actor chooses, Critic evaluates -- best of both"
    - "PPO: clip policy updates to prevent catastrophic changes"
  - Bottom: "See appendix A9 for policy gradient math; see L06_rl_full for full PPO derivation"
- This is intentionally NOT the full PPO math. The clipped objective goes into L06_rl_full (see TODO-19).
- Budget impact: +1 main body frame
- Acceptance: Taxonomy chart integrated; Actor-Critic and PPO explained intuitively; student knows where to find the math

**TODO-11: Enhance appendix A7 (SARSA vs Q-Learning) with cliff-walking chart** [P2, Medium]
- Location: Existing appendix A7 (SARSA vs Q-Learning) -- modify in-place, NO new frame
- Reason for appendix-only: Budget correction (Embeddings = 19 frames, not 18) means we cannot add another main body slide. The plan's fallback is to keep SARSA in appendix only.
- Changes to A7:
  - Add `\includegraphics` of new chart 21_sarsa_vs_qlearning_cliff (use two-column layout)
  - Left column: chart showing cliff-walking paths
  - Right column: existing SARSA vs Q-learning formula comparison (keep as-is)
  - Add finance note in bottomnote: "SARSA accounts for execution risk"
- Budget impact: 0 (appendix modification only, no change to main body or appendix count)
- Acceptance: Chart integrated into A7; cliff-walking visualization enhances existing formula comparison

**TODO-12: Merge References slides into one** [P1, Small]
- Location: Current slides 43-44 ("References: Embeddings" and "References: RL and Finance")
- Change: Combine into a single "References" slide. Use `\small` or `\scriptsize` for the combined list. Both reference lists are short enough to fit one slide.
- Budget impact: -1 main body frame
- Acceptance: Single references slide, all citations present, readable

**TODO-13: Merge Hands-on + Decision Framework slides** [P1, Small]
- Location: Current slides 37-38 ("Hands-on Exercise" and "Decision Framework and Best Practices")
- Change: Combine into one "Practice: Hands-on Exercise and Decision Framework" slide:
  - Top half: 3-bullet hands-on exercise (compressed from current 5 bullets)
  - Bottom half: 3 key decision rules (compressed from current table)
- Budget impact: -1 main body frame
- Acceptance: Both practice elements on one slide, no overflow

**TODO-14: Merge Walk-Forward + Trading Policy slides** [P1, Small]
- Location: Current slides 34-35 ("Walk-Forward Validation Timeline" and "Trading Policy")
- Change: Combine into one "How Do You Validate and Deploy a Trading Policy?" slide:
  - Walk-forward chart stays as visual
  - Policy summary bullets folded in as 2-3 items
- Budget impact: -1 main body frame
- Acceptance: Walk-forward + policy on one slide, chart visible

**TODO-15: Integrate unused top10 charts into existing deepdive slides** [P2, Small]
- No new frames. Add `\includegraphics` to EXISTING slides:
  - top10_14_qvalue_convergence: Add as small inset on Q-learning algorithm slide (slide 26) -- use `\begin{columns}` if needed
  - top10_15_state_action_heatmap: Add to Q-values visualization slide (slide 27, line ~567)
  - top10_17_td_learning_update: Add to TD learning slide (slide 25, line ~477)
- For each: specify exact slide by frame title and line number range
- Budget impact: 0 (modify existing slides)
- Acceptance: Each chart appears with `\includegraphics` in a main lecture slide

### PHASE 3: L06e Modern RL Enhancement

**TODO-16: Add Offline RL slide to L06e** [P1, Medium]
- Location: After RLHF slide (current slide 9)
- Content:
  - "What If You Can't Explore? Offline RL"
  - Use chart 23_offline_vs_online_rl
  - Finance motivation: "Live trading exploration is expensive. Offline RL learns from historical trade logs."
  - Key approaches: Conservative Q-Learning (CQL), Decision Transformer (name-drop only)
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

**TODO-18: Differentiate L06e XKCD comics from L06b** [P3, Small]
- Problem: L06b opens with XKCD #1838 and closes with #2173. L06e opens with #2173 and closes with #1838. Both comics appear in BOTH files.
- Fix: Replace BOTH L06e comics:
  - L06e opening: Replace XKCD #2173 with XKCD #2048 "Curve Fitting" (relevant to RL overfitting) OR create TikZ comic showing "From Q-Tables to Neural Networks"
  - L06e closing: Replace XKCD #1838 with a new TikZ comic or XKCD #1425 "Tasks" (relevant to AI difficulty)
- Acceptance: L06b and L06e share ZERO XKCD comics; each has unique opening and closing

### PHASE 4: L06_rl_full Consolidation

**TODO-19: Differentiate L06_rl_full.tex and add PPO math** [P1, Large]
- Problem: L06_rl_full duplicates ~80% of deepdive RL section content
- Decision: Reposition as "RL-Only Standalone Lecture" for when RL is taught separately from Embeddings. This file carries the full PPO math that the deepdive intentionally omits.
- Changes needed:
  - Add a header comment: `%% Standalone RL lecture for use when taught separately from Embeddings`
  - Add bandits entry point slide (matching deepdive TODO-07 content)
  - Add Actor-Critic slide with chart 22 (matching deepdive TODO-10 but expanded)
  - Add PPO slide WITH full clipped objective math:
    - $L^{CLIP}(\theta) = \mathbb{E}[\min(r_t(\theta) A_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) A_t)]$
    - This is the math that the deepdive deliberately skips (deepdive just gives intuition)
  - Add offline RL slide WITH formulas (CQL penalty term, unlike formula-free L06e version)
  - Add RL taxonomy chart (matching deepdive TODO-10)
  - Remove course-wrap-up slide (slide 24 -- only makes sense in combined L06 context)
- This is a REWRITE of selected sections, not a copy-paste from deepdive. The deepdive gives intuition; L06_rl_full gives the full math.
- Net change: approximately +4 slides, -1 slide = +3 (from 25 to ~28)
- Acceptance: L06_rl_full is a coherent standalone RL lecture; contains full PPO math; doesn't require Embeddings context

**TODO-20: Update L06_rl_full learning objectives** [P2, Small]
- Current LOs are Bloom's 4-5 but miss Actor-Critic, PPO, offline RL
- New LOs:
  1. Formalize sequential decisions as MDPs and solve with Q-learning
  2. Derive the Bellman equation and analyze convergence conditions
  3. Evaluate model-free RL methods (Q-learning vs SARSA vs PPO) for trading applications
  4. Critique RL trading strategies accounting for transaction costs, non-stationarity, and offline constraints
- Acceptance: LOs reflect expanded scope; Bloom's 4-5 maintained

### PHASE 5: L06b & L06_overview Polish

**TODO-21: Add bandit teaser to L06b** [P3, Small]
- Location: After "What Makes RL Different?" slide (slide 5)
- Content: 1 slide introducing multi-armed bandit as the simplest RL problem
  - TikZ comic: stick figure facing 3 slot machines
  - "Which machine pays the most? You can only find out by trying."
  - No math, purely visual
- Acceptance: L06b introduces bandits as RL gateway; consistent with deepdive

**TODO-22: Add RL taxonomy teaser to L06_overview** [P3, Small]
- Location: After "How Does an Agent Learn from Rewards?" (around slide 14)
- Content: Brief 1-slide mention: "Beyond Q-learning: the RL family"
  - Simple 3-item list: Value-based (today), Policy-based (PPO in L06e), Actor-Critic (deepdive)
  - "Q-learning is just the beginning -- see the deepdive for the full picture"
- Acceptance: Overview sets up deepdive content; no formulas

**TODO-23: Note L06_rl_mini.tex in plan scope** [P3, Small]
- L06_rl_mini.tex exists (10 frames) as a quick-reference condensed RL overview
- Action: No changes needed to L06_rl_mini.tex itself, but update AGENTS.md to mention it
- Acceptance: L06_rl_mini.tex acknowledged in documentation; not modified

### PHASE 6: Cross-File Consistency & Integration

**TODO-24: Ensure consistent RL notation across all 6 files** [P1, Medium]
- Audit all 6 RL files (including L06_rl_mini.tex) for:
  - Q-function notation: $Q(s,a)$ vs $Q^*(s,a)$ vs $Q^\pi(s,a)$ used consistently
  - Reward notation: $r_t$ vs $R_t$ vs $R_{t+1}$ -- pick one convention
  - Policy notation: $\pi(a|s)$ vs $\pi(s)$ used correctly (stochastic vs deterministic)
  - Discount factor: $\gamma$ used consistently (not $\delta$ or other symbols)
  - Learning rate: $\alpha$ in all files
- Acceptance: Same symbol means the same thing across all 6 files

**TODO-25: Update AGENTS.md with new chart inventory** [P2, Small]
- Add new charts (20-24) to the chart table in AGENTS.md
- Update slide counts for modified files to verified values
- Add L06_rl_mini.tex to the file table
- Add note about file purposes:
  - L06_overview: Combined overview (Embeddings + RL), 25 frames
  - L06_deepdive: Combined deep dive with full RL theory, 54->55 frames
  - L06b: Beginner visual RL guide (no math), 19 frames
  - L06e: Modern RL practical guide (no math), 12->14 frames
  - L06_rl_full: Standalone RL lecture with full math (for separate RL sessions), 25->28 frames
  - L06_rl_mini: Quick-reference condensed RL overview, 10 frames
- Acceptance: AGENTS.md accurately reflects current state including new charts and all files

**TODO-26: Update manifest.json with new charts** [P2, Small]
- Add entries for charts 20-24 with status "in_progress"
- Update any changed chart references
- Acceptance: manifest.json matches filesystem reality

**TODO-27: Add references for new content** [P2, Small]
- New references needed in deepdive:
  - Levine et al. (2020) for offline RL
  - Chen et al. (2021) for Decision Transformer
  - Konda & Tsitsiklis (2003) for Actor-Critic convergence
  - Liu et al. (2021) for FinRL (already in references, verify)
- References needed in L06_rl_full:
  - Schulman et al. (2017) for PPO (verify already present)
  - Same offline RL references as deepdive
- Acceptance: All new content has proper citations; references slides updated

### PHASE 7: Verification

**TODO-28: Build all new charts** [P1, Small]
- Run python on:
  - 20_rl_taxonomy_tree/chart.py
  - 21_sarsa_vs_qlearning_cliff/chart.py
  - 22_actor_critic_architecture/chart.py
  - 23_offline_vs_online_rl/chart.py
  - 24_bandit_to_mdp_progression/chart.py
- Check each generates chart.pdf without errors
- Acceptance: All 5 chart.pdf files exist and render correctly

**TODO-29: Compile all 6 RL files** [P1, Small]
- Run pdflatex on:
  - L06_overview.tex
  - L06_deepdive.tex
  - L06b_rl_simple.tex
  - L06e_modern_rl_simple.tex
  - L06_rl_full.tex
  - L06_rl_mini.tex
- Check for: 0 errors, 0 Overfull hbox warnings
- Acceptance: All 6 PDFs generated clean

**TODO-30: Verify bottomnote coverage** [P1, Small]
- Grep all 6 files for frames missing `\bottomnote{}`
- Fix any gaps
- Acceptance: Every `\begin{frame}` has a corresponding `\bottomnote{}`

**TODO-31: Verify question-based frame titles** [P2, Small]
- Audit all new/modified frames for question-based titles
- Fix any declarative titles (e.g., "RL Taxonomy" -> "Where Does Each Method Fit?")
- Acceptance: 90%+ of frames have question-based titles (exceptions: title slides, chart-only slides, appendix divider)

**TODO-32: Final slide count verification** [P1, Small]
- Verify against budget:
  - L06_overview: 25-27 frames (currently 25, adding 1 = 26)
  - L06_deepdive: **exactly 55** frames (45 main + 10 appendix, see budget table above)
  - L06b: 19-21 frames (currently 19, adding 1 = 20)
  - L06e: 12-14 frames (currently 12, adding 2 = 14)
  - L06_rl_full: 25-30 frames (currently 25, net +3 = 28)
  - L06_rl_mini: 10 frames (unchanged)
- Acceptance: No file exceeds its budget; deepdive at exactly 55

**TODO-33: Verify chart density ratio** [P2, Small]
- Target: approximately 1 chart per 4 slides in main body
- Deepdive: after changes = ~14 charts in 45 main body slides = 1:3.2 (acceptable, slightly chart-heavy)
- If ratio is below 1:3, consider moving one chart reference to appendix
- Acceptance: Chart ratio between 1:3 and 1:5 for all files

---

## Commit Strategy

| Commit | Content | Files |
|--------|---------|-------|
| 1 | New RL charts (TODO 01-05) | 5 new chart.py + chart.pdf |
| 2 | Deepdive RL section overhaul (TODO 06-15) | L06_deepdive.tex |
| 3 | L06e modern RL enhancements (TODO 16-18) | L06e_modern_rl_simple.tex |
| 4 | L06_rl_full consolidation + PPO math (TODO 19-20) | L06_rl_full.tex |
| 5 | L06b and overview polish (TODO 21-23) | L06b_rl_simple.tex, L06_overview.tex |
| 6 | Cross-file consistency + metadata (TODO 24-27) | All 6 .tex, AGENTS.md, manifest.json |
| 7 | Verification and compilation (TODO 28-33) | Compilation artifacts |

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Deepdive hits 56+ after slide merges don't compress enough | Medium | High | Merges specified precisely (3 merges = -3 frames); SARSA already demoted to appendix-only (iteration 3 fix). If a merge fails, drop TODO-08 bandits-to-MDP (fold content into TODO-07 bandits slide) |
| New charts fail to generate | Low | Medium | Use proven chart_style.py patterns from existing charts; architecture diagrams use patches not networkx |
| LaTeX Overfull hbox after adding content | Medium | Low | Use `\small` or split bullets; test after each addition |
| TODO-05 single-axes diagram too crowded | Medium | Low | If the 3-zone layout doesn't fit on one axes at figsize=(10,6), use figsize=(12,6) as exception or simplify zones |
| L06_rl_full still feels redundant | Medium | Low | Clear file-header comment + PPO math differentiator + offline RL with formulas |
| XKCD replacements for L06e unavailable | Low | Low | Fall back to TikZ comic instead |
| Notation inconsistency across files | Medium | Medium | Dedicated audit pass (TODO-24) |
| L06_rl_mini.tex breaks after other changes | Low | Low | It's independent; only update AGENTS.md to mention it |

---

## Priority Summary

| Priority | Count | Focus |
|----------|-------|-------|
| P1 (Critical) | 18 | Core charts, MVF fixes, taxonomy, Actor-Critic, slide merges, notation, compilation |
| P2 (Important) | 10 | SARSA cliff (appendix), offline RL, FinRL, chart integration, metadata, references, chart density |
| P3 (Nice-to-have) | 5 | Bandit teasers in simple files, XKCD dedup, overview teaser, rl_mini mention |

---

## Success Criteria

1. **Content Completeness**: Bandits, Actor-Critic, PPO (intuition in deepdive, math in L06_rl_full), Offline RL, FinRL all covered
2. **Pedagogical Flow**: Clear progression from bandits -> Q-learning -> DQN -> Actor-Critic -> PPO
3. **MVF Compliance**: All RL formulas have Motivate-Visualize-Formalize treatment
4. **Chart Integration**: All existing RL charts + 5 new charts used in at least one main lecture
5. **Zero Redundancy**: Each of the 6 files has a documented, distinct purpose
6. **Budget Compliance**: Deepdive at exactly 55 frames (45 main + 10 appendix), proven by slide-by-slide accounting
7. **Compilation**: All 6 files compile with 0 errors, 0 Overfull
8. **Notation**: Consistent symbols across all 6 files
9. **Finance Integration**: Trading running example threads through deepdive; FinRL practical guidance in L06e
10. **No Subplots**: All 5 new charts use single-axes layout per CLAUDE.md rules
