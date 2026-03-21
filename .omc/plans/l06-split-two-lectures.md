# Plan: Split L06 Combined Lecture into Two Standalone Lectures

## Task
Split `L06_embeddings_rl_simple.tex` (26 slides covering both Embeddings and RL) into two standalone formula-free visual lectures:
- `L06a_embeddings_simple.tex` (~16 slides, Embeddings only)
- `L06b_rl_simple.tex` (~16 slides, RL only)

Both follow the `formula-free-visual-lecture` skill pattern. The combined file is preserved unchanged.

## Skill Applied
`skills/formula-free-visual-lecture.md` — each standalone lecture gets its own complete narrative arc, TikZ comics, XKCD bookends, and chart selection.

### Skill Adaptation: Shorter Single-Topic Lectures

The skill targets ~25 slides for a contrast/parallel arc across two topics. Each split lecture covers ONE topic, so:
- **Slide budget**: 16-17 slides each (not 25) — 3 front + 7-8 core + 2-3 application + 3 closing
- **Chart budget**: 5 charts each (not 8) — enough for a single-topic arc
- **Comic budget**: 3 TikZ comics each (not 4) — opening problem, method analogy, closing resolution
- **Narrative arc**: Single-topic discovery arc ("problem → method → proof it works → application")

### XKCD Bookend Note

Both lectures use the same XKCD opening (`1838_machine_learning.png`) because only 2 XKCD images are available in `L06_Embeddings_RL/images/`. Each lecture frames the same comic differently (embeddings: "understand words"; RL: "make decisions"). Acquiring additional XKCD images is out of scope for this split.

## Requirements
1. **Zero formulas**: No `$$`, no loss functions, no gradient equations
2. **Comics**: 3 TikZ comics per lecture (opening, analogy, closing). Max 25 lines TikZ each
3. **Charts**: 5 per lecture, curated from existing pool (no new chart.py files)
4. **Course standards**: Madrid theme, 8pt, 16:9, `\bottomnote{}` on every content slide, XKCD bookends
5. **Standalone files**: Do not modify or replace L06_embeddings_rl_simple.tex or any other existing file
6. **Preamble**: Copy from L06_embeddings_rl_simple.tex (identical color definitions, footer, etc.)

## Acceptance Criteria
- [ ] AC1: Both .tex files compile with 0 errors, 0 Overfull
- [ ] AC2: L06a has 14-18 slides, L06b has 15-18 slides
- [ ] AC3: At least 3 TikZ comics per file (total tikzpictures ~5-7 per file including diagrams)
- [ ] AC4: Exactly 5 charts per file (no new chart.py files)
- [ ] AC5: Zero `$$` display math in both files
- [ ] AC6: `\bottomnote{}` on every content slide in both files
- [ ] AC7: XKCD bookends in both files (opening + closing)
- [ ] AC8: Combined file L06_embeddings_rl_simple.tex untouched

## Chart Allocation

### L06a: Embeddings (5 charts)

| # | Story Beat | Chart Path | Why |
|---|-----------|------------|-----|
| 1 | "Look, it works!" | `01_word_embedding_space` | Words as points — the core visual |
| 2 | "Words have math!" | `top10_08_word_analogy` | King-Queen analogy — the wow moment |
| 3 | "Who's similar?" | `02_similarity_heatmap` | Color-coded similarity — intuitive |
| 4 | "Show me neighbors" | `top10_13_embedding_neighbors` | Nearest words to a query — interactive feel |
| 5 | "Real vector arithmetic" | `11_word_analogy_arithmetic` | Visual proof of analogy math |

**Why these 5**: They form a complete discovery arc: see words as points → discover they have math → measure similarity → find neighbors → prove the math works.

### L06b: RL (5 charts)

| # | Story Beat | Chart Path | Why |
|---|-----------|------------|-----|
| 1 | "The RL loop" | `03_rl_loop` | Agent-environment diagram — the core concept |
| 2 | "Watch it learn" | `04_q_learning_grid` | Gridworld arrows — see the agent learn |
| 3 | "Does it improve?" | `05_reward_curves` | Reward going up — proof it works |
| 4 | "Explore vs Exploit" | `top10_09_epsilon_greedy` | The key tradeoff visualized |
| 5 | "See the policy" | `06_policy_viz` | What the agent actually learned — visual |

**Why these 5**: They form a complete RL arc: learn the loop → watch training → see improvement → understand tradeoff → see the final policy.

## TikZ Comics

### L06a: Embeddings Comics (3)

| # | Title | Description |
|---|-------|-------------|
| C1 | "Lost in Translation" | Reuse from combined: stick figure with word cards, speech bubble "These are just letters!" |
| C2 | "Words as Addresses" | Reuse from combined: city grid with words at positions, similar words nearby |
| C3 | "The Computer Gets It" | New: stick figure happy, word cloud organized into clusters. "Now words make sense!" |

### L06b: RL Comics (3)

| # | Title | Description |
|---|-------|-------------|
| C1 | "Robot at a Crossroads" | New: stick figure at T-junction, question marks above, two arrows. "Which way? No map, no teacher." |
| C2 | "The Maze Runner" | Reuse from combined: grid maze with wrong path (dashed red) and learned path (green arrow) |
| C3 | "The Expert Agent" | New: stick figure confidently walking a path, collecting stars. "Practice makes perfect!" |

## Slide Plans

### L06a: Embeddings Simple (~16 slides)

#### Front Matter (3 slides)
1. **Title page** — "Word Embeddings: A Visual Guide" / "Teaching Computers to Understand Language"
2. **XKCD Opening** — `images/1838_machine_learning.png` with framing: "How do you teach a computer to understand words?"
3. **Learning Objectives** — (1) Explain what word embeddings do, (2) Show why numbering words fails, (3) Use embeddings for real tasks

#### Act 1: The Problem (2 slides)
4. **TikZ Comic C1: "Lost in Translation"** — Computers see text as characters, not meaning
5. **Why Not Just Number Words?** — Simple numbering vs embeddings columns (reuse from combined slide 6)

#### Act 2: How Embeddings Work (5 slides)
6. **CHART: Word Embedding Space** (`01_word_embedding_space`) — Words become points, similar words cluster
7. **TikZ Comic C2: "Words as Addresses"** — City grid analogy
8. **CHART: Word Analogy** (`top10_08_word_analogy`) — King - Man + Woman = Queen
9. **How Embeddings Are Made** — TikZ 3-step flowchart (Read Text → Learn Context → Assign Coordinates)
10. **CHART: Similarity Heatmap** (`02_similarity_heatmap`) — Dark = similar, learned from text alone

#### Act 3: Deeper Proof (2 slides)
11. **CHART: Embedding Neighbors** (`top10_13_embedding_neighbors`) — Closest words to a query
12. **CHART: Word Analogy Arithmetic** (`11_word_analogy_arithmetic`) — Visual proof of vector math

#### Act 4: Application (2 slides)
13. **Finance Application** — Sentiment, fraud detection, document search (reuse from combined slide 11)
14. **Try It Yourself** — 3-line gensim code (embeddings column only from combined slide 23)

#### Closing (2 slides)
15. **TikZ Comic C3: "The Computer Gets It"** + Key Takeaways (3 bullets)
16. **XKCD Closing** — `images/2173_trained_a_neural_net.png`

**Total: 16 slides, 5 charts, 3 TikZ comics, ~6 TikZ pictures total, 0 formulas**

### L06b: RL Simple (~16 slides)

#### Front Matter (3 slides)
1. **Title page** — "Reinforcement Learning: A Visual Guide" / "Teaching Computers to Make Decisions"
2. **XKCD Opening** — `images/1838_machine_learning.png` with framing: "How do you teach a computer to make good decisions without a teacher?"
3. **Learning Objectives** — (1) Describe the RL agent-environment loop, (2) Explain explore vs exploit, (3) Identify when RL applies

#### Act 1: The Problem (2 slides)
4. **TikZ Comic C1: "Robot at a Crossroads"** — Agent faces choices with no map
5. **What Makes RL Different?** — Text slide: supervised = labeled data, unsupervised = find patterns, RL = learn from rewards

#### Act 2: How RL Works (5 slides)
6. **CHART: The RL Loop** (`03_rl_loop`) — Act, observe, learn, repeat
7. **TikZ Comic C2: "The Maze Runner"** — Trial and error in a maze
8. **CHART: Q-Learning Grid** (`04_q_learning_grid`) — Watch arrows converge to optimal path
9. **How RL Works (No Math)** — 3 steps with TikZ icons (reuse from combined slide 16)
10. **CHART: Reward Curves** (`05_reward_curves`) — Rewards go up = agent is learning

#### Act 3: Key Concepts (3 slides)
11. **CHART: Explore vs Exploit** (`top10_09_epsilon_greedy`) — The fundamental tradeoff
12. **CHART: Policy Visualization** (`06_policy_viz`) — What the trained agent actually learned
13. **RL Gotchas** — 3 warnings: needs lots of practice, reward design tricky, sim-to-real gap (reuse from combined slide 19)

#### Act 4: Application (2 slides)
14. **Finance Application** — Algorithmic trading, portfolio rebalancing, order execution (RL column from combined slide 22)
15. **Try It Yourself** — RL pseudo-code (RL column only from combined slide 23)

#### Closing (2 slides)
16. **TikZ Comic C3: "The Expert Agent"** + Key Takeaways (3 bullets)
17. **XKCD Closing** — `images/2173_trained_a_neural_net.png`

**Total: 17 slides, 5 charts, 3 TikZ comics, ~6 TikZ pictures total, 0 formulas**

## Implementation Steps

| Step | Description | Files |
|------|-------------|-------|
| 1 | Create `L06a_embeddings_simple.tex` with preamble from combined file | `slides/L06_Embeddings_RL/L06a_embeddings_simple.tex` |
| 2 | Write all 16 Embeddings slides per plan above | same file |
| 3 | Compile L06a, verify 0 errors 0 Overfull | `L06a_embeddings_simple.pdf` |
| 4 | Create `L06b_rl_simple.tex` with preamble from combined file | `slides/L06_Embeddings_RL/L06b_rl_simple.tex` |
| 5 | Write all 17 RL slides per plan above | same file |
| 6 | Compile L06b, verify 0 errors 0 Overfull | `L06b_rl_simple.pdf` |
| 7 | Copy both PDFs to `docs/slides/pdf/`. In `docs/index.html`, replace the existing L06 "Visual Guide" ccard entry with two new entries following the same `<a class="ccard" href="slides/pdf/FILENAME.pdf" download>` pattern: "Embeddings Visual Guide" and "RL Visual Guide" inside the L06 `<div class="cgrid">` block | `docs/slides/pdf/`, `docs/index.html` |
| 8 | Update manifest.json | `manifest.json` |

## Intentionally Omitted

These elements from the combined L06_embeddings_rl_simple.tex are intentionally dropped in the split:

| Combined Slide | Content | Why Dropped |
|---|---|---|
| 12 | Transition TikZ "Understanding vs Action" | Bridges two topics; not needed in single-topic lectures |
| 20 | Comparison table "Embeddings vs RL" | Requires both topics side-by-side |
| 21 | Decision flowchart (`07_decision_flowchart/chart.pdf`) | Compares both methods; not applicable to single-topic |
| 24 | Combined closing comic "Now the Computer Understands" (references both) | Replaced by topic-specific closing comics in each lecture |

## Verification
```bash
# L06a (16 slides: 15 content + 1 title → 15 bottomnotes)
grep -c "begin{frame" L06a_embeddings_simple.tex    # 16
grep -c "chart.pdf" L06a_embeddings_simple.tex       # 5
grep -c "bottomnote" L06a_embeddings_simple.tex      # >= 15
grep -c '\$\$' L06a_embeddings_simple.tex            # 0
grep -c "begin{tikzpicture}" L06a_embeddings_simple.tex  # >= 3
pdflatex -interaction=nonstopmode L06a_embeddings_simple.tex
grep -c "Overfull" L06a_embeddings_simple.log        # 0

# L06b (17 slides: 16 content + 1 title → 16 bottomnotes)
grep -c "begin{frame" L06b_rl_simple.tex             # 17
grep -c "chart.pdf" L06b_rl_simple.tex                # 5
grep -c "bottomnote" L06b_rl_simple.tex               # >= 16
grep -c '\$\$' L06b_rl_simple.tex                     # 0
grep -c "begin{tikzpicture}" L06b_rl_simple.tex       # >= 3
pdflatex -interaction=nonstopmode L06b_rl_simple.tex
grep -c "Overfull" L06b_rl_simple.log                 # 0
```

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Charts top10_13 or 11_word_analogy may not exist | Verified: both directories exist with chart.pdf |
| 06_policy_viz may be too complex for simple lecture | Use only if 2-sentence rule passes; fallback: top10_19_gridworld_trajectory |
| Both lectures use same XKCD opening | Different framing text; only 2 XKCD images available |

---
PLAN_READY: .omc/plans/l06-split-two-lectures.md
