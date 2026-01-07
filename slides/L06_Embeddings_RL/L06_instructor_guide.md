# Instructor Guide: L06 - Embeddings & Reinforcement Learning

## Session Overview

| Aspect | Details |
|--------|---------|
| **Duration** | 3 hours |
| **Topic** | Word Embeddings and Reinforcement Learning |
| **Finance Case** | Sentiment analysis, algorithmic trading |
| **Prerequisites** | L01-L05, basic probability |

## Learning Objectives

By the end of this session, students will be able to:

1. Explain word embeddings and their applications
2. Apply pre-trained embeddings for text analysis
3. Understand the reinforcement learning framework
4. Implement basic Q-learning for decision problems

## PMSP Structure

### Problem Phase (15 min)

**Motivation**: Present two distinct challenges in finance.

**Key Questions to Ask**:
- How do we extract meaning from financial news?
- Why can't we just count words?
- How do trading bots learn to trade without labeled data?

**Discussion Points**:
- Text is unstructured; ML needs numbers
- Embeddings capture semantics (similar meaning = similar vectors)
- Trading is sequential decisions with delayed rewards

### Method Phase (45 min)

**Core Concepts to Cover**:

1. **Word Embeddings**
   - From one-hot to dense vectors
   - Word2Vec: Skip-gram and CBOW
   - Cosine similarity
   - Pre-trained embeddings (GloVe, BERT)

2. **Reinforcement Learning Framework**
   - Agent, environment, state, action, reward
   - Markov Decision Process
   - Value functions and Q-functions
   - Bellman equation

3. **Q-Learning**
   - Update rule
   - Exploration vs exploitation
   - epsilon-greedy strategy

**Common Misconceptions**:
- "Embeddings understand language" - FALSE, they capture statistical patterns
- "RL always finds optimal solutions" - FALSE, many challenges in practice
- "DQN works for any problem" - FALSE, sample efficiency is a major issue

### Solution Phase (45 min)

**Implementation Walkthrough**:

1. **Embeddings Demo**
   - Load pre-trained Word2Vec/GloVe
   - Find similar words
   - Word arithmetic (king - man + woman = queen)
   - Visualize with t-SNE

2. **Q-Learning Demo**
   - Simple grid world
   - Watch Q-values converge
   - Show learned policy

**Live Coding Tips**:
- Use gensim for embeddings (easy API)
- Use gymnasium for RL environments
- Start with frozen lake (simple environment)

### Practice Phase (75 min)

**Hands-on Notebook**:
- Students work through L06_embeddings_rl.ipynb
- Sentiment analysis with embeddings
- Simple trading environment with Q-learning

**Exercise Difficulty Progression**:
1. Load embeddings, find similar words (guided)
2. Build sentence embeddings by averaging (semi-guided)
3. Implement Q-learning for simple trading (open-ended)

## Key Equations

### Embeddings
$$\text{sim}(u, v) = \frac{u \cdot v}{||u|| \cdot ||v||}$$

### Q-Learning
$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]$$

### Bellman Equation
$$Q^*(s, a) = \mathbb{E} \left[ R + \gamma \max_{a'} Q^*(s', a') \right]$$

## Materials Checklist

- [ ] Slides: L06_overview.pdf
- [ ] Slides: L06_deepdive.pdf
- [ ] Notebook: L06_embeddings_rl.ipynb
- [ ] Dataset: text_corpus_synthetic.json
- [ ] All 7 charts compiled

## Timing Guide

| Phase | Duration | Notes |
|-------|----------|-------|
| Problem | 15 min | Two challenges: text and sequential |
| Method | 45 min | Embeddings first, then RL |
| Solution | 45 min | Live coding both |
| **Break** | 15 min | |
| Practice | 60 min | Hands-on exercises |
| Q&A + Wrap | 15 min | Course summary, capstone intro |

## Common Student Questions

**Q: How are embeddings different from TF-IDF?**
A: TF-IDF is sparse and doesn't capture semantics. Embeddings are dense and similar words have similar vectors.

**Q: Why use discount factor gamma?**
A: Future rewards are uncertain and less valuable than immediate rewards. Gamma balances short-term vs long-term.

**Q: Can RL be used for real trading?**
A: Yes, but many challenges: non-stationarity, transaction costs, overfitting to historical data. Active research area.

**Q: What's the difference between Q-learning and policy gradient?**
A: Q-learning learns value function, derives policy. Policy gradient directly optimizes policy. Different tradeoffs.

## Assessment Connection

This topic is assessed in:
- **Quiz**: Quiz 3 (questions 8-15)
- **Presentations**: Topics 13-15 (BERT, DQN, Multi-Armed Bandits)
- **Capstone**: Can use NLP or RL for project

## Course Wrap-Up Notes

**Final Session Activities**:
- Summarize all 6 topics
- Review decision framework (when to use what)
- Introduce capstone project
- Answer questions about presentations

**Key Connections to Emphasize**:
- L01-L04: Supervised learning foundations
- L05: Dimensionality reduction (useful for both embeddings and state spaces)
- L06: Advanced topics (text, sequential decisions)

## Post-Session Notes

*Space for instructor notes after delivering the session*

---

*Last updated: 2026-01-07*
