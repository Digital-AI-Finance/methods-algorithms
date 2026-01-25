<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 | Updated: 2026-01-25 -->

# L06_Embeddings_RL/

**Parent**: [../AGENTS.md](../AGENTS.md) (slides/)

## Purpose

Lesson 6 introduces representation learning (word embeddings) and reinforcement learning with sentiment analysis and trading strategies as motivating finance cases. Students learn Word2Vec, Q-learning, and how to design reward functions.

## Finance Case

**Problem 1**: Banks need to analyze sentiment in earnings calls and news articles. Word embeddings capture semantic relationships (e.g., "bullish" ≈ "optimistic").

**Problem 2**: Trading algorithms must learn optimal actions (buy/sell/hold) from delayed rewards (profit/loss). Q-learning provides a framework for sequential decision making.

**Key Decision**: When to use embeddings vs bag-of-words, and when RL applies vs supervised learning.

## Learning Objectives

1. **Understand**: Explain word embeddings and similarity measures (cosine similarity)
2. **Apply**: Implement Q-learning for simple grid-world and trading environments
3. **Analyze**: Interpret embedding spaces for semantic relationships (e.g., king - man + woman ≈ queen)
4. **Create**: Design reward functions for trading agents (risk-adjusted returns)

## Files

| File | Purpose | Slides |
|------|---------|--------|
| `L06_overview.tex` | Overview slides with 7 charts | ~17 |
| `L06_deepdive.tex` | Deep dive with Q-learning derivation | ~30 |
| `L06_instructor_guide.md` | Teaching guide with PMSP breakdown | - |

## Charts

All charts follow the naming convention `XX_descriptive_name/` and output `chart.pdf`:

| Chart | Directory | Description | Key Visual |
|-------|-----------|-------------|------------|
| 01 | `01_word_embedding_space/` | 2D embedding projection | Financial terms in 2D space (e.g., "profit", "loss", "equity") |
| 02 | `02_similarity_heatmap/` | Cosine similarity matrix | Heatmap showing word-word similarities |
| 03 | `03_rl_loop/` | Agent-environment interaction | State → Action → Reward → Next State cycle |
| 04 | `04_q_learning_grid/` | Q-values in grid world | Heatmap showing learned Q-values per state-action |
| 05 | `05_reward_curves/` | Learning progress | Cumulative reward vs episode number |
| 06 | `06_policy_viz/` | Optimal policy | Arrows showing best action per state |
| 07 | `07_decision_flowchart/` | When to use embeddings/RL | Flowchart for algorithm selection |

## Chart Technical Details

**Standard settings** (same as L01-L05):
```python
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})
```

**Color palette**:
- MLPurple: #3333B2 (structure)
- MLBlue: #0066CC (Q-values, embeddings)
- MLOrange: #FF7F0E (optimal actions, high similarity)
- MLGreen: #2CA02C (positive rewards)
- MLRed: #D62728 (negative rewards, penalties)

## Building Charts

```bash
# Build all charts for L06 (from project root)
python infrastructure/course_cli.py build charts --topic L06

# Build single chart manually
cd slides/L06_Embeddings_RL/01_word_embedding_space
python chart.py

# Verify all charts generated
python infrastructure/course_cli.py validate charts --topic L06
```

## LaTeX Compilation

```bash
# Compile overview slides (from L06 directory)
cd slides/L06_Embeddings_RL
pdflatex -interaction=nonstopmode L06_overview.tex

# Compile deep dive slides
pdflatex -interaction=nonstopmode L06_deepdive.tex

# Clean auxiliary files
mkdir temp 2>nul & move *.aux *.log *.nav *.out *.snm *.toc temp/

# Build via CLI (from project root)
python infrastructure/course_cli.py build slides --topic L06
```

## PMSP Structure

The instructor guide breaks down the 3-hour session:

| Phase | Duration | Content |
|-------|----------|---------|
| **Problem** | 15 min | Sentiment analysis motivation, trading strategy learning |
| **Method** | 45 min | Word2Vec algorithm, Q-learning (Bellman equation, ε-greedy) |
| **Solution** | 45 min | Gensim Word2Vec implementation, Q-learning from scratch |
| **Practice** | 75 min | Jupyter notebook `L06_embeddings_rl.ipynb` with text corpus and grid world |

## Key Concepts - Embeddings

- **Word Embeddings**: Dense vector representations capturing semantic relationships
- **Word2Vec**: Two architectures: CBOW (predict word from context) and Skip-gram (predict context from word)
- **Cosine Similarity**: cos(θ) = (A·B) / (||A|| ||B||) measures semantic similarity
- **Analogies**: king - man + woman ≈ queen (vector arithmetic captures relationships)
- **Applications**: Sentiment analysis, document similarity, feature engineering

## Key Concepts - Reinforcement Learning

- **MDP**: Markov Decision Process (S, A, R, P, γ) framework
- **Q-Learning**: Off-policy TD algorithm learning Q(s,a) = expected future reward
- **Bellman Equation**: Q(s,a) = R + γ max_a' Q(s',a')
- **ε-greedy**: Exploration vs exploitation trade-off
- **Reward Design**: Critical for RL success (e.g., Sharpe ratio for trading)

## Q-Learning Algorithm

```python
# Pseudocode
for episode in range(n_episodes):
    s = env.reset()
    while not done:
        a = epsilon_greedy(Q[s])  # Explore vs exploit
        s', r, done = env.step(a)
        Q[s,a] = Q[s,a] + α * (r + γ * max(Q[s']) - Q[s,a])  # TD update
        s = s'
```

## Decision Framework

**When to use Word Embeddings**:
- Text similarity tasks (sentiment, clustering)
- Semantic relationships needed
- Large text corpus available
- Pre-trained models exist (Word2Vec, GloVe, BERT)

**When to use Reinforcement Learning**:
- Sequential decision making (trading, routing)
- Learning from interaction (no labels)
- Delayed rewards (long-term optimization)
- Exploration beneficial

**When NOT to use**:
- Embeddings: Small corpus, structured features better
- RL: Static prediction tasks, need sample efficiency, real-time critical (slow training)

## Common Pitfalls

1. **Word2Vec**: Need large corpus (millions of words for quality embeddings)
2. **Hyperparameters**: Window size (5-10), embedding dimension (100-300)
3. **Q-Learning**: Reward scaling critical (normalize to [-1, 1] range)
4. **Exploration**: Too much ε → slow convergence, too little → suboptimal policy
5. **Discount Factor γ**: High (0.99) → long-term, low (0.5) → myopic

## Hyperparameter Tuning

**Word2Vec**:
| Parameter | Effect | Typical Range |
|-----------|--------|---------------|
| `vector_size` | Embedding dimension | 100-300 |
| `window` | Context window | 5-10 |
| `min_count` | Rare word threshold | 5-100 |

**Q-Learning**:
| Parameter | Effect | Typical Range |
|-----------|--------|---------------|
| `α` (learning rate) | Update step size | 0.01-0.5 |
| `γ` (discount) | Future reward weight | 0.9-0.99 |
| `ε` (exploration) | Random action probability | 0.1-0.3 (decaying) |

## Testing Checklist

- [ ] All 7 chart.py scripts generate chart.pdf
- [ ] L06_overview.tex compiles without errors
- [ ] L06_deepdive.tex compiles without errors
- [ ] ZERO "Overfull \hbox" warnings in LaTeX output
- [ ] Embedding space shows semantic clusters (e.g., financial terms grouped)
- [ ] Q-learning reward curve shows convergence
- [ ] Policy visualization shows sensible actions

## Related Assets

- **Notebook**: `notebooks/L06_embeddings_rl.ipynb`
- **Dataset**: `datasets/text_corpus_synthetic.json` (financial news articles)
- **Quiz**: `quizzes/quiz3_topics_5_6.xml` (covers L05 + L06)
- **Template**: `templates/beamer_template.tex`, `templates/chart_template.py`

## Prerequisites

Students should know:
- L01-L02 (gradient descent for Word2Vec)
- Probability (conditional probability, expectation for RL)
- Python basics (NumPy for Q-learning implementation)

## Course Completion

This is the final lesson. Students complete the course with:
- **Capstone Project**: 10-15 page report applying methods to finance problem
- **Presentations**: 15-minute talks on selected ML topics
- **Quiz 3**: Covers L05 (PCA/t-SNE) and L06 (Embeddings/RL)

## Extensions

**Advanced Topics** (not covered in this course):
- Deep RL (DQN, A3C, PPO)
- Transformer embeddings (BERT, GPT)
- Multi-agent RL
- Meta-learning

**Further Reading**:
- Sutton & Barto: Reinforcement Learning (RL bible)
- Mikolov et al.: Word2Vec papers
- OpenAI Gym: RL environments
