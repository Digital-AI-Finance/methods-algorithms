# Work Plan: Fix Charts in PDF Downloads + Add Per-Lesson Quizzes

**Plan ID:** fix-charts-add-quizzes
**Created:** 2026-01-28
**Status:** Ready for execution
**Revision:** 2 (addressed Critic feedback)

---

## Context

### Original Request
Fix two issues in the Methods_and_Algorithms course:
1. Charts missing from PDF downloads (docs/slides/pdf/ versions are ~50% smaller than source PDFs)
2. Create 6 individual lesson quizzes following the probability-statistics HTML format

### Interview Summary
- **Issue 1 Root Cause:** The PDFs in `docs/slides/pdf/` are outdated copies from Jan 21 (387KB/223KB) while source PDFs were recompiled Jan 28 with charts (588KB/600KB). The source LaTeX compiles correctly with relative paths. Solution: copy freshly compiled PDFs from source to docs.
- **Issue 2 Scope:** 6 quizzes x 20 questions = 120 total questions covering L01-L06 deepdive content with KaTeX math, finance applications, and the probability-statistics quiz format.

### Research Findings
1. **LaTeX Compilation:** Source PDFs compile correctly; graphicspath not needed since relative paths work from slide directory
2. **Quiz Template:** probability-statistics/quiz/quiz1.html provides the exact format needed (3-column cards, KaTeX, progress tracking, A-F grades)
3. **Deepdive Content:** Each LXX_deepdive.tex file contains ~25-30 slides of technical content for quiz questions
4. **Existing Quizzes:** `docs/quiz/` has 3 combined quizzes (quiz1_regression.html, quiz2_classification_ensemble.html, quiz3_advanced.html)
5. **Quiz Location:** New per-lesson quizzes will go in `docs/quiz/` alongside existing combined quizzes

---

## Work Objectives

### Core Objective
1. Sync compiled PDFs from source to docs so downloads include charts
2. Create 6 self-contained HTML quiz files with 20 questions each
3. Update docs/index.html to provide navigation to new per-lesson quizzes

### Deliverables
| # | Deliverable | File(s) |
|---|-------------|---------|
| 1 | Updated docs PDFs with charts | `docs/slides/pdf/L0*.pdf` (12 files) |
| 2 | Quiz template | `docs/quiz/quiz_template.html` |
| 3 | L01 Quiz | `docs/quiz/L01_linear_regression.html` (20 questions) |
| 4 | L02 Quiz | `docs/quiz/L02_logistic_regression.html` (20 questions) |
| 5 | L03 Quiz | `docs/quiz/L03_knn_kmeans.html` (20 questions) |
| 6 | L04 Quiz | `docs/quiz/L04_random_forests.html` (20 questions) |
| 7 | L05 Quiz | `docs/quiz/L05_pca_tsne.html` (20 questions) |
| 8 | L06 Quiz | `docs/quiz/L06_embeddings_rl.html` (20 questions) |
| 9 | Updated docs/index.html | Add "Per-Lesson Quizzes" section with links |
| 10 | Updated manifest.json | Add 6 new quiz entries |

### Definition of Done
- [ ] All 12 docs/slides/pdf/ files match source PDF sizes (>400KB for deepdive, >500KB for overview)
- [ ] One source PDF visually verified to contain embedded charts
- [ ] 6 quiz HTML files exist in docs/quiz/ folder
- [ ] Each quiz has exactly 20 questions with 4 options (A-D)
- [ ] All quizzes render correctly in browser with KaTeX math (verified via local server)
- [ ] docs/index.html includes "Per-Lesson Quizzes" section with navigation links
- [ ] manifest.json includes all 6 new quiz entries with correct paths
- [ ] No broken links in quiz navigation

---

## Must Have / Must NOT Have

### Must Have (Guardrails)
1. Quiz format MUST match probability-statistics template exactly (3-column cards, KaTeX, grade system)
2. Each quiz MUST have exactly 20 questions
3. Questions MUST cover actual deepdive content (verified by reading deepdive.tex first)
4. Questions MUST include math notation where appropriate ($R^2$, $\sigma$, etc.)
5. PDFs MUST be copied from source directories (not recompiled)
6. Quiz files MUST go in `docs/quiz/` folder (alongside existing quizzes)
7. Navigation MUST be updated in docs/index.html

### Must NOT Have
1. Do NOT modify LaTeX source files (charts already compile correctly)
2. Do NOT change existing quiz files in docs/quiz/
3. Do NOT remove existing quizzes from manifest.json
4. Do NOT add external dependencies to quiz files (self-contained HTML)
5. Do NOT create a separate quiz/ folder at project root (use docs/quiz/)

---

## Task Flow and Dependencies

```
PHASE 1: Fix PDFs (Independent)
[Task 1.1] Copy compiled PDFs to docs (with visual verification)

PHASE 2: Quiz Development (Sequential)
[Task 2.0] Update docs/index.html with Per-Lesson Quizzes section
    |
    v
[Task 2.1] Create quiz template
    |
    v
[Task 2.2-2.7] Create 6 quizzes (can be parallelized after template)
    |           Each task: Read deepdive.tex FIRST, then write questions
    v
[Task 2.8] Update manifest.json

PHASE 3: Verification (Sequential)
[Task 3.1] Verify all deliverables (includes KaTeX local server test)
```

---

## Detailed TODOs

### PHASE 1: Fix PDF Downloads

#### Task 1.1: Copy Compiled PDFs to Docs
**Agent:** executor
**Model:** sonnet
**Estimated Time:** 10 minutes

**Steps:**
1. **Visual Verification First:** Open `slides/L01_Introduction_Linear_Regression/L01_overview.pdf` in a PDF viewer and visually confirm charts are embedded (not blank/missing)
2. Copy all 12 PDFs from source slide directories to docs/slides/pdf/
3. Verify file sizes are correct (deepdive >400KB, overview >400KB)

**Acceptance Criteria:**
- [ ] Visual confirmation: At least one source PDF contains visible charts
- [ ] `docs/slides/pdf/L01_overview.pdf` matches `slides/L01_.../L01_overview.pdf` size
- [ ] All 12 files copied successfully
- [ ] File sizes indicate charts are included

**Commands:**
```bash
# Step 1: Visual verification (executor should open and check one PDF)
# Open slides/L01_Introduction_Linear_Regression/L01_overview.pdf
# Confirm charts are visible, not blank

# Step 2: Copy L01 PDFs
cp "slides/L01_Introduction_Linear_Regression/L01_overview.pdf" "docs/slides/pdf/"
cp "slides/L01_Introduction_Linear_Regression/L01_deepdive.pdf" "docs/slides/pdf/"

# Copy L02 PDFs
cp "slides/L02_Logistic_Regression/L02_overview.pdf" "docs/slides/pdf/"
cp "slides/L02_Logistic_Regression/L02_deepdive.pdf" "docs/slides/pdf/"

# Copy L03 PDFs
cp "slides/L03_KNN_KMeans/L03_overview.pdf" "docs/slides/pdf/"
cp "slides/L03_KNN_KMeans/L03_deepdive.pdf" "docs/slides/pdf/"

# Copy L04 PDFs
cp "slides/L04_Random_Forests/L04_overview.pdf" "docs/slides/pdf/"
cp "slides/L04_Random_Forests/L04_deepdive.pdf" "docs/slides/pdf/"

# Copy L05 PDFs
cp "slides/L05_PCA_tSNE/L05_overview.pdf" "docs/slides/pdf/"
cp "slides/L05_PCA_tSNE/L05_deepdive.pdf" "docs/slides/pdf/"

# Copy L06 PDFs
cp "slides/L06_Embeddings_RL/L06_overview.pdf" "docs/slides/pdf/"
cp "slides/L06_Embeddings_RL/L06_deepdive.pdf" "docs/slides/pdf/"

# Step 3: Verify sizes
ls -la docs/slides/pdf/*.pdf
```

---

### PHASE 2: Quiz Development

#### Task 2.0: Update docs/index.html with Per-Lesson Quiz Navigation
**Agent:** executor
**Model:** sonnet
**Estimated Time:** 15 minutes

**Steps:**
1. Add "Per-Lesson Quizzes" subsection to the Quizzes section in docs/index.html
2. Add links to all 6 new quiz files (L01-L06)
3. Update quiz question count in hero stats (45 -> 165 questions: 45 existing + 120 new)
4. Update sidebar navigation to include per-lesson quizzes

**Acceptance Criteria:**
- [ ] docs/index.html has "Per-Lesson Quizzes" section with 6 cards/links
- [ ] Each link points to correct file: `docs/quiz/L0X_topic.html`
- [ ] Hero stats updated to show 165 quiz questions
- [ ] Sidebar shows per-lesson quiz links

**HTML to Add (after existing quizzes grid):**
```html
<!-- Per-Lesson Quizzes (20 questions each) -->
<h3 style="margin-top:24px;font-size:14px;color:#586069">Per-Lesson Deep Dive Quizzes (120 questions)</h3>
<div class="lgrid" style="grid-template-columns:repeat(3,1fr);margin-top:12px">
<a class="lcard" href="quiz/L01_linear_regression.html" style="border-left:3px solid #3333B2"><span class="lcard-num" style="background:#3333B2;color:white">L01</span><span class="lcard-title">Linear Regression</span><div style="font-size:9px;color:#3333B2;margin-top:4px;font-weight:600">20 questions</div></a>
<a class="lcard" href="quiz/L02_logistic_regression.html" style="border-left:3px solid #0066CC"><span class="lcard-num" style="background:#0066CC;color:white">L02</span><span class="lcard-title">Logistic Regression</span><div style="font-size:9px;color:#0066CC;margin-top:4px;font-weight:600">20 questions</div></a>
<a class="lcard" href="quiz/L03_knn_kmeans.html" style="border-left:3px solid #FF7F0E"><span class="lcard-num" style="background:#FF7F0E;color:white">L03</span><span class="lcard-title">KNN & K-Means</span><div style="font-size:9px;color:#FF7F0E;margin-top:4px;font-weight:600">20 questions</div></a>
<a class="lcard" href="quiz/L04_random_forests.html" style="border-left:3px solid #2CA02C"><span class="lcard-num" style="background:#2CA02C;color:white">L04</span><span class="lcard-title">Random Forests</span><div style="font-size:9px;color:#2CA02C;margin-top:4px;font-weight:600">20 questions</div></a>
<a class="lcard" href="quiz/L05_pca_tsne.html" style="border-left:3px solid #D62728"><span class="lcard-num" style="background:#D62728;color:white">L05</span><span class="lcard-title">PCA & t-SNE</span><div style="font-size:9px;color:#D62728;margin-top:4px;font-weight:600">20 questions</div></a>
<a class="lcard" href="quiz/L06_embeddings_rl.html" style="border-left:3px solid #9467BD"><span class="lcard-num" style="background:#9467BD;color:white">L06</span><span class="lcard-title">Embeddings & RL</span><div style="font-size:9px;color:#9467BD;margin-top:4px;font-weight:600">20 questions</div></a>
</div>
```

---

#### Task 2.1: Create Quiz Template
**Agent:** executor
**Model:** sonnet
**Estimated Time:** 15 minutes

**Steps:**
1. Create `docs/quiz/quiz_template.html` based on probability-statistics format
2. Adapt colors to ML palette (--mlpurple: #3333B2, --mlblue: #0066CC)
3. Update navigation links (Dashboard points to `../index.html`, GitHub link)
4. Parameterize quiz title, questions array

**Acceptance Criteria:**
- [ ] Template uses KaTeX for math rendering
- [ ] 3-column responsive layout
- [ ] Progress tracking with score badge
- [ ] Grade system (A/B/C/D/F) with percentage
- [ ] Self-contained (no external CSS/JS files except CDN KaTeX)
- [ ] Navigation links work (Dashboard: `../index.html`)

**Template Structure:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- KaTeX CDN -->
    <!-- Inline CSS with ML palette -->
</head>
<body>
    <nav class="nav">
        <div class="nav-title">Quiz X: Topic Name</div>
        <div class="nav-links">
            <a href="../index.html">Dashboard</a>
            <a href="https://github.com/Digital-AI-Finance/methods-algorithms">GitHub</a>
        </div>
    </nav>
    <main class="quiz-container">
        <!-- Header, progress, questions grid, results -->
    </main>
    <script>
        const quizData = { questions: [...] };
        // Quiz logic (init, render, answer handling, results)
    </script>
</body>
</html>
```

---

#### Task 2.2: Create L01 Linear Regression Quiz
**Agent:** executor-high
**Model:** opus
**Estimated Time:** 30 minutes

**Content Source:** `slides/L01_Introduction_Linear_Regression/L01_deepdive.tex`

**Step 0: Read and Verify Deepdive Content (MANDATORY)**
Before writing any questions, executor MUST:
1. Read `slides/L01_Introduction_Linear_Regression/L01_deepdive.tex`
2. Extract the actual topics covered in the deepdive slides
3. Adjust question topics below to match ACTUAL content (remove topics not covered, add topics that are)
4. Document which topics from the list below are NOT in deepdive and substitute appropriately

**Proposed Question Topics (20 questions) - verify against deepdive.tex:**
1. Matrix notation (design matrix X, beta vector)
2. OLS assumptions (linearity, exogeneity, homoscedasticity)
3. Normal equation derivation
4. Gradient computation
5. Gradient descent algorithm (update rule)
6. Learning rate selection
7. SGD vs batch gradient descent
8. R-squared interpretation
9. Adjusted R-squared formula
10. RMSE vs MAE comparison
11. Residual analysis
12. Train-test split rationale
13. Cross-validation (K-fold)
14. Ridge regression (L2 penalty)
15. Lasso regression (L1 penalty)
16. Elastic net
17. Lambda selection via CV
18. Bias-variance decomposition
19. Regularization and bias-variance tradeoff
20. Decision framework (when to use linear regression)

**Acceptance Criteria:**
- [ ] Step 0 completed: deepdive.tex read and topics verified
- [ ] 20 questions with 4 options each
- [ ] All questions cover topics ACTUALLY in the deepdive
- [ ] Math notation using KaTeX ($R^2$, $\beta$, $\mathbf{X}$, etc.)
- [ ] Mix of conceptual (40%), computational (30%), application (30%)
- [ ] Explanations for each answer
- [ ] Finance/business context where relevant

---

#### Task 2.3: Create L02 Logistic Regression Quiz
**Agent:** executor-high
**Model:** opus
**Estimated Time:** 30 minutes

**Content Source:** `slides/L02_Logistic_Regression/L02_deepdive.tex`

**Step 0: Read and Verify Deepdive Content (MANDATORY)**
Before writing any questions, executor MUST:
1. Read `slides/L02_Logistic_Regression/L02_deepdive.tex`
2. Extract the actual topics covered in the deepdive slides
3. Adjust question topics below to match ACTUAL content
4. Document which topics from the list below are NOT in deepdive and substitute appropriately

**Proposed Question Topics (20 questions) - verify against deepdive.tex:**
1. Sigmoid function properties
2. Odds and log-odds interpretation
3. Coefficient interpretation (odds ratios)
4. Maximum likelihood estimation
5. Binary cross-entropy loss
6. Gradient of log-loss
7. Decision boundary (linear)
8. Multi-class extensions (one-vs-rest, softmax)
9. Confusion matrix components (TP, FP, TN, FN)
10. Precision definition and use cases
11. Recall (sensitivity) importance
12. F1 score calculation
13. ROC curve interpretation
14. AUC meaning
15. Precision-recall tradeoff
16. Threshold selection
17. Class imbalance handling
18. Regularization in logistic regression
19. Feature scaling importance
20. Decision framework (when to use logistic regression)

**Acceptance Criteria:**
- [ ] Step 0 completed: deepdive.tex read and topics verified
- [ ] Same as Task 2.2
- [ ] Credit scoring examples where appropriate

---

#### Task 2.4: Create L03 KNN & K-Means Quiz
**Agent:** executor-high
**Model:** opus
**Estimated Time:** 30 minutes

**Content Source:** `slides/L03_KNN_KMeans/L03_deepdive.tex`

**Step 0: Read and Verify Deepdive Content (MANDATORY)**
Before writing any questions, executor MUST:
1. Read `slides/L03_KNN_KMeans/L03_deepdive.tex`
2. Extract the actual topics covered in the deepdive slides
3. Adjust question topics below to match ACTUAL content
4. Document which topics from the list below are NOT in deepdive and substitute appropriately

**Proposed Question Topics (20 questions) - verify against deepdive.tex:**
1. KNN algorithm (lazy learning)
2. Distance metrics (Euclidean, Manhattan, Minkowski)
3. Choosing K in KNN
4. KNN decision boundary properties
5. Curse of dimensionality
6. Feature scaling for distance-based methods
7. Weighted KNN
8. K-Means algorithm steps
9. Centroid initialization (K-means++)
10. Convergence criteria
11. Elbow method for K selection
12. Silhouette score interpretation
13. Inertia (within-cluster sum of squares)
14. K-Means limitations (spherical clusters)
15. Voronoi diagrams
16. KNN vs K-Means comparison
17. Computational complexity
18. Handling categorical features
19. Anomaly detection with KNN
20. Customer segmentation application

**Acceptance Criteria:**
- [ ] Step 0 completed: deepdive.tex read and topics verified
- [ ] Same as Task 2.2
- [ ] Distance formula math notation

---

#### Task 2.5: Create L04 Random Forests Quiz
**Agent:** executor-high
**Model:** opus
**Estimated Time:** 30 minutes

**Content Source:** `slides/L04_Random_Forests/L04_deepdive.tex`

**Step 0: Read and Verify Deepdive Content (MANDATORY)**
Before writing any questions, executor MUST:
1. Read `slides/L04_Random_Forests/L04_deepdive.tex`
2. Extract the actual topics covered in the deepdive slides
3. Adjust question topics below to match ACTUAL content
4. Document which topics from the list below are NOT in deepdive and substitute appropriately

**Proposed Question Topics (20 questions) - verify against deepdive.tex:**
1. Decision tree splitting criteria (Gini, entropy)
2. Information gain calculation
3. Tree depth and overfitting
4. Pruning strategies
5. Bootstrap sampling
6. Out-of-bag (OOB) error
7. Random feature selection (mtry)
8. Bagging vs boosting
9. Ensemble voting (majority/averaging)
10. Feature importance (permutation, impurity-based)
11. Variance reduction through ensembles
12. Number of trees selection
13. Max depth hyperparameter
14. Min samples split/leaf
15. Random forest vs single tree
16. Handling missing values
17. Feature interactions
18. Partial dependence plots
19. Fraud detection application
20. Hyperparameter tuning strategy

**Acceptance Criteria:**
- [ ] Step 0 completed: deepdive.tex read and topics verified
- [ ] Same as Task 2.2
- [ ] Gini/entropy formulas with math notation

---

#### Task 2.6: Create L05 PCA & t-SNE Quiz
**Agent:** executor-high
**Model:** opus
**Estimated Time:** 30 minutes

**Content Source:** `slides/L05_PCA_tSNE/L05_deepdive.tex`

**Step 0: Read and Verify Deepdive Content (MANDATORY)**
Before writing any questions, executor MUST:
1. Read `slides/L05_PCA_tSNE/L05_deepdive.tex`
2. Extract the actual topics covered in the deepdive slides
3. Adjust question topics below to match ACTUAL content
4. Document which topics from the list below are NOT in deepdive and substitute appropriately

**Proposed Question Topics (20 questions) - verify against deepdive.tex:**
1. PCA objective (variance maximization)
2. Covariance matrix
3. Eigenvalue decomposition
4. Principal components interpretation
5. Scree plot analysis
6. Explained variance ratio
7. Choosing number of components
8. PCA for noise reduction
9. PCA limitations (linear assumption)
10. Data centering requirement
11. t-SNE objective (probability preservation)
12. Perplexity parameter
13. t-SNE vs PCA comparison
14. t-SNE limitations (no new point projection)
15. Crowding problem and t-distribution
16. Swiss roll problem
17. Reconstruction error
18. Portfolio risk decomposition application
19. High-dimensional visualization
20. When to use PCA vs t-SNE

**Acceptance Criteria:**
- [ ] Step 0 completed: deepdive.tex read and topics verified
- [ ] Same as Task 2.2
- [ ] Eigenvalue/eigenvector notation

---

#### Task 2.7: Create L06 Embeddings & RL Quiz
**Agent:** executor-high
**Model:** opus
**Estimated Time:** 30 minutes

**Content Source:** `slides/L06_Embeddings_RL/L06_deepdive.tex`

**Step 0: Read and Verify Deepdive Content (MANDATORY)**
Before writing any questions, executor MUST:
1. Read `slides/L06_Embeddings_RL/L06_deepdive.tex`
2. Extract the actual topics covered in the deepdive slides
3. Adjust question topics below to match ACTUAL content
4. Document which topics from the list below are NOT in deepdive and substitute appropriately

**Proposed Question Topics (20 questions) - verify against deepdive.tex:**
1. Word embedding concept
2. Word2Vec architectures (CBOW, Skip-gram)
3. Cosine similarity
4. Embedding dimensionality
5. Semantic relationships (king - man + woman)
6. Pre-trained embeddings
7. Fine-tuning embeddings
8. MDP components (S, A, R, P, gamma)
9. Policy definition
10. Value function
11. Q-function
12. Bellman equation
13. Q-learning update rule
14. Exploration vs exploitation
15. Epsilon-greedy strategy
16. Discount factor interpretation
17. Reward shaping
18. Trading agent application
19. Sentiment analysis with embeddings
20. RL challenges (sample efficiency, stability)

**Acceptance Criteria:**
- [ ] Step 0 completed: deepdive.tex read and topics verified
- [ ] Same as Task 2.2
- [ ] Q-learning formula with math notation

---

#### Task 2.8: Update manifest.json
**Agent:** executor
**Model:** sonnet
**Estimated Time:** 10 minutes

**Steps:**
1. Add 6 new quiz entries to manifest.json quizzes array
2. Use consistent format with existing entries
3. Set status to "complete"
4. **CRITICAL:** Use `docs/quiz/` path (NOT `quiz/` or `quizzes/`)

**New Entries:**
```json
{
  "id": "quiz_L01",
  "title": "Quiz: L01 Linear Regression Deep Dive",
  "topics": ["L01"],
  "questions": 20,
  "duration_minutes": 25,
  "file": "docs/quiz/L01_linear_regression.html",
  "status": "complete"
},
{
  "id": "quiz_L02",
  "title": "Quiz: L02 Logistic Regression Deep Dive",
  "topics": ["L02"],
  "questions": 20,
  "duration_minutes": 25,
  "file": "docs/quiz/L02_logistic_regression.html",
  "status": "complete"
},
{
  "id": "quiz_L03",
  "title": "Quiz: L03 KNN & K-Means Deep Dive",
  "topics": ["L03"],
  "questions": 20,
  "duration_minutes": 25,
  "file": "docs/quiz/L03_knn_kmeans.html",
  "status": "complete"
},
{
  "id": "quiz_L04",
  "title": "Quiz: L04 Random Forests Deep Dive",
  "topics": ["L04"],
  "questions": 20,
  "duration_minutes": 25,
  "file": "docs/quiz/L04_random_forests.html",
  "status": "complete"
},
{
  "id": "quiz_L05",
  "title": "Quiz: L05 PCA & t-SNE Deep Dive",
  "topics": ["L05"],
  "questions": 20,
  "duration_minutes": 25,
  "file": "docs/quiz/L05_pca_tsne.html",
  "status": "complete"
},
{
  "id": "quiz_L06",
  "title": "Quiz: L06 Embeddings & RL Deep Dive",
  "topics": ["L06"],
  "questions": 20,
  "duration_minutes": 25,
  "file": "docs/quiz/L06_embeddings_rl.html",
  "status": "complete"
}
```

**Acceptance Criteria:**
- [ ] manifest.json valid JSON (no syntax errors)
- [ ] 6 new quiz entries added
- [ ] All file paths use `docs/quiz/` prefix
- [ ] Existing quiz entries unchanged

---

### PHASE 3: Verification

#### Task 3.1: Verify All Deliverables
**Agent:** architect
**Model:** opus
**Estimated Time:** 20 minutes

**Verification Checklist:**

**PDFs:**
1. PDF file sizes in docs/slides/pdf/ match source
2. Visual verification: Open at least one PDF and confirm charts are visible

**Quizzes:**
3. All 6 quiz HTML files exist in `docs/quiz/`
4. Each quiz loads in browser without errors
5. **KaTeX Testing (specific procedure):**
   - Start local server: `python -m http.server 8000` from project root
   - Open http://localhost:8000/docs/quiz/L01_linear_regression.html in Chrome
   - Verify math notation renders (e.g., $R^2$, $\beta$, fractions)
   - Repeat for at least 2 other quiz files (L03, L06)
   - Test in Firefox as well for cross-browser verification
6. Quiz functionality works (answer, score, results)

**Navigation:**
7. docs/index.html has "Per-Lesson Quizzes" section
8. All 6 quiz links in index.html work (no 404s)
9. Quiz files have working "Dashboard" link back to ../index.html

**Manifest:**
10. manifest.json is valid JSON
11. All 6 new quiz entries present with correct `docs/quiz/` paths

**Commands:**
```bash
# Check PDF sizes
ls -la docs/slides/pdf/*.pdf

# Validate JSON
python -m json.tool manifest.json > /dev/null && echo "Valid JSON"

# Check quiz files exist
ls -la docs/quiz/L0*.html

# Start local server for KaTeX testing
python -m http.server 8000
# Then manually test in browser:
# - http://localhost:8000/docs/quiz/L01_linear_regression.html
# - http://localhost:8000/docs/quiz/L03_knn_kmeans.html
# - http://localhost:8000/docs/quiz/L06_embeddings_rl.html

# Test navigation links
grep -o 'href="quiz/L0[1-6]_[^"]*"' docs/index.html | wc -l
# Should output: 6
```

---

## Commit Strategy

### Commit 1: Fix PDF Downloads
```
Fix: Copy compiled PDFs with charts to docs folder

The docs/slides/pdf/ copies were outdated and missing chart images.
Copied freshly compiled PDFs from source slide directories.

Files: docs/slides/pdf/L0*.pdf (12 files)
```

### Commit 2: Add Quiz Template and Update Index Navigation
```
Add: Quiz template and per-lesson quiz navigation

- Created quiz template based on probability-statistics format
- Updated docs/index.html with Per-Lesson Quizzes section
- Added navigation links for 6 upcoming quizzes

Features: KaTeX math, 3-column cards, progress tracking, A-F grades
```

### Commit 3: Add L01-L02 Quizzes
```
Add: Linear Regression and Logistic Regression quizzes

- Added L01 Linear Regression quiz (20 questions)
- Added L02 Logistic Regression quiz (20 questions)

Content verified against deepdive.tex sources
```

### Commit 4: Add L03-L04 Quizzes
```
Add: KNN/K-Means and Random Forests quizzes

- Added L03 KNN & K-Means quiz (20 questions)
- Added L04 Random Forests quiz (20 questions)

Content verified against deepdive.tex sources
```

### Commit 5: Add L05-L06 Quizzes and Update Manifest
```
Add: PCA/t-SNE, Embeddings/RL quizzes and manifest update

- Added L05 PCA & t-SNE quiz (20 questions)
- Added L06 Embeddings & RL quiz (20 questions)
- Updated manifest.json with 6 new quiz entries

Content verified against deepdive.tex sources
```

---

## Success Criteria

| Metric | Target | Verification |
|--------|--------|--------------|
| PDF size increase | >50% larger | `ls -la docs/slides/pdf/` |
| PDF visual check | Charts visible | Manual inspection |
| Quiz count | 6 files in docs/quiz/ | `ls docs/quiz/L0*.html` |
| Questions per quiz | 20 each | JSON array length |
| KaTeX rendering | Math displays correctly | Local server test in Chrome/Firefox |
| Quiz functionality | All work | Manual browser test |
| Navigation updated | 6 links in index.html | grep count = 6 |
| Manifest validity | Valid JSON + correct paths | `python -m json.tool manifest.json` |

---

## Estimated Total Time
- Phase 1 (PDFs): 10 minutes (includes visual verification)
- Phase 2 (Quizzes): 3 hours (navigation update + template + 6 quizzes with deepdive verification)
- Phase 3 (Verification): 20 minutes (includes KaTeX local server testing)
- **Total: ~3.5 hours**

---

## Notes for Executor

1. **Deepdive Content Verification (CRITICAL):** For each quiz (Tasks 2.2-2.7), you MUST read the corresponding deepdive.tex file FIRST and verify the proposed question topics are actually covered. Remove topics not in the deepdive, add topics that are. Document any changes.

2. **Quiz Location:** All quiz files go in `docs/quiz/` (NOT project root `quiz/` or `quizzes/`). This keeps them with the GitHub Pages site.

3. **Quiz Question Quality:** Each question should test understanding, not just recall. Include:
   - Conceptual questions (Why does X happen?)
   - Computational questions (Calculate Y given Z)
   - Application questions (When would you use X?)

4. **Math Notation:** Use KaTeX delimiters: `$...$` for inline, `$$...$$` for display

5. **Finance Context:** Include banking/finance examples where natural:
   - L01: House price prediction, portfolio factor models
   - L02: Credit scoring, default prediction
   - L03: Customer segmentation
   - L04: Fraud detection
   - L05: Portfolio risk decomposition
   - L06: Sentiment analysis, trading strategies

6. **Distractor Quality:** Wrong options should be plausible mistakes, not obviously wrong

7. **Navigation Links:** Quiz files should link back to `../index.html` (not `../docs/index.html`)

8. **KaTeX Testing:** Use local web server (`python -m http.server 8000`) to test, not file:// protocol which may have CORS issues with KaTeX CDN

---

**PLAN_READY: .omc/plans/fix-charts-add-quizzes.md**
