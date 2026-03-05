# Plan: L06 Full Lecture Decks + Visual-Heavy Notebooks

## Task
Bring L06 (Embeddings & RL) to parity with L03/L04/L05 by creating:
1. Embeddings full technical lecture (L06_embeddings_full.tex, ~25 slides)
2. RL full technical lecture (L06_rl_full.tex, ~25 slides)
3. Embeddings visual-heavy notebook (L06_embeddings.ipynb, ~17 cells, ~8 visuals)
4. RL visual-heavy notebook (L06_rl.ipynb, ~18 cells, ~8 visuals)

Plus: compile, deploy PDFs, update GH Pages + manifest, commit + push.

## Current State

### Existing L06 Assets
| File | Frames | Charts | Status |
|------|--------|--------|--------|
| L06_overview.tex | 24 | 4 (01, 03, 05, 07) | committed |
| L06_deepdive.tex | 50 | 6 (02, 04, 06, 08, 09, 10) | committed |
| L06_embeddings_mini.tex | 10 | 2 (01, 02) | committed |
| L06_rl_mini.tex | 10 | 2 (03, 04) | committed |
| L06_embeddings_rl.ipynb | combined | — | committed |

### Missing (vs L03/L04/L05 pattern)
| Asset | L05 Equivalent |
|-------|----------------|
| L06_embeddings_full.tex | L05_pca_full.tex |
| L06_rl_full.tex | L05_tsne_full.tex |
| L06_embeddings.ipynb | L05_pca.ipynb |
| L06_rl.ipynb | L05_tsne.ipynb |

Note: L06 already has TWO mini-lectures (embeddings_mini + rl_mini), matching L05's pattern. No additional mini-lectures needed.

### Chart Folders (10 total)
| ID | Content | Embeddings? | RL? |
|----|---------|-------------|-----|
| 01_word_embedding_space | Word vectors in 2D/3D | ✓ | |
| 02_similarity_heatmap | Cosine similarity between words | ✓ | |
| 03_rl_loop | Agent-environment loop | | ✓ |
| 04_q_learning_grid | Q-values on gridworld | | ✓ |
| 05_reward_curves | Cumulative reward over episodes | | ✓ |
| 06_policy_viz | Arrow policy on grid | | ✓ |
| 07_decision_flowchart | When to use embeddings vs RL | ✓ | |
| 08_skipgram_architecture | Skip-gram neural network | ✓ | |
| 09_dqn_architecture | Deep Q-Network diagram | | ✓ |
| 10_negative_sampling | Negative sampling illustration | ✓ | |

### XKCD Images
| Image | File | Use |
|-------|------|-----|
| #1838 machine_learning | images/1838_machine_learning.png | Both full decks (only XKCD available) |

---

## Deck Architecture & Chart Reuse Policy

### Relationship Between Slide Decks

L06 follows the same multi-deck architecture as L03/L04/L05:

| Deck Type | Purpose | Audience | Standalone? |
|-----------|---------|----------|-------------|
| **Overview** (L06_overview.tex) | Course-level intro covering BOTH Embeddings and RL | All students, first exposure | Yes |
| **Deepdive** (L06_deepdive.tex) | Course-level theory covering BOTH topics | All students, detailed theory | Yes |
| **Embeddings Mini** (L06_embeddings_mini.tex) | 10-slide BSc-accessible Embeddings overview | Gentle intro | Yes — 2 embedding charts |
| **RL Mini** (L06_rl_mini.tex) | 10-slide BSc-accessible RL overview | Gentle intro | Yes — 2 RL charts |
| **Embeddings Full** (L06_embeddings_full.tex) | Deep standalone Embeddings lecture | Topic-specific depth | Yes — 5 embedding charts |
| **RL Full** (L06_rl_full.tex) | Deep standalone RL lecture | Topic-specific depth | Yes — 5 RL charts |

### Chart Reuse Policy

Charts are shared across deck types (course-level vs topic-specific) — same pattern as L03/L04/L05. The "one chart per file" rule applies **within a tier**: no chart appears in BOTH embeddings_full AND rl_full.

### XKCD Image Reuse

Only one XKCD available (#1838 machine_learning). Used in all existing files. Will be reused as closing in embeddings_full. RL_full will use a TikZ closing comic instead (trading robot) to avoid exact repetition.

---

## Chart Allocation

### Embeddings Full (~25 slides): 5 charts
01_word_embedding_space, 02_similarity_heatmap, 07_decision_flowchart, 08_skipgram_architecture, 10_negative_sampling
→ Density: 25/5 = 1:5.0 (acceptable — 10 charts across 50 slides)

### RL Full (~25 slides): 5 charts
03_rl_loop, 04_q_learning_grid, 05_reward_curves, 06_policy_viz, 09_dqn_architecture
→ Density: 25/5 = 1:5.0 (acceptable)

### Within-tier exclusivity
Zero overlap between embeddings_full and rl_full chart sets. ✓

---

## Deliverable 1: L06_embeddings_full.tex (~25 slides)

### Design
- Three-zone architecture: INTRO (1-5, no formulas) → CORE (6-19, formulas) → CLOSING (20-25)
- 5 charts (01, 02, 07, 08, 10)
- TikZ comic opening (slide 2), XKCD #1838 closing (slide 25)
- Finance domain: sentiment analysis, financial NLP, named entity recognition
- Question-style frame titles, max 3-4 bullets per slide

### Slide-by-Slide

**INTRO (slides 1-5, no formulas)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 1 | Title Page | Title | "Word Embeddings: Teaching Machines to Understand Language" |
| 2 | "How Would You Teach a Computer What 'Bullish' Means?" | TikZ comic | Trader explaining market sentiment to a confused robot. "Words are just strings — how do we make them mathematical?" |
| 3 | Learning Objectives | LO list | 4 LOs: (1) Derive the Skip-gram objective and explain negative sampling, (2) Analyze embedding spaces using cosine similarity and analogy tasks, (3) Evaluate Word2Vec vs GloVe vs contextual embeddings, (4) Apply embeddings to financial sentiment analysis |
| 4 | "What Is a Word Embedding?" | Two-column | Left: "A mapping from words to dense vectors where similar words have similar vectors." king-queen=man-woman analogy. Right: key terms (embedding, dense vector, cosine similarity). |
| 5 | "Why Not Just Use One-Hot Encoding?" | Two-column | One-hot: sparse, no similarity. Embeddings: dense, capture semantics. Example: "bullish" and "optimistic" are far in one-hot, close in embedding space. |

**CORE — METHOD (slides 6-14)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 6 | "What Does the Embedding Space Look Like?" | Full-size chart | 01_word_embedding_space (0.65\textwidth). Words clustered by meaning. Finance words near each other. |
| 7 | "The Distributional Hypothesis" | Definition block | "You shall know a word by the company it keeps" (Firth, 1957). Words in similar contexts → similar meanings → similar vectors. |
| 8 | "Skip-gram: Predicting Context from a Word" | Chart + text | 08_skipgram_architecture. Given center word, predict surrounding words. Window size = how far to look. |
| 9 | "The Skip-gram Objective" | Formula + intuition | $\max \frac{1}{T}\sum_{t=1}^{T}\sum_{-c \le j \le c, j\neq 0} \log p(w_{t+j}|w_t)$. Where $p(w_O|w_I) = \frac{\exp(\mathbf{v}'_{w_O} \cdot \mathbf{v}_{w_I})}{\sum_{w=1}^{V}\exp(\mathbf{v}'_w \cdot \mathbf{v}_{w_I})}$. "Softmax over entire vocabulary — expensive!" |
| 10 | "Negative Sampling: Making Training Feasible" | Chart + text | 10_negative_sampling. Instead of softmax over V words, sample k negatives. $\log \sigma(\mathbf{v}'_{w_O} \cdot \mathbf{v}_{w_I}) + \sum_{i=1}^{k} \mathbb{E}[\log \sigma(-\mathbf{v}'_{w_i} \cdot \mathbf{v}_{w_I})]$. |
| 11 | "Measuring Similarity: Cosine Distance" | Chart + text | 02_similarity_heatmap. $\cos(\mathbf{a}, \mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}$. Show heatmap of finance term similarities. |
| 12 | "Word Analogies: The Magic of Vector Arithmetic" | Worked example | king - man + woman ≈ queen. Worked: compute numerically with 3D vectors. Finance: stock - equity + debt ≈ bond. |
| 13 | "GloVe: Global Vectors from Co-occurrence" | Two-column | GloVe minimizes: $\sum_{i,j} f(X_{ij})(\mathbf{w}_i \cdot \tilde{\mathbf{w}}_j + b_i + \tilde{b}_j - \log X_{ij})^2$. Combines global statistics with local context. Comparison table: Skip-gram (predictive) vs GloVe (count-based). |
| 14 | "When to Use Which Approach?" | Chart + text | 07_decision_flowchart. Decision tree: corpus size, task type, interpretability needs. |

**CORE — SOLUTION (slides 15-19)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 15 | "Financial Sentiment Analysis with Embeddings" | Two-column | Train Word2Vec on financial news corpus. Cluster: "bullish", "rally", "surge" vs "bearish", "crash", "plunge". Use as features for sentiment classifier. |
| 16 | "From Words to Documents: Averaging Embeddings" | Step-by-step | Document vector = mean of word vectors. TF-IDF weighting. Example: average embedding of an earnings call transcript → sentiment score. |
| 17 | "Contextual Embeddings: BERT and Beyond" | Comparison table | Static (Word2Vec, GloVe): same vector regardless of context. Contextual (BERT, GPT): "bank" has different vectors in "river bank" vs "investment bank". Trade-offs: speed vs quality. |
| 18 | "Embeddings as Preprocessing for ML" | Code [fragile] | sklearn Pipeline: text → TfidfVectorizer → TruncatedSVD(n_components=50) → LogisticRegression. "Simple embedding pipeline for classification." |
| 19 | "Named Entity Recognition in Finance" | Two-column | Embedding-based NER: identify company names, ticker symbols, monetary amounts in text. "Embeddings capture that 'AAPL' and 'Apple' refer to the same entity." |

**CLOSING (slides 20-25)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 20 | "When to Use Embeddings — and When Not To" | Pros/Cons | Pros: capture semantics, transfer learning, compact. Cons: need large corpus, not interpretable, static context (Word2Vec). |
| 21 | "Embeddings vs Bag-of-Words vs TF-IDF" | Comparison table | Sparsity, semantics, dimensionality, training data needed, interpretability. |
| 22 | "Hands-on: Explore Financial Word Vectors" | Code [fragile] | Code snippet for loading embeddings and computing similarities. Link to L06_embeddings.ipynb. |
| 23 | "Key Takeaways" | Summary | Left: concepts (distributional hypothesis, Skip-gram, negative sampling, cosine similarity). Right: practice (pre-trained > train-your-own, check analogies, BERT for context). |
| 24 | "What's Next: Reinforcement Learning" | Bridge | "Embeddings represent language. RL learns to ACT. Next: how agents learn optimal strategies from rewards." |
| 25 | "Closing Thought" | XKCD #1838 | `images/1838_machine_learning.png` with attribution. |

---

## Deliverable 2: L06_rl_full.tex (~25 slides)

### Design
- Three-zone architecture: INTRO (1-5) → CORE (6-19) → CLOSING (20-25)
- 5 charts (03, 04, 05, 06, 09)
- TikZ comic opening (slide 2), TikZ closing comic (slide 25) — no second XKCD available
- Finance domain: algorithmic trading, portfolio optimization, order execution
- Question-style titles, max 3-4 bullets

### Slide-by-Slide

**INTRO (slides 1-5, no formulas)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 1 | Title Page | Title | "Reinforcement Learning: Learning to Act from Rewards" |
| 2 | "Can a Machine Learn to Trade Stocks by Trial and Error?" | TikZ comic | Robot trader at a desk, making trades, seeing green (+$) and red (-$) outcomes. Thought bubble: "Buy low, sell high... but when?" |
| 3 | Learning Objectives | LO list | 4 LOs: (1) Formalize sequential decisions as MDPs with states, actions, rewards, (2) Derive the Bellman equation and implement Q-learning, (3) Analyze exploration-exploitation tradeoffs using epsilon-greedy, (4) Apply RL to algorithmic trading and portfolio management |
| 4 | "What Is Reinforcement Learning?" | Two-column | Left: "An agent learns to make decisions by interacting with an environment and receiving rewards." Not supervised (no labels), not unsupervised (has a goal). Right: key terms (agent, environment, state, action, reward, policy). |
| 5 | "Why Not Just Use Supervised Learning?" | Two-column | Supervised: needs labeled data. RL: learns from outcomes. Trading: "What's the correct action?" has no label — you only know P&L after the fact. Delayed rewards: today's trade affects tomorrow's portfolio. |

**CORE — METHOD (slides 6-14)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 6 | "The Agent-Environment Loop" | Full-size chart | 03_rl_loop (0.65\textwidth). State → Action → Reward → Next State → repeat. |
| 7 | "Markov Decision Process (MDP)" | Definition block | Tuple $(S, A, P, R, \gamma)$. $P(s'|s,a)$: transition probability. $R(s,a)$: reward. $\gamma \in [0,1]$: discount factor. Markov property: future depends only on current state. |
| 8 | "The Return and Value Functions" | Formula + intuition | Return: $G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}$. State-value: $V^\pi(s) = \mathbb{E}_\pi[G_t | S_t = s]$. Action-value: $Q^\pi(s,a) = \mathbb{E}_\pi[G_t | S_t = s, A_t = a]$. "How good is it to be in state s (or take action a in state s)?" |
| 9 | "The Bellman Equation" | Formula + worked example | $Q(s,a) = R(s,a) + \gamma \sum_{s'} P(s'|s,a) \max_{a'} Q(s',a')$. Worked: 3-state grid, compute Q-values by hand with $\gamma=0.9$. |
| 10 | "Q-Learning: Model-Free Temporal Difference" | Algorithm + chart | 04_q_learning_grid. Update: $Q(s,a) \leftarrow Q(s,a) + \alpha[R + \gamma \max_{a'} Q(s',a') - Q(s,a)]$. No need to know transition probabilities! |
| 11 | "Exploration vs Exploitation" | Two-column | Exploit: choose best known action. Explore: try random action. Epsilon-greedy: $\varepsilon$ chance of random action. Decaying epsilon: explore more early, exploit more later. |
| 12 | "Watching the Agent Learn" | Chart + text | 05_reward_curves. Cumulative reward over episodes. "Initially random, then converges to optimal policy." |
| 13 | "Visualizing the Learned Policy" | Full-size chart | 06_policy_viz. Arrows on grid showing optimal action per cell. |
| 14 | "Deep Q-Networks (DQN)" | Chart + text | 09_dqn_architecture. Replace Q-table with neural network. Experience replay + target network for stability. "Scales to continuous/large state spaces." |

**CORE — SOLUTION (slides 15-19)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 15 | "Algorithmic Trading as an MDP" | Two-column | State: (price, position, time). Actions: buy/sell/hold. Reward: realized P&L. "The trading agent learns when to enter and exit positions." |
| 16 | "Portfolio Optimization with RL" | Two-column | State: current portfolio weights + market features. Action: rebalance weights. Reward: risk-adjusted return (Sharpe ratio). "RL naturally handles transaction costs and constraints." |
| 17 | "Optimal Execution: Minimizing Market Impact" | Step-by-step | Large order → split into slices. RL agent decides timing and sizing. State: remaining shares, time left, market volatility. Reward: -slippage cost. |
| 18 | "Reward Engineering: The Hardest Part of RL" | Two-column | Bad reward: maximize return → agent takes extreme leverage. Better: maximize Sharpe ratio. Even better: maximize return with drawdown penalty. "The reward function IS your specification of the problem." |
| 19 | "RL Challenges in Finance" | Two-column | Non-stationarity: markets change. Partial observability: can't see everything. Sample efficiency: live trading data is expensive. Sim-to-real gap: backtests ≠ live markets. |

**CLOSING (slides 20-25)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 20 | "When to Use RL — and When Not To" | Pros/Cons | Pros: handles sequential decisions, no labels needed, adapts. Cons: slow training, reward design hard, sim-to-real gap, hard to debug. |
| 21 | "RL vs Supervised Learning vs Optimization" | Comparison table | Data needs, sequential decisions, adaptability, interpretability, training time. |
| 22 | "Hands-on: Train a Q-Learning Agent" | Code [fragile] | Gridworld Q-learning code snippet. Link to L06_rl.ipynb. |
| 23 | "Key Takeaways" | Summary | Left: concepts (MDP, Bellman, Q-learning, DQN, exploration). Right: practice (start with tabular, reward design matters, always compare to baseline, beware overfitting to backtest). |
| 24 | "Course Wrap-Up: From Regression to RL" | Bridge | "L01: predict → L02: classify → L03: cluster → L04: ensemble → L05: reduce → L06: represent & act. Your ML toolbox is complete." |
| 25 | "Closing Thought" | TikZ comic | Trading robot sitting on pile of profits, saying "I learned this all by trial and error... mostly error." With `\bottomnote{Thank you for a great semester! Good luck with your group assignments.}` |

---

## Deliverable 3: L06_embeddings.ipynb (~17 cells, ~8 visuals)

### Pattern
Follow L05_pca.ipynb exactly: markdown headers + code cells, ML color palette, no exercises.

**rcParams note:** Notebooks use `font.size=12` (matching L04/L05 convention), NOT `font.size=14` (CLAUDE.md chart standard). Intentional.

### Dataset
Use sklearn's 20 Newsgroups (small subset) for text data, plus a pre-defined small word embedding matrix for visualization:
```python
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
```
For word-level demos, use a small hand-crafted embedding matrix (10-15 finance words with 3D vectors) to avoid requiring gensim.

### Cell Structure

| # | Type | Content | Visual? |
|---|------|---------|---------|
| 1 | MD | Title "Word Embeddings: Visual Guide" + Colab badge + 4 LOs | — |
| 2 | Code | Setup: imports (TfidfVectorizer, TruncatedSVD, cosine_similarity), ML palette, rcParams, seed | — |
| 3 | MD | "## 1. One-Hot vs Dense Embeddings" | — |
| 4 | Code | Create 10 finance words, show one-hot matrix (sparse) vs dense embedding matrix (3D). Side-by-side heatmaps. | Visual 1: One-hot vs dense comparison |
| 5 | MD | "## 2. Exploring the Embedding Space" | — |
| 6 | Code | 15 finance words with hand-crafted 3D embeddings (bullish/bearish clusters). 3D scatter with annotations. | Visual 2: 3D embedding space |
| 7 | Code | Cosine similarity heatmap between all 15 words | Visual 3: Similarity heatmap |
| 8 | MD | "## 3. Word Analogies" | — |
| 9 | Code | king-man+woman=queen analogy. Also: stock-equity+debt≈bond. Bar chart showing nearest neighbors after vector arithmetic. | Visual 4: Analogy results |
| 10 | MD | "## 4. TF-IDF: A Simple Text Representation" | — |
| 11 | Code | Load 20newsgroups subset (200 docs, 4 categories). TfidfVectorizer. Show feature matrix shape and sparsity. Top terms per category bar chart. | Visual 5: Top TF-IDF terms |
| 12 | MD | "## 5. SVD Embeddings from TF-IDF" | — |
| 13 | Code | TruncatedSVD(n_components=2) on TF-IDF matrix. Scatter colored by category. | Visual 6: Document embeddings |
| 14 | MD | "## 6. Embeddings for Classification" | — |
| 15 | Code | Compare classification accuracy: raw TF-IDF (high-D) vs SVD(50) vs SVD(10). Bar chart of accuracies with LogisticRegression. | Visual 7: Embedding dimension vs accuracy |
| 16 | Code | t-SNE of SVD embeddings colored by category (for visualization) | Visual 8: t-SNE of document embeddings |
| 17 | MD | Summary with 4 bullets | — |

### Colab Badge URL
`https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L06_embeddings.ipynb`

---

## Deliverable 4: L06_rl.ipynb (~18 cells, ~8 visuals)

### Dataset
Pure numpy gridworld environment. No external dependencies.
```python
# 5x5 gridworld: start at (0,0), goal at (4,4), walls, traps
```

### Cell Structure

| # | Type | Content | Visual? |
|---|------|---------|---------|
| 1 | MD | Title "Reinforcement Learning: Visual Guide" + Colab badge + 4 LOs | — |
| 2 | Code | Setup: imports (numpy, matplotlib), ML palette, rcParams, seed=42 | — |
| 3 | MD | "## 1. The Gridworld Environment" | — |
| 4 | Code | Define 5x5 gridworld with start, goal, walls, traps. Visualize the grid with colored cells and labels. | Visual 1: Gridworld layout |
| 5 | MD | "## 2. Random Policy" | — |
| 6 | Code | Run random policy for 100 episodes. Show one trajectory on grid + cumulative reward histogram. | Visual 2: Random policy trajectory |
| 7 | MD | "## 3. Q-Learning Implementation" | — |
| 8 | Code | Implement Q-learning loop: initialize Q-table, epsilon-greedy, update rule. Train for 500 episodes. Print final Q-table shape. | — |
| 9 | Code | Plot cumulative reward per episode (learning curve). Moving average overlay. | Visual 3: Learning curve |
| 10 | MD | "## 4. Visualizing the Learned Policy" | — |
| 11 | Code | Show policy as arrows on grid (argmax of Q-values per state) | Visual 4: Optimal policy arrows |
| 12 | Code | Heatmap of max Q-values per state | Visual 5: Q-value heatmap |
| 13 | MD | "## 5. Exploration vs Exploitation" | — |
| 14 | Code | Train with epsilon=0.0, 0.1, 0.3, 0.5. Plot learning curves for each. | Visual 6: Epsilon comparison |
| 15 | MD | "## 6. Discount Factor Effect" | — |
| 16 | Code | Train with gamma=0.5, 0.9, 0.99. Plot final Q-value heatmaps side-by-side (1x3). | Visual 7: Gamma comparison |
| 17 | MD | "## 7. Decaying Epsilon Schedule" | — |
| 18 | Code | Implement linear epsilon decay. Compare fixed vs decaying epsilon learning curves. | Visual 8: Decay comparison |
| 19 | MD | Summary with 4 bullets | — |

### Colab Badge URL
`https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L06_rl.ipynb`

---

## GH Pages Updates

### docs/index.html changes

1. **Hero stat** (line 126): `<b>36</b>` → `<b>38</b>` (PDFs: +2 for embeddings_full + rl_full)
2. **Hero stat**: `<b>12</b><small>Notebooks</small>` → `<b>14</b><small>Notebooks</small>` (+2 split notebooks)
3. **L06 section** (around line 329-332): After existing RL Mini card, add 2 new PDF cards:
```html
<a class="ccard" href="slides/pdf/L06_embeddings_full.pdf" download><div class="ccard-icon">PDF</div>Embeddings Full Lecture<div class="ccard-label">25-slide embedding theory</div></a>
<a class="ccard" href="slides/pdf/L06_rl_full.pdf" download><div class="ccard-icon">PDF</div>RL Full Lecture<div class="ccard-label">25-slide RL theory</div></a>
```
4. **Relabel existing notebook**: "Colab Notebook" → "Combined Notebook" with label "Embeddings + RL Combined"
5. **Add 2 new notebook cards**:
```html
<a class="ccard" href="https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L06_embeddings.ipynb" target="_blank"><div class="ccard-icon">NB</div>Embeddings Notebook<div class="ccard-label">Visual-heavy embeddings</div></a>
<a class="ccard" href="https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L06_rl.ipynb" target="_blank"><div class="ccard-icon">NB</div>RL Notebook<div class="ccard-label">Visual-heavy Q-learning</div></a>
```

### manifest.json changes

Add to L06 assets (after existing entries, before closing of L06 block). Also backfill missing mini-lecture entries:
```json
"embeddings_mini_slides": {
    "file": "slides/L06_Embeddings_RL/L06_embeddings_mini.tex",
    "status": "complete"
},
"rl_mini_slides": {
    "file": "slides/L06_Embeddings_RL/L06_rl_mini.tex",
    "status": "complete"
},
"embeddings_full_slides": {
    "file": "slides/L06_Embeddings_RL/L06_embeddings_full.tex",
    "status": "complete"
},
"rl_full_slides": {
    "file": "slides/L06_Embeddings_RL/L06_rl_full.tex",
    "status": "complete"
},
"notebook_embeddings": {
    "file": "notebooks/L06_embeddings.ipynb",
    "status": "complete"
},
"notebook_rl": {
    "file": "notebooks/L06_rl.ipynb",
    "status": "complete"
}
```

---

## Implementation Steps

### Step 0: Verify all chart.pdf files exist
- Confirm all 10 chart.pdf files are present in slides/L06_Embeddings_RL/

### Step 1: Create L06_embeddings_full.tex
- Copy preamble from L06_embeddings_mini.tex (same 100-line preamble as all L06 files)
- ~25 slides as specified above
- 5 charts, TikZ opening, XKCD #1838 closing

### Step 2: Create L06_rl_full.tex
- Same preamble
- ~25 slides as specified above
- 5 charts, TikZ opening, TikZ closing comic

### Step 3: Compile both tex files
- `pdflatex -interaction=nonstopmode` (2 passes each)
- Verify 0 Overfull warnings

### Step 4: Create L06_embeddings.ipynb
- ~17 cells, ~8 visuals
- Finance words + 20newsgroups for text demos
- ML color palette, figsize=(10,6), font.size=12

### Step 5: Create L06_rl.ipynb
- ~18 cells, ~8 visuals (actually 19 cells per table above)
- Pure numpy gridworld Q-learning
- ML color palette, same rcParams

### Step 6: Test both notebooks
- `jupyter nbconvert --execute` for each

### Step 7: Deploy to GH Pages
- Copy 2 PDFs to docs/slides/pdf/
- Update docs/index.html (hero stats, L06 section)
- Update manifest.json

### Step 8: Commit and push

---

## Acceptance Criteria

1. `L06_embeddings_full.tex` exists with ~25 slides, 5 charts (01, 02, 07, 08, 10), TikZ + XKCD #1838
2. `L06_rl_full.tex` exists with ~25 slides, 5 charts (03, 04, 05, 06, 09), TikZ opening + TikZ closing
3. Both tex files compile with 0 errors, 0 Overfull warnings
4. `L06_embeddings.ipynb` exists with ~17 cells, ~8 visuals, finance word embeddings + 20newsgroups
5. `L06_rl.ipynb` exists with ~19 cells, ~8 visuals, gridworld Q-learning
6. Both notebooks execute without errors
7. docs/index.html hero stats: 38 PDFs, 14 notebooks
8. docs/index.html L06 section: 6 PDF cards + 3 notebook cards (Combined, Embeddings, RL)
9. manifest.json: 6 new entries (embeddings_mini backfill, rl_mini backfill, embeddings_full, rl_full, notebook_embeddings, notebook_rl)
10. Both PDFs deployed to docs/slides/pdf/
11. No chart appears in BOTH embeddings_full AND rl_full
12. Changes committed and pushed to master

---

## Risk Assessment

| Risk | Mitigation |
|------|------------|
| fetch_20newsgroups requires internet on first run | Use `subset='train'`, categories=['sci.space','rec.sport.baseball','comp.graphics','talk.politics.misc'] (4 cats, ~200 docs per). Colab has internet. |
| Hand-crafted embeddings may not show clean clusters | Use clearly separated finance terms: {bullish, rally, surge, profit} vs {bearish, crash, plunge, loss} vs {stock, bond, equity, debt}. |
| Q-learning may not converge in 500 episodes | Use small 5x5 grid, alpha=0.1, gamma=0.99, epsilon=0.1. This reliably converges. |
| TikZ comics cause Overfull warnings | Keep simple: stick figures, speech bubbles. Test individually. |
| chart.pdf files missing or stale | Step 0 verifies all 10 chart.pdf files exist. |
| Only 1 XKCD available for 2 full decks | RL full uses TikZ closing comic instead of XKCD. |
| 20newsgroups download slow in some environments | Use `remove=('headers','footers','quotes')` to reduce size. First run caches locally. |

---

PLAN_READY: .omc/plans/l06-full-decks-notebooks.md
