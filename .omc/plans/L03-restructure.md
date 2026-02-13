# L03 KNN & K-Means: Three-Zone Restructure Plan

## Context

### Original Request
Restructure L03 KNN & K-Means slides (overview + deepdive) using the slide creation skill v3 three-zone architecture with XKCD comics at opening and closing.

### Current State
- **L03_overview.tex**: 14 slides, 243 lines. No XKCD comics, LOs at wrong position (slide 2), all 7 charts dual-assigned with deepdive. Missing intro zone, closing comic.
- **L03_deepdive.tex**: 35 slides, 825 lines. No XKCD comics, no \appendix section, LOs at wrong position (slide 2). Good MSc content (Cover & Hart, bias-variance, convergence proof, Gap statistic, Hopkins, EM connection, DBSCAN/hierarchical).
- **Preamble**: Lines 1-92 identical in both files. MUST preserve byte-for-byte.

### Decisions Made
- **Chart allocation** (no dual-assignment): Overview gets 01_knn_boundaries, 03_kmeans_iteration, 04_elbow_method, 07_decision_flowchart. Deepdive gets 02_distance_metrics, 05_silhouette, 06_voronoi.
- **XKCD Opening**: #1838 "Machine Learning" (images/1838_machine_learning.png)
- **XKCD Closing**: #2731 "K-Means Clustering" (images/2731_kmeans_clustering.png)
- **Pattern source**: L02 overview (24 slides, 3 zones) and L02 deepdive (41 main + 8 appendix = 49 slides)

### Key Pattern Rules (from L01/L02)
1. Lines 1-92: Identical preamble -- DO NOT TOUCH
2. Add `\institute{MSc Data Science}` to title block
3. Zone comments: `% ZONE 1: INTRODUCTION (NO formulas, NO Greek letters)`, `% ZONE 2: CORE CONTENT (PMSP)`, `% ZONE 3: WRAP-UP`
4. Every slide gets a numbered comment header: `% SLIDE N: Title`
5. Every content slide gets `\bottomnote{...}`
6. XKCD opening at slide 3 (both files), closing before References
7. LOs placed AFTER intro section (slide 7 in overview, slide 4 in deepdive)
8. Charts: `\includegraphics[width=0.55\textwidth]` (with text) or `width=0.65\textwidth` (chart-only)
9. Deepdive gets `\appendix` + `\section*{Advanced Topics}` before appendix slides
10. Closing XKCD is a textual callback (quote + witty remark), NOT the image again

---

## Work Objectives

### Core Objective
Rewrite both L03 .tex files to match the L02 three-zone pattern exactly, producing a 24-slide overview and ~42 main + ~8 appendix = ~50 slide deepdive.

### Deliverables
1. `L03_overview.tex` rewritten: 24 slides, 3 zones, 4 charts, XKCD open/close
2. `L03_deepdive.tex` rewritten: ~42 main + ~8 appendix slides, 3 charts, XKCD open/close, \appendix section, KNN pseudocode with tie-breaking + K-Means pseudocode with empty cluster handling
3. Both PDFs compiled with 0 errors and 0 Overfull warnings
4. Architect verification passed

### Definition of Done
- Preamble lines 1-92 byte-for-byte identical to current
- All slide numbering comments present and sequential
- Every content slide has \bottomnote{}
- Chart allocation: 4 to overview, 3 to deepdive, zero overlap
- XKCD #1838 at slide 3 (both files), XKCD #2731 callback at closing
- LOs at correct position (after intro, not slide 2)
- \institute{MSc Data Science} in title block
- Zone comments present
- 0 LaTeX compilation errors
- 0 Overfull \hbox warnings
- Max 3-4 bullets per slide

---

## Must Have / Must NOT Have

### MUST Have
- Three-zone architecture (Intro / Core PMSP / Wrap-up)
- XKCD #1838 opening comic (slide 3, both files)
- XKCD #2731 closing callback (textual, both files)
- \institute{MSc Data Science} in title block
- \bottomnote{} on every content slide
- Slide number comments (% SLIDE N: Title)
- Zone boundary comments
- \appendix + \section*{Advanced Topics} in deepdive
- All existing MSc-level content preserved (Cover & Hart, bias-variance, convergence proof, Gap statistic, Hopkins, EM, DBSCAN)
- KNN pseudocode with tie-breaking (algorithmic environment, per instructor guide)
- K-Means pseudocode with empty cluster handling (algorithmic environment, per instructor guide)
- Bloom's Level 4-5 LOs

### MUST NOT Have
- Any modification to preamble (lines 1-92)
- Dual-assigned charts (each chart in exactly ONE file)
- LOs at slide 2 (must be after intro section)
- Subplots or multi-figure slides
- More than 4 bullets per slide
- Any slide without \bottomnote{}
- XKCD image reused at closing (use text callback only)

---

## Task Flow

```
Task 1 (Rewrite L03_overview.tex)
    |
    v
Task 2 (Rewrite L03_deepdive.tex)  [can run in PARALLEL with Task 1]
    |
    v
Task 3 (Compile both PDFs)  [depends on Tasks 1+2]
    |
    v
Task 4 (Architect verify)  [depends on Task 3]
```

---

## Task 1: Rewrite L03_overview.tex

**Target: 24 slides, 3 zones, 4 charts**

### Preamble (lines 1-92): PRESERVE UNCHANGED

### Title Block (line 93-97): Minor update
```latex
\title[L03: KNN \& K-Means]{L03: K-Nearest Neighbors \& K-Means}
\subtitle{Classification and Clustering with Distance}
\author{Methods and Algorithms}
\institute{MSc Data Science}       % <-- ADD THIS LINE
\date{Spring 2026}
```

### ZONE 1: INTRODUCTION (Slides 1-7, NO formulas, NO Greek letters)

**SLIDE 1: Title Page**
- \titlepage (standard)

**SLIDE 2: Outline**
- \tableofcontents (standard)

**SLIDE 3: Opening Comic -- XKCD #1838**
- Frame title: "The Machine Learning Approach"
- `\includegraphics[height=0.70\textheight]{images/1838_machine_learning.png}`
- \bottomnote{XKCD \#1838 by Randall Munroe (CC BY-NC 2.5)}

**SLIDE 4: Classification vs Clustering**
- Two distinct business problems explained in plain language
- Classification: "Given labeled examples, which category does this new case belong to?"
- Clustering: "No labels -- what natural groups exist in our data?"
- Use concrete banking examples (fraud classification, customer segmentation)
- \bottomnote about supervised vs unsupervised distinction

**SLIDE 5: The Nearest Neighbor Idea**
- Human intuition: "You judge new situations by finding the most similar past experience"
- KNN does exactly this with data -- find the K most similar cases and vote
- No training phase needed -- the data IS the model
- Relatable example: appraising a house by looking at similar nearby houses
- \bottomnote about instance-based learning

**SLIDE 6: Why Banks Segment Customers**
- Banks have millions of customers with diverse needs
- One-size-fits-all marketing wastes money; segmentation enables targeted campaigns
- RFM idea in plain language: how recently, how often, how much?
- K-Means discovers these segments automatically from transaction data
- \bottomnote about customer analytics in banking

**SLIDE 7: Learning Objectives**
- 4 LOs at Bloom's Level 4-5:
  1. Analyze the bias-variance tradeoff in KNN as a function of K
  2. Evaluate K-Means initialization strategies and convergence properties
  3. Compare distance metrics and their impact on algorithm behavior
  4. Apply KNN and K-Means to finance use cases (fraud detection, customer segmentation)
- Finance Applications line
- \bottomnote{Bloom's Level 4--5: Analyze, Evaluate, Compare, Apply}

### ZONE 2: CORE CONTENT -- PMSP (Slides 8-21)

**\section{Problem}**

**SLIDE 8: The Business Problem**
- Two distinct problems formalized:
  - Classification (supervised): given labeled data, predict category for new observation
  - Clustering (unsupervised): discover natural groupings without labels
- Both rely on the concept of "distance" between data points
- \bottomnote{KNN = supervised classification, K-Means = unsupervised clustering}

**SLIDE 9: KNN Decision Boundaries (CHART: 01_knn_boundaries)**
- Use columns layout: text left (0.42), chart right (0.55)
- Explain how K affects boundary complexity
- Small K: complex, jagged boundary (overfitting risk)
- Large K: smooth boundary (underfitting risk)
- `\includegraphics[width=\textwidth]{01_knn_boundaries/chart.pdf}`
- \bottomnote{KNN creates non-linear, locally adaptive decision boundaries}

**\section{Method}**

**SLIDE 10: Distance: How to Measure Similarity**
- Euclidean distance formula: $d(\mathbf{x}, \mathbf{x}') = \sqrt{\sum_{j=1}^p (x_j - x'_j)^2}$
- Manhattan distance mention (L1): sum of absolute differences
- Key insight: choice of metric changes which points are "nearest"
- Feature scaling is critical (income in thousands vs age in years)
- \bottomnote{Always scale features for distance-based methods}

**SLIDE 11: KNN Classification**
- The algorithm in 3 steps: store data, find K nearest, majority vote
- Formal: $\hat{y} = \text{mode}\{y_i : \mathbf{x}_i \in N_K(\mathbf{x})\}$
- Choosing K: start with $K = \sqrt{n}$, use odd K for binary, cross-validate
- Bias-variance: K=1 high variance, K=n high bias
- \bottomnote{KNN: no training cost, but prediction requires scanning all data}

**SLIDE 12: K-Means: The Objective**
- Goal: partition n points into K clusters to minimize WCSS
- WCSS formula: $J = \sum_{k=1}^{K}\sum_{\mathbf{x}_i \in C_k} \|\mathbf{x}_i - \boldsymbol{\mu}_k\|^2$
- Each point assigned to nearest centroid; centroids are cluster means
- Finding optimal solution is NP-hard; Lloyd's algorithm finds local optimum
- \bottomnote{K-Means minimizes within-cluster variance -- a form of compression}

**SLIDE 13: K-Means: The Algorithm**
- Pseudocode-style description (itemized, not algorithmic environment):
  1. Initialize K centroids (randomly or K-Means++)
  2. Assign each point to nearest centroid
  3. Recompute centroids as cluster means
  4. Repeat until convergence
- Convergence guaranteed: WCSS decreases each step, finite partitions
- \bottomnote{Each iteration: $O(nKd)$ -- linear in samples, clusters, and features}

**SLIDE 14: K-Means Iteration (CHART: 03_kmeans_iteration)**
- Full-width chart: `\includegraphics[width=0.65\textwidth]{03_kmeans_iteration/chart.pdf}`
- \bottomnote{Iteratively assign points and update centroids until convergence}

**SLIDE 15: Choosing K: Elbow Method (CHART: 04_elbow_method)**
- Full-width chart: `\includegraphics[width=0.65\textwidth]{04_elbow_method/chart.pdf}`
- Brief text above or below: "Plot WCSS vs K; look for the elbow where adding clusters gives diminishing returns"
- \bottomnote{The elbow is subjective -- Gap statistic provides a formal alternative (deep dive)}

**SLIDE 16: K-Means++: Smart Initialization**
- Problem: random init is sensitive to starting points
- K-Means++ solution: spread initial centroids apart
  - First centroid: random
  - Each subsequent: probability proportional to squared distance from nearest existing centroid
- Result: $O(\log k)$-competitive approximation guarantee
- Default in scikit-learn
- \bottomnote{Arthur \& Vassilvitskii (2007): K-Means++ expected cost $\leq 8(\ln k + 2) \times$ optimal}

**\section{Solution}**

**SLIDE 17: KNN vs K-Means Comparison**
- Side-by-side table (tabular with booktabs):
  | Aspect | KNN | K-Means |
  | Task | Classification | Clustering |
  | Learning | Supervised | Unsupervised |
  | K means | Neighbors | Clusters |
  | Training | None (lazy) | Iterative |
  | Output | Class label | Cluster ID |
- \bottomnote{The ``K'' in KNN and K-Means mean completely different things!}

**SLIDE 18: Finance Application: Customer Segmentation**
- RFM Analysis (Recency, Frequency, Monetary)
- K-Means on standardized RFM features (K=4-6 typical)
- Profile segments: "Champions" (high R,F,M), "At Risk" (low R), "New" (high R, low F)
- Business value: targeted retention, CLV prediction per segment
- \bottomnote{RFM segmentation is foundational for CRM and marketing analytics in banking}

**SLIDE 19: Finance Application: Fraud Detection with KNN**
- Class imbalance problem: fraud < 1% of transactions
- Naive majority vote: 99% accuracy but catches zero fraud
- Solutions: weighted KNN, SMOTE, anomaly score (distance to K-th neighbor)
- Always use Precision-Recall AUC, not accuracy
- \bottomnote{Always check class distribution before applying majority vote!}

**SLIDE 20: Decision Framework (CHART: 07_decision_flowchart)**
- Use columns layout: text left (0.42), chart right (0.55)
- Left: "Best When" for KNN (labeled data, local patterns, moderate size) and K-Means (no labels, natural groupings, spherical clusters)
- `\includegraphics[width=\textwidth]{07_decision_flowchart/chart.pdf}`
- \bottomnote{Start with KNN for classification, K-Means for clustering}

**\section{Practice}**

**SLIDE 21: Hands-on Exercise**
- Open the Colab Notebook
- Exercise 1: Implement KNN classifier, vary K, observe boundary changes
- Exercise 2: Apply K-Means to customer segmentation data, profile clusters
- Exercise 3: Compare elbow and silhouette methods for K selection
- Link: See course materials on GitHub
- \bottomnote{Estimated time: 45--60 minutes for all three exercises}

### ZONE 3: WRAP-UP (Slides 22-24)

**\section{Summary}**

**SLIDE 22: Key Takeaways**
- KNN: instance-based, lazy learner; scale features; choose K via CV; works best moderate dimensionality
- K-Means: iterative assign+update; K-Means++ init; elbow/silhouette for K; assumes spherical clusters
- Both: feature scaling critical; "K" means different things
- \bottomnote{Both are foundational: simple, interpretable, widely used in finance}

**SLIDE 23: Closing Comic -- XKCD #2731 Callback**
- Frame title: "Until Next Time..."
- Center text: italic quote referencing XKCD #2731 K-Means clustering comic
- Something like: *"Turns out the real clusters were the friends we segmented along the way."*
- Then: "Now you can classify with neighbors and cluster with centroids."
- Next Session: L04 -- Random Forests (from distance-based to tree-based methods)
- \bottomnote{XKCD \#2731 callback -- even K-Means can find structure in noise (if you let it)}

**SLIDE 24: References**
- \footnotesize
- James et al. (2021). ISLR, Chapters 2, 12. URL
- Hastie et al. (2009). ESL, Chapters 13, 14. URL
- Arthur & Vassilvitskii (2007). K-Means++
- Cover & Hart (1967). Nearest Neighbor Pattern Classification
- \bottomnote{Primary textbooks: ISLR Ch.~2, 12}

### Acceptance Criteria -- Task 1
- [ ] Exactly 24 slides
- [ ] Preamble lines 1-92 unchanged
- [ ] \institute{MSc Data Science} present
- [ ] Zone comments present (3 zones)
- [ ] XKCD #1838 at slide 3
- [ ] XKCD #2731 callback at slide 23
- [ ] LOs at slide 7 (after intro section)
- [ ] 4 charts used: 01, 03, 04, 07
- [ ] No charts from deepdive set (02, 05, 06)
- [ ] Every content slide has \bottomnote{}
- [ ] Every slide has numbered comment header
- [ ] Max 3-4 bullets per itemize
- [ ] No formulas in Zone 1 (slides 1-7)
- [ ] Bloom's Level 4-5 in LOs

---

## Task 2: Rewrite L03_deepdive.tex

**Target: ~41 main slides + ~8 appendix slides = ~49 total, 3 charts**

### Preamble (lines 1-92): PRESERVE UNCHANGED

### Title Block (line 93-97): Update
```latex
\title[L03: KNN \& K-Means Deep Dive]{L03: KNN \& K-Means}
\subtitle{Deep Dive: Mathematical Foundations and Implementation}
\author{Methods and Algorithms}
\institute{MSc Data Science}       % <-- ADD THIS LINE
\date{Spring 2026}
```

### Main Slides (1-41)

**SLIDE 1: Title Page**
- \titlepage

**SLIDE 2: Outline**
- \tableofcontents

**SLIDE 3: Opening Comic -- XKCD #1838**
- Frame title: "The ML Pipeline"
- `\includegraphics[height=0.65\textheight]{images/1838_machine_learning.png}`
- Slight vertical compression (height=0.65 not 0.70, following L02 deepdive pattern)
- \bottomnote{XKCD \#1838 by Randall Munroe (CC BY-NC 2.5) -- ``Pour the training data into this pile...''}

**SLIDE 4: Learning Objectives**
- 4 LOs at Bloom's Level 4-5:
  1. Analyze the bias-variance tradeoff in KNN and derive its asymptotic error bounds
  2. Evaluate clustering validity using statistical tests (Hopkins, Gap statistic, silhouette)
  3. Prove K-Means convergence and analyze computational complexity
  4. Compare distance metrics and assess their suitability for high-dimensional finance data
- Finance Applications: Customer segmentation, fraud detection
- \bottomnote{Bloom's Level 4--5: Analyze, Evaluate, Prove, Compare}

#### Section 1: KNN Foundations (~8 slides)

**\section{KNN Foundations}**

**SLIDE 5: KNN: The Lazy Learner**
- Key insight: no explicit model training (store all data)
- Classification by majority vote of K nearest neighbors
- "Lazy" because work is done at prediction time
- The algorithm: 1) Store, 2) Find K nearest, 3) Vote
- \bottomnote{Instance-based learning: the training data IS the model}

**SLIDE 6: KNN Algorithm (Pseudocode)**
- Use `algorithmic` environment (formal pseudocode)
- Input: training set, query point x, K
- Compute distances from x to all training points
- Select K nearest neighbors
- **Tie-breaking**: if vote is tied, use distance-weighted vote among tied classes; if still tied, choose class with nearest single neighbor
- Return majority class (with tie-breaking)
- \bottomnote{Tie-breaking is critical: without it, KNN is non-deterministic on decision boundaries}

**SLIDE 7: Distance Metrics Visualization (CHART: 02_distance_metrics)**
- `\includegraphics[width=0.55\textwidth]{02_distance_metrics/chart.pdf}`
- Brief text: common metrics -- Euclidean, Manhattan
- \bottomnote{Choice of distance metric determines which points are considered ``nearest''}

**SLIDE 8: Distance Metrics: Minkowski Family**
- Minkowski formula: $d_p(\mathbf{x}, \mathbf{y}) = \left(\sum_{i=1}^{n}|x_i - y_i|^p\right)^{1/p}$
- p=1: Manhattan, p=2: Euclidean, p=inf: Chebyshev
- Note: p < 1 violates triangle inequality
- Choosing p: p=2 default, p=1 robust to outliers
- \bottomnote{In high dimensions, all distances become similar (curse of dimensionality)}

**SLIDE 9: Beyond Minkowski: Cosine and Mahalanobis**
- Cosine similarity formula (critical for text/embeddings)
- Mahalanobis distance formula (accounts for correlation)
- Use cases: cosine for sparse/text, Mahalanobis for correlated features
- \bottomnote{Choose metric based on data type: Euclidean for dense, Cosine for sparse/text}

**SLIDE 10: Choosing K: Bias-Variance Tradeoff**
- K=1: high variance, low bias; K=n: high bias, low variance
- Guidelines: K = sqrt(n), odd K for binary, cross-validate
- Common choices: K in {3, 5, 7, 11}
- \bottomnote{Small K for complex patterns, larger K for noisy data}

**SLIDE 11: Weighted KNN**
- Problem with equal voting: distant neighbor same weight as closest
- Inverse-distance weighting formula: $w_i = 1/d(\mathbf{x}, \mathbf{x}_i)$
- Reduces sensitivity to K choice
- scikit-learn: weights='uniform' vs weights='distance'
- \bottomnote{Distance weighting often improves performance, especially for larger K}

**SLIDE 12: K Selection via Cross-Validation**
- GridSearchCV code walkthrough
- Validation curve: plot accuracy vs K for train/val
- Choose K where validation accuracy peaks
- \bottomnote{Cross-validation provides objective, data-driven K selection}

#### Section 2: KNN Theory (~5 slides)

**\section{KNN Theory}**

**SLIDE 13: Feature Scaling for KNN**
- Why scaling matters: income (20k-200k) vs age (20-80) example
- Standardization: z = (x - mu) / sigma
- Min-Max: x' = (x - min) / (max - min)
- Edge cases: constant features
- Rule: ALWAYS scale for distance-based methods
- \bottomnote{StandardScaler for Gaussian-like, MinMaxScaler for bounded features}

**SLIDE 14: Curse of Dimensionality**
- All points become approximately equidistant (Beyer et al., 1999)
- "Nearest neighbor" becomes meaningless in high d
- Solutions: PCA, feature selection, domain knowledge
- \bottomnote{KNN works best with moderate features (typically $d < 15$--$20$, problem-dependent)}

**SLIDE 15: Cover and Hart (1967) Consistency Theorem**
- As n -> inf: 1-NN error <= 2 x Bayes error
- KNN universally consistent: converges to optimal
- Requires: K -> inf but K/n -> 0
- VC dimension: 1-NN has infinite VC dimension
- Practical implication: need LARGE datasets
- \bottomnote{The $2\times$ Bayes error bound makes KNN a strong nonparametric baseline}

**SLIDE 16: Cover and Hart: Proof Sketch**
- Theorem statement
- 1-NN case binary proof: nearest neighbor converges to query as n -> inf
- Error bound derivation: $R_{1\text{-NN}}(\mathbf{x}) = 2\eta(\mathbf{x})(1 - \eta(\mathbf{x}))$
- Final bound: $R^* \leq R_{1\text{-NN}} \leq 2R^*(1 - R^*)$
- \bottomnote{For $K$-NN with $K/n \to 0$: $R_{K\text{-NN}} \to R^*$ exactly.}

**SLIDE 17: Bias-Variance Decomposition for KNN**
- MSE decomposition: Bias^2 + Variance + irreducible noise
- Variance: sigma^2 / K (averaging K neighbors)
- Bias: increases with K (farther neighbors)
- At K=1: zero bias, variance = sigma^2
- At K=n: high bias, variance = sigma^2/n
- \bottomnote{Optimal K balances bias and variance; found via cross-validation}

#### Section 3: K-Means Algorithm (~7 slides)

**\section{K-Means Algorithm}**

**SLIDE 18: K-Means: The Idea**
- Goal: partition n points into K clusters
- WCSS objective formula
- Key insight: assign to nearest centroid, centroids are means, iterate
- K-Means finds locally optimal solution (NP-hard to find global)
- \bottomnote{K-Means minimizes within-cluster sum of squares -- a compression objective}

**SLIDE 19: K-Means Algorithm (Pseudocode)**
- Use algorithmic environment (algorithm + algorithmic packages)
- Input: Data X, number of clusters K
- Initialize, Repeat: Assign + Update + Handle empty, Until convergence
- Convergence: guaranteed (WCSS decreases), but local optimum
- \bottomnote{Each iteration: $O(nKd)$ where $n$ = samples, $K$ = clusters, $d$ = features}

**SLIDE 20: K-Means++: Smart Initialization**
- Random init problem: sensitive to starting points
- K-Means++ algorithm: first random, then probability proportional to d^2
- Approximation guarantee: O(log k)-competitive
- Default in scikit-learn
- \bottomnote{Arthur \& Vassilvitskii (2007): expected cost $\leq 8(\ln k + 2) \times$ optimal}

**SLIDE 21: Silhouette Score: Cluster Quality**
- Define a(i): mean intra-cluster distance
- Define b(i): mean nearest-cluster distance
- Silhouette formula: s(i) = (b(i) - a(i)) / max(a(i), b(i))
- Interpretation: s near 1 = well-matched, s near 0 = boundary, s < 0 = misassigned
- Singleton convention: s(i) = 0
- \bottomnote{Average silhouette score summarizes overall clustering quality}

**SLIDE 22: Silhouette Plot (CHART: 05_silhouette)**
- `\includegraphics[width=0.55\textwidth]{05_silhouette/chart.pdf}`
- Brief interpretation: all clusters should have similar width and scores above average
- \bottomnote{Look for clusters with consistent silhouette widths and scores above the mean}

**SLIDE 23: K-Means Decision Regions (CHART: 06_voronoi)**
- `\includegraphics[width=0.55\textwidth]{06_voronoi/chart.pdf}`
- Brief text: Voronoi tessellation -- each region contains all points closest to one centroid
- \bottomnote{K-Means creates Voronoi tessellation of the feature space}

**SLIDE 24: K-Means Assumptions and Limitations**
- Assumes: spherical clusters, similar sizes, similar densities
- Fails on: non-convex shapes, very different sizes, different densities, outliers
- \bottomnote{Consider DBSCAN or Gaussian Mixture Models when these assumptions are violated}

#### Section 4: K-Means Theory (~4 slides)

**\section{K-Means Theory}**

**SLIDE 25: K-Means Convergence Proof**
- Theorem: Lloyd's algorithm converges in finite iterations
- Proof via coordinate descent: Assignment step minimizes J over C (fix mu), Update step minimizes J over mu (fix C)
- J >= 0, strictly decreasing, finitely many partitions => convergence QED
- NP-hardness note: Aloise et al., 2009
- \bottomnote{Coordinate descent on bounded objective: alternating optimization of $C$ and $\boldsymbol{\mu}$}

**SLIDE 26: K-Means as EM Special Case**
- K-Means = "Hard EM" for Gaussian Mixture Models
- Assumes: spherical Gaussians with equal variance
- E-step: hard assignment to nearest centroid
- M-step: update centroids as means
- Opens door to soft clustering via GMM
- \bottomnote{Understanding the EM connection deepens theoretical understanding of K-Means}

**SLIDE 27: K-Means Variants**
- Mini-Batch K-Means: random subsets, faster, slightly worse
- K-Medoids: centroids must be data points, more robust to outliers
- K-Modes / K-Prototypes: categorical / mixed data
- \bottomnote{Mini-Batch K-Means: recommended for datasets $> 10{,}000$ samples}

**SLIDE 28: Computational Considerations**
- KNN: O(1) training, O(nd) prediction brute force
- KD-Tree: O(d log n) avg for d < 15
- Ball Tree: better in higher dimensions
- Mini-Batch K-Means for large datasets
- scikit-learn: algorithm='auto'
- \bottomnote{For large datasets: approximate nearest neighbor methods trade accuracy for speed}

#### Section 5: Cluster Validation (~3 slides)

**\section{Cluster Validation}**

**SLIDE 29: Should We Cluster? Hopkins Statistic**
- Test for cluster tendency BEFORE clustering
- Hopkins formula: H = sum(u_i) / (sum(u_i) + sum(w_i))
- H near 0.5: uniform (no clusters), H > 0.75: significant clustering
- Use case: verify data has structure before running K-Means
- \bottomnote{Don't cluster uniform data -- Hopkins test catches this}

**SLIDE 30: Gap Statistic for K Selection**
- Problem with elbow: subjective, no formal test
- Gap statistic formula: Gap_n(k) = E*[log W_k] - log W_k
- Choose smallest K where Gap(k) >= Gap(k+1) - s_{k+1}
- Reference distribution via bootstrap
- \bottomnote{Gap statistic provides statistical justification for K selection (Tibshirani et al., 2001)}

**SLIDE 31: Comparison of K Selection Methods**
- Table comparing: Elbow (visual/subjective, fast, no formal test), Silhouette (per-point quality, moderate speed, interpretable), Gap (formal test, slow, gold standard)
- Practical recommendation: use elbow for quick exploration, Gap for formal justification
- \bottomnote{Use multiple methods together -- they complement each other}

#### Section 6: Comparison and Finance Applications (~5 slides)

**\section{Comparison and Applications}**

**SLIDE 32: KNN vs K-Means: Key Differences**
- Detailed comparison table (expand from overview): Task, Learning type, K meaning, Training, Prediction, Output, Complexity, When to use
- \bottomnote{Despite sharing the letter K, these algorithms solve fundamentally different problems}

**SLIDE 33: Finance Application: RFM Customer Segmentation**
- RFM: Recency, Frequency, Monetary (industry standard)
- Pipeline: standardize RFM -> K-Means (K=4-6) -> profile segments
- Segment profiles: Champions, Loyal, At Risk, Hibernating
- Business value: CLV prediction, targeted retention
- \bottomnote{RFM segmentation is foundational for CRM and marketing analytics}

**SLIDE 34: Finance Application: Fraud Detection**
- Class imbalance: fraud < 1%, naive KNN predicts all non-fraud
- Solutions: SMOTE, weighted KNN, cost-sensitive learning, anomaly score
- Use Precision-Recall AUC, NOT accuracy
- \bottomnote{Always check class distribution before applying majority vote!}

**SLIDE 35: Alternative Clustering: DBSCAN and Hierarchical**
- DBSCAN: core/border/noise points, non-spherical clusters, no K required
- Hierarchical: bottom-up merging, dendrogram, cut at desired height
- Linkage criteria: single, complete, Ward
- \bottomnote{DBSCAN for irregular shapes, hierarchical for exploring multiple K values}

**SLIDE 36: When to Use What**
- KNN when: labeled data, local patterns, interpretability, moderate size
- K-Means when: no labels, natural groupings, spherical, fast needed
- Alternatives: Random Forest (many features), GMM (soft clusters), DBSCAN (non-spherical)
- \bottomnote{K-Means often used as preprocessing before supervised learning}

#### Section 7: Implementation (~3 slides)

**\section{Implementation}**

**SLIDE 37: KNN in scikit-learn**
- Code walkthrough: KNeighborsClassifier
- Key parameters: n_neighbors, weights, metric, algorithm
- Also: KNeighborsRegressor
- \bottomnote{Use \texttt{weights='distance'} as default -- usually outperforms uniform voting}

**SLIDE 38: K-Means in scikit-learn**
- Code walkthrough: KMeans
- Key parameters: n_clusters, init, n_init, max_iter
- Accessing results: labels_, cluster_centers_, inertia_
- \bottomnote{\texttt{inertia\_} gives WCSS -- use for elbow plot}

**SLIDE 39: Pipeline: Scaling + Algorithm**
- Show Pipeline combining StandardScaler + KNN/KMeans
- Emphasis: never fit scaler on test data
- Best practice: GridSearchCV over pipeline
- \bottomnote{Always pipeline preprocessing with model to prevent data leakage}

#### Section 8: Practice + Summary (~3 slides)

**\section{Practice}**

**SLIDE 40: Hands-On Exercise**
- Exercise 1: Implement weighted KNN with distance weighting
- Exercise 2: Compare Gap statistic vs Elbow for K selection
- Exercise 3: Apply SMOTE for imbalanced fraud detection
- Link: See course materials for Colab notebook
- \bottomnote{Exercises reinforce mathematical concepts with real finance data}

**\section{Summary}**

**SLIDE 41: Key Takeaways**
- KNN: instance-based, scale features, CV for K, Cover & Hart consistency
- K-Means: WCSS objective, K-Means++ init, convergence guaranteed (local), validate with silhouette/Gap
- Both: feature scaling critical, curse of dimensionality limits high-d
- Finance: RFM segmentation, fraud detection with class imbalance handling
- \bottomnote{KNN and K-Means are foundational: simple, interpretable, and widely deployed}

**SLIDE 42: Closing Comic -- XKCD #2731 Callback**
- Frame title: "Until Next Time..."
- Center text: italic quote referencing XKCD #2731 K-Means clustering
- E.g., *"Even K-Means would struggle to cluster the ways students misuse K-Means."*
- Then: "With KNN and K-Means, you can now classify the known and discover the unknown."
- Next Session: L04 -- Random Forests (from distance-based to tree-based methods)
- \bottomnote{XKCD \#2731 callback -- clustering is easy, knowing when to cluster is the hard part}

### APPENDIX (Slides 43-50)

**\appendix**
**\section*{Advanced Topics}**

**APPENDIX SLIDE 1: Section Divider**
- Centered beamercolorbox: "Appendix: Advanced Topics and Proofs"
- Subtitle: "These slides are supplementary material for self-study"
- (Follow exact L02 deepdive pattern)

**APPENDIX SLIDE 2: Distance Metric Properties -- Triangle Inequality**
- Triangle inequality: d(x,z) <= d(x,y) + d(y,z)
- Proof sketch for Euclidean via Cauchy-Schwarz
- Why it matters: enables efficient search (KD-tree pruning)
- Note: p < 1 Minkowski violates this
- \bottomnote{Triangle inequality is what makes tree-based nearest neighbor search possible}

**APPENDIX SLIDE 3: K-Means Convergence -- Formal Proof**
- Full formal proof with explicit steps
- Define J(C, mu) as the objective
- Show each step is a block coordinate descent
- Prove strict decrease unless at fixed point
- Finite partition bound
- \bottomnote{Lloyd's algorithm is monotonically convergent but may require exponential iterations in worst case}

**APPENDIX SLIDE 4: Empty Cluster Handling**
- What happens when a cluster gets zero members during iteration
- Strategies: reinitialize from farthest point, split largest cluster, random restart
- scikit-learn behavior: reinitializes from farthest point
- Impact on convergence guarantees
- \bottomnote{Empty clusters are rare with K-Means++ but must be handled for correctness}

**APPENDIX SLIDE 5: Cover and Hart -- Full Proof**
- More detailed proof of the 1-NN consistency theorem
- Conditional risk calculation at point x
- Integration over feature space
- Extension to K-NN with K -> inf, K/n -> 0
- \bottomnote{Stone (1977) generalized this to the universal consistency of K-NN estimators}

**APPENDIX SLIDE 6: KNN Computational Complexity Analysis**
- Brute force: O(nd) per query
- KD-Tree: O(d log n) average, O(dn) worst case
- Ball Tree: O(d log n) but better constants in high d
- Locality-Sensitive Hashing (LSH): approximate O(d) with tunable accuracy
- \bottomnote{For $n > 10^6$: approximate methods (LSH, FAISS) become necessary}

**APPENDIX SLIDE 7: Gap Statistic Implementation Details**
- Reference distribution generation (uniform over bounding box or PCA-aligned box)
- Bootstrap computation: B = 10-50 reference datasets
- Standard error calculation for the gap
- Full decision rule with simulation correction
- \bottomnote{Tibshirani et al.~(2001): use PCA-aligned reference for non-isotropic data}

**APPENDIX SLIDE 8: References and Resources**
- Two-column layout (following L02 pattern)
- Left column: Textbooks (ISLR Ch 2/12, ESL Ch 13/14, Cover & Hart 1967, Arthur & Vassilvitskii 2007)
- Right column: Online resources (scikit-learn clustering docs, Stanford CS229)
- \bottomnote{Primary textbook: ISLR Chapters 2, 12}

### Acceptance Criteria -- Task 2
- [ ] ~41 main slides (38-43 acceptable range)
- [ ] ~8 appendix slides (6-9 acceptable range)
- [ ] Preamble lines 1-92 unchanged
- [ ] \institute{MSc Data Science} present
- [ ] XKCD #1838 at slide 3
- [ ] XKCD #2731 callback at slide 41 (or last main slide)
- [ ] LOs at slide 4 (after opening comic)
- [ ] 3 charts used: 02, 05, 06
- [ ] No charts from overview set (01, 03, 04, 07)
- [ ] \appendix + \section*{Advanced Topics} present
- [ ] Appendix divider slide present
- [ ] All existing MSc content preserved:
  - [ ] Cover & Hart theorem + proof sketch
  - [ ] Bias-variance decomposition for KNN
  - [ ] K-Means convergence proof
  - [ ] K-Means as EM special case
  - [ ] Hopkins statistic
  - [ ] Gap statistic
  - [ ] DBSCAN and hierarchical clustering
  - [ ] K-Means variants (Mini-Batch, K-Medoids)
  - [ ] Weighted KNN
  - [ ] Feature scaling
  - [ ] Curse of dimensionality
  - [ ] Computational considerations
- [ ] Every content slide has \bottomnote{}
- [ ] Every slide has numbered comment header
- [ ] Max 3-4 bullets per itemize
- [ ] algorithm/algorithmic environment for K-Means pseudocode

---

## Task 3: Compile Both PDFs

**Depends on**: Tasks 1 and 2

### Steps
1. Navigate to `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L03_KNN_KMeans\`
2. Compile overview:
   ```
   pdflatex -interaction=nonstopmode L03_overview.tex
   pdflatex -interaction=nonstopmode L03_overview.tex
   ```
3. Compile deepdive:
   ```
   pdflatex -interaction=nonstopmode L03_deepdive.tex
   pdflatex -interaction=nonstopmode L03_deepdive.tex
   ```
4. Move aux files:
   ```
   mkdir temp 2>nul
   move *.aux *.log *.nav *.out *.snm *.toc temp/
   ```

### Verification
- Check compilation output for "0 errors"
- Grep output for "Overfull": must be 0 occurrences
- Verify PDF page count: overview ~24 pages, deepdive ~49 pages

### Acceptance Criteria -- Task 3
- [ ] L03_overview.pdf exists and is valid
- [ ] L03_deepdive.pdf exists and is valid
- [ ] 0 LaTeX errors in both compilations
- [ ] 0 Overfull \hbox warnings in both compilations
- [ ] Overview PDF: ~24 pages
- [ ] Deepdive PDF: ~49 pages

---

## Task 4: Architect Verification

**Depends on**: Task 3

### 15-Point Checklist

| # | Check | Target |
|---|-------|--------|
| 1 | Preamble integrity | Lines 1-92 byte-identical in both files |
| 2 | \institute line | Present in both files |
| 3 | Zone comments | 3 zones marked in overview; zone-style sections in deepdive |
| 4 | Slide count | Overview: 24; Deepdive: ~41 main + ~8 appendix |
| 5 | XKCD opening | Slide 3 in both files, XKCD #1838, CC BY-NC 2.5 attribution |
| 6 | XKCD closing | Text callback to #2731 in both files (not image reuse) |
| 7 | LO placement | After intro (slide 7 overview, slide 4 deepdive), NOT slide 2 |
| 8 | Chart allocation | Overview: 01,03,04,07; Deepdive: 02,05,06; zero overlap |
| 9 | \bottomnote coverage | Every content slide has one |
| 10 | Slide numbering comments | Sequential % SLIDE N: headers throughout |
| 11 | Bullet discipline | Max 3-4 per itemize/enumerate |
| 12 | \appendix section | Present in deepdive with \section*{Advanced Topics} |
| 13 | Content preservation | All MSc topics from current deepdive preserved |
| 14 | Compilation | 0 errors, 0 Overfull warnings |
| 15 | Bloom's LOs | Level 4-5 verbs in both files |

### Acceptance Criteria -- Task 4
- [ ] All 15 checks pass
- [ ] Written verification report

---

## Commit Strategy

### Single Commit After All Tasks Pass
```
Restructure L03 KNN & K-Means slides with three-zone architecture

- Rewrite L03_overview.tex: 24 slides, 3 zones, XKCD #1838 open/#2731 close
- Rewrite L03_deepdive.tex: ~41 main + ~8 appendix slides, XKCD open/close
- Fix chart dual-assignment: 4 to overview, 3 to deepdive
- Move LOs after intro section (was slide 2)
- Add \institute{MSc Data Science} to both files
- Add \appendix + \section*{Advanced Topics} to deepdive
- Preserve all MSc-level content (Cover & Hart, convergence, Gap, Hopkins, EM)
```

### Files Changed
- `slides/L03_KNN_KMeans/L03_overview.tex`
- `slides/L03_KNN_KMeans/L03_deepdive.tex`
- `slides/L03_KNN_KMeans/L03_overview.pdf`
- `slides/L03_KNN_KMeans/L03_deepdive.pdf`

---

## Success Criteria

1. Both files follow L02 three-zone pattern exactly
2. Chart allocation is clean (no dual-assignment)
3. XKCD comics at opening and closing in both files
4. All MSc-level mathematical content preserved and properly placed
5. Compilation clean (0 errors, 0 Overfull)
6. Architect verification passes all 15 checks
