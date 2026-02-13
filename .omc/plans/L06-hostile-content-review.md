# Hostile Content Review Plan: L06 - Embeddings & Reinforcement Learning

**Plan Type:** Critical Academic Review
**Target:** L06 Embeddings & RL lecture materials
**Review Mode:** HOSTILE - Seeking deficiencies at MSc level
**Reviewer Persona:** External academic examiner with NLP/distributional semantics and sequential decision theory research background

---

## Executive Summary

This plan defines a systematic hostile review of L06 content. L06 is structurally unusual: it covers TWO distinct major topics (word embeddings AND reinforcement learning) in a single session. This creates an inherent tension between breadth and depth that a hostile examiner will exploit aggressively. Key concerns:

1. **Two full MSc topics crammed into one session** -- each could warrant its own 3-hour lecture
2. **Skip-gram softmax formula is computationally intractable as written** -- negative sampling not mentioned
3. **Word analogy arithmetic presented without caveats** -- known to be fragile and misleading
4. **RL formalization appears correct but shallow** -- no derivations, no convergence proofs
5. **Finance applications are bullet-point-level** -- no quantitative depth, no backtesting discussion
6. **100% chart redundancy** between overview and deepdive (all 7 charts appear in both)
7. **All charts use synthetic/fabricated data** -- no real finance data anywhere
8. **Policy gradient formula stated without derivation** -- major MSc-level gap
9. **BERT/FinBERT mentioned but transformer architecture not explained** -- incomplete for MSc
10. **Trading RL formulation mentions challenges but provides no solutions or mitigations**

**Calibration Reference:**
- L01 (Linear Regression): ~66%
- L02 (Logistic Regression): ~55-65%
- L03 (KNN & K-Means): 29%
- L04 (Random Forests): 41%
- L05 (PCA & t-SNE): 37%

**Expected Outcome:** 25-40/100 based on preliminary scan. This is the weakest lecture so far because it attempts to cover two enormous topics superficially rather than one topic well. The breadth-over-depth approach will be punished severely under MSc-level rigor criteria.

---

## Files Under Review

| File | Lines | Est. Slides | Role |
|------|-------|-------------|------|
| `L06_overview.tex` | 219 | ~13 | High-level introduction |
| `L06_deepdive.tex` | 544 | ~25 | Mathematical depth (both topics) |
| `L06_instructor_guide.md` | 166 | N/A | Teaching notes |
| 7 chart folders | varies | N/A | Visualizations |

**Chart Inventory:**
1. `01_word_embedding_space/` - 2D scatter of finance word clusters
2. `02_similarity_heatmap/` - Cosine similarity matrix
3. `03_rl_loop/` - Agent-environment interaction diagram
4. `04_q_learning_grid/` - Q-values in 4x4 grid world
5. `05_reward_curves/` - Learning curves (Q-learning vs DQN vs random)
6. `06_policy_viz/` - Trading policy as RSI/momentum heatmap
7. `07_decision_flowchart/` - When to use embeddings vs RL

---

## SECTION 1: CONTENT ACCURACY (30 points)

### 1.1 Formula Verification (15 points)

**Target Formulas to Audit:**

| # | Formula | Location | Line | Check |
|---|---------|----------|------|-------|
| F1 | Skip-gram softmax | deepdive | 134 | $P(w_{context} \mid w_{target}) = \frac{\exp(v_{context}^T v_{target})}{\sum_{w \in V} \exp(v_w^T v_{target})}$ |
| F2 | Word analogy | deepdive | 156 | $\vec{king} - \vec{man} + \vec{woman} \approx \vec{queen}$ |
| F3 | Cosine similarity | deepdive | 176 | $\text{sim}(u,v) = \frac{u \cdot v}{\|u\| \cdot \|v\|} = \cos(\theta)$ |
| F4 | MDP tuple | deepdive | 246 | $(S, A, P, R, \gamma)$ |
| F5 | Markov property | deepdive | 257 | $P(s_{t+1} \mid s_t, a_t, s_{t-1}, ...) = P(s_{t+1} \mid s_t, a_t)$ |
| F6 | Policy | deepdive | 263 | $\pi(a \mid s) = P(A_t = a \mid S_t = s)$ |
| F7 | Value function | deepdive | 271 | $V^\pi(s) = \mathbb{E}_\pi[\sum_{t=0}^{\infty} \gamma^t R_{t+1} \mid S_0 = s]$ |
| F8 | Q-function | deepdive | 276 | $Q^\pi(s,a) = \mathbb{E}_\pi[\sum_{t=0}^{\infty} \gamma^t R_{t+1} \mid S_0 = s, A_0 = a]$ |
| F9 | Bellman optimality | deepdive | 284 | $Q^*(s,a) = \mathbb{E}[R + \gamma \max_{a'} Q^*(s', a')]$ |
| F10 | Optimal policy | deepdive | 295 | $\pi^*(s) = \arg\max_a Q^*(s,a)$ |
| F11 | Q-learning update | deepdive | 303 | $Q(s,a) \leftarrow Q(s,a) + \alpha[r + \gamma \max_{a'} Q(s',a') - Q(s,a)]$ |
| F12 | Epsilon-greedy | deepdive | 338-341 | Piecewise: $\arg\max$ w.p. $1-\epsilon$, random w.p. $\epsilon$ |
| F13 | DQN approximation | deepdive | 388 | $Q(s,a;\theta) \approx Q^*(s,a)$ |
| F14 | Policy gradient | deepdive | 403 | $\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta}[\nabla_\theta \log \pi_\theta(a \mid s) \cdot Q^{\pi_\theta}(s,a)]$ |

**Issues to Flag:**

- [ ] **F1 (CRITICAL): Skip-gram softmax is computationally intractable.** The denominator $\sum_{w \in V} \exp(v_w^T v_{target})$ sums over the ENTIRE vocabulary (often 100K+ words). This is the central computational problem of Word2Vec. The formula is technically correct but presenting it without mentioning that it is NEVER computed in practice is deeply misleading. Negative sampling (Mikolov et al., 2013b) or hierarchical softmax are REQUIRED for practical training. An MSc student implementing this formula directly would produce intractable code. This is a CRITICAL omission.

- [ ] **F1 (MODERATE): Missing distinction between input and output embedding vectors.** The formula uses $v_{context}$ and $v_{target}$ but does not clarify these are from TWO DIFFERENT embedding matrices (input W and output W'). This is a fundamental architectural detail of Word2Vec that students need to understand.

- [ ] **F2 (MAJOR): Word analogy formula presented without caveats.** The king-man+woman=queen example is the most over-cited result in NLP. Research has shown: (a) it only works for a small subset of analogies, (b) cosine similarity has inherent biases that inflate analogy accuracy (Linzen 2016, Rogers et al. 2017), (c) the 3CosAdd method used here is inferior to 3CosMul, (d) success rates for word analogies are typically 40-70% not near-100% as implied. The finance analogies (stock-equity+debt=bond) are even more dubious -- no evidence these work reliably with standard embeddings.

- [ ] **F3 (MINOR): Cosine similarity equals cos(theta) only for the angle between vectors.** The notation $= \cos(\theta)$ should specify $\theta$ is the angle between $u$ and $v$. Also, the claim "Range: [-1, 1]; 1=identical" is imprecise -- 1 means same direction, not identical (magnitudes can differ).

- [ ] **F4 (MINOR): MDP tuple uses R(s,a,s') but later formulas use R as random variable.** Line 251 defines $R(s,a,s')$ as a function of three arguments, but lines 271-284 use $R_{t+1}$ and $R$ without subscripts inconsistently. Should clarify: $R(s,a,s')$ is the expected reward, $R_{t+1}$ is the random reward received at time $t+1$.

- [ ] **F5 (CORRECT): Markov property correctly stated.** No issues with this formula.

- [ ] **F6-F8 (MINOR): Notation mixing.** Policy uses $A_t, S_t$ (capital = random variable) but Q-function uses $s, a$ (lowercase = specific values) without explaining the distinction. Standard Sutton & Barto notation is being mixed with shorthand.

- [ ] **F7-F8 (MODERATE): Missing discount factor convergence condition.** For $\gamma = 1$ the infinite sum diverges for non-terminating MDPs. Should state $\gamma \in [0,1)$ for infinite-horizon MDPs, or specify episodic tasks. Line 252 says $\gamma \in [0,1]$ including 1, which is only valid for episodic tasks.

- [ ] **F9 (MODERATE): Bellman optimality equation is simplified.** The full Bellman optimality equation is $Q^*(s,a) = \sum_{s'} P(s' \mid s,a)[R(s,a,s') + \gamma \max_{a'} Q^*(s',a')]$. The expectation form shown is correct but hides the dependence on transition probabilities, which is the whole point of model-free vs model-based RL.

- [ ] **F11 (MINOR): Q-learning convergence conditions not stated.** The update rule is correct, but Q-learning converges to $Q^*$ only under specific conditions: (a) all state-action pairs visited infinitely often, (b) learning rate $\alpha_t$ satisfies Robbins-Monro conditions ($\sum \alpha_t = \infty$, $\sum \alpha_t^2 < \infty$). A fixed $\alpha$ as implied does NOT guarantee convergence in the theoretical sense.

- [ ] **F13 (TRIVIAL): DQN formula is just a statement, not a formula.** Writing $Q(s,a;\theta) \approx Q^*(s,a)$ defines the goal but says nothing about the loss function: $L(\theta) = \mathbb{E}[(r + \gamma \max_{a'} Q(s',a';\theta^-) - Q(s,a;\theta))^2]$ with target network $\theta^-$. An MSc student cannot implement DQN from this.

- [ ] **F14 (MAJOR): Policy gradient theorem stated without derivation or conditions.** This is the REINFORCE gradient estimator. Missing: (a) derivation from the policy gradient theorem, (b) high variance problem and need for baselines, (c) the actual form used in practice (advantage $A^{\pi}$ not $Q^{\pi}$). Stating Actor-Critic, PPO, A3C as "algorithms" without explaining their relationship to this formula is name-dropping, not teaching.

**Scoring Rubric:**
| Finding | Deduction |
|---------|-----------|
| Intractable softmax without negative sampling | -4 |
| Word analogy caveats missing | -2 |
| Missing embedding matrix distinction | -1 |
| Notation inconsistencies (MDP/reward) | -1 |
| Discount factor convergence condition | -1 |
| Simplified Bellman (hides transition model) | -1 |
| Policy gradient without derivation/conditions | -2 |
| DQN loss function missing | -1 |
| **Estimated F1 score** | **2-5/15** |

### 1.2 Misleading Statements (10 points)

**Review Targets:**

| # | Statement | Location | Line | Concern |
|---|-----------|----------|------|---------|
| M1 | "Map words to dense vectors (50-300 dimensions)" | deepdive | 122 | Modern embeddings (BERT) use 768+ dims. This range is Word2Vec/GloVe era only. Misleading if students think 300 is state-of-art. |
| M2 | "Similar words -> similar vectors" | deepdive | 123 | Distributional similarity != semantic similarity. "good" and "bad" often have HIGH similarity because they appear in similar contexts (adjective + noun patterns). This is a well-known limitation. |
| M3 | "Learn from context (distributional hypothesis)" | deepdive | 124 | The Firth quote (line 126) is appropriate, but the distributional hypothesis has known limitations: it cannot distinguish antonyms, struggles with rare words, and conflates multiple word senses. |
| M4 | "Skip-gram works well for rare words; CBOW better for frequent words" | deepdive | 143 | This is the Mikolov claim but empirical evidence is mixed. The statement is presented as fact without qualification. |
| M5 | "$\vec{stock} - \vec{equity} + \vec{debt} \approx \vec{bond}$" | deepdive | 161 | Fabricated finance analogy with no empirical verification. Word embeddings trained on general corpora will NOT reliably produce this result. Even domain-specific finance embeddings have not been shown to produce clean financial analogies. This is MISLEADING. |
| M6 | "FinBERT: Pre-trained on financial text" | deepdive | 200 | FinBERT (Araci 2019) is actually BERT fine-tuned on financial text, not trained from scratch. The distinction between pre-training and fine-tuning is fundamental and conflating them is incorrect at MSc level. Also, FinBERT uses contextual embeddings which are architecturally different from Word2Vec-style static embeddings -- this critical distinction is not made. |
| M7 | "Average word vectors (simple baseline)" for sentence embeddings | deepdive | 217 | Presented as "simple baseline" without noting that averaging destroys word order information entirely. "Bank robber" and "robber bank" produce identical embeddings. For an MSc audience this limitation must be stated. |
| M8 | "RL: Learning from interaction, not from labeled examples" | deepdive | 242 | Partially misleading. RL learns from reward signals which ARE labels (scalar feedback). The distinction is delayed/sparse feedback vs per-example labels, which should be stated precisely. |
| M9 | "Q-learning is off-policy: learns optimal Q regardless of policy followed" | deepdive | 317 | Missing critical qualifier: "regardless of policy followed, PROVIDED all state-action pairs are visited sufficiently often." With poor exploration, Q-learning can converge to suboptimal values or not converge at all. |
| M10 | "DQN: breakthrough for RL on Atari games (Mnih et al., 2015)" | deepdive | 397 | True but misleading in a finance context. DQN's Atari success involved: stationary environments, dense rewards, pixel inputs. Financial markets have: non-stationary dynamics, sparse/noisy rewards, structured numerical inputs. The transfer is NOT straightforward and this should be stated. |
| M11 | "Policy gradient: directly optimize policy, can handle continuous actions" | deepdive | 413 | The "can handle continuous actions" part is true but leaves the impression Q-learning cannot. In fact, continuous-action Q-learning methods exist (NAF, CAQL). The real advantage of policy gradient is direct stochastic policy representation. |
| M12 | "Reward improves as agent learns; DQN often outperforms tabular Q-learning" | deepdive | 356 | The claim "often outperforms" is context-dependent. In small state spaces (like the grid world shown), tabular Q-learning converges faster and more reliably. DQN advantages appear only in large/continuous state spaces. |
| M13 | bottomnote overview line 121: "From text to numbers, from decisions to optimal policies" | overview | 121 | "Optimal policies" oversells. RL rarely finds truly optimal policies in practice, especially in finance. |

**Scoring Rubric:**
| Finding | Deduction |
|---------|-----------|
| Fabricated finance analogy (M5) | -2 |
| FinBERT pre-training vs fine-tuning confusion (M6) | -2 |
| Intractable softmax presented as usable (M1.1 overlap) | -1 |
| Missing antonym problem (M2) | -1 |
| Missing word order limitation (M7) | -1 |
| DQN Atari vs finance applicability (M10) | -1 |
| Off-policy claim without exploration qualifier (M9) | -1 |
| **Estimated M score** | **1-4/10** |

### 1.3 Algorithm Correctness (5 points)

**Check Skip-gram Training Algorithm (deepdive 137-142):**
```
Stated:
1. Slide window over text corpus
2. For each word, predict surrounding words
3. Update embeddings via gradient descent
```

**Issues:**
- [ ] CRITICAL: No mention of negative sampling or hierarchical softmax. Step 3 with the full softmax gradient is O(|V|) per update -- completely impractical for vocabularies above a few hundred words.
- [ ] Missing: Window size parameter (hyperparameter not discussed)
- [ ] Missing: Subsampling of frequent words (Mikolov et al., 2013b)
- [ ] Missing: Learning rate schedule
- [ ] Missing: Number of negative samples (typically 5-20)
- [ ] Missing: CBOW architecture (mentioned in bottomnote line 143 but algorithm not shown)

**Check Q-Learning Algorithm (deepdive 307-316):**
```
Stated:
1. Initialize Q(s,a) arbitrarily
2. For each episode:
   - Observe state s
   - Choose action a (epsilon-greedy)
   - Execute a, observe r, s'
   - Update Q(s,a)
```

**Issues:**
- [ ] Line 308: "Initialize Q(s,a) arbitrarily" -- should note optimistic initialization is a common technique, and terminal states should have Q=0.
- [ ] Missing: Terminal state handling (Q(terminal, a) = 0)
- [ ] Missing: Episode termination condition
- [ ] Missing: Learning rate alpha not mentioned in algorithm (only in formula)
- [ ] Missing: Epsilon decay schedule (mentioned later in line 344-348 but not in algorithm)
- [ ] The algorithm as stated is incomplete -- it does not specify what happens after the update (loop back to observe s' as new s)

**DQN Algorithm (deepdive 391-396):**
```
Stated as "Key Innovations":
- Experience Replay: Store transitions, sample randomly
- Target Network: Separate network for stability
- Function Approximation: Handle large state spaces
```

**Issues:**
- [ ] No actual algorithm pseudocode
- [ ] Experience replay: does not explain WHY random sampling (breaks temporal correlation for i.i.d. training batches)
- [ ] Target network: does not explain update frequency or soft vs hard update
- [ ] "Function Approximation" is not an innovation -- it's the core idea. The innovation is using neural networks specifically with the replay buffer and target network to stabilize training.
- [ ] Missing: Gradient clipping (used in original DQN)
- [ ] Missing: Replay buffer size considerations

**Policy Gradient (deepdive 406-411):**
```
Stated as "Algorithms":
- REINFORCE (vanilla policy gradient)
- Actor-Critic (combine value and policy)
- PPO (Proximal Policy Optimization)
- A3C (Asynchronous Advantage Actor-Critic)
```

**Issues:**
- [ ] REINFORCE not described beyond the name
- [ ] Actor-Critic architecture not explained (what is the critic?)
- [ ] PPO not explained (what is the clipping? what is proximal?)
- [ ] A3C not explained (what is asynchronous? what is advantage?)
- [ ] This is pure name-dropping with no pedagogical content
- [ ] Missing: TRPO (historically important bridge between PG and PPO)

**Scoring Rubric:**
| Finding | Deduction |
|---------|-----------|
| Skip-gram missing negative sampling in algorithm | -2 |
| Q-learning incomplete algorithm | -1 |
| DQN listed innovations, no algorithm | -1 |
| Policy gradient name-dropping without content | -1 |
| **Estimated A score** | **0-2/5** |

---

## SECTION 2: LEARNING OBJECTIVES ALIGNMENT (20 points)

### 2.1 Stated Objectives (overview lines 113-118, deepdive inherits same)

| # | Objective | Bloom's Level | Coverage | Assessment |
|---|-----------|---------------|----------|------------|
| 1 | "Explain word embeddings and their applications" | Understand (L2) | PARTIAL | Can explain what they are; cannot explain how they work (no training details) |
| 2 | "Apply pre-trained embeddings for text analysis" | Apply (L3) | WEAK | Library names listed (gensim, transformers) but no code walkthrough, no worked example |
| 3 | "Understand the reinforcement learning framework" | Understand (L2) | ADEQUATE | MDP, policy, value functions covered at formula level |
| 4 | "Implement basic Q-learning for decision problems" | Apply (L3) | WEAK | Algorithm shown but incomplete, no pseudocode for implementation, no worked example |

### 2.2 Objective Gaps Analysis

**SYSTEMIC PROBLEM: All objectives at Bloom's Level 2-3 (Understand/Apply)**

For an MSc program, at least 2 objectives should be at Level 4-5 (Analyze/Evaluate). There are ZERO higher-order thinking objectives. Compare:
- Good MSc objective: "Evaluate when word embeddings vs bag-of-words features are appropriate for financial text classification, considering dataset size, domain specificity, and computational constraints"
- Good MSc objective: "Analyze the convergence properties of Q-learning and explain when function approximation is necessary"
- Good MSc objective: "Critically assess the suitability of RL for algorithmic trading, identifying assumptions that may be violated in real markets"

None of these are present.

**Objective 1: "Explain word embeddings and their applications"**
- Coverage: One-hot problem stated, dense vector solution stated, Skip-gram formula shown
- **Gap:** Cannot actually explain HOW embeddings learn -- negative sampling omitted, CBOW not formalized
- **Gap:** Applications listed as bullets (sentiment, NER, document similarity) but none demonstrated
- **Gap:** No discussion of static vs contextual embeddings (Word2Vec vs BERT) -- fundamental distinction for modern NLP
- **Gap:** The word "explain" at MSc level should require understanding of the loss function and optimization -- currently only the intractable softmax is shown
- **Bloom's achieved:** Remember (L1) -- students can recall what embeddings are, but cannot explain the mechanism

**Objective 2: "Apply pre-trained embeddings for text analysis"**
- Coverage: Library names (gensim, transformers) on line 467-469, practical tips on line 484-488
- **Gap:** No actual code example -- not even pseudocode
- **Gap:** No worked example of loading embeddings and computing similarity
- **Gap:** No discussion of fine-tuning strategy (when to fine-tune, how many epochs, what learning rate)
- **Gap:** No data preprocessing pipeline (tokenization, vocabulary handling, OOV strategy)
- **Gap:** The Colab link is TBD (line 426) -- the practice portion is non-functional
- **Bloom's achieved:** Remember (L1) -- students know library names, cannot apply anything

**Objective 3: "Understand the reinforcement learning framework"**
- Coverage: Agent/environment/state/action/reward defined, MDP formalized, value functions stated, Bellman equation shown
- **Gap:** No worked example (a specific MDP with numbers)
- **Gap:** Markov property stated but no discussion of when it fails (partially observable environments)
- **Gap:** Discount factor gamma: its effect on policy behavior not explained (myopic vs far-sighted agents)
- **Gap:** Reward shaping mentioned (line 494) but not formalized -- a critical practical topic
- **Bloom's achieved:** Understand (L2) -- students can state the framework components

**Objective 4: "Implement basic Q-learning for decision problems"**
- Coverage: Update rule formula, algorithm sketch, epsilon-greedy strategy
- **Gap:** Algorithm is incomplete (no terminal state handling, no learning rate specification, no loop structure)
- **Gap:** No worked numerical example (e.g., "given Q(s1,up)=3.2, alpha=0.1, r=1, gamma=0.9, Q(s2,up)=4.0, the new Q(s1,up) = ...")
- **Gap:** No pseudocode suitable for implementation
- **Gap:** Grid world chart shows Q-values but never explains how they were computed
- **Gap:** Again, Colab link is TBD
- **Bloom's achieved:** Remember/Understand (L1-L2) -- students can write the formula but cannot implement from what's given

**Scoring Rubric:**
| Finding | Deduction |
|---------|-----------|
| All objectives at Bloom's L2-L3 (no higher-order) | -4 |
| Objective 1 partially met (explain mechanism missing) | -3 |
| Objective 2 weakly met (no code, no worked example) | -5 |
| Objective 3 adequately met | -1 |
| Objective 4 weakly met (incomplete algorithm, no worked example) | -4 |
| **Estimated LO score** | **3-8/20** |

---

## SECTION 3: MSc LEVEL APPROPRIATENESS (20 points)

### 3.1 Theoretical Depth Gaps (10 points)

**STRUCTURAL PROBLEM: Covering two full MSc topics in one session guarantees insufficient depth in both.**

A hostile examiner would note: Word Embeddings and Reinforcement Learning are each covered as full courses at major universities (Stanford CS224N for NLP, CS234 for RL). Attempting both in 3 hours means neither can reach MSc depth.

**Critical Missing Theory -- Embeddings:**

| Topic | Expected at MSc | Present? | Location |
|-------|-----------------|----------|----------|
| Negative sampling derivation | CRITICAL | NO | Not mentioned at all |
| CBOW formalization | HIGH | NO | Name only (line 143) |
| Skip-gram loss function (proper form) | CRITICAL | NO | Only intractable softmax shown |
| Embedding dimension selection | HIGH | NO | "50-300" stated as fact |
| GloVe objective function (global co-occurrence) | HIGH | NO | Name only (line 194) |
| Static vs contextual embeddings distinction | CRITICAL | NO | Word2Vec and BERT listed together as if equivalent |
| Transformer/attention mechanism (for BERT context) | HIGH | NO | BERT mentioned, architecture not explained |
| Subword tokenization (BPE, WordPiece) | HIGH | NO | FastText "handles subwords" but mechanism not explained |
| Evaluation metrics for embeddings (intrinsic/extrinsic) | HIGH | NO | No evaluation methodology |
| Bias in word embeddings (gender, racial) | MEDIUM | NO | Major ethical concern, entirely missing |
| Word sense disambiguation | MEDIUM | NO | Polysemy problem not discussed |

**Critical Missing Theory -- Reinforcement Learning:**

| Topic | Expected at MSc | Present? | Location |
|-------|-----------------|----------|----------|
| Temporal difference (TD) learning | CRITICAL | NO | Foundation of Q-learning, not formalized |
| TD(0), TD(lambda) | HIGH | NO | Not mentioned |
| SARSA (on-policy Q-learning) | HIGH | NO | Not mentioned |
| Model-based vs model-free RL distinction | HIGH | NO | Not formalized |
| Dynamic programming (policy iteration, value iteration) | HIGH | NO | Mentioned only as "enables dynamic programming" (line 291) |
| Convergence proof for Q-learning (sketch) | HIGH | NO | No convergence discussion |
| Function approximation theory (deadly triad) | HIGH | NO | DQN uses it but instability not discussed |
| Multi-armed bandits | HIGH | NO | Simpler RL problem, good pedagogical bridge |
| Credit assignment problem | HIGH | NO | Mentioned in comparison table (line 452) but never formalized |
| Reward shaping formalization | MEDIUM | NO | "Crucial" (line 494) but not formalized |
| Partially observable MDPs (POMDPs) | MEDIUM | NO | Financial markets are partially observable -- this matters |
| Regret bounds | MEDIUM | NO | No sample complexity discussion |
| Exploration theory (UCB, Thompson sampling) | MEDIUM | NO | Only epsilon-greedy shown |

### 3.2 Statistical Inference and Rigor (5 points)

**CRITICAL GAP: Zero statistical inference content**

MSc-level should include:
- [ ] Confidence intervals for embedding similarity scores
- [ ] Statistical significance of word analogy results
- [ ] Hypothesis testing: "Is this embedding similarity score meaningful?"
- [ ] Variance of Q-value estimates
- [ ] Confidence bounds for learned policies (offline evaluation)
- [ ] Bootstrap or cross-validation for embedding evaluation
- [ ] Importance sampling for off-policy evaluation
- [ ] No discussion of sample complexity in either embeddings or RL

**Current Coverage:** NONE. Zero inference, zero uncertainty quantification.

### 3.3 Advanced Topics (5 points)

**Missing Advanced Material:**

| Topic | Importance for MSc | Present? |
|-------|-------------------|----------|
| Negative sampling theory | Critical | NO |
| GloVe mathematical framework | High | NO |
| Attention mechanism (for BERT) | High | NO |
| Transfer learning for NLP | High | Mentioned (FinBERT) but not explained |
| TD learning fundamentals | Critical | NO |
| SARSA / on-policy methods | High | NO |
| Multi-armed bandits | High | NO |
| Model-based RL | Medium | NO |
| Inverse RL | Medium | NO |
| Safe RL | Medium | NO |
| Offline/batch RL | High (for finance) | NO |
| Embedding bias and fairness | Medium | NO |
| Sentence transformers architecture | Medium | NO |
| Double DQN, Dueling DQN | Medium | NO |

**Scoring Rubric:**
| Finding | Deduction |
|---------|-----------|
| Missing negative sampling (critical for embeddings) | -3 |
| Missing TD learning (critical for RL) | -3 |
| Missing static vs contextual distinction | -2 |
| Missing SARSA/on-policy methods | -1 |
| Zero statistical inference | -5 |
| Missing advanced topics (6+ items) | -3 |
| **Estimated MSc score** | **0-5/20** |

---

## SECTION 4: FINANCE USE CASES (15 points)

### 4.1 Embeddings in Finance (7 points)

**Current Coverage (deepdive lines 207-221):**
```
Applications (bullet list):
- Sentiment Analysis: News -> embedding -> positive/negative
- Document Similarity: Find similar SEC filings
- Named Entity Recognition: Extract company names
- Event Detection: Identify earnings announcements

Sentence Embeddings:
- Average word vectors (simple baseline)
- Doc2Vec (paragraph vectors)
- Sentence-BERT (state-of-the-art)
```

**MSc Finance Expectations -- MISSING:**

| Topic | Expected | Present? | Severity |
|-------|----------|----------|----------|
| Quantitative sentiment analysis example | CRITICAL | NO | CRITICAL |
| Actual SEC filing similarity computation | HIGH | NO | HIGH |
| Comparison: embeddings vs TF-IDF for finance | HIGH | NO (instructor guide mentions it, slides don't) | HIGH |
| Financial NER challenges (ticker symbols, abbreviations) | MEDIUM | NO | MEDIUM |
| Earnings call transcript analysis | HIGH | NO | HIGH |
| Domain adaptation: general -> finance embeddings | HIGH | Mentioned (FinBERT) but not explained | HIGH |
| Word embedding bias in financial context | MEDIUM | NO | MEDIUM |
| Numerical data + text multimodal approaches | MEDIUM | NO | MEDIUM |
| Backtesting NLP trading signals | HIGH | NO | HIGH |
| Real-world example with actual data | CRITICAL | NO | CRITICAL |

**Critical Issue: All finance applications are one-line bullet points.**

Not a single application is demonstrated with data, code, or quantitative results. "Sentiment Analysis: News -> embedding -> positive/negative" is a 10-word description of what could be a 30-minute lecture segment. An MSc student cannot learn to DO sentiment analysis from this slide.

### 4.2 RL in Finance (8 points)

**Current Coverage (deepdive lines 361-382):**
```
Formulation:
- State: Price history, portfolio, technical indicators
- Action: Buy, sell, hold (+ position size)
- Reward: Profit/loss, risk-adjusted return

Challenges:
- Non-stationary environment
- High noise, low signal-to-noise ratio
- Transaction costs
- Partial observability
```

**MSc Finance Expectations -- MISSING:**

| Topic | Expected | Present? | Severity |
|-------|----------|----------|----------|
| Specific reward function formulation | CRITICAL | NO | CRITICAL |
| Transaction cost modeling in reward | CRITICAL | Mentioned as challenge but no formula | CRITICAL |
| State representation design (what features, how many) | HIGH | Generic list only | HIGH |
| Sharpe ratio as reward (advantages/disadvantages) | HIGH | NO | HIGH |
| Backtesting methodology for RL trading | CRITICAL | NO | CRITICAL |
| Overfitting to historical data (lookahead bias) | CRITICAL | NO | CRITICAL |
| Market impact of RL-based trading | HIGH | NO | HIGH |
| Regulatory considerations | MEDIUM | NO | MEDIUM |
| Comparison to traditional quant strategies | HIGH | NO | HIGH |
| Real performance numbers from literature | HIGH | NO | HIGH |
| Risk management within RL framework | HIGH | NO | HIGH |
| Multi-asset portfolio RL | MEDIUM | NO | MEDIUM |
| FinRL framework details | MEDIUM | Name only (line 496) | MEDIUM |

**Critical Issues:**

1. **No reward function formulation.** The slides say "Reward: Profit/loss, risk-adjusted return" but never write $r_t = \text{portfolio\_return}_t - c \cdot |\Delta\text{position}_t|$ or similar. Without a concrete reward function, students cannot implement RL for trading.

2. **Transaction costs acknowledged but not modeled.** Transaction costs are THE make-or-break factor in RL trading. Acknowledging they exist without showing how to incorporate them in the reward function is insufficient.

3. **No backtesting discussion.** RL for trading is extremely prone to overfitting. Walk-forward validation, out-of-sample testing, and the distinction between in-sample and out-of-sample performance are critical. None mentioned.

4. **No comparison to benchmarks.** Does RL actually outperform buy-and-hold? Moving-average crossover? The literature shows RL strategies often fail to beat simple benchmarks after transaction costs. This honest assessment is missing.

5. **Policy visualization chart (06_policy_viz) is a hardcoded rule, not a learned policy.** The chart.py file (line 40-47) implements a DETERMINISTIC rule: buy if RSI<30 or momentum>2, sell if RSI>70 or momentum<-2. This is a simple technical trading rule, NOT a learned RL policy. Presenting it as "Learned Trading Policy" is misleading. A real learned policy would be a neural network's output, not an if-else rule.

**Scoring Rubric:**
| Finding | Deduction |
|---------|-----------|
| No quantitative sentiment analysis example | -3 |
| No concrete reward function for trading | -3 |
| No backtesting methodology | -2 |
| Policy viz is hardcoded rule, not learned | -2 |
| No transaction cost formulation | -2 |
| All finance content is bullet-point depth | -2 |
| No real data anywhere | -1 |
| **Estimated Finance score** | **0-4/15** |

---

## SECTION 5: PEDAGOGICAL FLOW (10 points)

### 5.1 PMSP Compliance Check (3 points)

**Overview Structure:**
- [x] Learning Objectives (lines 111-122)
- [x] Problem: Business Problem (lines 124-138)
- [x] Method: 2 chart-only slides (lines 140-167)
- [x] Solution: 2 chart-only slides (lines 170-184)
- [x] Practice: Hands-on (lines 188-197)
- [x] Decision Framework (lines 201-206)
- [x] References (lines 210-217)

**Issue with Overview:** The Method and Solution sections are chart-only slides with no explanatory text. The overview relies entirely on bottom notes for explanation. For a first-pass introduction, students see charts without context. Compare L05 overview which had text slides introducing concepts before charts.

**Deepdive Structure:**
- [x] Part 1: Embeddings Introduction (lines 112-127)
- [x] Method: Skip-gram, embedding space, analogies, similarity, pre-trained, finance apps (lines 131-222)
- [x] Part 2: RL Framework (lines 227-317) -- Solution section
- [x] Q-values viz, exploration/exploitation, learning curves (lines 320-357)
- [x] Part 3: RL for Trading (lines 360-398) -- Finance application
- [x] DQN, Policy Gradient (lines 385-414)
- [x] Practice (lines 418-427)
- [x] Part 4: Comparison (lines 432-458)
- [x] Part 5: Implementation, tips, summary, references (lines 463-543)

**Issue:** The PMSP flow is distorted because TWO topics are interleaved. The "Problem" section covers embeddings, then "Method" covers embeddings, then suddenly "Solution" starts RL. There is no clear "Problem" framing for RL (it appears mid-lecture in the "Solution" section). This violates the PMSP principle that each topic should have its own Problem -> Method -> Solution arc.

### 5.2 Overview/Deepdive Redundancy (4 points)

**Chart Usage Analysis:**

| Chart | Overview? | Deepdive? | Redundancy? |
|-------|-----------|-----------|-------------|
| 01_word_embedding_space | Line 144 | Line 148 | YES - DUPLICATED |
| 02_similarity_heatmap | Line 152 | Line 184 | YES - DUPLICATED |
| 03_rl_loop | Line 158 | Line 239 | YES - DUPLICATED |
| 04_q_learning_grid | Line 165 | Line 323 | YES - DUPLICATED |
| 05_reward_curves | Line 174 | Line 354 | YES - DUPLICATED |
| 06_policy_viz | Line 181 | Line 380 | YES - DUPLICATED |
| 07_decision_flowchart | Line 203 | Line 435 | YES - DUPLICATED |

**Redundancy Summary:**
- **ALL 7 charts appear in BOTH overview and deepdive (100% duplication)**
- Deepdive has ZERO unique charts
- This is the WORST redundancy in the course (tied with pre-improvement L04)
- Overview is essentially a chart slideshow (4 of 7 content slides are chart-only)
- The deepdive adds text context around the same charts but no new visualizations

**What's Missing:**
- Deepdive should have unique charts: Skip-gram architecture diagram, negative sampling illustration, Word2Vec training process, Q-learning step-by-step walkthrough, DQN architecture, experience replay illustration, actual RL training convergence from real experiment
- The overview should use a SUBSET of charts, not all 7

### 5.3 TBD Placeholders (2 points)

**Found:**
- Line 196 (overview): `[TBD]` for Colab notebook link
- Line 426 (deepdive): `[TBD]` for Colab notebook link

**2 TBD placeholders -- same issue as L03, L04, L05**

### 5.4 Time Budget Verification (1 point)

**Instructor Guide Timing (Lines 116-123):**
| Phase | Duration | Notes |
|-------|----------|-------|
| Problem | 15 min | Two challenges: text and sequential |
| Method | 45 min | Embeddings first, then RL |
| Solution | 45 min | Live coding both |
| Break | 15 min | |
| Practice | 60 min | Hands-on exercises |
| Q&A + Wrap | 15 min | Course summary, capstone intro |
| **Total** | **195 min** | **3h 15min -- EXCEEDS 3h by 15min** |

**Additional timing concerns:**
- 45 minutes for Method to cover both embeddings AND RL is insufficient. Skip-gram alone requires 20+ minutes if explained properly.
- 45 minutes for Solution (live coding BOTH embedding exploration AND Q-learning implementation) is extremely ambitious.
- 60 minutes for Practice covering 3 exercises (embeddings, Q-learning, trading RL) is tight.
- The session also includes "Course summary" and "capstone intro" in the Q&A slot -- further time pressure.

**Scoring Rubric:**
| Finding | Deduction |
|---------|-----------|
| 100% chart redundancy (worst in course) | -3 |
| PMSP violated (no Problem framing for RL) | -2 |
| TBD placeholders (x2) | -1 |
| Time budget exceeded by 15 min | -1 |
| Overview is chart slideshow (no explanatory slides) | -1 |
| **Estimated Pedagogy score** | **2-4/10** |

---

## SECTION 6: COMPLETENESS (5 points)

### 6.1 Essential Topics Checklist -- Embeddings

| Topic | Required | Present? | Lines |
|-------|----------|----------|-------|
| One-hot encoding problem | YES | YES | deepdive 114-117 |
| Distributional hypothesis | YES | YES | deepdive 124, 126 |
| Word2Vec / Skip-gram | YES | PARTIAL (formula but not training) | deepdive 131-143 |
| CBOW | YES | NAME ONLY | deepdive 143 bottomnote |
| Negative sampling | CRITICAL | **NO** | Not mentioned |
| GloVe | YES | NAME ONLY | deepdive 194 |
| FastText / subword | YES | NAME ONLY | deepdive 195 |
| Cosine similarity | YES | YES | deepdive 173-187 |
| Word analogies | YES | YES (but uncaveated) | deepdive 153-170 |
| Pre-trained embeddings | YES | YES | deepdive 190-203 |
| Static vs contextual | CRITICAL | **NO** | Word2Vec and BERT conflated |
| BERT / transformers | HIGH | NAME ONLY | deepdive 200, 469 |
| Evaluation methodology | YES | **NO** | No intrinsic/extrinsic evaluation |
| Embedding bias | MEDIUM | **NO** | Not mentioned |

### 6.2 Essential Topics Checklist -- Reinforcement Learning

| Topic | Required | Present? | Lines |
|-------|----------|----------|-------|
| Agent-environment loop | YES | YES | deepdive 228-242 |
| MDP formalization | YES | YES | deepdive 245-259 |
| Policy definition | YES | YES | deepdive 262-267 |
| Value function | YES | YES | deepdive 269-272 |
| Q-function | YES | YES | deepdive 274-278 |
| Bellman equation | YES | YES | deepdive 281-297 |
| Q-learning algorithm | YES | PARTIAL (incomplete) | deepdive 300-317 |
| Epsilon-greedy | YES | YES | deepdive 329-349 |
| DQN | YES | SHALLOW | deepdive 385-397 |
| Policy gradient | YES | FORMULA ONLY | deepdive 400-413 |
| TD learning | CRITICAL | **NO** | Not mentioned |
| SARSA | HIGH | **NO** | Not mentioned |
| Multi-armed bandits | HIGH | **NO** | Not mentioned |
| Model-based RL | HIGH | **NO** | Not mentioned |
| Convergence theory | HIGH | **NO** | Not discussed |
| Exploration beyond epsilon-greedy | HIGH | **NO** | UCB, Thompson not mentioned |

### 6.3 Charts Completeness

All 7 charts present but assessment:

| Chart | Template Compliance | Pedagogical Value | Finance Relevance |
|-------|-------------------|-------------------|-------------------|
| 01_word_embedding_space | figsize OK (10,6). Synthetic data. | GOOD: Shows clustering concept | MODERATE: Uses finance words |
| 02_similarity_heatmap | **figsize (10,8) -- SPEC VIOLATION** | GOOD: Shows cosine similarity | MODERATE: Finance words |
| 03_rl_loop | figsize OK (10,6). Diagram. | GOOD: Classic RL diagram | GOOD: Uses market terminology |
| 04_q_learning_grid | figsize OK (10,6). Grid world. | MODERATE: Generic grid, not finance | POOR: No finance connection |
| 05_reward_curves | figsize OK (10,6). Synthetic. | MODERATE: Shows learning concept | POOR: Generic rewards, not returns |
| 06_policy_viz | figsize OK (10,6). **HARDCODED RULE**. | **MISLEADING**: Not a learned policy | **MISLEADING**: Simple RSI/momentum rule |
| 07_decision_flowchart | figsize OK (10,6). Diagram. | GOOD: Decision support | MODERATE: General ML framing |

**Chart Gaps -- Missing Visualizations:**
- [ ] Skip-gram architecture diagram (how the network looks)
- [ ] Negative sampling illustration
- [ ] Word embedding training loss curve
- [ ] ACTUAL learned RL policy (from a real training run)
- [ ] DQN architecture diagram
- [ ] Experience replay buffer illustration
- [ ] Real financial text similarity example
- [ ] Backtesting results chart (RL vs benchmark)
- [ ] t-SNE visualization of actual financial embeddings (cross-reference with L05!)

### 6.4 Chart Quality Bonus Assessment (+5)

| Criterion | Score | Justification |
|-----------|-------|---------------|
| Template compliance | 3/5 | One spec violation (similarity heatmap figsize) |
| Pedagogical value | 2/5 | 06_policy_viz is actively misleading |
| Finance relevance | 1/5 | Synthetic data throughout, no real finance visualization |
| Technical accuracy | 2/5 | Q-learning grid is a toy, reward curves are simulated |
| Visual clarity | 4/5 | Charts are clean and readable |
| **Average** | 2.4/5 | |

**Estimated Chart Bonus: +1 to +2 out of +5**

**Scoring Rubric for Completeness:**
| Finding | Deduction |
|---------|-----------|
| Missing negative sampling (critical for embeddings) | -2 |
| Missing TD learning (critical for RL) | -1 |
| Missing static vs contextual distinction | -1 |
| Missing evaluation methodology for embeddings | -0.5 |
| Missing SARSA, bandits, model-based | -0.5 |
| **Estimated Completeness score** | **0-2/5** |

---

## SCORING MATRIX

| Section | Max | Expected Issues | Est. Score |
|---------|-----|-----------------|------------|
| Formula Verification | 15 | Intractable softmax, missing negative sampling, policy gradient unexplained, word analogy uncaveated | 2-5 |
| Misleading Statements | 10 | Fabricated finance analogies, FinBERT confusion, off-policy claim, policy viz is hardcoded | 1-4 |
| Algorithm Correctness | 5 | Skip-gram incomplete, Q-learning incomplete, DQN no algorithm, PG name-dropping | 0-2 |
| Learning Objectives | 20 | All L2-L3, no higher-order, Obj 2 & 4 weakly met, no worked examples | 3-8 |
| MSc Level | 20 | Two topics means neither has depth, zero inference, missing critical theory for both | 0-5 |
| Finance Use Cases | 15 | Bullet-point depth only, no quantitative examples, hardcoded policy chart, no backtesting | 0-4 |
| Pedagogical Flow | 10 | 100% chart redundancy, PMSP violated for RL, TBDs, time exceeded | 2-4 |
| Completeness | 5 | Major topics missing in both halves, no evaluation methodology | 0-2 |
| Chart Quality Bonus | +5 | One spec violation, policy viz misleading, all synthetic | +1-2 |
| **TOTAL** | **100** | | **9-36** |

**Estimated Final Score: 20-35/100**

This would make L06 the LOWEST-scoring lecture in the course, consistent with the structural problem of attempting two full MSc topics in one session without sufficient depth in either.

---

## REVIEW EXECUTION CHECKLIST

### Phase 1: Formula & Claims Verification (Parallel Task 1)
Agent: `architect` or `analyst`
- [ ] Verify all 14 mathematical formulas for correctness
- [ ] Specifically check: Skip-gram softmax -- is the partition function acknowledged as intractable?
- [ ] Verify word analogy: is it presented with appropriate caveats?
- [ ] Check cosine similarity notation
- [ ] Verify MDP notation consistency (R function vs R random variable)
- [ ] Check discount factor range ($\gamma \in [0,1]$ vs $[0,1)$)
- [ ] Verify Bellman equation completeness (explicit transition probabilities?)
- [ ] Check Q-learning update: is alpha specified?
- [ ] Verify policy gradient formula (REINFORCE vs advantage form)
- [ ] Flag all 13+ misleading statements with line references
- [ ] Verify FinBERT description (pre-trained vs fine-tuned)

**Key Lines to Examine:**
- deepdive 131-143 (Skip-gram)
- deepdive 153-170 (analogies)
- deepdive 173-187 (cosine similarity)
- deepdive 245-297 (MDP/Bellman)
- deepdive 300-317 (Q-learning algorithm)
- deepdive 385-413 (DQN/Policy gradient)

### Phase 2: Learning Objectives & MSc-Level Analysis (Parallel Task 2)
Agent: `architect` or `analyst`
- [ ] Map each of 4 objectives to specific content in both .tex files
- [ ] Verify Bloom's level achieved (claim: all at L2-L3, none at L4+)
- [ ] Identify all missing derivations
- [ ] Check for: negative sampling, TD learning, SARSA, static vs contextual embeddings
- [ ] Assess statistical inference content (claim: zero)
- [ ] Compare embeddings coverage to Jurafsky & Martin Ch6 (Speech & Language Processing)
- [ ] Compare RL coverage to Sutton & Barto Ch1-6 (RL: An Introduction)
- [ ] Assess whether the "two topics in one session" structure fundamentally undermines MSc depth

**Key Sections:**
- overview 111-118 (stated objectives)
- deepdive Part 1 (embeddings theory)
- deepdive Part 2 (RL theory)
- deepdive Part 5 (implementation)

### Phase 3: Finance Applications & Structure Review (Parallel Task 3)
Agent: `analyst`
- [ ] Evaluate sentiment analysis application depth
- [ ] Evaluate RL trading formulation depth
- [ ] Check: is there a concrete reward function anywhere?
- [ ] Check: transaction costs -- mentioned or formalized?
- [ ] Check: backtesting methodology -- present or absent?
- [ ] Verify the policy visualization chart (06_policy_viz) -- is it actually learned or hardcoded?
- [ ] Evaluate finance analogies (stock-equity+debt=bond) -- do these work with real embeddings?
- [ ] Check PMSP compliance for both topic arcs
- [ ] Count chart redundancies (expect 100%)
- [ ] Find all TBD placeholders
- [ ] Verify time budget
- [ ] Check overview for chart-only slides without explanatory text

**Key Sections:**
- deepdive 207-221 (embeddings in finance)
- deepdive 360-382 (RL for trading)
- overview structure (chart-only slides)
- instructor guide timing

### Phase 4: Chart Quality Audit (Parallel Task 4)
Agent: `explore` + `vision`
- [ ] Read all 7 chart.py files
- [ ] Verify figsize=(10, 6) compliance (flag similarity_heatmap at 10,8)
- [ ] Check font sizes against CLAUDE.md specification
- [ ] Verify color palette usage
- [ ] Check single figure per chart (no subplots)
- [ ] **CRITICAL: Verify 06_policy_viz is hardcoded rule, not learned policy**
- [ ] Check 05_reward_curves: are curves simulated or from actual training?
- [ ] Check 04_q_learning_grid: are Q-values from actual Q-learning or hardcoded?
- [ ] Assess pedagogical value of each chart
- [ ] Identify missing visualizations (Skip-gram diagram, DQN architecture, etc.)

**Chart Files:**
```
slides/L06_Embeddings_RL/01_word_embedding_space/chart.py
slides/L06_Embeddings_RL/02_similarity_heatmap/chart.py
slides/L06_Embeddings_RL/03_rl_loop/chart.py
slides/L06_Embeddings_RL/04_q_learning_grid/chart.py
slides/L06_Embeddings_RL/05_reward_curves/chart.py
slides/L06_Embeddings_RL/06_policy_viz/chart.py
slides/L06_Embeddings_RL/07_decision_flowchart/chart.py
```

### Phase 5: Gap Analysis & Scoring (Sequential, after 1-4)
Agent: `architect`
- [ ] Compile findings from all phases
- [ ] Calculate section-by-section scores
- [ ] Prioritize gaps by severity (CRITICAL > HIGH > MEDIUM > LOW)
- [ ] Generate improvement recommendations
- [ ] Produce final score with justification
- [ ] Compare score to L01-L05 calibration range
- [ ] Assess: is splitting L06 into two sessions recommended?

---

## EXPECTED MAJOR FINDINGS

Based on deep content analysis, the review should identify:

1. **CRITICAL: Skip-gram softmax is intractable as presented**
   - Location: deepdive line 134
   - Impact: Students implementing this formula produce O(|V|) per update
   - Fix: Add negative sampling formula and explain why it's needed

2. **CRITICAL: Two full MSc topics in one session = neither at MSc depth**
   - Location: Structural
   - Impact: Entire lecture fails MSc-level rigor criteria
   - Fix: Consider splitting into L06a (Embeddings) and L06b (RL), or drastically reduce scope

3. **CRITICAL: No quantitative finance example in either topic**
   - Location: deepdive 207-221 (embeddings), 360-382 (RL)
   - Impact: Finance objectives unmet
   - Fix: Add worked sentiment analysis example; add concrete reward function with transaction costs

4. **CRITICAL: Policy visualization chart is a hardcoded trading rule, not a learned policy**
   - Location: 06_policy_viz/chart.py lines 40-47
   - Impact: Misrepresents RL output
   - Fix: Replace with output from actual Q-learning training run

5. **MAJOR: Missing negative sampling -- the key innovation of Word2Vec**
   - Location: Absent from entire lecture
   - Impact: Cannot explain how Word2Vec actually trains
   - Fix: Add 1-2 slides on negative sampling with formula

6. **MAJOR: Missing TD learning -- foundation of Q-learning**
   - Location: Absent from entire lecture
   - Impact: Q-learning presented without theoretical foundation
   - Fix: Add TD(0) update rule and explain connection to Q-learning

7. **MAJOR: 100% chart redundancy between overview and deepdive**
   - Location: All 7 charts duplicated
   - Impact: Worst redundancy in course
   - Fix: Overview uses 3-4 key charts; deepdive has 8-10 unique charts

8. **MAJOR: Policy gradient is pure name-dropping**
   - Location: deepdive 400-413
   - Impact: REINFORCE, Actor-Critic, PPO, A3C listed without explanation
   - Fix: Either explain Actor-Critic properly or remove the list

9. **MAJOR: Static vs contextual embeddings not distinguished**
   - Location: Word2Vec and BERT listed as equivalent on deepdive 190-203
   - Impact: Fundamental conceptual confusion for students
   - Fix: Add explicit comparison slide

10. **MAJOR: Word analogies presented without known limitations**
    - Location: deepdive 153-170
    - Impact: Students believe analogies work reliably -- they don't
    - Fix: Add caveats about success rates, bias, evaluation methodology

11. **MAJOR: No backtesting discussion for RL trading**
    - Location: Absent from deepdive 360-382
    - Impact: Students may believe RL trading "works" without understanding overfitting risk
    - Fix: Add backtesting methodology, out-of-sample evaluation, comparison to benchmarks

12. **MODERATE: FinBERT described as "pre-trained" rather than "fine-tuned"**
    - Location: deepdive line 200
    - Impact: Pre-training vs fine-tuning distinction is fundamental
    - Fix: Correct terminology

13. **MODERATE: Discount factor range includes 1**
    - Location: deepdive line 252
    - Impact: gamma=1 diverges for infinite-horizon
    - Fix: Specify episodic vs continuing tasks

14. **MODERATE: Similarity heatmap uses figsize=(10,8) not (10,6)**
    - Location: 02_similarity_heatmap/chart.py line 22
    - Impact: Template spec violation
    - Fix: Change to (10,6) or justify exception

15. **MINOR: TBD placeholders in practice sections**
    - Location: overview 196, deepdive 426
    - Impact: Incomplete materials
    - Fix: Add actual Colab links

16. **MINOR: Time budget exceeds 3 hours by 15 minutes**
    - Location: instructor guide lines 116-123
    - Impact: Session overrun
    - Fix: Reduce Method or Solution phase

---

## ACCEPTANCE CRITERIA

**Passing Score:** >= 70/100

**Current Estimated Score:** 20-35/100 (FAIL)

**Primary Blockers to Passing:**
1. Structural: Two topics means neither has depth (-20+ points across sections)
2. Negative sampling entirely missing (-5-8 points across formula/algorithm/completeness)
3. No quantitative finance examples (-6-8 points)
4. Policy viz chart is fabricated (-3-4 points)
5. Zero statistical inference (-5 points)
6. 100% chart redundancy (-3 points)
7. No TD learning foundation (-3-4 points)

**Quick Wins (1-2 hours each):**
- Add negative sampling formula and explanation to Skip-gram slide
- Fix FinBERT description (fine-tuned, not pre-trained)
- Add caveats to word analogy slide
- Fix discount factor range
- Add epsilon-greedy decay to Q-learning algorithm
- Fix similarity heatmap figsize
- Fix TBD placeholders

**Medium Additions (2-4 hours each):**
- Add TD(0) learning slide before Q-learning
- Add static vs contextual embeddings comparison slide
- Replace policy_viz chart with actual learned policy output
- Add concrete RL reward function with transaction costs
- Add worked numerical Q-learning example (single update step)
- Create 3-5 unique deepdive charts

**Major Additions (4+ hours each):**
- Add quantitative sentiment analysis case study with real data
- Add backtesting methodology section for RL trading
- Add statistical inference discussion (embedding significance, Q-value confidence)
- Add Actor-Critic explanation (not just name)
- Consider restructuring: either split into two sessions or drastically narrow scope

**Structural Recommendation:**
Consider splitting L06 into:
- L06a: Text Representations & NLP for Finance (embeddings, Word2Vec, BERT, sentiment analysis)
- L06b: Sequential Decision Making (RL, Q-learning, DQN, trading applications)

This would allow MSc-level depth in each topic.

---

## DELIVERABLES

Upon completion, generate:
1. **Hostile Review Report** (`.omc/reports/L06-hostile-review-report.md`)
2. **Issue List** with severity ratings and line references
3. **Recommended Additions** prioritized by impact
4. **Final Score** with per-section justification
5. **Structural Recommendation** on whether to split L06

---

**Plan Created:** 2026-02-06
**Plan Status:** READY FOR EXECUTION
**Estimated Review Time:** 90-120 minutes
**Parallel Execution:** Phases 1-4 can run concurrently

---

PLAN_READY: .omc/plans/L06-hostile-content-review.md
