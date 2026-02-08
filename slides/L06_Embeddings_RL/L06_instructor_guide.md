# Instructor Guide: L06 - Embeddings & Reinforcement Learning

## Session Overview

| Aspect | Details |
|--------|---------|
| **Duration** | 3 hours (180 min) |
| **Topic** | Word Embeddings and Reinforcement Learning |
| **Finance Case** | Sentiment analysis (FinBERT), algorithmic trading (Q-learning) |
| **Prerequisites** | L01-L05, basic probability, linear algebra |
| **Deepdive Slides** | ~35 frames |
| **Overview Slides** | ~15 frames |

## Learning Objectives (Bloom's Level 4-5)

By the end of this session, students will be able to:

1. **Derive** the Skip-Gram objective and analyze the negative sampling approximation
2. **Evaluate** static vs. contextual embeddings for domain-specific NLP tasks (e.g., FinBERT)
3. **Analyze** the convergence properties of Q-learning and the role of the exploration-exploitation tradeoff
4. **Critique** RL-based trading strategies and their limitations (transaction costs, non-stationarity, overfitting)

## PMSP Structure

### Problem Phase (15 min)

**Slides**: Title, Outline, Word Embeddings Introduction (deepdive)

**Motivation**: Present two distinct challenges in finance.

**Key Questions to Ask**:
- How do we extract meaning from financial news?
- Why can't we just count words? (one-hot encoding limitations)
- How do trading bots learn to trade without labeled data?

**Discussion Points**:
- Text is unstructured; ML needs numbers
- Embeddings capture semantics (similar meaning = similar vectors)
- Trading is sequential decisions with delayed rewards
- Firth (1957): "You shall know a word by the company it keeps"

### Method Phase --- Part 1: Embeddings (30 min)

**Slides covered** (deepdive):
1. **Word2Vec: Skip-gram** (4 min) --- softmax objective, training procedure
2. **Skip-gram: Computational Challenge** (4 min) --- why full softmax is intractable, negative sampling objective
3. **Negative Sampling Illustrated** (2 min) --- chart showing positive/negative pairs
4. **Skip-gram Architecture** (2 min) --- two embedding matrices W and W'
5. **Skip-Gram with Negative Sampling: Algorithm** (4 min) --- formal pseudocode, walk through line by line; emphasize the 3/4 power for noise distribution
6. **Word Embedding Space** (2 min) --- chart showing finance term clusters
7. **Word Analogies** (2 min) --- vector arithmetic examples
8. **Word Analogy Limitations** (4 min) --- CRITICAL: stress that success rates are 40-70%, not near 100%; discuss bias in embeddings (Bolukbasi et al., 2016)
9. **Similarity Measures** (2 min) --- cosine similarity formula, heatmap chart
10. **Pre-trained Embeddings** (2 min) --- Word2Vec, GloVe, FastText, FinBERT
11. **Static vs Contextual Embeddings** (2 min) --- one fixed vector vs context-dependent; polysemy problem

**Teaching Notes**:
- When covering negative sampling pseudocode, ask students why the 3/4 power helps (downweights frequent words like "the")
- The analogy limitations slide is important for critical thinking --- do not skip
- Static vs contextual distinction: use the "bank" example (river bank vs bank account)

### Method Phase --- Part 2: RL Framework (20 min)

**Slides covered** (deepdive):
1. **RL Framework** (4 min) --- agent, environment, state, action, reward + chart
2. **Markov Decision Process** (4 min) --- MDP tuple, Markov property; note gamma in [0,1) for continuing, [0,1] for episodic
3. **Policy and Value Functions** (4 min) --- policy, V-function, Q-function definitions
4. **Bellman Equation** (4 min) --- optimal Q-function, recursive structure, optimal policy derivation
5. **Temporal Difference Learning** (4 min) --- TD(0) update, TD error as "surprise signal", comparison to MC and DP

### Method Phase --- Part 3: Embeddings in Finance (7 min)

**Slides covered** (deepdive):
1. **Embeddings in Finance** (3 min) --- applications list, sentence embedding approaches (note averaging limitation: "bank robber" = "robber bank")
2. **Finance Example: Embedding-Based Sentiment** (4 min) --- worked example with cosine similarity to sentiment anchors; note FinBERT achieves up to 87% accuracy (Araci, 2019), not the commonly cited but unsourced 92%

### Solution Phase --- Q-Learning Deep Dive (25 min)

**Slides covered** (deepdive):
1. **Q-Learning Algorithm** (4 min) --- update rule, informal algorithm steps
2. **Q-Learning: Worked Example** (6 min) --- walk through arithmetic step by step; verify: -0.5 + 0.9 x 4.0 - 3.2 = -0.1, then 3.2 + 0.1 x (-0.1) = 3.19
3. **Q-Learning Algorithm: Pseudocode** (4 min) --- formal pseudocode with line numbers; emphasize that max makes it off-policy (Watkins & Dayan, 1992)
4. **Q-Values Visualization** (3 min) --- chart with arrows showing policy, colors showing values
5. **Exploration vs Exploitation** (4 min) --- epsilon-greedy, decay schedule
6. **Learning Curves** (4 min) --- reward improvement chart, DQN vs tabular comparison

### Solution Phase --- RL in Finance (15 min)

**Slides covered** (deepdive):
1. **RL for Trading** (4 min) --- state/action/reward formulation, challenges
2. **Trading Reward Function Design** (3 min) --- reward with transaction costs, state features, alternative rewards (Sharpe, log return)
3. **Backtesting RL Trading Strategies** (3 min) --- walk-forward validation, honest evaluation, "if it beats buy-and-hold after costs, verify carefully"
4. **Trading Policy** (2 min) --- policy visualization chart
5. **Deep Q-Networks** (3 min) --- DQN loss, experience replay, target network

### Solution Phase --- Advanced Topics (8 min)

**Slides covered** (deepdive):
1. **Policy Gradient Methods** (4 min) --- policy gradient theorem, REINFORCE, Actor-Critic, PPO
2. **Statistical Inference for Embeddings & RL** (4 min) --- bootstrap CI for cosine similarity, Q-value confidence intervals, off-policy evaluation

**Break** (10 min)

### Practice Phase (45 min)

**Slides**: Hands-on Exercise frame (both overview and deepdive)

**Hands-on Notebook**:
- Students work through L06_embeddings_rl.ipynb
- Sentiment analysis with embeddings
- Simple trading environment with Q-learning

**Exercise Difficulty Progression**:
1. Load embeddings, find similar words (guided)
2. Build sentence embeddings by averaging (semi-guided)
3. Implement Q-learning for simple trading (open-ended)

### Wrap-up Phase (10 min)

**Slides covered** (deepdive):
1. **When to Use What** (3 min) --- decision flowchart chart
2. **Comparison Table** (2 min) --- embeddings vs RL side-by-side
3. **Implementation** (2 min) --- Python libraries overview
4. **Practical Tips** (2 min) --- start simple, iterate, validate
5. **Summary** (2 min) --- key takeaways
6. **References** (1 min) --- point students to Sutton & Barto (free online)

## Detailed Timing Guide

| Phase | Duration | Slides | Notes |
|-------|----------|--------|-------|
| Problem | 15 min | 3 frames | Motivate both topics |
| Method: Embeddings | 30 min | 11 frames | Includes negative sampling + SGNS pseudocode + analogy limitations + static vs contextual |
| Method: RL Framework | 20 min | 5 frames | MDP through TD learning |
| Method: Finance NLP | 7 min | 2 frames | Worked sentiment example |
| Solution: Q-Learning | 25 min | 6 frames | Worked example + pseudocode + exploration |
| Solution: RL Finance | 15 min | 5 frames | Trading formulation through DQN |
| Solution: Advanced | 8 min | 2 frames | Policy gradient + inference |
| **Break** | **10 min** | --- | |
| Practice | 45 min | 1 frame | Hands-on notebook |
| Wrap-up | 10 min | 6 frames | Decision framework + summary |
| **TOTAL** | **185 min** | **~35 deepdive** | 5 min buffer for Q&A/transitions |

## Key Equations

### Embeddings

**Skip-Gram Objective:**
$$\max \sum_{t=1}^{T} \sum_{-c \leq j \leq c, j \neq 0} \log p(w_{t+j} \mid w_t)$$

**Negative Sampling Objective:**
$$\log \sigma(v'_{w_O}{}^T v_{w_I}) + \sum_{i=1}^{k} \mathbb{E}_{w_i \sim P_n}[\log \sigma(-v'_{w_i}{}^T v_{w_I})]$$

**Cosine Similarity:**
$$\text{sim}(u, v) = \frac{u \cdot v}{||u|| \cdot ||v||}$$

### Reinforcement Learning

**Bellman Equation:**
$$Q^*(s, a) = \mathbb{E}\bigl[r + \gamma \max_{a'} Q^*(s', a') \mid s, a\bigr]$$

**Q-Learning Update (TD):**
$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]$$

**Policy Gradient Theorem:**
$$\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a|s) \cdot A^{\pi_\theta}(s, a) \right]$$

## Materials Checklist

- [ ] Slides: L06_overview.pdf (with key equations frame)
- [ ] Slides: L06_deepdive.pdf (with SGNS pseudocode + Q-learning pseudocode)
- [ ] Notebook: L06_embeddings_rl.ipynb
- [ ] Dataset: text_corpus_synthetic.json
- [ ] All 10 charts compiled (01-09 + 10_negative_sampling)

## Common Misconceptions

- "Embeddings understand language" --- FALSE, they capture statistical co-occurrence patterns
- "Word analogies always work" --- FALSE, success rates are 40-70% (Levy & Goldberg, 2014)
- "FinBERT achieves 92% accuracy" --- MISLEADING, published figure is up to 87% (Araci, 2019)
- "RL always finds optimal solutions" --- FALSE, many challenges in practice (non-stationarity, sparse rewards)
- "DQN works for any problem" --- FALSE, sample efficiency is a major issue
- "Averaging word vectors is a good sentence embedding" --- PARTIALLY, it loses word order ("bank robber" = "robber bank"); use Sentence-BERT for production

## Common Student Questions

**Q: How are embeddings different from TF-IDF?**
A: TF-IDF is sparse and doesn't capture semantics. Embeddings are dense and similar words have similar vectors. TF-IDF treats "good" and "excellent" as completely different; embeddings place them nearby.

**Q: Why the 3/4 power in negative sampling?**
A: It smooths the unigram distribution, giving rare words a higher chance of being sampled as negatives. Without it, very frequent words like "the" would dominate the negative samples.

**Q: What is the difference between static and contextual embeddings?**
A: Static (Word2Vec, GloVe) give one vector per word regardless of context. Contextual (BERT, FinBERT) give different vectors depending on the sentence. "Bank" in "river bank" vs "bank account" gets different contextual vectors but the same static vector.

**Q: Why use discount factor gamma?**
A: Future rewards are uncertain and less valuable than immediate rewards. Gamma in [0,1) ensures the sum converges for continuing tasks. Gamma = 0 means myopic (only immediate reward); gamma near 1 means far-sighted.

**Q: Can RL be used for real trading?**
A: Yes, but with extreme caution: non-stationarity, transaction costs, overfitting to historical data. Most academic RL trading results do not survive realistic backtesting. Active research area (see FinRL by Liu et al., 2021).

**Q: What's the difference between Q-learning and policy gradient?**
A: Q-learning learns a value function and derives policy from it (value-based, off-policy). Policy gradient directly optimizes the policy (on-policy). Q-learning works well for discrete actions; policy gradient handles continuous actions.

**Q: Why is Q-learning called off-policy?**
A: Because the max operator in the update learns the optimal policy regardless of what exploration strategy (e.g., epsilon-greedy) generated the data. The behavior policy (exploration) differs from the target policy (greedy optimal).

## Assessment Connection

This topic is assessed in:
- **Quiz**: Quiz 3 (questions 8-15)
- **Presentations**: Topics 13-15 (BERT, DQN, Multi-Armed Bandits)
- **Capstone**: Can use NLP or RL for project

## Course Wrap-Up Notes

**Final Session Activities**:
- Summarize all 6 topics and their connections
- Review decision framework (when to use what)
- Introduce capstone project requirements
- Answer questions about presentations

**Key Connections to Emphasize**:
- L01-L04: Supervised learning foundations
- L05: Dimensionality reduction (PCA/t-SNE useful for both embedding visualization and RL state spaces)
- L06: Advanced topics (text representations, sequential decision-making)
- Unifying theme: all methods transform raw data into learnable representations

## Post-Session Notes

*Space for instructor notes after delivering the session*

---

*Last updated: 2026-02-07*
