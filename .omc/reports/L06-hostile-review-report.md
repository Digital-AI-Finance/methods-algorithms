# L06 Hostile Content Review Report: Embeddings & RL

**Review Date:** 2026-02-06
**Reviewer Persona:** Hostile External Academic Examiner
**Target Audience:** MSc Data Science (various backgrounds, NO pre-knowledge)
**Execution Mode:** Ralplan (Planner + Architect + Critic consensus)

---

## Executive Summary

**Final Score: 35/100 (FAIL - Grade F)**

The L06 lecture materials attempt to cover two substantial MSc-level topics -- word embeddings and reinforcement learning -- in a single 3-hour session. The fundamental problem is INCOMPLETENESS rather than INCORRECTNESS: the Architect audit found zero outright wrong formulas and verified all technical claims as TRUE or TRUE-with-caveats. However, the materials are critically shallow in both halves, presenting formulas without the machinery needed to understand or implement them, and offering finance applications at bullet-point depth only.

**Key Findings:**
1. **Skip-gram softmax correct but incomplete** -- negative sampling never mentioned, making the formula pedagogically useless (INCOMPLETE)
2. **No quantitative finance example** in either embeddings or RL (INCOMPLETE)
3. **Policy visualization chart is a hardcoded if-else rule** labeled "Learned Trading Policy" (MISLEADING)
4. **Zero statistical inference** across both topics (INCOMPLETE)
5. **RL formalization mathematically correct** -- MDP, Bellman, Q-learning all verified (POSITIVE)
6. **ALL technical claims verified as TRUE or TRUE-with-caveats** -- zero factual errors found (POSITIVE)
7. **100% chart redundancy** between overview and deepdive (7/7 duplicated)
8. **TD learning completely absent** -- the theoretical foundation of Q-learning is never introduced

**Calibration vs. Previous Reviews:**
- L01 (Linear Regression): ~66%
- L02 (Logistic Regression): ~55-65%
- L03 (KNN & K-Means): 29%
- L04 (Random Forests): 41%
- L05 (PCA & t-SNE): 37%
- **L06 (Embeddings & RL): 35%**

L06 scores higher than L03 (29%) because L03 contained outright wrong claims (K-Means++ O(log k) unsubstantiated, EM relationship incorrectly omitted while claiming convergence). L06's problem is shallow coverage, not factual error. L06 scores lower than L04 (41%) because L04 at least had correct and moderately detailed decision tree and ensemble content for one topic, whereas L06 spreads thin across two topics with neither reaching adequate depth.

---

## Score Breakdown

| Section | Max | Score | Deductions |
|---------|-----|-------|------------|
| Formula Verification | 15 | 7 | -8 (softmax incomplete -3, analogy uncaveated -2, policy gradient imprecise -2, DQN trivial -1) |
| Misleading Statements | 10 | 5 | -5 (policy viz "learned" -2, FinBERT imprecise -1, off-policy unqualified -1, DQN Atari vs finance -1) |
| Algorithm Correctness | 5 | 2 | -3 (skip-gram missing neg. sampling -1, Q-learning incomplete -1, DQN no algorithm -1) |
| Learning Objectives | 20 | 7 | -13 (Obj 1 partial -3, Obj 2 weak -5, Obj 3 adequate -1, Obj 4 weak -4) |
| MSc Level | 20 | 3 | -17 (zero inference -5, missing neg. sampling theory -3, missing TD learning -3, missing static vs contextual -2, no advanced topics -4) |
| Finance Use Cases | 15 | 3 | -12 (no quant. sentiment example -3, no reward function -3, no backtesting -2, hardcoded policy -2, all bullet-point depth -2) |
| Pedagogical Flow | 10 | 4 | -6 (100% chart redundancy -3, TBD placeholders -1, time exceeded -1, no XKCD image -1) |
| Completeness | 5 | 2 | -3 (major gaps both halves -2, no evaluation methodology -1) |
| Chart Quality Bonus | +5 | +2 | One spec violation, one misleading chart, but clean visuals |
| **TOTAL** | **100** | **35** | **-65** |

---

## CRITICAL FINDINGS (Must Fix)

### C1: Skip-gram Softmax Presented Without Negative Sampling
**Location:** `L06_deepdive.tex` line 134
**Type:** INCOMPLETE (major pedagogical gap)
**Current:**
```latex
P(w_{context} | w_{target}) = \frac{\exp(v_{context}^T v_{target})}{\sum_{w \in V} \exp(v_w^T v_{target})}
```
**Issue:** The formula is mathematically correct. However, the denominator sums over the ENTIRE vocabulary (typically 100K+ words), making this softmax computationally intractable. This is the central computational problem of Word2Vec. Mikolov et al. (2013b) introduced negative sampling specifically because this formula cannot be computed in practice. An MSc student attempting to implement this formula directly would produce O(|V|) computation per update -- completely impractical. The formula is never identified as intractable, and negative sampling is never mentioned anywhere in the lecture.
**Evidence:** Zero occurrences of "negative sampling", "hierarchical softmax", or "NCE" in either .tex file.
**Impact:** Students cannot understand how Word2Vec actually trains. The formula gives a false impression of simplicity.
**Deduction:** -3 points (Formula Verification). This is a pedagogical gap, not a mathematical error -- the formula IS correct, just useless without the computational workaround. Contrast with L05's "PCA assumes Gaussian" which was actually FALSE (-3 there); equal severity is appropriate here because while L06's formula is correct, presenting it as the complete story is more misleading than a simple omission.

### C2: No Quantitative Finance Example in Either Topic
**Location:** `L06_deepdive.tex` lines 207-221 (embeddings), 360-374 (RL)
**Type:** INCOMPLETE
**Issue:** Both finance application sections consist entirely of bullet-point descriptions:
- Embeddings: "Sentiment Analysis: News -> embedding -> positive/negative" (one line, deepdive line 209)
- RL: "State: Price history, portfolio, technical indicators" (one line, deepdive line 363)
Neither topic provides a single quantitative example with actual numbers, actual data, or actual computation. An MSc course with "finance/banking applications" must demonstrate at least one application with concrete numbers.
**Missing (Embeddings):** Actual sentiment score computation, cosine similarity between real financial terms with real embeddings, SEC filing comparison with numbers.
**Missing (RL):** Concrete reward function formula (e.g., $r_t = \text{return}_t - c \cdot |\Delta\text{position}_t|$), specific state representation design, comparison to benchmark returns.
**Impact:** Finance objectives cannot be considered met at any Bloom's level above Remember.
**Deduction:** -6 points (Finance Use Cases: -3 embeddings, -3 RL)

### C3: Policy Visualization Chart is a Hardcoded Rule Labeled "Learned"
**Location:** `06_policy_viz/chart.py` lines 40-47; `L06_deepdive.tex` line 382; `L06_overview.tex` line 179
**Type:** MISLEADING
**Current:** The chart title reads "Learned Trading Policy: Action based on State" (chart.py line 86). The deepdive bottomnote says "Learned policy: buy when oversold/high momentum, sell when overbought" (line 382). The overview frame title is "Learned Trading Policy" (line 179).
**Evidence:** The chart.py implements a deterministic if-else rule:
```python
def policy(rsi, mom):
    if rsi < 30 or mom > 2:
        return 1  # Buy
    elif rsi > 70 or mom < -2:
        return -1  # Sell
    else:
        return 0  # Hold
```
This is a simple RSI/momentum technical trading rule with hardcoded thresholds. It is NOT a policy learned by any RL algorithm. Presenting it as "Learned" is factually misleading -- it misrepresents what RL output looks like and gives students a false understanding of what a trained agent produces.
**Impact:** Students associate RL-learned policies with hand-coded technical indicators, undermining the core concept of the RL section.
**Deduction:** -2 points (Misleading Statements), -2 points (Finance Use Cases)

### C4: Zero Statistical Inference Content
**Location:** Missing throughout both files
**Type:** INCOMPLETE
**Expected at MSc level:**
- Confidence intervals for embedding similarity scores
- Statistical significance of word analogy results
- Variance of Q-value estimates
- Bootstrap or cross-validation for embedding evaluation
- Importance sampling for off-policy evaluation
- Confidence bounds for learned policies
**Current Coverage:** NONE. Zero inference, zero uncertainty quantification in either topic.
**Impact:** Not MSc-level without any ability to assess reliability of results.
**Deduction:** -5 points (MSc Level)

---

## MAJOR FINDINGS (Should Fix)

### M1: 100% Chart Redundancy Between Overview and Deepdive
**Location:** All 7 charts appear in both files
**Type:** INCOMPLETE (pedagogical waste)

| Chart | Overview Line | Deepdive Line | Redundant? |
|-------|---------------|---------------|------------|
| 01_word_embedding_space | 144 | 148 | YES |
| 02_similarity_heatmap | 151 | 184 | YES |
| 03_rl_loop | 158 | 239 | YES |
| 04_q_learning_grid | 165 | 323 | YES |
| 05_reward_curves | 174 | 354 | YES |
| 06_policy_viz | 181 | 380 | YES |
| 07_decision_flowchart | 203 | 435 | YES |

The deepdive has ZERO unique charts. This is the worst redundancy pattern in the course (tied with L03, L04, L05 pre-improvement). Missing unique deepdive charts: skip-gram architecture diagram, negative sampling illustration, DQN architecture, experience replay buffer, actual RL training output, Word2Vec training loss curve.
**Deduction:** -3 points (Pedagogical Flow)

### M2: Word Analogies Presented Without Caveats
**Location:** `L06_deepdive.tex` lines 153-170
**Type:** IMPRECISE
**Current:** The king-man+woman=queen example and two finance analogies ($\vec{stock} - \vec{equity} + \vec{debt} \approx \vec{bond}$, $\vec{CEO} - \vec{company} + \vec{country} \approx \vec{president}$) are presented as reliable properties of embeddings.
**Issue:** Research has demonstrated significant limitations:
- Success rates for word analogies are typically 40-70%, not near-100% as implied (Linzen 2016)
- The 3CosAdd evaluation method has known biases that inflate accuracy (Rogers et al. 2017)
- Finance-domain analogies (stock-equity+debt=bond) have no published empirical verification with standard embeddings
- Word embeddings encode gender and racial biases through analogies (Bolukbasi et al. 2016)
**Impact:** Students believe analogy arithmetic is a reliable property. It is not.
**Deduction:** -2 points (Formula Verification)

### M3: TD Learning Completely Absent
**Location:** Missing throughout
**Type:** INCOMPLETE
**Issue:** Temporal Difference learning is the theoretical foundation of Q-learning. The TD(0) update rule ($V(s) \leftarrow V(s) + \alpha[r + \gamma V(s') - V(s)]$) is the precursor to the Q-learning update. Without TD learning, Q-learning appears as an unmotivated formula rather than a member of a theoretical family. SARSA (on-policy TD) is also absent, preventing comparison of on-policy vs off-policy methods.
**Impact:** Students cannot understand WHY the Q-learning update rule has its specific form, or how it relates to Monte Carlo methods and dynamic programming.
**Deduction:** -3 points (MSc Level)

### M4: Negative Sampling Never Mentioned
**Location:** Missing throughout
**Type:** INCOMPLETE
**Issue:** Negative sampling (Mikolov et al. 2013b) is the key computational innovation that made Word2Vec practical. Without it, the skip-gram objective (line 134) requires O(|V|) computation per update. The negative sampling objective replaces the full softmax with a binary classification task using k negative samples, reducing computation to O(k) where k is typically 5-20. This is arguably the single most important practical detail of Word2Vec.
**Impact:** Students know the mathematical goal but not how it is achieved in practice.
**Deduction:** -1 point (Algorithm Correctness). Note: primary deduction for this gap is already captured in C1 (Formula Verification -3). This is the secondary algorithmic impact only.

### M5: Static vs Contextual Embeddings Not Distinguished
**Location:** `L06_deepdive.tex` lines 190-203
**Type:** INCOMPLETE
**Issue:** Word2Vec (line 193) and BERT (line 469) are listed as if they are equivalent approaches. The fundamental distinction -- Word2Vec produces one fixed vector per word regardless of context, while BERT produces different vectors for the same word in different sentences -- is never stated. "Bank" in "river bank" vs "bank account" gets the SAME vector in Word2Vec but DIFFERENT vectors in BERT. This is the single most important conceptual advance in NLP embeddings over the last decade.
**Impact:** Students conflate static and contextual embeddings, leading to fundamental misunderstanding of modern NLP.
**Deduction:** -2 points (MSc Level)

### M6: Policy Gradient is Name-Dropping Without Content
**Location:** `L06_deepdive.tex` lines 400-413
**Type:** INCOMPLETE
**Issue:** The policy gradient theorem is stated (line 403) but:
- REINFORCE is named but not described (what is the return estimator? what is the baseline?)
- Actor-Critic is named but the critic is never defined (what is it? what does it learn?)
- PPO is named but the clipping mechanism is never explained (what is "proximal"?)
- A3C is named but "asynchronous" and "advantage" are not explained
This is listing algorithm names, not teaching them. The formula itself uses $Q^{\pi_\theta}(s,a)$ but the REINFORCE algorithm actually uses returns $G_t$, and modern methods use advantage $A^{\pi}(s,a) = Q^{\pi}(s,a) - V^{\pi}(s)$ -- none of which is mentioned.
**Impact:** Students can recite names but cannot explain any algorithm beyond basic Q-learning.
**Deduction:** -2 points (Formula Verification: imprecise policy gradient presentation)

### M7: DQN Loss Function Absent
**Location:** `L06_deepdive.tex` lines 385-397
**Type:** INCOMPLETE
**Issue:** The DQN slide shows only $Q(s,a;\theta) \approx Q^*(s,a)$ -- a goal statement, not a formula. The actual DQN loss function $L(\theta) = \mathbb{E}[(r + \gamma \max_{a'} Q(s',a';\theta^-) - Q(s,a;\theta))^2]$ with target network parameters $\theta^-$ is absent. "Function Approximation" is listed as a "Key Innovation" but it is the core idea, not an innovation -- the innovations are experience replay (to break temporal correlation) and the target network (to stabilize training). Neither mechanism is explained beyond one-line descriptions.
**Impact:** An MSc student cannot implement DQN from these materials.
**Deduction:** -1 point (Formula Verification: DQN trivially stated)

### M8: No Worked Numerical Example Anywhere
**Location:** Missing throughout
**Type:** INCOMPLETE
**Issue:** Neither topic contains a single concrete numerical computation:
- No Q-table update walkthrough (e.g., "given Q(s1,up)=3.2, alpha=0.1, r=1, gamma=0.9, Q(s2,best)=4.0, new Q = 3.2 + 0.1[1 + 0.9*4.0 - 3.2] = 3.48")
- No embedding vector arithmetic with actual numbers
- No cosine similarity computation on real vectors
**Impact:** Students see formulas but never see them produce a number. This blocks comprehension for students who learn by example.
**Deduction:** Already captured in C2 (Finance) and Learning Objectives deductions.

### M9: Q-Learning Convergence Conditions Not Stated
**Location:** `L06_deepdive.tex` lines 300-317
**Type:** INCOMPLETE
**Issue:** The Q-learning update rule (line 303) is correct, but convergence to $Q^*$ requires: (a) all state-action pairs visited infinitely often, (b) learning rate satisfying Robbins-Monro conditions ($\sum \alpha_t = \infty$, $\sum \alpha_t^2 < \infty$). A fixed $\alpha$ as implied does NOT guarantee convergence in the theoretical sense. Additionally, the bottomnote "Q-learning is off-policy: learns optimal Q regardless of policy followed" (line 317) is TRUE only under these conditions -- with poor exploration, Q-learning can converge to suboptimal values.
**Deduction:** -1 point (Misleading Statements: off-policy claim unqualified)

---

## MODERATE FINDINGS

### Mo1: FinBERT Description Imprecise
**Location:** `L06_deepdive.tex` line 200
**Type:** IMPRECISE
**Current:** "FinBERT: Pre-trained on financial text"
**Issue:** Araci (2019) performed domain-adaptive pre-training: taking the original BERT model (already pre-trained on general text) and further pre-training it on financial corpora. The slide's phrasing "Pre-trained on financial text" is ambiguous -- it could imply training from scratch on financial text only, which is not what happened. The correct description would be "further pre-trained on financial text" or "BERT fine-tuned for financial domain". The distinction between pre-training and domain-adaptive pre-training/fine-tuning is fundamental at MSc level.
**Note:** This is imprecise, not wrong. Araci DID perform additional pre-training on financial text. The slide is technically defensible but could mislead.
**Deduction:** -1 point (Misleading Statements)

### Mo2: Similarity Heatmap figsize Violation
**Location:** `02_similarity_heatmap/chart.py` line 22
**Type:** INCORRECT (spec violation)
**Current:** `fig, ax = plt.subplots(figsize=(10, 8))`
**Required:** `figsize=(10, 6)` per CLAUDE.md chart creation rules
**Impact:** Template compliance failure. All other 6 charts use correct (10, 6).
**Deduction:** Captured in Chart Quality Bonus reduction.

### Mo3: Overview References Include ISLR (Misplaced)
**Location:** `L06_overview.tex` line 215
**Type:** IMPRECISE
**Current:** "James et al. (2021). Introduction to Statistical Learning."
**Issue:** ISLR (James et al. 2021) does not cover word embeddings or reinforcement learning. This reference is appropriate for L01-L04 but misplaced in L06. It gives students a false impression that they can find L06 content in this textbook.
**Deduction:** -1 point (Pedagogical Flow, captured in total)

### Mo4: Discount Factor Range Includes 1
**Location:** `L06_deepdive.tex` line 252
**Type:** IMPRECISE
**Current:** $\gamma \in [0,1]$
**Issue:** For infinite-horizon (continuing) MDPs, $\gamma = 1$ causes the infinite sum $\sum_{t=0}^{\infty} \gamma^t R_{t+1}$ to diverge when rewards are non-zero. The correct specification is $\gamma \in [0,1)$ for infinite-horizon tasks, or $\gamma \in [0,1]$ for episodic tasks with guaranteed termination. The distinction is not made.
**Deduction:** Captured within MSc Level deductions (theoretical completeness).

### Mo5: Instructor Guide Timing Inconsistency
**Location:** `L06_instructor_guide.md` line 83 vs lines 116-123
**Type:** INCORRECT (internal inconsistency)
**Issue:** The Practice Phase header (line 83) says "75 min" but the timing table (line 122) says "60 min". The total timing table sums to 195 min (3h 15min), exceeding the stated 3-hour session by 15 minutes. If the Practice phase is actually 75 min (as the header states), the total would be 210 min (3h 30min).
**Deduction:** -1 point (Pedagogical Flow: time exceeded)

### Mo6: Reward Curves and Q-Values Are Fabricated
**Location:** `05_reward_curves/chart.py` lines 34-43; `04_q_learning_grid/chart.py` lines 35-40
**Type:** IMPRECISE
**Issue:** The reward curves are generated from exponential functions with random noise:
```python
q_learning = -50 + 45 * (1 - np.exp(-episodes / 150)) + np.random.randn(len(episodes)) * 5
dqn = -50 + 55 * (1 - np.exp(-episodes / 100)) + np.random.randn(len(episodes)) * 4
```
The Q-learning grid uses hardcoded Q-values:
```python
q_values = np.array([
    [0.3, 0.4, 0.5, 0.6],
    [0.4, 0.5, -0.8, 0.7],
    ...
])
```
Neither comes from actual RL training. The reward curves are synthetic formulas, not empirical results. The Q-values are manually specified, not computed by running Q-learning. While synthetic data is acceptable for pedagogical illustration, the charts are titled "Q-Learning: Grid World with Learned Q-Values" and "RL Training: Cumulative Reward vs Episode" -- implying actual training runs.
**Impact:** Students may not realize these are illustrations, not evidence of algorithm behavior.
**Deduction:** Captured within Chart Quality Bonus reduction.

### Mo7: "Averaging Word Vectors" Limitation Not Stated
**Location:** `L06_deepdive.tex` line 217
**Type:** IMPRECISE
**Current:** "Average word vectors (simple baseline)"
**Issue:** Averaging destroys word order entirely. "Bank robber" and "robber bank" produce identical sentence embeddings. For an MSc audience, this fundamental limitation of bag-of-embeddings approaches must be stated.
**Deduction:** Captured within Learning Objectives (Obj 1 partial).

### Mo8: No XKCD Image
**Location:** Missing throughout both files
**Type:** INCOMPLETE
**Issue:** Per CLAUDE.md, course slides include XKCD cartoons for engagement with CC BY-NC 2.5 attribution. L06 has zero XKCD images. All previous lectures include at least one.
**Deduction:** -1 point (Pedagogical Flow)

---

## MINOR FINDINGS

### Mi1: TBD Placeholders (x2)
**Location:** `L06_overview.tex` line 196; `L06_deepdive.tex` line 426
**Issue:** "[TBD]" for Colab notebook links. Same pattern as L03, L04, L05.
**Deduction:** -1 point (Pedagogical Flow)

### Mi2: Time Budget Exceeds 3 Hours
**Location:** `L06_instructor_guide.md` lines 116-123
**Issue:** Timing table sums to 195 min (3h 15min), exceeding the 3-hour session by 15 min. Additionally, this session includes "Course summary" and "capstone intro" in the Q&A slot, adding further time pressure.
**Deduction:** Already captured in Mo5.

### Mi3: Cosine Similarity "1=identical" Imprecise
**Location:** `L06_deepdive.tex` line 180
**Type:** IMPRECISE
**Current:** "1=identical, 0=orthogonal, -1=opposite"
**Issue:** Cosine similarity of 1 means "same direction", not "identical". Vectors [1,0] and [2,0] have cosine similarity 1 but are not identical (different magnitudes). For an MSc audience, this distinction matters.
**Deduction:** Captured within formula verification (minor).

### Mi4: Notation Inconsistency in MDP/Reward
**Location:** `L06_deepdive.tex` lines 251, 271-284
**Type:** IMPRECISE
**Issue:** Line 251 defines $R(s,a,s')$ as a function of three arguments. Lines 271-284 use $R_{t+1}$ and bare $R$ without subscripts. The distinction between the deterministic reward function and the random variable representing received reward is not clarified.
**Deduction:** Captured within formula verification (minor notation).

---

## POSITIVE FINDINGS

### P1: RL Formalization Mathematically Correct and Coherent
The MDP formalization (lines 245-297) is mathematically sound:
- MDP tuple correctly specified (line 246)
- Markov property correctly stated (line 257)
- Policy definition correct (line 263)
- Value function correct (line 271)
- Q-function correct (line 276)
- Bellman optimality equation correct (line 284)
- Optimal policy derivation correct (line 295)
- Q-learning update rule correct (line 303)
- Epsilon-greedy strategy correctly formalized (lines 337-341)

This is a coherent mathematical chain from MDP definition through to the Q-learning algorithm.

### P2: ALL Technical Claims Verified as TRUE or TRUE-with-caveats
The Architect audit found zero factually incorrect statements. Every claim in both files is either TRUE or TRUE-with-caveats (needing qualification but not correction). This distinguishes L06 from L03 (wrong K-Means++ claim), L05 (false "PCA assumes Gaussian"), and even L04 (wrong Breiman attribution). L06's problem is what is MISSING, not what is WRONG.

### P3: Comparison Table Clear and Useful
**Location:** `L06_deepdive.tex` lines 441-458
The embeddings vs RL comparison table provides a clean, accurate side-by-side comparison across 6 dimensions (Input, Output, Learning, Signal, Key challenge, Finance use). This is pedagogically sound and helps students organize the two topics.

### P4: Decision Flowchart Pedagogically Sound
**Location:** `07_decision_flowchart/chart.py`
The when-to-use-what flowchart provides actionable guidance for choosing between embeddings and RL based on problem characteristics. This is consistently one of the stronger elements across all lectures.

### P5: Finance-Relevant Terminology in Charts
Charts use finance-relevant terms: market/portfolio/buy/sell/hold in the RL loop diagram, stock/equity/bond/risk/volatility in the embedding space and similarity heatmap. While the data is synthetic, the vocabulary anchors the material in the finance domain.

### P6: Instructor Guide Common Misconceptions All Accurate
**Location:** `L06_instructor_guide.md` lines 58-61
Three misconceptions listed:
- "Embeddings understand language" -- correctly labeled FALSE
- "RL always finds optimal solutions" -- correctly labeled FALSE
- "DQN works for any problem" -- correctly labeled FALSE
All three are genuine student misconceptions, accurately identified and corrected.

### P7: Charts Clean and Readable
Excluding the policy_viz content accuracy issue and the similarity heatmap figsize violation, all 7 charts are visually clean, use correct color palettes, have appropriate font sizes, and include CHART_METADATA. The RL loop diagram is particularly effective as a conceptual overview.

---

## Recommended Additions (Prioritized by Impact)

### HIGH PRIORITY (Would raise score to 55+)

| # | Addition | Effort | Impact |
|---|----------|--------|--------|
| 1 | Add negative sampling formula and explanation to Skip-gram slide | 1 hour | +5 points |
| 2 | Add one quantitative sentiment analysis example (embeddings + cosine sim on real text) | 3 hours | +5 points |
| 3 | Replace policy_viz chart with output from actual Q-learning training run | 2 hours | +4 points |
| 4 | Add concrete RL reward function with transaction costs: $r_t = R_t - c|\Delta w_t|$ | 1 hour | +3 points |
| 5 | Add caveats to word analogy slide (success rates, bias, limitations) | 30 min | +2 points |
| 6 | Add TD(0) learning slide before Q-learning | 1 hour | +3 points |

### MEDIUM PRIORITY (Would raise score to 70+)

| # | Addition | Effort | Impact |
|---|----------|--------|--------|
| 7 | Add static vs contextual embeddings comparison slide (Word2Vec vs BERT) | 1 hour | +3 points |
| 8 | Add worked numerical Q-learning update example | 30 min | +2 points |
| 9 | Explain Actor-Critic properly (not just name) or remove the list | 1 hour | +2 points |
| 10 | Add DQN loss function with target network explanation | 45 min | +2 points |
| 11 | Add statistical inference section (embedding significance, Q-value confidence) | 3 hours | +5 points |
| 12 | Clarify FinBERT as domain-adaptive pre-training | 5 min | +1 point |
| 13 | Create 3-5 unique deepdive charts (skip-gram architecture, DQN diagram, real training curve) | 4 hours | +3 points |

### LOW PRIORITY (Polish)

| # | Addition | Effort | Impact |
|---|----------|--------|--------|
| 14 | Remove TBD placeholders | 5 min | +1 point |
| 15 | Fix similarity heatmap figsize to (10, 6) | 5 min | +0.5 points |
| 16 | Fix time budget (trim to 180 min) | 15 min | +1 point |
| 17 | Fix cosine similarity "1=same direction" not "1=identical" | 5 min | +0.5 points |
| 18 | Remove ISLR from L06 overview references | 5 min | +0.5 points |
| 19 | Add XKCD cartoon with attribution | 15 min | +1 point |
| 20 | Fix instructor guide timing inconsistency (75 min vs 60 min) | 5 min | +0.5 points |
| 21 | Specify Q-learning convergence conditions (Robbins-Monro) | 15 min | +0.5 points |
| 22 | Add discount factor note: $\gamma \in [0,1)$ for continuing tasks | 5 min | +0.5 points |

**Total potential improvement:** +46 points --> 81/100 (Grade B)

**Structural Note:** The course design constrains L06 to cover two topics in one session (6 sessions for 6 topics). This is a structural observation, not an L06-specific deficiency -- the effects are already captured in the shallow per-section scores. If the course structure allows it in the future, splitting into L06a (Embeddings/NLP) and L06b (Reinforcement Learning) would enable MSc-level depth in both.

---

## Acceptance Criteria for Passing (>=70)

**All CRITICAL issues must be resolved:**
- [ ] Negative sampling added to Skip-gram presentation (C1)
- [ ] At least one quantitative finance example with real numbers (C2)
- [ ] Policy visualization replaced with actual learned policy or relabeled (C3)
- [ ] At least one statistical inference method discussed (C4)

**At least 6/9 MAJOR issues resolved:**
- [ ] Chart redundancy reduced (at least 3 unique deepdive charts) (M1)
- [ ] Word analogy caveats added (M2)
- [ ] TD learning introduced before Q-learning (M3)
- [ ] Static vs contextual embeddings distinguished (M5)
- [ ] Policy gradient section expanded or honestly scoped down (M6)
- [ ] DQN loss function added (M7)
- [ ] Worked numerical example added (M8)
- [ ] Q-learning convergence conditions stated (M9)
- [ ] Negative sampling algorithm described (M4)

---

## Verdict

**FAIL** -- The L06 materials are not suitable for MSc-level delivery in their current state.

**Primary Deficiencies:**
1. **Incompleteness, not incorrectness:** All formulas are mathematically correct, but critical content is missing (negative sampling, TD learning, static vs contextual, DQN loss, policy gradient details)
2. **Finance applications hollow:** Both topics offer only bullet-point descriptions with zero quantitative demonstration
3. **Misleading visualization:** The policy chart actively misrepresents what RL produces
4. **No statistical inference:** Cannot assess reliability of any result
5. **Two topics means neither has depth:** The structural constraint forces shallow coverage in both halves

**Distinguishing Factor:** L06 is unique in the course for having zero factual errors while still failing. The problem is exclusively about DEPTH and COMPLETENESS. This makes it more fixable than L03 (which required correcting wrong claims) -- most fixes involve ADDING content rather than correcting existing content.

**Comparison to L04/L05:** Similar issues pattern (missing inference, chart redundancy, shallow finance). L06 scores slightly lower than L04 (41%) due to the two-topic dilution effect but higher than L03 (29%) due to absence of factual errors.

**Recommendation:** Major revision required. Estimate 15-20 hours to reach passing threshold, focused primarily on adding content (negative sampling, TD learning, finance examples, unique charts) rather than correcting errors.

---

## Issues Summary for Fix Phase

| ID | Severity | Type | Issue | Location | Fix |
|----|----------|------|-------|----------|-----|
| C1 | CRITICAL | INCOMPLETE | Skip-gram missing negative sampling | deepdive 134 | Add neg. sampling formula + explanation |
| C2 | CRITICAL | INCOMPLETE | No quantitative finance example | deepdive 207-221, 360-374 | Add worked examples both topics |
| C3 | CRITICAL | MISLEADING | Policy viz is hardcoded rule | chart.py lines 40-47, deepdive 382 | Replace with actual trained policy |
| C4 | CRITICAL | INCOMPLETE | Zero statistical inference | N/A | Add inference section |
| M1 | MAJOR | INCOMPLETE | 100% chart redundancy (7/7) | Both .tex files | Create unique deepdive charts |
| M2 | MAJOR | IMPRECISE | Word analogies uncaveated | deepdive 153-170 | Add limitations + bias |
| M3 | MAJOR | INCOMPLETE | TD learning absent | N/A | Add TD(0) before Q-learning |
| M4 | MAJOR | INCOMPLETE | Negative sampling never mentioned | N/A | Add algorithm description |
| M5 | MAJOR | INCOMPLETE | Static vs contextual conflated | deepdive 190-203 | Add comparison slide |
| M6 | MAJOR | INCOMPLETE | Policy gradient name-dropping | deepdive 400-413 | Explain or scope down |
| M7 | MAJOR | INCOMPLETE | DQN loss function absent | deepdive 385-397 | Add loss + target network |
| M8 | MAJOR | INCOMPLETE | No worked numerical example | N/A | Add Q-table update walkthrough |
| M9 | MAJOR | IMPRECISE | Q-learning convergence unstated | deepdive 317 | Add conditions |
| Mo1 | MODERATE | IMPRECISE | FinBERT "pre-trained" ambiguous | deepdive 200 | Clarify domain-adaptive |
| Mo2 | MODERATE | INCORRECT | Heatmap figsize (10,8) not (10,6) | chart.py line 22 | Fix to (10,6) |
| Mo3 | MODERATE | IMPRECISE | ISLR in L06 references | overview 215 | Remove or replace |
| Mo4 | MODERATE | IMPRECISE | Discount factor includes 1 | deepdive 252 | Specify episodic vs continuing |
| Mo5 | MODERATE | INCORRECT | Timing inconsistency 75 vs 60 min | guide lines 83, 122 | Reconcile |
| Mo6 | MODERATE | IMPRECISE | Reward curves / Q-values fabricated | chart.py files | Label as illustration or use real data |
| Mo7 | MODERATE | IMPRECISE | Averaging destroys word order | deepdive 217 | State limitation |
| Mo8 | MODERATE | INCOMPLETE | No XKCD image | N/A | Add with attribution |
| Mi1 | MINOR | INCOMPLETE | TBD placeholders (x2) | overview 196, deepdive 426 | Add Colab links |
| Mi2 | MINOR | INCOMPLETE | Time budget 195 min > 180 min | guide 116-123 | Trim content |
| Mi3 | MINOR | IMPRECISE | "1=identical" should be "1=same direction" | deepdive 180 | Fix wording |
| Mi4 | MINOR | IMPRECISE | MDP/reward notation inconsistent | deepdive 251, 271-284 | Clarify R function vs R_t |

---

**Report Generated:** 2026-02-06
**Execution Mode:** Ralplan (Planner + Architect + Critic consensus)
**Calibration Reference:** L01: 66%, L02: 55-65%, L03: 29%, L04: 41%, L05: 37%
