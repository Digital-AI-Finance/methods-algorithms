# Plan: Ultra-Simple Embeddings & RL Visual Guide

## Task
Create `L06_embeddings_rl_simple.tex` — a beginner-friendly, visually-rich lecture covering Word Embeddings and Reinforcement Learning with TikZ comics, visual analogies, and a curated subset of existing charts. Following the `formula-free-visual-lecture` skill pattern exactly.

## Skill Applied
`skills/formula-free-visual-lecture.md` — adapted from the L05_pca_tsne_simple.tex pattern.

### Skill Adaptation: Parallel-Topics Arc (not Contrast Arc)

The skill's core dramatic engine is "method A fails, method B saves" (e.g., PCA fails on swiss roll, t-SNE succeeds). **This contrast arc does not apply to Embeddings & RL** because they solve completely different problems: embeddings turn text into numbers, RL teaches agents to make decisions. Neither "fails" where the other "succeeds."

**Adaptation**: We use a **parallel-topics arc** instead: "Two complementary AI skills — understanding language (embeddings) and making decisions (RL)." The transition slide frames this as "understanding isn't enough — sometimes you need to act" rather than "method A has a limit."

This changes 3 template slots:
- Slide 12: "Understanding is powerful, but what about action?" (topic pivot, not failure)
- Slides 14-15: RL core concept charts (not "A fails / B saves" pair)
- Act 3 follows the skill's chart pattern (core → diagnostic → realistic) but without the contrast setup

## Requirements
1. **Zero formulas**: No `$$`, no loss functions, no gradient equations. Concepts via pictures only.
2. **Comics**: 4 TikZ stick-figure comics (opening, embedding analogy, RL analogy, closing). Max 25 lines TikZ each, stick figures and geometric shapes only.
3. **Chart subset**: 8 charts curated from existing 25-chart L06 pool.
4. **Embeddings + RL**: Both topics covered with roughly equal weight (~6 slides each).
5. **Course standards**: Madrid theme, 8pt, 16:9, `\bottomnote{}` on every content slide, XKCD bookends.
6. **Standalone file**: Does not replace L06_overview.tex, L06_deepdive.tex, or any existing file.
7. **Preamble**: Copy from L06_embeddings_rl_top10.tex (same color definitions, footer, etc.).

## Acceptance Criteria
- [ ] AC1: .tex compiles with 0 errors, 0 Overfull
- [ ] AC2: ~25 slides (22-28 range)
- [ ] AC3: At least 4 TikZ comics/cartoons (total tikzpictures ~7-9 including diagrams)
- [ ] AC4: Exactly 8 reused charts (no new chart.py files)
- [ ] AC5: Zero `$$` display math
- [ ] AC6: Both Embeddings and RL covered (~6 slides each)
- [ ] AC7: `\bottomnote{}` on every content slide
- [ ] AC8: XKCD bookends (opening + closing)
- [ ] AC9: Second XKCD image copied to L06 images/ folder

## Pre-Requisite
Copy `2173_trained_a_neural_net.png` from L00_Prerequisites/images/ to L06_Embeddings_RL/images/ for the closing bookend.

## Step 1: Chart Curation (8 from existing 25)

Following the skill's story-arc heuristic:

| # | Story Beat | Chart Path | Why |
|---|-----------|------------|-----|
| 1 | "Look, it works!" | `01_word_embedding_space` | Shows words as points — embeddings are visual |
| 2 | "Words have relationships" | `top10_08_word_analogy` | King-Queen analogy — the "wow" moment |
| 3 | "Who's similar?" | `02_similarity_heatmap` | Color-coded similarity — intuitive |
| 4 | "Here's the RL loop" | `03_rl_loop` | Agent-environment diagram — the core concept |
| 5 | "Learning in action" | `04_q_learning_grid` | Gridworld with arrows — see the agent learn |
| 6 | "Does it improve?" | `05_reward_curves` | Reward going up — proof it works |
| 7 | "Explore vs Exploit" | `top10_09_epsilon_greedy` | The key tradeoff visualized |
| 8 | "When to use what" | `07_decision_flowchart` | Decision aid for method selection |

**Why these 8**: They tell two parallel stories (words-as-numbers → analogies → similarity) and (agent-loop → grid → rewards → explore/exploit) without requiring any math.

**Rejected charts** (too complex for simple lecture):
- `08_skipgram_architecture` — requires explaining neural network layers
- `09_dqn_architecture` — requires explaining replay buffers, target networks
- `10_negative_sampling` — requires explaining probability distributions
- `top10_14_qvalue_convergence` — requires explaining convergence theory
- `top10_17_td_learning_update` — requires explaining temporal difference formula

## Step 2: TikZ Comics (4 planned)

| # | Title | Description | Analogy |
|---|-------|-------------|---------|
| C1 | "Lost in Translation" | Stick figure holding word cards "bank", "river", "money". Speech bubble: "These are just letters — how does a computer understand meaning?" | Opening problem |
| C2 | "Words as Addresses" (Embedding analogy) | Simple city grid (rectangles). Words placed at locations: "king" near "queen", "cat" near "dog", far from "car". Caption: "Embeddings = giving every word a home address" | Method A intuition |
| C3 | "The Maze Runner" (RL analogy) | Simple grid maze. Stick figure at start, star at goal. Arrows showing trial paths. Caption: "RL = learning by trying, failing, and trying again" | Method B intuition |
| C4 | "Now the Computer Understands" | Single panel: stick figure happy, speech bubble "I speak AND I decide!", small word-cloud on left side, small grid with arrow-path on right side. Keep simple: ~6 elements max. | Resolution |

**Total TikZ elements: ~7-9** (4 comics + 1 flowchart on slide 9 + 1 TikZ transition on slide 12 + 3 inline icons on slide 16). All subject to 25-line budget.

## Step 3: Slide Plan (~25 slides)

### Front Matter (3 slides)
1. **Title page** — "Embeddings & RL: A Visual Guide"
2. **XKCD Opening** — `images/1838_machine_learning.png` with framing: "How do you teach a computer to understand language and make decisions?"
3. **Learning Objectives** — (1) Explain what word embeddings do, (2) Describe how an RL agent learns from rewards, (3) Choose when to use embeddings vs RL for a problem

### Act 1: The Problem (3 slides)
4. **TikZ Comic C1: "Lost in Translation"** — Computers see text as numbers. But which numbers?
5. **CHART: Word Embedding Space** (`01_word_embedding_space`) — "Look! Words become points in space, and similar words are close together!"
6. **Why can't we just number words 1, 2, 3...?** — Text slide: numbering creates false order (word 3 isn't "between" words 2 and 4), loses meaning, can't capture relationships

### Act 2: Embeddings = Addresses for Words (6 slides)
7. **TikZ Comic C2: "Words as Addresses"** — Embedding = city grid where similar words live in the same neighborhood
8. **CHART: Word Analogy** (`top10_08_word_analogy`) — "King - Man + Woman = Queen — embeddings capture meaning!"
9. **How Embeddings Are Made** — TikZ flowchart (3 steps): Read lots of text → Learn which words appear near each other → Assign coordinates. No formulas.
10. **CHART: Similarity Heatmap** (`02_similarity_heatmap`) — "Dark squares = similar words. The computer learned this from text alone."
11. **Finance Application** — "Banks use embeddings for: sentiment analysis (is this news good or bad?), fraud detection (is this transaction description suspicious?), document search (find similar contracts)"
12. **Transition** — "Embeddings teach computers to understand language. But what about making decisions?"

### Act 3: RL = Learning by Doing (6 slides)
13. **TikZ Comic C3: "The Maze Runner"** — Trial and error in a maze = reinforcement learning
14. **CHART: RL Loop** (`03_rl_loop`) — "The agent acts, the environment responds with a reward, the agent learns"
15. **CHART: Q-Learning Grid** (`04_q_learning_grid`) — "Watch the agent learn the best path — arrows show what it learned"
16. **How RL Works (No Math)** — 3 steps with small TikZ icons: (1) Try an action, (2) Get a reward (or penalty), (3) Update your strategy. Repeat.
17. **CHART: Reward Curves** (`05_reward_curves`) — "The agent gets better over time — rewards go up as it learns"
18. **CHART: Explore vs Exploit** (`top10_09_epsilon_greedy`) — "Explore = try new things. Exploit = stick with what works. RL must balance both."
19. **RL Gotchas** — 3 warnings: (1) Needs LOTS of practice (millions of episodes), (2) Reward design is tricky (agent finds loopholes), (3) Works best in simulation first, then real world

### Act 4: When to Use What (4 slides)
20. **Embeddings vs RL Side-by-Side** — Table: Input (text vs actions), Output (representations vs decisions), Learning (patterns in text vs rewards), Use case (understanding vs acting)
21. **CHART: Decision Flowchart** (`07_decision_flowchart`) — "Follow the arrows to pick the right tool"
22. **Finance Teaser** — "RL agents are being used for: algorithmic trading, portfolio rebalancing, optimal order execution. Embeddings power: chatbots, credit scoring from text, ESG report analysis."
23. **The Python Recipe** — Two columns using `\texttt{}` (not lstlisting):
    - Left (Embeddings): `from gensim.models import Word2Vec` / `model = Word2Vec(sentences, vector_size=100)` / `similar = model.wv.most_similar("bank")`
    - Right (RL): Pseudo-code only (no formulas): `for each episode:` / `  observe state, pick action` / `  get reward, update strategy` / `  repeat until done`

### Closing (3 slides)
24. **TikZ Comic C4: "Now the Computer Understands"** — Resolution of opening
25. **Key Takeaways** — 5 bullets: (1) Embeddings turn words into numbers that capture meaning, (2) Similar words get similar numbers, (3) RL agents learn by trial and error with rewards, (4) Explore vs exploit is the key RL tradeoff, (5) Both are used in finance: embeddings for text, RL for decisions
26. **XKCD Closing** — `images/2173_trained_a_neural_net.png`

**Total: 26 slides, 8 charts, 4 TikZ comics, 0 formulas**

## Implementation Steps

| Step | Description | Files |
|------|-------------|-------|
| 1 | Copy `2173_trained_a_neural_net.png` to L06 images/ | `slides/L06_Embeddings_RL/images/` |
| 2 | Create `L06_embeddings_rl_simple.tex` with preamble from L06_embeddings_rl_top10.tex | `slides/L06_Embeddings_RL/L06_embeddings_rl_simple.tex` |
| 3 | Write all 25 slides following slide plan above | same file |
| 4 | Compile and verify 0 errors, 0 Overfull | `L06_embeddings_rl_simple.pdf` |
| 5 | Copy PDF to docs/ and update index.html | `docs/slides/pdf/`, `docs/index.html` |
| 6 | Update manifest.json | `manifest.json` |

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| RL concepts harder to simplify than PCA | Focus on gridworld (visual) not Bellman equations (math) |
| "Words as Addresses" comic overflow | Keep to 5x4 grid, 5 word labels max, scale=0.75 |
| Only 1 XKCD in L06 images/ | Pre-copy 2173 from L00 (Step 1) |
| Word2Vec code requires gensim not sklearn | Show gensim for embeddings, simple pseudo-code for Q-learning |

## Verification
Same as skill specifies:
```bash
grep -c "begin{frame" FILE.tex           # 22-28
grep -c "chart.pdf" FILE.tex             # 8
grep -c "bottomnote" FILE.tex            # >= 24
grep -c '\$\$' FILE.tex                  # 0
grep -c "begin{tikzpicture}" FILE.tex    # >= 4
pdflatex -interaction=nonstopmode FILE.tex
grep -c "Overfull" FILE.log              # 0
```

---
PLAN_READY: .omc/plans/l06-simple-visual-lecture.md
