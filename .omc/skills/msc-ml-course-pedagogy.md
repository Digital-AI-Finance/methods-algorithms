---
id: msc-ml-course-pedagogy
name: MSc ML Course Pedagogical Framework
description: Complete pedagogical architecture for the Methods & Algorithms MSc Data Science course - extracted from 44 tex files, 6 instructor guides, 16 quizzes, and 1063+ slide frames across L00-L06
source: extracted from full course audit (L00-L06, all deck types, all 44 .tex files)
triggers:
  - "course pedagogy"
  - "teaching structure"
  - "lecture design"
  - "slide pedagogy"
  - "PMSP framework"
  - "three-zone"
  - "Bloom's taxonomy"
  - "learning objectives"
  - "course architecture"
quality: verified across 44 .tex files with 1063+ frames
scope: project
---

# MSc ML Course: Complete Pedagogical Framework

## The Insight

This MSc course uses a layered pedagogical system where EVERY design choice - from frame titles phrased as questions, to the three-zone formula-free introduction, to the XKCD opening/closing bookends - serves a specific cognitive purpose. The system was refined through hostile review (67.7→90+ score), multiple Critic iterations, and Architect verification. The key principle: **students learn algorithms by encountering the PROBLEM first (in plain language), then the METHOD (with formulas), then applying the SOLUTION (with code)** - never the reverse.

## Why This Matters

Without this framework:
- Slides become formula dumps that lose students in the first 10 minutes
- Charts appear without context, becoming decoration rather than teaching tools
- Learning objectives sit at Bloom's Level 1-2 (remember/understand) instead of 4-5 (analyze/evaluate)
- Finance applications feel bolted-on rather than woven through the narrative
- Students cannot transfer knowledge across algorithms because each lecture feels disconnected

## Recognition Pattern

Use this skill when:
- Creating or modifying ANY slide deck for this course
- Reviewing lecture content for pedagogical quality
- Designing new lectures or standalone decks
- Creating quizzes, assignments, or instructor guides
- Evaluating whether content meets MSc-level standards

---

## Part 1: Course Architecture

### 1.1 Course Progression (L00-L06)

| ID | Topic | Type | Difficulty | Finance Case |
|----|-------|------|------------|--------------|
| L00 | Prerequisites | Foundation mini-lectures | 0 | N/A (linear algebra, ML taxonomy) |
| L01 | Linear Regression | Parametric supervised | 1 | Property valuation, CAPM |
| L02 | Logistic Regression | Parametric classification | 1 | Credit scoring, Basel PD |
| L03 | KNN & K-Means | Non-parametric + unsupervised | 2 | Fraud detection, customer segmentation |
| L04 | Random Forests | Ensemble methods | 2 | Fraud detection with feature importance |
| L05 | PCA & t-SNE | Dimensionality reduction | 3 | Portfolio risk, yield curve factors |
| L06 | Embeddings & RL | Modern methods | 4 | Sentiment analysis, algorithmic trading |

**Progression logic**: prerequisites → parametric → non-parametric → ensemble → dimensionality reduction → modern. Each lecture builds on concepts from previous ones. Difficulty multipliers (0,1,1,2,2,3,4) reflect complexity jumps. L00 provides mathematical foundations assumed by L01+.

### 1.2 Slide Deck Ecosystem (10 Types, 44 .tex files)

Each topic has multiple deck types serving different pedagogical purposes:

| Type | Slides | Purpose | Structure | Example |
|------|--------|---------|-----------|---------|
| **Overview** | ~24 | Main lecture, gentle intro | Three-zone + PMSP | L01_overview.tex |
| **Deepdive** | ~42-68 | Full math, proofs | Three-zone + PMSP + Appendix | L01_deepdive.tex |
| **Topic Mini** | 10 | Single-algorithm primer | Standalone, dense, TikZ diagrams | L01_linreg_mini.tex |
| **Prerequisite Mini** | 10 | Course foundation material | Standalone, pgfplots + TikZ | P01_linear_algebra_mini.tex |
| **Full** | 25 | Single-algorithm deep lecture | Standalone, focused | L01_linreg_full.tex |
| **Top-10/20** | 27 | Chart-only visual reference | 3 sections, chart-per-slide | L04_dt_rf_top10.tex |
| **Simple Narrative** | 25 | Chart-first discovery learning | 3-act narrative | L05_pca_simple.tex |
| **Self-Study** | N/A | Reading material (article class) | Continuous prose, wrapfigures | L02_selfstudy.tex |
| **Self-Study Intro** | N/A | Introductory reading (article) | Shorter, gentler prose | L02_selfstudy_intro.tex |
| **Accessible** | ~28 | Simplified for broader audience | Reduced math, more visuals | L03_overview_accessible.tex |

**File count per topic**: L00=3, L01=4, L02=6, L03=9, L04=7, L05=8, L06=7 → **44 total**

**Key rules**:
- Every type has a self-contained preamble. No `\input{}` dependencies.
- Self-study types use `\documentclass[10pt]{article}` (not Beamer).
- Prerequisite minis load extra packages: `pgfplots`, `colortbl`, extended TikZ libraries.

### 1.3 Three-Zone Architecture

Every overview and deepdive follows this mandatory structure:

```
ZONE 1: INTRODUCTION (NO formulas, NO Greek letters)
├── Title page
├── Outline / TOC
├── Opening XKCD cartoon (with CC BY-NC 2.5 attribution)
├── SCQ opening (Situation-Complication-Question)
├── Plain-language concept introduction
├── Finance motivation
└── Learning Objectives (Bloom's 4-5)

ZONE 2: CORE CONTENT (PMSP framework, formulas allowed)
├── Section: Problem (business motivation)
├── Section: Method (formulas, algorithms, key equations)
├── Section: Solution (interpretation, evaluation, metrics)
└── Section: Decision Framework (when to use, pros/cons)

ZONE 3: WRAP-UP
├── Practice slide (Colab notebook, exercises)
├── Summary / Key Takeaways (two-column)
├── Closing XKCD / comic callback
└── References
```

**Deepdive addition**: `\appendix` section after Zone 3 with `\section*{Advanced Topics}` containing proofs, convergence theory, and advanced finance applications. The `\section*` hides from TOC.

---

## Part 2: Pedagogical Patterns

### 2.1 Question-Driven Frame Titles

**EVERY frame title is a question**, not a statement. This activates curiosity before content delivery.

| BAD (statement) | GOOD (question) |
|-----------------|-----------------|
| "Decision Tree Classification" | "How Does a Decision Tree Classify?" |
| "Gradient Descent Algorithm" | "How Does the Computer Learn?" |
| "ROC Curve and AUC" | "How Do We Measure Model Quality?" |
| "Regularization Overview" | "How Do We Prevent Overfitting?" |
| "Bias-Variance Tradeoff" | "Why Can't We Minimize Both Errors?" |
| "Feature Importance" | "Which Features Matter Most?" |

**Exceptions** (only these): Title page, Outline, References, Appendix dividers, Summary/Key Takeaways.

### 2.2 SCQ Opening (Situation-Complication-Question)

Slide 3 of every overview uses the McKinsey SCQ framework:

```latex
\begin{frame}[t]{Can a Computer Learn to Predict Prices?}  % The Question
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Situation:} Banks approve millions of mortgage applications...
\textbf{Complication:} Manual appraisals are slow, expensive...
\textbf{Question:} Can we build a model that predicts value automatically?
\column{0.48\textwidth}
\includegraphics[width=0.45\textwidth]{images/XKCD.png}
\end{columns}
\bottomnote{XKCD \#NNNN by Randall Munroe (CC BY-NC 2.5)}
\end{frame}
```

The XKCD image sits beside the SCQ text, creating visual+narrative engagement simultaneously.

### 2.3 Bloom's Taxonomy Enforcement

All Learning Objectives use Bloom's Level 4-5 verbs:

| Level | Verbs Used | Example |
|-------|-----------|---------|
| 4 (Analyze) | Analyze, Compare, Distinguish | "Analyze the bias-variance tradeoff in KNN as a function of K" |
| 5 (Evaluate) | Evaluate, Critique, Justify | "Evaluate cluster validity using silhouette analysis" |
| 4 (Apply/Derive) | Derive, Prove, Apply | "Derive the MLE for logistic regression" |

**Never used**: Remember, Define, List, Describe (Level 1-2). These are banned from MSc learning objectives.

The bottomnote on LO slides always states: `Bloom's Level 4-5: [verbs used]`

### 2.4 Bottomnote System

**EVERY content slide has a `\bottomnote{}`** - no exceptions. This is the single most consistent pattern across all 1063 frames.

Bottomnotes serve 5 distinct purposes:

| Purpose | Example | When |
|---------|---------|------|
| **Key takeaway** | "The bias-variance tradeoff guides model complexity decisions" | Formula/concept slides |
| **Practical guidance** | "Always evaluate on held-out test data" | Method slides |
| **Interpretation aid** | "Coefficients show marginal effect, holding others constant" | Results slides |
| **Forward pointer** | "Foundation for all supervised learning methods" | Summary slides |
| **Attribution** | "XKCD #1725 by Randall Munroe (CC BY-NC 2.5)" | Comic slides |

**Think of bottomnotes as**: a teaching assistant whispering the one thing the student should take away from this slide.

### 2.5 XKCD Bookend Pattern

**Opening AND closing comic** in every lecture. The closing comic creates a **callback** to the opening:

| Lecture | Opening XKCD | Closing Callback |
|---------|-------------|-----------------|
| L01 | #1725 Linear Regression | Text callback: "fitting a line is an art" |
| L02 | #1132 Frequentist/Bayesian | "Now you can answer with a probability" |
| L03 | #1838 Machine Learning + #2731 K-Means | "classify the known, discover the unknown" |
| L04 | #1885 Ensemble Model + #1838 ML | Quote callback to ensemble model |
| L05 | #2048 Curve Fitting | #2400 Statistics callback |
| L06 | #1838 Machine Learning | **TikZ robot illustration** with L01-L06 toolbelt: "Six lectures, one toolkit" |

The callback pattern creates **narrative closure** - students leave with the emotional memory of the comic linked to the intellectual content.

**L06 closing variant**: Instead of a second XKCD image, L06 uses a custom TikZ stick-figure robot with labeled toolbelt items for each lecture (L01: Regression, L02: Classification, etc.), creating a visual "course complete" moment. This is the only lecture that replaces the closing XKCD with a TikZ illustration.

### 2.6 Finance Application Threading

Finance is NOT a bolted-on section - it's woven throughout every lecture:

- **Opening SCQ**: Finance scenario (banks, mortgages, fraud)
- **LO slide**: "Finance Applications: [specific case]"
- **Problem section**: Business motivation from finance
- **Method section**: Formulas use finance notation where possible
- **Solution section**: Metrics relevant to finance (Gini, Basel PD)
- **Practice**: Exercises use finance datasets
- **Appendix**: Extended finance application (CAPM, credit scoring)

**L02 exemplar**: Credit scoring appears in 8 of 24 overview slides, including sigmoid interpretation, odds ratios, Basel PD requirements, and Gini coefficient.

### 2.7 Chart-First Pedagogy

In narrative/simple decks (L05_pca_simple.tex pattern):

```
1. Show the chart (centered, 0.55-0.65\textwidth)
2. \vspace{-2mm}
3. Interpretive bullets (2-3 items) BELOW the chart
4. \bottomnote{key insight}
```

The student sees the PATTERN in data before hearing the EXPLANATION. This activates visual reasoning before symbolic reasoning.

In overview/deepdive decks, charts can appear in Layout 22 (chart+text) or Layout 21 (full-width chart only).

### 2.8 Formula Progression

Formulas are introduced with a strict escalation:

| Zone | Math Level | Example |
|------|-----------|---------|
| Zone 1 (Intro) | Zero formulas, zero Greek | "Price goes up as size increases" |
| Zone 1→2 transition | Simple algebra with letters | $y = a + b \times x$ |
| Zone 2 (Core) | Full formulas with Greek | $\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ |
| Zone 2 (Core) | Worked numerical examples | "A 100 sqm apartment: 50,000 + 200 × 100 = 70,000" |
| Deepdive | Full derivations | Taking derivatives, setting to zero, proving optimality |
| Appendix | Proof sketches | Gauss-Markov theorem, convergence rates |

**Critical rule**: Every formula slide must have a worked numerical example OR an interpretation in plain language.

### 2.9 Comparison Pattern

When introducing two related concepts (common across the course):

```latex
\begin{frame}[t]{Question comparing A and B?}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Concept A}
\begin{itemize}
  \item Property 1
  \item Property 2
  \item Property 3
\end{itemize}
\column{0.48\textwidth}
\textbf{Concept B}
\begin{itemize}
  \item Property 1
  \item Property 2
  \item Property 3
\end{itemize}
\end{columns}
\bottomnote{Key difference or decision criterion}
```

Used for: Normal Equation vs Gradient Descent, Ridge vs Lasso, Supervised vs Unsupervised, KNN vs K-Means, ROC vs PR curves, AIC vs BIC.

### 2.10 Pseudocode Pattern

Formal algorithm descriptions use the `algorithmic` package (6 deepdive/full files: L02, L03, L04, L06):

```latex
\begin{algorithmic}[1]
\STATE \textbf{Input}: Training set $\mathcal{D}$, query point $\mathbf{x}$, ...
\STATE Compute $d(\mathbf{x}, \mathbf{x}_i)$ for all $\mathbf{x}_i \in \mathcal{D}$
\IF{condition}
\STATE action
\ENDIF
\STATE \textbf{return} result
\end{algorithmic}
```

Line numbers (`[1]`) are always enabled. Complexity statement follows below the algorithm block.

### 2.11 TikZ Diagram Pattern

27 of 44 tex files use TikZ for in-slide diagrams. Common uses:

| Use | Example | Files |
|-----|---------|-------|
| **Decision flowcharts** | Algorithm selection trees | All overview + full decks |
| **Custom illustrations** | Robot with toolbelt (L06 closing) | L06_overview.tex |
| **Comic-style figures** | Stick figures, speech bubbles | Mini + prerequisite decks |
| **Concept diagrams** | Neural network layouts, tree structures | Deepdive decks |

Prerequisite minis load extended TikZ libraries: `arrows.meta`, `positioning`, `shapes.callouts`, `shapes.geometric`, `decorations.pathreplacing`. Standard decks load only base TikZ.

### 2.12 Tabular Comparison Pattern

`booktabs` tables (`\toprule`, `\midrule`, `\bottomrule`) are used extensively for structured comparisons. Every lecture has at least one comparison table slide. Common patterns:

- **Algorithm comparison**: KNN vs K-Means, PCA vs t-SNE, Static vs Contextual embeddings
- **Complexity table**: Training/Prediction time complexity per method
- **Method selection**: Objectivity/Speed/Best-For columns

---

## Part 3: Layout Diversity

### 3.1 Minimum Layout Variety

A 25-slide deck must use **8+ distinct layout patterns** (verified via hostile review). No two consecutive slides should share the same layout.

### 3.2 Core Layout Patterns

| ID | Name | Structure | Use For |
|----|------|-----------|---------|
| 1 | Title | `\titlepage` | Opening only |
| 3 | Two-col text | `\begin{columns}` 48/48 | Concept comparisons |
| 4 | Two-col math | Columns with equations | Definition + Example |
| 6 | Three-way split | 31/31/31 columns | Three variants (Ridge/Lasso/EN) |
| 7 | Full-width text | No columns | Roadmaps, explanations |
| 8 | Mixed media | Text + image columns | SCQ opening |
| 9 | Definition-Example | Left: formula, Right: worked example | Formal definitions |
| 10 | Comparison | Two columns with contrasting content | A vs B decisions |
| 11 | Step-by-step | Numbered steps across columns | Algorithms, procedures |
| 12 | Formula reference | Three-column equation sheet | Summary/cheat sheet |
| 13 | Summary two-col | Key Concepts + Practical Guidance | Final takeaway |
| 18 | Pros/Cons | Green + / Orange - | Decision frameworks |
| 20 | References | Two-col: Textbooks + Online | Last slide |
| 21 | Full-size chart | Centered chart, 0.65\textwidth | Chart-only slides |
| 22 | Chart + bullets | Chart above, bullets below | Chart interpretation |

### 3.3 Chart Density Rule

**1 chart per 4 slides** is the governing ratio. A 25-slide deck should have 5-7 charts. Verified across all deck types:

| Deck Type | Slides | Charts | Ratio |
|-----------|--------|--------|-------|
| Overview | ~24 | 5-7 | 1:3.4-4.8 |
| Deepdive | ~42-68 | 7-8 | 1:5-8 |
| Full | 25 | 5-7 | 1:3.5-5 |
| Top-10/20 | 27 | 20 | 1:1.35 (special) |
| Simple narrative | 25 | 8 | 1:3.1 |

### 3.4 Chart Allocation Rule

**Each chart.py belongs to exactly ONE tex file.** No chart is shared between decks. If two decks need the same visualization, they reference the same chart folder. The Critic caught a dual-assignment bug during L01 restructuring.

---

## Part 4: Slide Formatting Rules

### 4.1 Content Density

- **Max 3-4 bullets** per slide (overflow prevention)
- Use `\compactlist` for slides needing 5+ items (2pt itemsep)
- Chart widths: **0.55\textwidth** (with text) or **0.65\textwidth** (standalone)
- `\highlight{keyword}` for key terms (renders as orange bold)
- `[t]` alignment on all content frames: `\begin{frame}[t]{Title}`

### 4.2 Mandatory Structural Elements

Every overview/deepdive MUST include:
1. Title page (slide 1)
2. Outline with `\tableofcontents` (slide 2)
3. Opening XKCD (slide 3)
4. Learning Objectives with Bloom's 4-5 verbs (slide 4-7)
5. PMSP sections: `\section{Problem}`, `\section{Method}`, `\section{Solution}`
6. Decision Framework slide (flowchart or pros/cons)
7. Practice slide (Colab link, exercises)
8. Summary/Key Takeaways
9. Closing comic/callback
10. References

### 4.3 Appendix Structure (Deepdive Only)

```latex
\appendix
\section*{Advanced Topics}  % \section* hides from TOC

% Section divider slide
\begin{frame}[t]
\vfill
\centering
\begin{beamercolorbox}[sep=8pt,center]{title}
\usebeamerfont{title}\Large Appendix: Advanced Topics and Proofs\par
\vspace{0.3em}
\normalsize These slides are supplementary material for self-study
\end{beamercolorbox}
\vfill
\end{frame}

% Content slides...
```

Appendix contains: proofs (Gauss-Markov, convergence), finance applications (CAPM, Basel details), advanced theory (Bayesian interpretation, Firth's method).

### 4.4 Preamble Template (All Beamer Files)

Every Beamer file copies a self-contained preamble with these exact elements:

1. **Document class**: `\documentclass[8pt,aspectratio=169]{beamer}` + `\usetheme{Madrid}`
2. **Packages**: graphicx, booktabs, adjustbox, multicol, amsmath, amssymb, tikz, hyperref, algorithm, algorithmic
3. **Colors**: 7 ML colors (mlblue, mlpurple, mllavender/2/3/4, mlorange, mlgreen, mlred, mlgray) + uppercase aliases (MLPurple, etc.)
4. **Madrid theme colors**: 4 palette overrides + structure, toc, title, frametitle, block title/body
5. **Footer**: 3-column (Methods and Algorithms | MSc Data Science | page/total)
6. **Custom commands**: `\bottomnote{}`, `\highlight{}`, `\mathbold{}`
7. **Optional**: `\compactlist` environment (defined when needed), `\compactmath`, pgfplots

The preamble is ~100 lines and identical across all Beamer files. Changes to the template must be propagated to all 38 Beamer files (6 article-class files excluded).

---

## Part 5: Instructor Guide Pattern

Every lecture has an instructor guide (`L0X_instructor_guide.md`) with:

### 5.1 Session Overview Table

```markdown
| Aspect | Details |
|--------|---------|
| **Duration** | 3 hours |
| **Topic** | [Topic name] |
| **Finance Case** | [Specific use case] |
| **Prerequisites** | [Prior lectures + skills] |
```

### 5.2 PMSP Time Allocation

| Phase | Duration | Content |
|-------|----------|---------|
| Problem | 15 min | Business motivation, discussion questions |
| Method | 45 min | Core concepts, algorithms, common misconceptions |
| Solution | 45 min | Implementation walkthrough, live coding |
| Practice | 75 min | Hands-on notebook, exercises |

### 5.3 Common Misconceptions Section

Each guide lists 3-5 misconceptions specific to the topic:
- L01: "R-squared always increases means model improves"
- L02: "Accuracy is a good metric for imbalanced data"
- L03: "KNN doesn't have a training phase means it's simple"
- L04: "More trees always means better performance"
- L05: "t-SNE cluster sizes are meaningful" / "t-SNE distances between clusters are meaningful"
- L06: "Word analogies always work" (success rates are 40-70%, not near 100%)

### 5.4 Per-Slide Timing (Advanced Guides)

L06 instructor guide provides the most detailed format: per-slide timing within each PMSP phase:

```markdown
### Method Phase --- Part 1: Embeddings (30 min)
1. **Word2Vec: Skip-gram** (4 min) --- softmax objective, training procedure
2. **Skip-gram: Computational Challenge** (4 min) --- negative sampling
3. **Negative Sampling Illustrated** (2 min) --- chart showing positive/negative pairs
...
```

This granularity helps instructors pace their delivery. Not all guides have this level of detail.

### 5.5 Teaching Notes Pattern

Instructor guides include inline teaching notes for specific slides:
- "When covering negative sampling pseudocode, ask students why the 3/4 power helps"
- "The analogy limitations slide is important for critical thinking -- do not skip"
- "Use the 'bank' example (river bank vs bank account) for static vs contextual distinction"

These notes flag slides that require special instructor attention or discussion facilitation.

---

## Part 6: Assessment Architecture

### 6.1 Quiz System (16 HTML files)

**Quiz inventory** (docs/quiz/):

| Type | Files | Purpose |
|------|-------|---------|
| **Per-topic** | L01-L06 (6 files) | End-of-lecture self-assessment |
| **Cross-topic** | quiz1 (regression), quiz2 (classification+ensemble), quiz3 (advanced) | Multi-topic review |
| **Split-topic** | L03_knn, L03_kmeans, L04_decision_trees, L04_ensemble_methods | Focused sub-topic quizzes |
| **Accessible** | L03_knn_kmeans_accessible | Reduced complexity version |
| **Simple** | L04_random_forests_simple | Simplified version |
| **Template** | quiz_template.html | Reusable quiz scaffold |

**Technical format**:
- KaTeX for math rendering (loaded via CDN)
- CSS variables matching ML palette: `--mlpurple: #3333B2`, `--mlblue: #0066CC`
- JavaScript-based, no backend, progress tracking via stat badges
- Initialization: call `render()` or `initQuiz()` directly at end of `<body>` (not in DOMContentLoaded -- may have already fired)
- Questions progress through Bloom's levels within each quiz

### 6.2 Group Assignment

- 60% of course grade
- Groups of 2-3 students
- Choose 5 of 6 topics
- Difficulty multiplier: L01=1, L02=1, L03=2, L04=2, L05=3, L06=4 (total=13)
- Deliverables: GitHub repo + report + presentation

### 6.3 Exercise Progression

Within each Practice section, exercises escalate:
1. **Implement from scratch** (NumPy) - Bloom's 3 (Apply)
2. **Use scikit-learn** on provided data - Bloom's 3 (Apply)
3. **Evaluate and compare** methods - Bloom's 4-5 (Analyze/Evaluate)

---

## Part 7: Cross-Cutting Themes

### 7.1 Algorithm Connection Narrative

Each lecture explicitly connects to previous and next:
- L01 summary → "Next: Logistic Regression turns this line into a curve"
- L02 summary → "Next: KNN & K-Means (from parametric to non-parametric)"
- L03 summary → "Next: Random Forests (from distance-based to tree-based)"
- L04 summary → "Next: PCA & t-SNE (from prediction to understanding)"
- L05 summary → "Next: Embeddings & RL (from classical to modern)"
- L06: "Course complete!" - full circle back to XKCD #1838

### 7.2 Recurring Concepts

These concepts appear in EVERY lecture, creating thematic coherence:
- **Bias-variance tradeoff**: L01 (regularization), L02 (regularization), L03 (K selection), L04 (tree depth/forest), L05 (components), L06 (exploration-exploitation)
- **Feature scaling**: L01-L06 (standardization before distance/optimization)
- **Cross-validation**: L01-L06 (hyperparameter tuning)
- **Overfitting**: L01-L06 (diagnostic + prevention)
- **Interpretability**: L01-L06 (coefficients, feature importance, attention)

### 7.3 Notation Consistency

Maintained across all 44 tex files:
- $\mathbf{X}$: design matrix (bold uppercase)
- $\boldsymbol{\beta}$ or $\mathbf{w}$: coefficients (bold lowercase)
- $\hat{y}$: predictions (hat accent)
- $\alpha$: learning rate
- $\lambda$: regularization strength
- $K$: context-dependent (neighbors in KNN, clusters in K-Means, classes in softmax)

---

## Part 8: Quality Checklist

Use this checklist when creating or reviewing any slide deck:

### Structural
- [ ] Three-zone architecture (Intro/Core/Wrap-up)
- [ ] PMSP sections present (Problem/Method/Solution/Practice)
- [ ] Opening XKCD with CC BY-NC 2.5 attribution
- [ ] Closing comic/callback to opening
- [ ] Learning Objectives at Bloom's 4-5
- [ ] Decision framework slide (flowchart or pros/cons)

### Content
- [ ] All frame titles are questions (except exempted slides)
- [ ] Zone 1 has ZERO formulas and ZERO Greek letters
- [ ] Every formula has a worked example or plain-language interpretation
- [ ] Finance application threaded throughout (not bolted-on)
- [ ] bottomnote on EVERY content slide

### Formatting
- [ ] Max 3-4 bullets per slide
- [ ] 8+ distinct layout patterns
- [ ] Chart density ~1 per 4 slides
- [ ] Chart widths: 0.55 (with text) or 0.65 (standalone)
- [ ] No two consecutive slides share layout
- [ ] compactlist for dense slides
- [ ] booktabs tables for comparisons (\toprule/\midrule/\bottomrule)
- [ ] TikZ diagrams for flowcharts and custom illustrations

### Assessment Alignment
- [ ] Practice exercises escalate through Bloom's levels
- [ ] Exercises use course finance datasets
- [ ] Instructor guide has misconceptions listed
- [ ] Quiz exists on GitHub Pages with KaTeX math support

### Compilation
- [ ] 0 LaTeX errors
- [ ] 0 Overfull warnings
- [ ] Self-contained preamble (no \input dependencies)
- [ ] Preamble matches template (7 ML colors, Madrid theme, 3-col footer)
