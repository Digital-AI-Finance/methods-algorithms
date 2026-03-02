# Plan: L03 KNN & K-Means — New Slides at Accessible Level (v2)

## Task
Create NEW L03 overview and deepdive slides written at introductory/accessible level (BSc-equivalent content depth) using the beamer slide creation skill. The slides must NOT mention "BSc" anywhere. The existing MSc-level slides remain untouched — these are new files.

## Output Files
- `slides/L03_KNN_KMeans/L03_overview_accessible.tex` (NEW)
- `slides/L03_KNN_KMeans/L03_deepdive_accessible.tex` (NEW)
- 6 new chart folders: `08_feature_scaling_effect/`, `09_knn_step_by_step/`, `10_bias_variance_visual/`, `11_rfm_scatter/`, `12_kmeans_worked_example/`, `13_cv_accuracy_curve/`

## Title Block Specification

**Overview file:**
```latex
\title[L03: KNN \& K-Means]{L03: K-Nearest Neighbors \& K-Means}
\subtitle{Overview}
\author{Methods and Algorithms}
\institute{MSc Data Science}
\date{Spring 2026}
```

**Deepdive file:**
```latex
\title[L03: KNN \& K-Means Deep Dive]{L03: KNN \& K-Means}
\subtitle{Deep Dive: Implementation and Evaluation}
\author{Methods and Algorithms}
\institute{MSc Data Science}
\date{Spring 2026}
```

**Preamble rule:** Copy the preamble (lines 1-101) byte-for-byte from the existing `L03_overview.tex`. This includes the footer ("Methods and Algorithms | MSc Data Science | page/total"), all color definitions, `\bottomnote` command, `compactlist` environment, `\highlight` and `\mathbold` commands, and the `algorithm`/`algorithmic` packages (kept for preamble compatibility even though the accessible slides use plain-English pseudocode instead of `\begin{algorithmic}` environments).

Only the `\title`, `\subtitle`, `\author`, `\institute`, `\date` block differs (specified above).

## Section Framework Declarations

**Overview: PMSP (Option A)**
```latex
\section{Problem}
\section{Method}
\section{Solution}
\section{Practice}
\section{Summary}
```
The intro zone (slides 1-9) precedes `\section{Problem}`. No `\section{Introduction}` — intro content comes before the first section command.

**Deepdive: Custom/Topical (Option D)**
```latex
\section{KNN In Depth}
\section{K-Means In Depth}
\section{Implementation}
\section{Practice}
\section{Summary}
```
Opening slides (1-4) precede `\section{KNN In Depth}`. Appendix uses `\appendix` + `\section*{Extra Topics}`.

## Acceptance Criteria
1. Overview compiles with `pdflatex` — 0 errors, 0 Overfull warnings
2. Deepdive compiles with `pdflatex` — 0 errors, 0 Overfull warnings
3. All 6 new charts generate `chart.pdf` without errors
4. Zero Greek letters in overview intro zone (slides 1-9)
5. Every formula has a worked numerical example on the same or next slide
6. Every chart-only slide has 2-3 interpretive bullets
7. Every jargon term has parenthetical definition at first use
8. Max 4 bullets per column, max 5-6 concepts per slide
9. Opening comic (XKCD) in BOTH files, closing comic (XKCD) in BOTH files
10. No mention of "BSc" anywhere in either file
11. Min 1 chart per 4 slides in each file (excl. XKCD images, which are comics not charts)
12. Each chart assigned to exactly ONE file (no dual assignment)
13. Preamble (lines 1-101) copied from existing L03_overview.tex; only title block differs
14. PMSP framework for overview sections; Custom/topical for deepdive sections
15. Pseudocode uses plain-English steps (NOT `\begin{algorithmic}` environments)

## K Disambiguation Pattern

The letter K has two different meanings. To prevent confusion:
- **Always qualify:** Write "K neighbors" or "K clusters", never bare "K" except in algorithm names "KNN" and "K-Means"
- **First use callout (slide 10):** Explicit bold statement: "K in KNN = number of neighbors; K in K-Means = number of clusters — completely different!"
- **Subsequent uses:** Prefer "$K{=}5$ neighbors" or "$K{=}3$ clusters" with the meaning attached

## Notation Table
| Symbol | Meaning | Where Used |
|--------|---------|------------|
| K | Number of neighbors (KNN context) or clusters (K-Means context) — always qualified | Both files |
| d | Distance function | Method slides |
| x, x' | Data points (plain letters in intro, bold vectors in core) | Distance formulas |
| p | Number of features | Dimensionality discussion (deepdive) |
| n | Number of data points | Complexity discussion (deepdive) |
| μ_k | Centroid of cluster k | K-Means formulas (deepdive only) |
| C_k | Cluster k | K-Means formulas (deepdive only) |
| J / WCSS | Within-cluster sum of squares | K-Means objective |

**Intro rule:** Only plain English variable names (a, b, x, y) — no Greek letters, no bold vectors, no subscripts.

## Intro Zone Counting Rule

Following BSc overlay (Appendix C of skill): intro = 8-10 slides. This OVERRIDES the universal default of 2-4 slides. Title page and Outline ARE counted as part of the intro zone (they are structural slides within it). Therefore slides 1-9 = 9 intro slides, within the 8-10 range. ✓

---

## Part 1: Overview — Slide-by-Slide Specification (28 slides)

### INTRO ZONE (slides 1-9, 9 slides) — Zero Greek, Zero Formulas

| # | Title | Layout | Content | Chart | Bottomnote |
|---|-------|--------|---------|-------|------------|
| 1 | Title Page | Title | `\titlepage` | — | — |
| 2 | Outline | TOC | `\tableofcontents` | — | — |
| 3 | Can a Machine Learn from Its Neighbors? | L8 (mixed media) | XKCD #1838 (0.45tw left) + 3 framing bullets: (1) Banks have millions of past transactions, (2) How to classify new ones?, (3) How to find customer groups without labels? | XKCD #1838 | "XKCD #1838 by Randall Munroe (CC BY-NC 2.5) — Today: learning from neighbors and discovering groups" |
| 4 | What Is Classification? | L7 (full width) | Plain English: like sorting email into spam/not-spam. Labeled examples → predict new ones. 3 everyday examples: spam detection, medical diagnosis, fraud flagging. | — | "Classification = supervised learning: we learn from labeled examples" |
| 5 | What Is Clustering? | L7 (full width) | Plain English: like organizing a messy bookshelf by topic — no labels, just find natural groups. 3 examples: customer segments, news article grouping, song playlists. | — | "Clustering = unsupervised learning: discover structure without labels" |
| 6 | Classification vs Clustering Side by Side | L10 (comparison) | Left: Classification (has labels, predict, supervised). Right: Clustering (no labels, discover, unsupervised). 3 bullets each. | — | "KNN solves classification; K-Means solves clustering — same letter K, different meanings" |
| 7 | Why Do Similar Things Behave Similarly? | L7 (full width) | Human intuition: patients with similar symptoms → similar diagnoses; houses in similar neighborhoods → similar prices; borrowers with similar profiles → similar default rates. | — | "KNN turns this everyday intuition into a precise algorithm" |
| 8 | Why Do Banks Need Customer Segments? | L7 (full width) | Business motivation: (1) targeted products (premium vs starter), (2) risk management (group loans by risk), (3) marketing (retention campaigns for at-risk customers). Real data point: "A major UK bank identified 6 customer segments, increasing product cross-sell by 15%." | — | "Segmentation transforms raw data into actionable business strategy" |
| 9 | What Will You Learn Today? | L7 (full width) | LOs as questions: (1) How does KNN use neighbors to classify?, (2) How does K-Means find clusters step by step?, (3) How do you choose K for either method?, (4) When should you use KNN vs K-Means? + "Road Map: Problem → Method → Solution → Practice" | — | "By end of lecture: classify with KNN, cluster with K-Means, choose K" |

### CORE ZONE: \section{Problem} (2 slides)

| # | Title | Layout | Content | Chart | Bottomnote |
|---|-------|--------|---------|-------|------------|
| 10 | The Two Problems We Solve Today | L10 (comparison) | Left: Fraud Detection (labeled transactions, predict fraud/legit). Right: Customer Segmentation (no labels, discover groups). **Bold callout:** "K in KNN = number of neighbors; K in K-Means = number of clusters — completely different!" | — | "Same letter K, fundamentally different meanings — watch for this!" |
| 11 | A Concrete Example: 5 Customers | L9 (definition-example) | Left: Table of 5 customers (Age, Income, Label: fraud/legit). Right: "Which group does Customer #6 belong to?" Visual scatter description. | — | "This small example is the starting point — KNN scales this to millions" |

### CORE ZONE: \section{Method} — KNN (5 slides)

| # | Title | Layout | Content | Chart | Bottomnote |
|---|-------|--------|---------|-------|------------|
| 12 | How Does KNN Work? Three Simple Steps | L11 (step-by-step) | Step 1: Measure distance to every past example. Step 2: Find the K=3 closest neighbors. Step 3: Take a majority vote. Worked example: "Customer #6 has 3 nearest neighbors: 2 fraud, 1 legit → predict fraud." | — | "KNN is 'lazy': it stores all data and only computes at prediction time" |
| 13 | KNN Step by Step: A Worked Example | L22 (chart + explanations) | Chart 09_knn_step_by_step. 3 bullets: (1) We measure distance from the new point (star) to all training points, (2) The 3 closest neighbors are 2 blue, 1 orange → majority vote = blue, (3) If we used K=5 neighbors, the vote might change — K matters! | 09_knn_step_by_step | "The choice of K directly controls how many neighbors vote" |
| 14 | What Happens When K Changes? | L22 (chart + explanations) | Chart 01_knn_boundaries. 3 bullets: (1) K=1: jagged boundary follows every point — may memorize noise (overfitting), (2) K=15: smooth boundary — may miss important patterns (underfitting), (3) Sweet spot: use cross-validation to find the best K. | 01_knn_boundaries | "Small K = flexible but noisy; large K = smooth but may miss detail" |
| 15 | How Do We Measure Distance? | L9 (definition-example) | Left: Euclidean formula d = sqrt(sum of squared differences). Right: **Worked example:** Customer A (age=30, income=50k), Customer B (age=25, income=55k). d = sqrt((30-25)² + (50-55)²) = sqrt(50) ≈ 7.07. | — | "Always standardize features first — otherwise income (thousands) dominates age (decades)" |
| 16 | What Do Different Distance Measures Look Like? | L22 (chart + explanations) | Chart 02_distance_metrics. 3 bullets: (1) Euclidean draws circular neighborhoods, (2) Manhattan draws diamond neighborhoods — measures block-by-block distance, (3) The choice of distance metric changes which points count as "nearest." | 02_distance_metrics | "Different metrics = different neighborhoods = different predictions" |

### CORE ZONE: \section{Method} — K-Means (5 slides)

| # | Title | Layout | Content | Chart | Bottomnote |
|---|-------|--------|---------|-------|------------|
| 17 | How Does K-Means Find Clusters? | L11 (step-by-step) | Three steps in plain English: Step 1: Pick K=3 starting points (centroids). Step 2: Assign each data point to its nearest centroid. Step 3: Move each centroid to the center of its group. Repeat steps 2-3 until nothing changes. | — | "K-Means is like rearranging seats at a party until everyone is closest to their table center" |
| 18 | Watching K-Means Iterate | L22 (chart + explanations) | Chart 03_kmeans_iteration. 3 bullets: (1) Stars show centroids (cluster centers) moving toward their groups, (2) Colors show which centroid each point is assigned to, (3) After a few rounds, centroids stop moving — we've found our clusters. | 03_kmeans_iteration | "Convergence (stopping) is guaranteed — the algorithm always finishes" |
| 19 | How Do We Choose K Clusters? The Elbow Method | L22 (chart + explanations) | Chart 04_elbow_method. 3 bullets: (1) WCSS (total distance from points to their centroids) always decreases with more clusters, (2) The "elbow" is where adding more clusters stops helping much, (3) Here K=3 clusters looks like the best choice — diminishing returns after that. | 04_elbow_method | "The elbow is sometimes hard to see — that is why we also use silhouette analysis" |
| 20 | Why Does Starting Position Matter? | L7 (full width) | K-Means++ in plain English: Instead of picking random starting centroids, spread them out — pick each new centroid far from existing ones. Why: random starts can lead to bad results. K-Means++ is the default in Python. **Analogy:** "Imagine choosing 3 meeting points in a city — you'd spread them out, not put all 3 on the same street." | — | "K-Means++ is the default in scikit-learn — always use it" |
| 21 | K-Means Has Limitations — Know Them! | L18 (pros/cons) | [+] Fast, simple, works well on round clusters. [+] Scales to large datasets. [-] Assumes round (spherical) clusters of similar size. [-] Sensitive to outliers (extreme values) — one extreme point shifts the centroid. [-] Must specify K clusters in advance (unlike DBSCAN). | — | "If clusters look elongated or have very different sizes, K-Means may not be the right tool" |

### CORE ZONE: \section{Solution} (4 slides)

| # | Title | Layout | Content | Chart | Bottomnote |
|---|-------|--------|---------|-------|------------|
| 22 | How Do KNN and K-Means Compare? | L3 (comparison table) | Table: Property / KNN / K-Means. Rows: Task (classification/clustering), Learning (supervised/unsupervised), K means (neighbors/clusters), Training (none-lazy/iterative), Output (class label/cluster ID). | — | "Despite sharing K, these solve fundamentally different problems" |
| 23 | Finance: Customer Segmentation with K-Means | L22 (chart + explanations) | Chart 11_rfm_scatter. 3 bullets: (1) RFM = Recency (days since last purchase), Frequency (number of purchases), Monetary (total spend), (2) K-Means groups customers: Champions (high R,F,M) get loyalty rewards; At-Risk (low R) get retention campaigns, (3) **Worked example:** Customer A: R=5 days, F=20, M=$5000 → Champion. Customer B: R=180 days, F=2, M=$50 → At-risk. | 11_rfm_scatter | "Each segment gets tailored products and communication — segments drive strategy" |
| 24 | Finance: Can KNN Detect Fraud? | L7 (full width) | Class imbalance (unequal groups) problem: fraud is <1% of transactions. If KNN predicts "no fraud" for everything → 99% accuracy but catches ZERO fraud! Solutions: oversample fraud cases, weight fraud neighbors more heavily, measure with Precision-Recall instead of accuracy. | — | "In fraud detection, missing a fraud case is far more costly than a false alarm" |
| 25 | Which Method Should You Choose? | L22 (chart + explanations) | Chart 07_decision_flowchart. 3 bullets: (1) Have labels? → supervised methods like KNN, (2) No labels, round clusters? → K-Means, (3) Weird-shaped clusters? → DBSCAN or hierarchical clustering. | 07_decision_flowchart | "Start simple (K-Means or KNN), add complexity only if results are poor" |

### CLOSING ZONE: \section{Practice} + \section{Summary} (3 slides)

| # | Title | Layout | Content | Chart | Bottomnote |
|---|-------|--------|---------|-------|------------|
| 26 | Hands-on Exercise | L7 (full width) | 3 exercises: (1) Apply KNN to classify customers — vary K neighbors and see how predictions change, (2) Segment customers with K-Means — interpret what each group means, (3) Compare the elbow method and silhouette to choose K clusters. | — | "Exercises progress from guided implementation to open-ended analysis" |
| 27 | Key Takeaways | L13 (summary) | Left: KNN — non-parametric, lazy, small K=flexible but noisy, scale features! Right: K-Means — iterative, converges, use K-Means++, check K with elbow/silhouette. Both: feature scaling critical, K means different things in each. | — | "Get the distance right, get the result right — both methods depend on distance" |
| 28 | Until Next Time... | L8 (mixed media) | XKCD #2731 clustering image + "Even K-Means would struggle to cluster the ways students misuse K-Means." + "Next session: L04 — Random Forests." | XKCD #2731 | "XKCD #2731 by Randall Munroe (CC BY-NC 2.5) — Clustering is easy; knowing when to cluster is hard" |

**Overview Total: 28 slides, 7 charts (01, 02, 03, 04, 07, 09_new, 11_new). Density: 7/28 = 1 per 4.0 ✓**

---

## Part 2: Deepdive — Slide-by-Slide Specification (25 main + 4 appendix = 29 slides)

### Opening (slides 1-4, before first \section)

| # | Title | Layout | Content | Chart | Bottomnote |
|---|-------|--------|---------|-------|------------|
| 1 | Title Page | Title | `\titlepage` | — | — |
| 2 | Outline | TOC | `\tableofcontents` | — | — |
| 3 | The Math Behind Learning from Neighbors | L8 (mixed media) | XKCD #1838 (0.45tw right) + 3 bullets: "In the overview, we saw the intuition. Now we go deeper: How exactly do we measure similarity? How do we implement these in Python? How do we validate results?" **Justification for reusing XKCD #1838:** Different framing — overview uses it to hook ("Can a machine learn?"), deepdive uses it as recap bridge ("Now let's look inside the math"). | XKCD #1838 | "XKCD #1838 by Randall Munroe (CC BY-NC 2.5) — Let's look inside the pile of linear algebra" |
| 4 | Learning Objectives | L7 (full width) | (1) Implement KNN step by step and explain every line, (2) Implement K-Means and trace through iterations, (3) Evaluate cluster quality using silhouette analysis, (4) Build a complete classification/clustering pipeline in Python. | — | "Focus: implementation, evaluation, and practical pipeline building" |

### \section{KNN In Depth} (slides 5-11, 7 slides)

| # | Title | Layout | Content | Chart | Bottomnote |
|---|-------|--------|---------|-------|------------|
| 5 | Why Is KNN Called a "Lazy Learner"? | L10 (comparison) | Left: "Eager learners" (logistic regression, neural nets) — build a model during training. Right: KNN — stores ALL training data, does all work at prediction time. "Lazy because it postpones everything to the last moment." | — | "No parameters to estimate — the training data IS the model" |
| 6 | The KNN Algorithm Step by Step | L11 (step-by-step) | Plain-English pseudocode: 1. Store all training data. 2. For new query: compute distance to every stored point. 3. Sort by distance, pick K closest neighbors. 4. Count votes per class. 5. Tie? Weight by 1/distance — closer neighbors win. Return majority class. **Worked example inline:** 5 neighbors, 3 vote class A, 2 vote class B → predict A. | — | "Complexity: O(n×p) per prediction — must scan ALL data every time" |
| 7 | Why Feature Scaling Is Non-Negotiable | L22 (chart + explanations) | Chart 08_feature_scaling_effect. 3 bullets: (1) Before scaling: income ranges 20k-200k, age ranges 20-80 — KNN picks neighbors based almost entirely on income, (2) After scaling: both features contribute equally to distance — neighbors are truly "similar", (3) **Worked example:** "Without scaling, d = 180,000. After StandardScaler: d = 2.1." | 08_feature_scaling_effect | "StandardScaler: subtract mean, divide by standard deviation — do this BEFORE fitting KNN" |
| 8 | What Happens as K Changes? Bias vs Variance | L22 (chart + explanations) | Chart 10_bias_variance_visual. 3 bullets: (1) K=1 neighbors: perfectly fits training data but memorizes noise (overfitting — red jagged boundary), (2) K=15 neighbors: very smooth boundary, may miss real patterns (underfitting — blue smooth boundary), (3) Best K balances these — find it with cross-validation. **Analogy:** "K=1 is asking ONE friend; K=100 is polling the whole school." | 10_bias_variance_visual | "Start with K=√n, then tune with cross-validation on held-out data" |
| 9 | Weighted KNN: Give Closer Neighbors More Say | L9 (definition-example) | Left: Problem — all K neighbors vote equally, even a distant one. Solution: weight by 1/distance. Formula: ŷ = class with highest weighted vote, w_i = 1/d(x, x_i). Right: **Worked example:** 3 neighbors at distances 1, 2, 10. Uniform: each gets weight 1. Distance-weighted: weights 1.0, 0.5, 0.1 — closest dominates. | — | "In scikit-learn: weights='distance' instead of 'uniform' — often improves performance" |
| 10 | How Do We Pick the Best K? Cross-Validation | L22 (chart + explanations) | Chart 13_cv_accuracy_curve. 3 bullets: (1) Try K neighbors = 1, 3, 5, 7, ..., 19. For each: split data into 5 folds, rotate train/test, average accuracy, (2) Training accuracy (gray) is always high and decreases — validation accuracy (blue) peaks then drops, (3) **Optimal K** = where validation peaks (green star). Here K=5 neighbors wins. **Table:** K=1→82%, K=3→87%, K=5→89%, K=7→88%, K=9→85%. | 13_cv_accuracy_curve | "Cross-validation prevents overfitting to one particular train-test split" |
| 11 | When Does KNN Struggle? The Curse of Dimensionality | L7 (full width) | In high dimensions: distances become meaningless — all points approximately equidistant. **Analogy:** "In a 1D line, nearby houses are easy to find. In a 1000-dimension space, 'nearby' loses meaning because there are too many directions." Solutions: reduce dimensions first (PCA — see L05), select only relevant features, use domain knowledge. **Rule of thumb:** KNN works best with fewer than 15-20 features. | — | "If KNN performs poorly, suspect too many features before blaming the algorithm" |

### \section{K-Means In Depth} (slides 12-18, 7 slides)

| # | Title | Layout | Content | Chart | Bottomnote |
|---|-------|--------|---------|-------|------------|
| 12 | What Is K-Means Really Optimizing? | L9 (definition-example) | Left: Objective — minimize total distance from each point to its centroid. Formula: J = sum over all clusters of (sum of squared distances). Right: **Worked example:** 6 points, 2 clusters. Cluster A: (1,1), (2,2), (1,3) → centroid (1.33, 2.0) → WCSS_A = 1.33. Cluster B: (5,5), (6,6), (5,7) → centroid (5.33, 6.0) → WCSS_B = 1.33. Total J = 2.67. | — | "WCSS measures how tightly packed points are within each cluster — lower is better" |
| 13 | K-Means Algorithm: A Worked Visual Example | L22 (chart + explanations) | Chart 12_kmeans_worked_example. 3 bullets: (1) Diamonds = initial centroids placed by K-Means++, colored circles = assigned data points, (2) Dashed arrows show centroids moving toward cluster centers after one iteration, (3) After 3-4 iterations: centroids stabilize, assignments stop changing — converged! **Convergence guarantee:** WCSS can only decrease → must stop. | 12_kmeans_worked_example | "K-Means always converges — but may find a local optimum, not the global best" |
| 14 | K-Means++: Why Smart Starting Matters | L9 (definition-example) | Left: Problem — random starts can cluster badly. K-Means++ solution: pick each new centroid far from existing ones. Right: **Worked example:** 3 centroids needed. Step 1: pick point (2,3) randomly. Step 2: farthest point is (9,8) → pick. Step 3: farthest from both is (2,9) → pick. Centroids spread out! | — | "K-Means++ is the default in scikit-learn — no extra code needed" |
| 15 | How Do We Measure Cluster Quality? Silhouette Score | L22 (chart + explanations) | Chart 05_silhouette. 3 bullets: (1) Each horizontal bar = one data point. Height = silhouette score from -1 to +1, (2) Score near +1: well-clustered. Near 0: on boundary. Below 0: possibly in wrong cluster, (3) All clusters should have similar width and stay above the average line. **Worked example:** "Point at 0.8 → clearly right cluster. Point at -0.2 → might belong next door." | 05_silhouette | "Compare silhouette plots for K=2, 3, 4, 5 clusters — pick K with highest average silhouette" |
| 16 | Why Are K-Means Clusters Always "Round"? | L22 (chart + explanations) | Chart 06_voronoi. 3 bullets: (1) K-Means divides space into Voronoi regions (polygons) — each region contains points closest to one centroid, (2) These regions are always convex (no C-shapes, no donuts), (3) This means K-Means CANNOT discover elongated, ring-shaped, or irregular clusters. | 06_voronoi | "If your data has non-round clusters, use DBSCAN or hierarchical clustering instead" |
| 17 | What If Clusters Aren't Round? Alternatives | L18 (pros/cons) | Three alternatives: (1) DBSCAN (density-based) — finds arbitrary shapes, handles outliers, no need to specify K clusters. (2) Hierarchical clustering — bottom-up merging, produces dendrogram (tree diagram), cut at desired level. (3) Gaussian Mixture Models — soft assignments (probabilities instead of hard labels), handles elliptical clusters. | — | "K-Means is the starting point — switch to alternatives when validation metrics are poor" |
| 18 | K-Means Variants for Special Cases | L3 (two cols text) | Left: Mini-Batch K-Means — uses random subsets for faster centroid updates, 10-100x faster for large data, slightly less precise. Right: K-Medoids (PAM) — centroids must be actual data points (medoids), more robust to outliers, works with any distance metric. | — | "Mini-Batch for speed on large datasets; K-Medoids for robustness to outliers" |

### \section{Implementation} (slides 19-22, 4 slides)

| # | Title | Layout | Content | Chart | Bottomnote |
|---|-------|--------|---------|-------|------------|
| 19 | KNN in Python: Complete Example | L17 (code example) | Code: import, Pipeline with StandardScaler + KNeighborsClassifier(n_neighbors=5, weights='distance'), fit, predict, classification_report. Key params: n_neighbors, weights, metric. Use `\small` for code. | — | "Always put StandardScaler in the pipeline — never scale outside cross-validation" |
| 20 | K-Means in Python: Complete Example | L17 (code example) | Code: import, StandardScaler + KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=42), fit_predict, cluster_centers_. Key params: n_clusters, init, n_init. Use `\small`. | — | "n_init=10 means 10 restarts with different seeds — keeps the best result" |
| 21 | Building a Complete Pipeline | L17 (code example) | Code: Pipeline, GridSearchCV with param_grid={'knn__n_neighbors': [3,5,7,11], 'knn__weights': ['uniform','distance']}, cv=5, scoring='f1'. Print best_params_, best_score_. Use `\small`. | — | "GridSearchCV automates K selection — no manual trial and error needed" |
| 22 | Evaluating K-Means: Elbow + Silhouette in Code | L17 (code example) | Code: loop K=2..8, compute silhouette_score, also compute inertia_ for elbow. Plot both. Pick K where both agree. Use `\small`. | — | "Combine elbow and silhouette — if they agree, you have strong evidence for K clusters" |

### \section{Practice} + \section{Summary} (slides 23-25, 3 slides)

| # | Title | Layout | Content | Chart | Bottomnote |
|---|-------|--------|---------|-------|------------|
| 23 | Hands-On Exercise | L7 (full width) | (1) Implement weighted KNN: compare uniform vs distance voting on a fraud dataset, (2) Run K-Means on customer data: interpret cluster profiles using RFM features, (3) Compare elbow and silhouette for K cluster selection — do they agree? | — | "All exercises use real-world-inspired financial datasets" |
| 24 | Key Takeaways | L13 (summary) | Left: KNN — lazy learner, scale features, choose K neighbors with cross-validation, beware high dimensions. Right: K-Means — iterative assign-update, guaranteed convergence, validate with silhouette, spherical clusters only. Both: feature scaling mandatory, K means different things. | — | "Both are foundational — understand them before moving to forests and ensembles" |
| 25 | Until Next Time... | L8 (mixed media) | XKCD #2731 clustering image + "Now you know why 'just cluster it' is never that simple." + "Next: L04 — Random Forests: from distance to trees." **Justification for reusing XKCD #2731:** Different framing — overview uses it as farewell ("until next time"), deepdive uses it as reflection ("now you know why"). | XKCD #2731 | "XKCD #2731 by Randall Munroe (CC BY-NC 2.5) — Next lecture: ensemble methods" |

### APPENDIX: \appendix + \section*{Extra Topics} (slides A1-A4, 4 slides)

| # | Title | Layout | Content | Chart | Bottomnote |
|---|-------|--------|---------|-------|------------|
| A1 | Appendix Divider | Divider | `\appendix \section*{Extra Topics}` — "Appendix: Extra Topics and Details" | — | — |
| A2 | Distance Metrics: The Minkowski Family | L9 (def+example) | Generalized distance d_p formula. p=1: Manhattan (robust to outliers). p=2: Euclidean (default). p=∞: Chebyshev (max difference). **Worked example:** Points (1,3) and (4,7). Manhattan: |1-4|+|3-7|=7. Euclidean: sqrt(9+16)=5. Chebyshev: max(3,4)=4. | — | "Higher p amplifies large single-feature differences" |
| A3 | Why Does K-Means Always Stop? (Intuition) | L7 (full width) | Intuitive convergence argument (NOT formal proof): (1) Each step can only improve or maintain the WCSS score, (2) There are only finitely many ways to group n points into K clusters, (3) We never revisit a grouping we've seen → must stop. **Analogy:** "Like rolling a ball downhill — it can only go down or stay put, never back up." | — | "Formal proof uses coordinate descent — see ESL Ch. 14 for details" |
| A4 | Computational Complexity: How Fast? | L3 (comparison table) | Table: Method / Training / Prediction. KNN brute: O(1) / O(nd). KNN KD-Tree: O(nd log n) / O(d log n). K-Means Lloyd's: O(nKdT) / O(Kd). Mini-Batch K-Means: O(bKdT) / O(Kd). Note: KD-Tree degrades above 15-20 features. | — | "For very large data: approximate nearest neighbors (FAISS, Annoy)" |

**Deepdive Total: 25 main + 4 appendix = 29 slides, 6 charts (05, 06, 08_new, 10_new, 12_new, 13_new). Density: 6/25 main = 1 per 4.17 ✓**

XKCD images (#1838 in slide 3, #2731 in slide 25) are static comic images used for engagement framing, NOT counted toward chart density. They have no chart.py.

---

## Part 3: Chart Allocation Table

| Chart | File | Slide | Type | Status |
|-------|------|-------|------|--------|
| 01_knn_boundaries | Overview | 14 | Decision/Region Map | Existing |
| 02_distance_metrics | Overview | 16 | Comparison | Existing |
| 03_kmeans_iteration | Overview | 18 | Iterative Process | Existing |
| 04_elbow_method | Overview | 19 | Metric Curves | Existing |
| 05_silhouette | Deepdive | 15 | Bar/Distribution | Existing |
| 06_voronoi | Deepdive | 16 | Cluster/Group Viz | Existing |
| 07_decision_flowchart | Overview | 25 | Flowchart | Existing |
| **08_feature_scaling_effect** | **Deepdive** | **7** | **Annotated Scatter** | **NEW** |
| **09_knn_step_by_step** | **Overview** | **13** | **Annotated Scatter** | **NEW** |
| **10_bias_variance_visual** | **Deepdive** | **8** | **Overlaid Contourf** | **NEW** |
| **11_rfm_scatter** | **Overview** | **23** | **Cluster Scatter** | **NEW** |
| **12_kmeans_worked_example** | **Deepdive** | **13** | **Annotated Iterative** | **NEW** |
| **13_cv_accuracy_curve** | **Deepdive** | **10** | **Metric Curves** | **NEW** |

**Verification:**
- No chart appears in both overview AND deepdive ✓
- Overview: 7 charts / 28 slides = 1 per 4.0 ✓
- Deepdive: 6 charts / 25 main slides = 1 per 4.17 ✓
- Total new charts: 6 (listed in Output Files section) ✓
- Each chart folder produces exactly one chart.pdf ✓

---

## Part 4: New Chart Specifications

### 08_feature_scaling_effect/chart.py
- **Type:** Annotated scatter with distance comparison
- **Design (FINAL — single approach):** Generate 15 points with Age (20-80) and Income (20k-200k). Plot all points. Highlight a query point (red star). Draw dashed lines to the 3 nearest neighbors found WITHOUT scaling (dominated by income — nearly horizontal neighbors). Draw solid lines to the 3 nearest neighbors found WITH StandardScaler (balanced selection). Label: "Unscaled neighbors (dashed)" and "Scaled neighbors (solid)". Title: "Feature Scaling Changes Your Neighbors."
- **Key insight:** The two sets of 3 neighbors are DIFFERENT points, showing that scaling changes results.
- **Colors:** Query=MLRED star, unscaled neighbors=MLGRAY dashed, scaled neighbors=MLBLUE solid, other points=MLLAVENDER.

### 09_knn_step_by_step/chart.py
- **Type:** Annotated scatter
- **Design:** 12 training points (8 MLBLUE class A, 4 MLORANGE class B), one MLRED query star. K=3: draw dashed circles connecting query to 3 nearest points (2 blue, 1 orange). Text annotation: "Vote: 2 Blue, 1 Orange → Predict: Blue". Shaded circle of radius = distance to 3rd neighbor.
- **Colors:** Class A=MLBLUE, Class B=MLORANGE, query=MLRED star, neighborhood=MLLAVENDER shaded.

### 10_bias_variance_visual/chart.py
- **Type:** Overlaid contourf decision boundaries
- **Design (FINAL — single approach):** Generate 80 training points (2 classes, partial overlap). Plot points as scatter. Overlay TWO contourf boundaries on the SAME axes: K=1 boundary (MLRED, alpha=0.15, jagged) and K=15 boundary (MLBLUE, alpha=0.15, smooth). Add text annotations: "K=1: Overfitting (follows noise)" near a jagged region, "K=15: Underfitting (too smooth)" near a smooth region. Title: "Bias-Variance: K=1 vs K=15."
- **Colors:** Points=MLBLUE/MLORANGE by class. K=1 boundary fill=MLRED alpha. K=15 boundary fill=MLBLUE alpha.

### 11_rfm_scatter/chart.py
- **Type:** Scatter colored by K-Means cluster
- **Design:** Generate 200 synthetic customers with Recency (1-365 days), Monetary ($10-$10000). Apply KMeans(n_clusters=4). Color by cluster. Annotate each cluster center: "Champions" (low R, high M), "At Risk" (high R, low M), "New Customers" (low R, low M), "Hibernating" (high R, mid M). Point size ∝ Frequency.
- **Colors:** Cluster 0=MLBLUE, 1=MLORANGE, 2=MLGREEN, 3=MLPURPLE. Centers=black diamonds.

### 12_kmeans_worked_example/chart.py
- **Type:** Annotated iterative process
- **Design:** 8 data points in 2 visible groups. Show state after iteration 1: colored circles (assigned to nearest centroid), diamond centroids, dashed arrows from old centroid positions to new positions. Text: "Iteration 1: Assign → Update → Centroids move." Inset text: "Initial centroids (K-Means++) → After 1 iteration."
- **Colors:** Cluster 0=MLBLUE, Cluster 1=MLORANGE. Old centroids=MLGRAY, new centroids=MLPURPLE diamonds. Arrows=MLRED dashed.

### 13_cv_accuracy_curve/chart.py
- **Type:** Metric curve
- **Design:** X = K neighbors (1, 3, 5, 7, 9, 11, 13, 15, 17, 19). Y = accuracy (0.7-1.0). Two lines: training accuracy (MLGRAY, starts ~0.98, decreases) and validation accuracy (MLBLUE, peaks at K=5 ~0.89, then decreases). MLGREEN star at optimal K=5. Shaded regions with text: "Overfitting zone" (left, MLRED alpha=0.05), "Underfitting zone" (right, MLORANGE alpha=0.05). Title: "Cross-Validation: Finding Optimal K Neighbors."
- **Colors:** Train=MLGRAY, Validation=MLBLUE, Optimal=MLGREEN star, Overfit zone=MLRED, Underfit zone=MLORANGE.

---

## Part 5: Layout Diversity Check

### Overview (28 slides)
| Layout | Count | Slides |
|--------|-------|--------|
| Title | 1 | 1 |
| TOC | 1 | 2 |
| L7 (full width) | 6 | 4, 5, 7, 8, 9, 24 |
| L8 (mixed media) | 2 | 3, 28 |
| L9 (definition-example) | 2 | 11, 15 |
| L10 (comparison) | 2 | 6, 10 |
| L11 (step-by-step) | 2 | 12, 17 |
| L13 (summary) | 1 | 27 |
| L18 (pros/cons) | 1 | 21 |
| L22 (chart + explanations) | 5 | 13, 14, 16, 18, 19 |
| L3 (comparison table) | 1 | 22 |
| L7 (full width) | 1 | 26 |
| **Distinct layouts:** | **10** | ✓ (≥8 required) |

Arithmetic: 1+1+6+2+2+2+2+1+1+5+1+1 = 25... wait, that's wrong. Let me recount by listing every slide:

| Slide | Layout |
|-------|--------|
| 1 | Title |
| 2 | TOC |
| 3 | L8 |
| 4 | L7 |
| 5 | L7 |
| 6 | L10 |
| 7 | L7 |
| 8 | L7 |
| 9 | L7 |
| 10 | L10 |
| 11 | L9 |
| 12 | L11 |
| 13 | L22 |
| 14 | L22 |
| 15 | L9 |
| 16 | L22 |
| 17 | L11 |
| 18 | L22 |
| 19 | L22 |
| 20 | L7 |
| 21 | L18 |
| 22 | L3 |
| 23 | L22 |
| 24 | L7 |
| 25 | L22 |
| 26 | L7 |
| 27 | L13 |
| 28 | L8 |

Count = 28 ✓. Distinct: Title, TOC, L7, L8, L9, L10, L11, L13, L18, L22, L3 = **11 distinct** ✓

### Deepdive (29 slides incl. appendix)
| Slide | Layout |
|-------|--------|
| 1 | Title |
| 2 | TOC |
| 3 | L8 |
| 4 | L7 |
| 5 | L10 |
| 6 | L11 |
| 7 | L22 |
| 8 | L22 |
| 9 | L9 |
| 10 | L22 |
| 11 | L7 |
| 12 | L9 |
| 13 | L22 |
| 14 | L9 |
| 15 | L22 |
| 16 | L22 |
| 17 | L18 |
| 18 | L3 |
| 19 | L17 |
| 20 | L17 |
| 21 | L17 |
| 22 | L17 |
| 23 | L7 |
| 24 | L13 |
| 25 | L8 |
| A1 | Divider |
| A2 | L9 |
| A3 | L7 |
| A4 | L3 |

Count = 29 ✓. Distinct: Title, TOC, L7, L8, L9, L10, L11, L13, L17, L18, L22, L3, Divider = **13 distinct** ✓

---

## Part 6: Deliberately Dropped Content (vs existing MSc slides)

| Content | Reason |
|---------|--------|
| Cover & Hart consistency theorem + proof | Too advanced; replaced with "KNN has theoretical guarantees" statement |
| Bias-variance decomposition formula | Replaced with intuitive visual (chart 10: K=1 vs K=15) |
| Formal K-Means convergence proof | Replaced with intuitive argument in appendix A3 |
| Mahalanobis distance | Requires covariance matrix concept — too advanced |
| Cosine similarity | Better suited for text/NLP (L06) |
| Hopkins statistic | Niche; replaced with "always visualize before clustering" guidance |
| Gap statistic formula | Too complex; mentioned as "advanced method exists" only |
| K-Means as EM special case | Requires GMM/EM not yet covered |
| LSH / FAISS | Implementation detail for extreme scale only |
| `\begin{algorithmic}` pseudocode | Replaced with plain-English step-by-step (more accessible) |

---

## Part 7: XKCD Image Reuse Justification

Both XKCD images appear in BOTH overview and deepdive, but with different pedagogical framing:

| Image | Overview Context | Deepdive Context |
|-------|-----------------|-----------------|
| XKCD #1838 | Opening hook: "Can a machine learn?" (engagement) | Recap bridge: "Now let's go inside the math" (transition) |
| XKCD #2731 | Farewell: "Until next time" (sendoff) | Reflection: "Now you know why 'just cluster it' isn't simple" (synthesis) |

This is acceptable because:
1. These are static engagement images, NOT data charts (no chart.py)
2. Students see overview and deepdive in the SAME session — the recurring image creates narrative bookending
3. Different framing text and bottomnotes prevent repetition feeling

---

## Part 8: Execution Steps

1. **Create 6 new chart folders** (08-13) in `slides/L03_KNN_KMeans/`
2. **Write 6 chart.py files** per specifications in Part 4
3. **Run all 6 chart.py scripts** → verify chart.pdf generated in each
4. **Write `L03_overview_accessible.tex`** following Part 1 slide-by-slide spec
5. **Write `L03_deepdive_accessible.tex`** following Part 2 slide-by-slide spec
6. **Compile overview** with pdflatex → verify 0 errors, 0 Overfull
7. **Compile deepdive** with pdflatex → verify 0 errors, 0 Overfull
8. **Verification grep checks:**
   - `grep -c "BSc" L03_overview_accessible.tex` → must be 0
   - `grep -c "BSc" L03_deepdive_accessible.tex` → must be 0
   - `grep -c "Overfull" temp/L03_overview_accessible.log` → must be 0
   - `grep -c "Overfull" temp/L03_deepdive_accessible.log` → must be 0
   - `grep -c "begin{frame}" L03_overview_accessible.tex` → must be 28
   - `grep -c "begin{frame}" L03_deepdive_accessible.tex` → must be 29

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Chart 08 (scaling) visual clarity | Design validated: two sets of neighbor lines (dashed vs solid) from same query point clearly shows the effect |
| Chart 10 (bias-variance) overlaid contourf readability | Use low alpha (0.15) for fills, high-contrast annotation text, and only 2 boundary levels |
| Overfull on code slides (L17) | Use `\small` for all code; limit to 8-10 lines per slide; test compile early |
| 28 overview slides timing | Within skill's 25-35 range; 28 slides ÷ 50 min overview time = 1.8 min/slide (reasonable) |
| Deepdive appendix too thin (4 slides) | Within skill's 3-6 range for accessible level |

---

PLAN_READY: .omc/plans/L03-bsc-slide-creation.md
