# Plan: Decision Trees + Random Forests Standalone Slide Decks

## Task Summary

Create two new slide decks in the L04 folder:
1. **L04_dt_mini.tex** — Decision Trees mini-lecture (~10 slides, accessible, TikZ comics)
2. **L04_dt_full.tex** — Decision Trees full technical lecture (~25 slides, going deep)

The existing RF decks (L04_rf_mini.tex, L04_rf_full.tex) already cover Random Forests. This plan creates the missing DT pair, plus 5 new DT-specific chart.py files.

## Existing Assets

| File | Slides | Content |
|------|--------|---------|
| L04_overview.tex | 25 | Combined DT+RF overview |
| L04_deepdive.tex | 42 | Combined DT+RF deep dive |
| L04_rf_mini.tex | 10 | RF mini (WHY-FEEL-WHAT-CASE-HOW-RISK-WHERE-IMPACT-SO_WHAT-ACT) |
| L04_rf_full.tex | 31 | RF full technical (with boosting) |

**Missing:** No standalone Decision Trees deck. The overview covers DT basics in ~5 slides mixed with RF content.

### Existing Charts (reusable for DT)

| Chart | Content | Use in DT? |
|-------|---------|------------|
| 01_decision_tree/chart.py | DT structure (fraud detection) | YES — both mini and full |
| 02_feature_importance/chart.py | RF feature importance | NO (RF-specific) |
| 03_bootstrap/chart.py | Bootstrap sampling | NO (RF-specific) |
| 07_decision_flowchart/chart.py | When to use RF flowchart | NO (RF-specific) |

### New Charts Needed

| ID | Chart | Description | Used In |
|----|-------|-------------|---------|
| 08_gini_split | Gini impurity before/after split | Bar chart: parent G=0.48 (60/40) → left G=0.42 (70/30), right G=0.18 (90/10), weighted=0.276 | dt_mini slide 5, dt_full slide 9 |
| 09_dt_overfitting | DT overfitting vs pruned tree | Train/test error curves vs max_depth | dt_full slide 18 |
| 10_dt_decision_boundary | DT decision boundary (2D) | Axis-aligned splits on scatter plot using sklearn | dt_full slide 12 |
| 11_gini_vs_entropy | Gini vs Entropy curves | Line chart: both criteria plotted as f(p) for p∈[0,1], showing near-identical shape | dt_full slide 10 |
| 12_nonlinear_classes | Non-linearly separable data | Scatter plot: 2 classes in XOR-like pattern that a straight line cannot separate | dt_full slide 6 |

### XKCD Images Available

| Image | File | Use |
|-------|------|-----|
| #1885 ensemble_model | images/1885_ensemble_model.png | Available but NOT used in DT decks (used in RF decks) |
| #1838 machine_learning | images/1838_machine_learning.png | dt_full closing |

---

## Execution Order

1. **Create 5 new chart.py files** (08, 09, 10, 11, 12) and generate chart.pdf
2. **Create L04_dt_mini.tex** (10 slides)
3. **Create L04_dt_full.tex** (~25 slides)
4. **Compile both .tex files** and verify 0 Overfull
5. **Update manifest.json** — add entries for L04_dt_mini.tex, L04_dt_full.tex, and 5 new chart.py files with status "complete"
6. **Update docs/index.html** to add DT deck links
7. **Copy PDFs to docs/slides/pdf/** for GH Pages

---

## Deck 1: L04_dt_mini.tex (10 slides)

### Design Principles
- Follow the 10-slide mini-lecture pattern (WHY-FEEL-WHAT-CASE-HOW-RISK-WHERE-IMPACT-SO_WHAT-ACT)
- BSc accessibility: define ALL terms, plain English first, no Greek in intro
- TikZ stick-figure comics on slides 1 and 6 (opening dilemma + risk scene)
- No XKCD images — TikZ comics only for this mini-lecture
- 2 charts: 01_decision_tree (slide 4) and 08_gini_split (slide 5)
- Question-style titles throughout
- Finance domain: loan approval (simple yes/no decisions)

### Slide-by-Slide Specification

| # | Section | Title | Layout | Content |
|---|---------|-------|--------|---------|
| 1 | WHY | "Why Would a Bank Let a Flowchart Decide Who Gets a Loan?" | TikZ comic | Dilemma: loan officer drowning in 500 applications. Flowchart robot helps. Punchline: "What if the flowchart is wrong?" |
| 2 | FEEL | "You Are the Loan Officer — What Questions Would You Ask?" | Reflection prompt | Students think: income? employment? credit history? Build intuition that a tree is just asking questions in sequence. |
| 3 | WHAT | "What IS a Decision Tree?" | Definition + visual | Plain English: "A flowchart that learns which questions to ask from data." Key terms: node, split, leaf. NO formulas. |
| 4 | CASE | "How Does One Transaction Navigate the Tree?" | Chart + step trace | Use 01_decision_tree/chart.pdf (fraud-detection tree). Trace a single transaction: Amount > $500? → Yes → Time < 2am? → No → Foreign IP? → Yes → FRAUD. Highlight the path in red text next to the chart. |
| 5 | HOW | "How Does the Tree Decide Which Question to Ask First?" | Chart + text | Use 08_gini_split/chart.pdf. Explain Gini intuition: "pick the question that creates the purest groups." Worked example: 100 applicants, 60 repay, 40 default (G=0.48). Split by income: left child 28 repay/12 default out of 40 (G=0.42), right child 54 repay/6 default out of 60 (G=0.18). Weighted = 0.276. Reduction = 0.204. |
| 6 | RISK | "What Happens When the Tree Memorizes the Training Data?" | TikZ comic | Scene: tree with 500 branches (overfit). New applicant arrives, tree says "I've never seen THIS before!" Punchline: "A tree that memorizes can't generalize." |
| 7 | WHERE | "Where Do Banks Actually Use Decision Trees?" | Industry examples | Credit scoring, fraud detection, anti-money laundering. Note: DTs are the building block inside Random Forests. |
| 8 | IMPACT | "Who Wins and Who Loses When Trees Replace Human Judgment?" | Stakeholder map | Winners: consistency, speed, scalability. Losers: edge cases, explainability pressure from regulators. |
| 9 | SO WHAT | "When Should You Use a Single Tree — and When Should You Not?" | Decision framework | Use when: interpretability required, small data, first baseline. Don't use when: high accuracy needed (→ Random Forest), many features (→ prone to overfit). |
| 10 | ACT | "Can You Build This Tree by Hand?" | Exercise + TikZ closing comic | Given 6 loan applicants with 2 features, manually build a 2-level tree. Scaffolded step-by-step. Bottom: small TikZ comic — stick figure with a tree diagram saying "I grew my first tree!" (closing comic per beamer skill rule). |

### Preamble
Copy from L04_rf_mini.tex (identical preamble with Madrid theme, TikZ libraries, custom colors).

---

## Deck 2: L04_dt_full.tex (~25 slides)

### Design Principles
- PMSP framework: Introduction → Problem → Method → Solution → Decision Framework → Practice → Summary
- Three-zone architecture: INTRO (slides 1-5, no Greek) → CORE (slides 6-19, formulas) → CLOSING (slides 20-25)
- MSc depth: 2+ derivations (Gini, entropy, information gain), worked numerical examples, pseudocode
- Charts (6 total, ratio 25:6 = 1:4.2 ✓): 12_nonlinear_classes (slide 6), 01_decision_tree (slide 7), 08_gini_split (slide 9), 11_gini_vs_entropy (slide 10), 10_dt_decision_boundary (slide 12), 09_dt_overfitting (slide 18)
- XKCD: opening TikZ comic (slide 2), closing #1838 (slide 25)
- Finance domain: credit scoring with realistic data
- Question-style titles
- At least 8 distinct layout patterns

### Notation Table

| Symbol | Meaning | First Use |
|--------|---------|-----------|
| G(p) | Gini impurity | Slide 8 |
| H(p) | Entropy | Slide 10 |
| IG | Information gain | Slide 11 |
| D | Dataset | Slide 8 |
| D_L, D_R | Left/right child datasets after split | Slide 8 |
| p_k | Proportion of class k in node | Slide 8 |
| α | Cost-complexity pruning parameter | Slide 17 |

### Slide-by-Slide Specification

**INTRO ZONE (slides 1-5, no formulas)**

| # | Section | Title | Layout | Content |
|---|---------|-------|--------|---------|
| 1 | — | Title Page | Title | "Decision Trees: From Questions to Predictions" |
| 2 | Intro | "A Loan Officer Asks Three Questions and Decides in 30 Seconds" | TikZ comic (L8 mixed media) | SCQ: Situation=banks process millions of loans. Complication=humans are slow and inconsistent. Question=can we automate this? TikZ: officer with thought bubbles "Income?", "Credit?", "Employed?" |
| 3 | Intro | Learning Objectives | Full width (L7) | 4 LOs at Bloom 4+: (1) Derive Gini impurity and information gain from first principles, (2) Analyze how recursive partitioning builds a tree, (3) Evaluate overfitting using pruning strategies, (4) Compare DTs with linear models for interpretability vs accuracy |
| 4 | Intro | "What Is a Decision Tree in Plain English?" | Two cols text (L3) | Left: "A flowchart that learns from data." Analogy: 20-questions game. Right: Key vocabulary: root, internal node, leaf, split, depth, branch. NO formulas yet. |
| 5 | Intro | "Where Do Decision Trees Fit in ML?" | Comparison (L10) | Left: Parametric (linear/logistic regression) — learn fixed coefficients. Right: Non-parametric (decision trees) — learn flexible rules. Bridge: "DTs are building blocks for Random Forests (next lecture)." |

**CORE ZONE — METHOD (slides 6-16, formulas allowed)**

| # | Section | Title | Layout | Content |
|---|---------|-------|--------|---------|
| 6 | Problem | "Why Can't a Straight Line Separate These Borrowers?" | Chart + text (L22) | Use 12_nonlinear_classes/chart.pdf. Scatter plot: 2 borrower classes in XOR-like pattern. "A straight line can't separate these — but axis-aligned splits can." Motivate non-linear boundaries. |
| 7 | Method | "What Does a Trained Decision Tree Look Like?" | Full-size chart (L21) | Use 01_decision_tree/chart.pdf. Annotate: root question, Yes/No branches, leaf predictions with confidence. |
| 8 | Method | "How Does the Tree Choose the Best Split? (Gini Impurity)" | Definition-Example (L9) | Left: Formula G(p) = 1 - Σ p_k². Right: Worked example — 100 applicants, 60 repay, 40 default → G = 1 - (0.6² + 0.4²) = 0.48. |
| 9 | Method | "Which Split Reduces Impurity the Most?" | Chart + text (L22) | Use 08_gini_split/chart.pdf. Show weighted Gini before/after. Worked example: parent G=0.48, left child (70/30) G=0.42, right child (90/10) G=0.18, weighted = (40/100)×0.42 + (60/100)×0.18 = 0.276. Reduction = 0.48 - 0.276 = 0.204. |
| 10 | Method | "What Does Entropy Add Beyond Gini?" | Chart + text (L22) | Use 11_gini_vs_entropy/chart.pdf. Left: H(p) = -Σ p_k log₂(p_k). Same example: H = -(0.6 log₂ 0.6 + 0.4 log₂ 0.4) = 0.971 bits. Right: Chart shows both curves — nearly identical shape, entropy penalizes impure nodes slightly more. |
| 11 | Method | "Information Gain: The Decision Rule" | Formula reference (L12) | IG(D, feature) = H(D) - Σ |D_v|/|D| × H(D_v). "Choose the feature with highest IG at each node." Worked example with 2 candidate features. |
| 12 | Method | "How Does the Tree Partition Feature Space?" | Full-size chart (L21) | Use 10_dt_decision_boundary/chart.pdf. 2D scatter with axis-aligned decision boundaries. Annotate: each rectangle = one leaf. |
| 13 | Method | "The Recursive Partitioning Algorithm" | Code example (L17) | Pseudocode: GROW-TREE(D, features): if stopping criterion met → return leaf. For each feature: find best split. Pick best overall. Partition D into D_L, D_R. Recurse on children. |
| 14 | Method | "What Are the Stopping Rules?" | Three-way split (L6) | Max depth, min samples per leaf, min impurity decrease. Each with trade-off explanation. |

**CORE ZONE — SOLUTION (slides 15-19)**

| # | Section | Title | Layout | Content |
|---|---------|-------|--------|---------|
| 15 | Solution | "Interpreting the Tree: What Does Each Path Mean?" | Step-by-step (L11) | Trace 3 different loan applicants through the tree. Each path = an interpretable rule: "IF income > 50k AND credit > 700 THEN approve (confidence: 92%)." |
| 16 | Solution | "Reading Feature Importance from a Single Tree" | Two cols text (L3) | MDI (Mean Decrease in Impurity): features used near the root matter most. Example: income is root → most important. Compare with permutation importance. |
| 17 | Solution | "The Overfitting Problem: Why Deep Trees Memorize" | Two cols text (L3) | Left: Deep tree = perfect train accuracy, poor test accuracy. Right: Pruning strategies: pre-pruning (stop early) vs post-pruning (grow then cut). Cost-complexity pruning: minimize (error + α × |tree size|). |
| 18 | Solution | "Can You See the Overfitting?" | Chart + text (L22) | Use 09_dt_overfitting/chart.pdf. Train/test error vs max_depth. Sweet spot where test error is minimized. Cross-validation to find optimal depth. |
| 19 | Solution | "Regression Trees: Predicting Numbers, Not Categories" | Definition-Example (L9) | Same algorithm, different criterion: MSE instead of Gini. Worked example: predict house price. Leaf prediction = mean of training samples in that leaf. |

**CLOSING ZONE (slides 20-25)**

| # | Section | Title | Layout | Content |
|---|---------|-------|--------|---------|
| 20 | Decision | "When to Use a Decision Tree — and When Not To" | Pros/Cons (L18) | Pros: interpretable, handles mixed features, no scaling needed, fast. Cons: high variance, overfitting, axis-aligned only, unstable (small data change → different tree). Bridge: "These weaknesses motivate Random Forests." |
| 21 | Decision | "DT vs Logistic Regression for Credit Scoring" | Comparison (L10) | Head-to-head: interpretability (DT=visual path, LR=coefficients), non-linearity (DT=yes, LR=no), stability (DT=low, LR=high), regulatory acceptance (DT=harder, LR=established). |
| 22 | Practice | "Hands-on: Build a Credit Scoring Tree" | Full width (L7) | Exercise: sklearn DecisionTreeClassifier on credit data. Steps: (1) fit, (2) visualize with plot_tree, (3) calculate train/test accuracy, (4) prune and compare. Link to Colab notebook. |
| 23 | Summary | "Key Takeaways" | Summary two cols (L13) | Left: concepts (Gini, entropy, IG, recursive partitioning, pruning). Right: practical (interpret paths, choose depth, when DT vs other models). |
| 24 | Summary | "What's Next: From One Tree to a Forest" | Full width (L7) | Bridge to RF: "A single tree overfits. What if we grew 500 different trees and let them vote?" Teaser for Random Forests lecture. |
| 25 | Summary | "Closing Thought" | Mixed media (L8) | XKCD #1838 image + quote: "We asked three questions and predicted default with 85% accuracy. Imagine what 500 trees can do." |

### Preamble
Copy from L04_rf_full.tex (identical preamble with Madrid theme, TikZ libraries, algorithm/algorithmic packages, custom colors).

---

## New Chart Specifications

### 08_gini_split/chart.py

**Purpose:** Visualize Gini impurity before and after a split
**Type:** Grouped bar chart
**Data:** Parent node: 100 applicants, 60 repay, 40 default → Gini=0.48. Left child: 40 applicants (28 repay, 12 default) → Gini=0.42. Right child: 60 applicants (54 repay, 6 default) → Gini=0.18. Weighted = (40/100)×0.42 + (60/100)×0.18 = 0.276.
**Annotations:** Arrow showing "Impurity reduction = 0.204"
**Colors:** MLPurple for parent, MLBlue for children, MLGreen for weighted
**Output:** chart.pdf in 08_gini_split/

### 09_dt_overfitting/chart.py

**Purpose:** Show train vs test error as max_depth increases
**Type:** Line chart with two curves
**Method:** sklearn DecisionTreeClassifier on make_classification(n_samples=500, n_features=10)
**X-axis:** max_depth (1 to 20)
**Y-axis:** Classification error (1 - accuracy)
**Annotations:** Vertical dashed line at optimal depth, "Underfitting" and "Overfitting" zone labels
**Colors:** MLBlue for train, MLOrange for test
**Output:** chart.pdf in 09_dt_overfitting/

### 10_dt_decision_boundary/chart.py

**Purpose:** Show axis-aligned decision boundaries of a DT on 2D data
**Type:** Scatter plot with rectangular decision regions
**Method:** sklearn DecisionTreeClassifier(max_depth=3) on make_classification(n_features=2, n_redundant=0)
**Plot:** Background colored by predicted class, scatter points by true class
**Annotations:** "Each rectangle = one leaf node"
**Colors:** MLBlue/MLOrange for classes, light fill for regions
**Output:** chart.pdf in 10_dt_decision_boundary/

### 11_gini_vs_entropy/chart.py

**Purpose:** Compare Gini impurity and Entropy as functions of class probability
**Type:** Line chart with 2 curves
**Data:** For binary classification, plot p from 0 to 1: Gini(p) = 2p(1-p), Entropy(p) = -p log₂(p) - (1-p) log₂(1-p). Scale entropy by 0.5 so both peak at ~0.5 for visual comparison.
**X-axis:** Class probability p (0 to 1)
**Y-axis:** Impurity measure
**Annotations:** Peak at p=0.5, note "Nearly identical ranking of splits"
**Colors:** MLPurple for Gini, MLOrange for Entropy
**Output:** chart.pdf in 11_gini_vs_entropy/

### 12_nonlinear_classes/chart.py

**Purpose:** Show data that a straight line cannot separate but axis-aligned splits can
**Type:** Scatter plot
**Method:** Generate XOR-like pattern using make_classification or manual 4-cluster placement: class 0 at (low, low) and (high, high), class 1 at (low, high) and (high, low)
**Annotations:** Dashed diagonal line with "Linear boundary fails", dotted axis-aligned lines showing "DT splits here"
**Colors:** MLBlue for class 0, MLOrange for class 1
**Output:** chart.pdf in 12_nonlinear_classes/

---

## Verification

1. All 5 chart.py files (08, 09, 10, 11, 12) generate chart.pdf without errors
2. Both .tex files compile with `pdflatex -interaction=nonstopmode` — 0 errors
3. Grep for "Overfull" — must be 0
4. Count slides: dt_mini = 10 frames, dt_full = 25 frames
5. Count charts: dt_mini uses 2 (01, 08), dt_full uses 6 (01, 08, 09, 10, 11, 12) — ratio 25:6 = 1:4.2 ✓
6. Count cartoons: dt_mini has 3 TikZ comics (slides 1, 6, 10), dt_full has 1 TikZ + 1 XKCD #1838
7. All worked examples use CONSISTENT numbers: parent=100 applicants (60 repay, 40 default), G=0.48
8. manifest.json updated with all new assets
9. PDFs copied to docs/slides/pdf/ and index.html updated

## Acceptance Criteria

- [ ] L04_dt_mini.tex exists with 10 slides, 3 TikZ comics (opening, risk, closing), 2 charts, finance examples
- [ ] L04_dt_full.tex exists with ~25 slides, 6 charts (1:4.2 density), 2+ derivations, worked examples
- [ ] 5 new chart.py files (08, 09, 10, 11, 12) generate valid chart.pdf
- [ ] Both PDFs compile with 0 Overfull warnings
- [ ] Every formula slide has a worked numerical example
- [ ] Gini numbers consistent everywhere: parent G=0.48, left G=0.42, right G=0.18, weighted=0.276
- [ ] BSc accessibility: no jargon without definition, plain English in intro zone
- [ ] MSc depth: Gini derivation, entropy derivation, IG, pruning, pseudocode
- [ ] XKCD #1838 image used in dt_full closing (no XKCD in dt_mini — TikZ only)
- [ ] manifest.json updated with all new entries
- [ ] docs/slides/pdf/ updated, docs/index.html has links to both new decks
- [ ] No new slides in any EXISTING .tex files (only NEW files created)
