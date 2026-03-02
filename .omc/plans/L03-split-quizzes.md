# Plan: L03 Split Quizzes — 20 KNN + 20 K-Means

## Task
Create two separate quiz files from the L03 MSc-level slide content (overview + deepdive):
1. `docs/quiz/L03_knn.html` — 20 KNN-focused questions
2. `docs/quiz/L03_kmeans.html` — 20 K-Means-focused questions

Template: Copy HTML/CSS/JS verbatim from `docs/quiz/L03_knn_kmeans.html`, changing only title, nav-title, and `quizData.questions`.

---

## Part 1: KNN Quiz (20 questions)

### Source Content (from L03_overview.tex + L03_deepdive.tex)

| # | Topic | Source Slide(s) |
|---|-------|----------------|
| 1 | Lazy learner / instance-based concept | Overview:5, Deepdive:5 |
| 2 | Euclidean distance formula + worked example | Overview:10, Deepdive:8 |
| 3 | Manhattan distance formula + worked example | Overview:10, Deepdive:8 |
| 4 | Minkowski distance family (p=1,2,∞) | Deepdive:8 |
| 5 | Feature scaling: why critical for KNN | Deepdive:13 |
| 6 | Standardization vs Min-Max scaling | Deepdive:13 |
| 7 | KNN classification: majority vote formula | Overview:11, Deepdive:6 |
| 8 | Weighted KNN: inverse distance weighting | Deepdive:11 |
| 9 | Bias-variance tradeoff: K=1 vs K=large | Overview:11, Deepdive:10,17 |
| 10 | Choosing K via cross-validation | Deepdive:12 |
| 11 | K=sqrt(n) heuristic | Deepdive:10 |
| 12 | Decision boundaries: K=1 jagged vs K=large smooth | Overview:9, Deepdive:boundary vis |
| 13 | Curse of dimensionality | Deepdive:14 |
| 14 | Cover & Hart theorem: 1-NN error bound | Deepdive:15 |
| 15 | KD-Tree and Ball Tree acceleration | Deepdive:9(triangle ineq), A6 |
| 16 | Cosine similarity for text/embeddings | Deepdive:9 |
| 17 | Mahalanobis distance for correlated features | Deepdive:9 |
| 18 | Fraud detection with KNN + class imbalance | Overview:19, Deepdive:34 |
| 19 | SMOTE for imbalanced data | Deepdive:34 |
| 20 | scikit-learn Pipeline: scaling + KNN (data leakage) | Deepdive:39 |

### Quiz Design Rules
- Every question tests reasoning ("What would happen if..."), not memorization
- Distractors are plausible (common misconceptions)
- Explanations cite specific slide concepts
- KaTeX for math formulas
- Difficulty: MSc-level (matches overview + deepdive content)

---

## Part 2: K-Means Quiz (20 questions)

### Source Content (from L03_overview.tex + L03_deepdive.tex)

| # | Topic | Source Slide(s) |
|---|-------|----------------|
| 1 | WCSS objective function | Overview:12, Deepdive:18 |
| 2 | Lloyd's algorithm: 3 steps | Overview:13, Deepdive:19 |
| 3 | Convergence guarantee (monotonic WCSS decrease) | Overview:13, Deepdive:25 |
| 4 | K-Means++ initialization: algorithm | Overview:16, Deepdive:20 |
| 5 | K-Means++ competitive guarantee: O(log K) | Deepdive:20 |
| 6 | Elbow method for choosing K | Overview:15 |
| 7 | Silhouette score formula + interpretation | Deepdive:21 |
| 8 | Silhouette plot reading | Deepdive:22 |
| 9 | Voronoi tessellation: cluster shapes are convex | Deepdive:23 |
| 10 | K-Means assumptions: spherical, similar size/density | Deepdive:24 |
| 11 | When K-Means fails: non-convex shapes | Deepdive:24 |
| 12 | Hopkins statistic: clustering tendency | Deepdive:29 |
| 13 | Gap statistic: formal K selection | Deepdive:30 |
| 14 | K-Means as EM special case | Deepdive:26 |
| 15 | Mini-Batch K-Means | Deepdive:27 |
| 16 | K-Medoids (PAM): robustness to outliers | Deepdive:27 |
| 17 | DBSCAN: density-based alternative | Deepdive:35 |
| 18 | RFM customer segmentation | Overview:18, Deepdive:33 |
| 19 | Empty cluster handling | Deepdive:A4 |
| 20 | Computational complexity: O(nKdT) | Deepdive:28 |

---

## Part 3: index.html Updates

### 3A. Hero Stats
- Quiz Questions: `185` → `225` (+40 new questions)

### 3B. Per-Lesson Quizzes Section Header
- `Per-Lesson Quizzes (140 questions)` → `Per-Lesson Quizzes (180 questions)`

### 3C. Add Two New Quiz Cards
After the existing `L03_knn_kmeans.html` card (line 341), add:
```html
<a class="lcard" href="quiz/L03_knn.html" style="border-left:3px solid #FF7F0E;background:linear-gradient(135deg,#f5f3ff,#ede9fe)"><span class="lcard-num" style="background:#8b5cf6;color:white">L03</span><span class="lcard-title">KNN (Deep)</span><div style="font-size:9px;color:#7c3aed;margin-top:4px;font-weight:600">20 questions</div></a>
<a class="lcard" href="quiz/L03_kmeans.html" style="border-left:3px solid #FF7F0E;background:linear-gradient(135deg,#f5f3ff,#ede9fe)"><span class="lcard-num" style="background:#8b5cf6;color:white">L03</span><span class="lcard-title">K-Means (Deep)</span><div style="font-size:9px;color:#7c3aed;margin-top:4px;font-weight:600">20 questions</div></a>
```

### 3D. Sidebar Navigation
After L03 KNN & K-Means (Accessible) entry (line 102), add:
```html
<li><a href="#per-lesson-quizzes">L03 KNN (Deep)</a></li>
<li><a href="#per-lesson-quizzes">L03 K-Means (Deep)</a></li>
```

---

## Part 4: HTML Structure

Both quiz files copy verbatim from `docs/quiz/L03_knn_kmeans.html`:
- **Same**: CSS, JavaScript, KaTeX loading, `waitForKaTeX(renderMath)` pattern, three-column layout, results card
- **Changed per file**:
  - `<title>`: "Quiz 3: KNN | Methods & Algorithms" / "Quiz 3: K-Means | Methods & Algorithms"
  - `.nav-title`: "Quiz 3: KNN" / "Quiz 3: K-Means"
  - `.quiz-title`: "Quiz 3: K-Nearest Neighbors" / "Quiz 3: K-Means Clustering"
  - `quizData.questions`: 20 new questions (JSON array)
  - Progress badge: `0/20`

**KaTeX gotcha**: `renderMath()` renders `.q-text`, `.option-text`, `.feedback` elements (NOT `document.body`). `waitForKaTeX(renderMath)` called at end of `<body>`, NOT inside DOMContentLoaded. Copy this pattern exactly.

---

## Execution Steps

1. **Create `docs/quiz/L03_knn.html`** — Copy template, replace title/nav/quizData with 20 KNN questions
2. **Create `docs/quiz/L03_kmeans.html`** — Copy template, replace title/nav/quizData with 20 K-Means questions
3. **Update `docs/index.html`** — All 4 edits in single pass:
   a. Hero stats: 185 → 225
   b. Per-Lesson header: 140 → 180
   c. Add 2 quiz cards after L03 combined quiz
   d. Add 2 sidebar entries after L03 accessible entry

## Acceptance Criteria

1. `docs/quiz/L03_knn.html` exists with exactly 20 questions
2. `docs/quiz/L03_kmeans.html` exists with exactly 20 questions
3. All 20 KNN questions reference KNN content from overview + deepdive .tex
4. All 20 K-Means questions reference K-Means content from overview + deepdive .tex
5. Zero question overlap between the two quizzes
6. Zero question overlap with existing `L03_knn_kmeans.html` (20 Qs) or `L03_knn_kmeans_accessible.html` (20 Qs)
7. KaTeX renders correctly (renderMath at end of body, not in DOMContentLoaded)
8. `docs/index.html` hero stats: 225 Quiz Questions
9. `docs/index.html` Per-Lesson count: 180
10. `docs/index.html` has quiz cards for both new quizzes
11. `docs/index.html` sidebar has entries for both new quizzes

---

PLAN_READY: .omc/plans/L03-split-quizzes.md
