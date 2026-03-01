# All-Quiz Bloom's Taxonomy Audit Report

## Summary
- Date: 2026-03-01
- Quizzes analyzed: 8 (+ L04 from separate analysis)
- Total questions classified: 160 (+ 20 L04 = 180 total)
- Source files: `docs/quiz/L0X_*.html`

---

## Per-Quiz Analysis

### L01: Linear Regression (20 questions)

| Q# | Topic | Bloom Level | Finance App |
|----|-------|-------------|-------------|
| 1 | OLS closed-form formula | 1 - Remember | N |
| 2 | Design matrix dimensions | 1 - Remember | N |
| 3 | SSE loss definition | 1 - Remember | N |
| 4 | Homoscedasticity assumption | 1 - Remember | N |
| 5 | Gradient descent update rule | 1 - Remember | N |
| 6 | Learning rate too large | 2 - Understand | N |
| 7 | Normal eq. vs gradient descent | 5 - Evaluate | N |
| 8 | R-squared interpretation | 2 - Understand | N |
| 9 | Adjusted R-squared purpose | 2 - Understand | N |
| 10 | RMSE vs MAE outliers | 4 - Analyze | Y |
| 11 | Residual plot interpretation | 4 - Analyze | N |
| 12 | Train-test split purpose | 2 - Understand | N |
| 13 | K-fold cross-validation | 1 - Remember | N |
| 14 | Ridge penalty formula | 1 - Remember | N |
| 15 | Lasso feature selection | 1 - Remember | N |
| 16 | Elastic Net definition | 1 - Remember | N |
| 17 | Lambda selection method | 2 - Understand | N |
| 18 | Bias-variance vs complexity | 2 - Understand | N |
| 19 | Overfitting diagnosis | 2 - Understand | N |
| 20 | When linear reg. inappropriate | 2 - Understand | N |

**Distribution:** L1: 9, L2: 8, L3: 0, L4: 2, L5: 1
**Finance coverage:** 1/20 questions
**Topic gaps:** No calculation questions, no finance scenario application, no regularization parameter tradeoff evaluation.

---

### L02: Logistic Regression (20 questions)

| Q# | Topic | Bloom Level | Finance App |
|----|-------|-------------|-------------|
| 1 | Sigmoid range | 1 - Remember | N |
| 2 | Sigmoid at z=0 | 3 - Apply | N |
| 3 | Log-odds (logit) meaning | 2 - Understand | N |
| 4 | Odds ratio calculation | 3 - Apply | N |
| 5 | Why not MSE for logreg | 2 - Understand | N |
| 6 | Cross-entropy calculation | 3 - Apply | N |
| 7 | Log-loss gradient formula | 1 - Remember | N |
| 8 | Decision boundary shape | 1 - Remember | N |
| 9 | Threshold effect on P/R | 4 - Analyze | N |
| 10 | Softmax ensures sum to 1 | 1 - Remember | N |
| 11 | Confusion matrix cell | 1 - Remember | N |
| 12 | Precision calculation | 3 - Apply | N |
| 13 | Recall calculation | 3 - Apply | N |
| 14 | F1 score calculation | 3 - Apply | N |
| 15 | ROC curve perfect point | 1 - Remember | N |
| 16 | AUC of 0.5 meaning | 2 - Understand | N |
| 17 | PR curve vs ROC imbalanced | 4 - Analyze | N |
| 18 | L1 regularization effect | 1 - Remember | N |
| 19 | Class imbalance handling | 5 - Evaluate | N |
| 20 | Credit scoring coefficient | 3 - Apply | Y |

**Distribution:** L1: 7, L2: 3, L3: 7, L4: 2, L5: 1
**Finance coverage:** 1/20 questions
**Topic gaps:** No ROC/AUC computation, no multi-class scenario. Strongest quiz for Apply-level (7 calculation questions).

---

### L03: KNN (standalone, 20 questions)

| Q# | Topic | Bloom Level | Finance App |
|----|-------|-------------|-------------|
| 1 | Non-parametric meaning | 2 - Understand | N |
| 2 | Euclidean vs Manhattan outliers | 4 - Analyze | N |
| 3 | Chebyshev distance definition | 1 - Remember | N |
| 4 | KD-Tree triangle inequality | 2 - Understand | N |
| 5 | Feature scale dominance | 3 - Apply | Y |
| 6 | Standardization vs MinMax | 5 - Evaluate | N |
| 7 | Tie-breaking K=4 binary | 2 - Understand | N |
| 8 | Inverse-distance weighted vote | 3 - Apply | N |
| 9 | Variance formula Var=sigma/K | 4 - Analyze | N |
| 10 | Training accuracy bias K=1 | 4 - Analyze | N |
| 11 | Odd K for binary | 2 - Understand | N |
| 12 | K approaches n behavior | 4 - Analyze | N |
| 13 | Curse of dimensionality | 4 - Analyze | N |
| 14 | Cover-Hart bound calculation | 3 - Apply | N |
| 15 | Cosine vs Euclidean for text | 5 - Evaluate | N |
| 16 | Mahalanobis distance purpose | 2 - Understand | N |
| 17 | KNN regression vs classify | 2 - Understand | N |
| 18 | Imbalanced fraud 99% accuracy | 4 - Analyze | Y |
| 19 | SMOTE mechanism | 2 - Understand | N |
| 20 | Pipeline data leakage | 4 - Analyze | N |

**Distribution:** L1: 1, L2: 7, L3: 3, L4: 7, L5: 2
**Finance coverage:** 2/20 questions
**Topic gaps:** Strongest quiz overall. Excellent Analyze balance. Missing: "given 5 points, classify point X" calculation.

---

### L03: K-Means (standalone, 20 questions)

| Q# | Topic | Bloom Level | Finance App |
|----|-------|-------------|-------------|
| 1 | K=n trivial clustering | 4 - Analyze | N |
| 2 | Assignment step WCSS monotone | 2 - Understand | N |
| 3 | Mean minimizes SSE (proof) | 2 - Understand | N |
| 4 | K-Means++ squared distance | 2 - Understand | N |
| 5 | O(log K) competitive guarantee | 2 - Understand | N |
| 6 | Elbow ambiguity in practice | 4 - Analyze | N |
| 7 | Silhouette score s=0 meaning | 4 - Analyze | N |
| 8 | Silhouette plot thin cluster | 4 - Analyze | N |
| 9 | Voronoi cells non-convex fail | 4 - Analyze | N |
| 10 | Different density cluster fail | 4 - Analyze | N |
| 11 | DBSCAN for non-convex shapes | 5 - Evaluate | N |
| 12 | Hopkins statistic H=0.5 | 4 - Analyze | N |
| 13 | Gap statistic standard error | 2 - Understand | N |
| 14 | K-Means as hard EM special case | 4 - Analyze | N |
| 15 | Mini-Batch K-Means tradeoff | 4 - Analyze | N |
| 16 | K-Medoids outlier robustness | 4 - Analyze | N |
| 17 | Hierarchical vs K-Means | 4 - Analyze | N |
| 18 | RFM standardization necessity | 3 - Apply | Y |
| 19 | Empty cluster reinitialization | 2 - Understand | N |
| 20 | Complexity O(nKdT) dominant | 3 - Apply | N |

**Distribution:** L1: 0, L2: 6, L3: 2, L4: 11, L5: 1
**Finance coverage:** 1/20 questions
**Topic gaps:** Very strong on Analyze. Zero L1 recall -- excellent for MSc. Missing: "given points and centroids, compute new assignments" calculation.

---

### L03: KNN & K-Means combined (20 questions)

| Q# | Topic | Bloom Level | Finance App |
|----|-------|-------------|-------------|
| 1 | KNN lazy learner definition | 1 - Remember | N |
| 2 | Euclidean distance calculation | 3 - Apply | N |
| 3 | Manhattan distance calculation | 3 - Apply | N |
| 4 | Minkowski p=1 equivalence | 1 - Remember | N |
| 5 | K = sqrt(n) heuristic | 1 - Remember | N |
| 6 | Weighted KNN mechanism | 1 - Remember | N |
| 7 | Feature scaling importance | 2 - Understand | N |
| 8 | Curse of dimensionality | 2 - Understand | N |
| 9 | KD-Tree / Ball Tree purpose | 1 - Remember | N |
| 10 | WCSS objective function | 1 - Remember | N |
| 11 | K-Means two steps | 1 - Remember | N |
| 12 | K-Means++ purpose | 2 - Understand | N |
| 13 | WCSS convergence guarantee | 2 - Understand | N |
| 14 | Elbow method for K | 2 - Understand | N |
| 15 | Silhouette score range | 1 - Remember | N |
| 16 | K-Means spherical assumption | 1 - Remember | N |
| 17 | K-Means non-convex failure | 2 - Understand | N |
| 18 | KNN vs K-Means difference | 2 - Understand | N |
| 19 | K-Means customer segmentation | 3 - Apply | Y |
| 20 | KNN fraud detection use | 3 - Apply | Y |

**Distribution:** L1: 9, L2: 7, L3: 4, L4: 0, L5: 0
**Finance coverage:** 2/20 questions
**Topic gaps:** Zero Analyze or Evaluate. Surface-level recall quiz. Stark contrast with standalone L03 quizzes.

---

### L03: KNN & K-Means Accessible (20 questions)

| Q# | Topic | Bloom Level | Finance App |
|----|-------|-------------|-------------|
| 1 | KNN lazy learner definition | 1 - Remember | N |
| 2 | KNN worked example majority vote | 3 - Apply | Y |
| 3 | K=1 vs K=15 boundary effect | 4 - Analyze | N |
| 4 | Feature scale dominance | 3 - Apply | Y |
| 5 | Euclidean distance calculation | 3 - Apply | N |
| 6 | Distance-weighted voting | 3 - Apply | N |
| 7 | Cross-validation for K | 2 - Understand | N |
| 8 | Curse of dimensionality | 2 - Understand | N |
| 9 | KNN vs K-Means confusion | 2 - Understand | N |
| 10 | Imbalanced fraud 99% accuracy | 4 - Analyze | Y |
| 11 | K-Means three steps | 1 - Remember | N |
| 12 | WCSS definition | 1 - Remember | N |
| 13 | Elbow method pattern | 2 - Understand | N |
| 14 | Silhouette +0.8 meaning | 2 - Understand | N |
| 15 | K-Means++ spread rationale | 2 - Understand | N |
| 16 | Voronoi convexity limitation | 4 - Analyze | N |
| 17 | RFM segmentation example | 3 - Apply | Y |
| 18 | K-Means convergence why | 2 - Understand | N |
| 19 | Mini-Batch / K-Medoids compare | 2 - Understand | N |
| 20 | DBSCAN for non-convex shapes | 5 - Evaluate | N |

**Distribution:** L1: 3, L2: 8, L3: 5, L4: 3, L5: 1
**Finance coverage:** 4/20 questions (best of all quizzes)
**Topic gaps:** Best-balanced of the L03 variants. Highest finance coverage. Light on Evaluate (1 question).

---

### L05: PCA & t-SNE (20 questions)

| Q# | Topic | Bloom Level | Finance App |
|----|-------|-------------|-------------|
| 1 | PCA maximizes variance | 1 - Remember | N |
| 2 | Covariance matrix formula | 1 - Remember | N |
| 3 | Eigendecomposition for PCs | 1 - Remember | N |
| 4 | PCs are eigenvectors | 1 - Remember | N |
| 5 | Eigenvalues = variance | 1 - Remember | N |
| 6 | Scree plot elbow method | 2 - Understand | N |
| 7 | Kaiser criterion lambda > 1 | 1 - Remember | N |
| 8 | Explained variance ratio calc | 3 - Apply | N |
| 9 | Reconstruction error definition | 2 - Understand | N |
| 10 | Why center data for PCA | 2 - Understand | N |
| 11 | PCA linear-only limitation | 2 - Understand | N |
| 12 | t-SNE preserves what | 1 - Remember | N |
| 13 | Perplexity parameter meaning | 1 - Remember | N |
| 14 | Low vs high perplexity effect | 4 - Analyze | N |
| 15 | t-distribution crowding problem | 2 - Understand | N |
| 16 | KL divergence loss function | 1 - Remember | N |
| 17 | t-SNE no projection limitation | 2 - Understand | N |
| 18 | PCA vs t-SNE comparison | 4 - Analyze | N |
| 19 | Swiss roll PCA failure | 4 - Analyze | N |
| 20 | PCA in portfolio risk | 3 - Apply | Y |

**Distribution:** L1: 9, L2: 6, L3: 2, L4: 3, L5: 0
**Finance coverage:** 1/20 questions
**Topic gaps:** No Evaluate questions. 45% at L1 (too high for MSc). Missing: eigenvalue-based PC selection, t-SNE parameter tuning scenario.

---

### L06: Embeddings & RL (20 questions)

| Q# | Topic | Bloom Level | Finance App |
|----|-------|-------------|-------------|
| 1 | One-hot encoding limitation | 2 - Understand | N |
| 2 | Dense embedding advantage | 2 - Understand | N |
| 3 | Distributional hypothesis | 1 - Remember | N |
| 4 | Skip-gram predicts what | 1 - Remember | N |
| 5 | CBOW vs Skip-gram | 2 - Understand | N |
| 6 | Word analogy vector arithmetic | 2 - Understand | N |
| 7 | Cosine similarity calculation | 3 - Apply | N |
| 8 | Cosine similarity self-vector | 3 - Apply | N |
| 9 | FastText character n-grams | 1 - Remember | N |
| 10 | FinBERT vs BERT preference | 5 - Evaluate | Y |
| 11 | MDP tuple definition | 1 - Remember | N |
| 12 | Markov property definition | 1 - Remember | N |
| 13 | Policy pi(a|s) meaning | 1 - Remember | N |
| 14 | Q-function meaning | 2 - Understand | N |
| 15 | Bellman equation formula | 1 - Remember | N |
| 16 | Q-learning update rule | 1 - Remember | N |
| 17 | Exploration-exploitation | 2 - Understand | N |
| 18 | Epsilon-greedy mechanism | 3 - Apply | N |
| 19 | Discount factor gamma=0.9 | 2 - Understand | N |
| 20 | DQN improvement over tabular | 2 - Understand | N |

**Distribution:** L1: 8, L2: 8, L3: 3, L4: 0, L5: 1
**Finance coverage:** 1/20 questions
**Topic gaps:** Zero Analyze. RL section (Q11-16) is pure recall. Missing: Q-table trace, compare policies, evaluate RL for trading scenario.

---

### L04: Random Forests (from plan analysis, being upgraded separately)

**Pre-upgrade distribution:** L1: 9, L2: 11, L3: 0, L4: 0, L5: 0
**Post-upgrade distribution:** L1: 4, L2: 8, L3: 2, L4: 4, L5: 2 (8 questions at L3+)
**Finance coverage:** 5/20 questions post-upgrade (SHAP loan denial, ECOA compliance, fraud detection, class imbalance)

---

## Aggregate Distribution

| Quiz | L1 | L2 | L3 | L4 | L5 | Total | L3+ | L3+% | Finance |
|------|----|----|----|----|----|----|-----|------|---------|
| L01 Linear Regression | 9 | 8 | 0 | 2 | 1 | 20 | 3 | 15% | 1/20 |
| L02 Logistic Regression | 7 | 3 | 7 | 2 | 1 | 20 | 10 | 50% | 1/20 |
| L03 KNN (standalone) | 1 | 7 | 3 | 7 | 2 | 20 | 12 | 60% | 2/20 |
| L03 K-Means (standalone) | 0 | 6 | 2 | 11 | 1 | 20 | 14 | 70% | 1/20 |
| L03 KNN+K-Means (combined) | 9 | 7 | 4 | 0 | 0 | 20 | 4 | 20% | 2/20 |
| L03 KNN+K-Means (accessible) | 3 | 8 | 5 | 3 | 1 | 20 | 9 | 45% | 4/20 |
| **L04 Random Forests (post-upgrade)** | **4** | **8** | **2** | **4** | **2** | **20** | **8** | **40%** | **5/20** |
| L05 PCA & t-SNE | 9 | 6 | 2 | 3 | 0 | 20 | 5 | 25% | 1/20 |
| L06 Embeddings & RL | 8 | 8 | 3 | 0 | 1 | 20 | 4 | 20% | 1/20 |
| **TOTAL** | **50** | **61** | **28** | **32** | **9** | **180** | **69** | **38.3%** | **18/180** |

## Systemic Findings

1. **Massive quality gap between standalone and combined L03 quizzes.** Standalone KNN/K-Means are 60-70% L3+; combined is only 20% L3+ with zero Analyze/Evaluate.

2. **Finance application severely underrepresented.** Only 18/180 questions (10%) have finance context. For an MSc Data Science course with finance/banking focus, target should be 20%+ per quiz.

3. **L1 Remember dominates most quizzes.** 5 of 9 quizzes have L1 as the largest or tied-largest category. Overall 27% at L1 is too high for MSc (target: 10-15%).

4. **L5 Evaluate is nearly absent.** Only 9/180 questions (5%) reach L5. Four quizzes have zero or one Evaluate question.

5. **L3 Apply concentrates in L02.** L02 has 6 calculation questions; L01 has zero despite being the most computation-friendly topic.

6. **RL section of L06 is pure recall.** Q11-16 are all "What is X?" at L1.

7. **L05 has zero Evaluate questions** despite PCA/t-SNE offering natural comparison scenarios.

## Recommendations (for future work, no execution now)

### Priority 1 -- Critical
1. Add finance scenario questions to every quiz (target: 4/20 minimum)
2. Add calculation questions to L01 (currently zero Apply-level)
3. Upgrade L03 KNN+K-Means combined quiz or retire it in favor of accessible version
4. Add Evaluate questions to L05 and L06

### Priority 2 -- Important
5. Reduce L1 recall in L05 PCA & t-SNE (currently 45% at L1)
6. Add L3 Apply to L06 RL section (replace Q11-16 recall block)
7. Standardize quiz difficulty across L03 variants

### Priority 3 -- Desirable
8. Add "diagnose the failure" questions to each quiz (L4-L5)
9. Add cross-topic integration questions
10. Consider retiring `L03_knn_kmeans.html` in favor of `L03_knn_kmeans_accessible.html`
