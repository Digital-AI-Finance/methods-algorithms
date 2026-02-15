# Plan: KNN Mini-Lecture (10-Slide Standalone)

## Context

### Original Request
Create a 10-slide standalone mini-lecture on K-Nearest Neighbors (KNN) following two simultaneous skill templates: the Mini-Lecture Generator (WHY-FEEL-WHAT-CASE-HOW-RISK-WHERE-IMPACT-SO WHAT-ACT arc) and the Beamer Slide Creator (two-column [T] layout, insight blocks, compactlist, TikZ comics, pgfplots).

### Core Tension
KNN is the simplest algorithm to explain -- just "find the closest neighbors and vote" -- **but** that simplicity hides devastating failure modes in high dimensions, wrong K choices, and imbalanced data that can silently destroy classification quality in production.

### Research Findings (Codebase Exploration)

**Preamble source**: `slides/L03_KNN_KMeans/L03_deepdive.tex` lines 1-107. Identical preamble across L03_overview.tex and L03_deepdive.tex. Defines: mlblue, mlpurple, mllavender (4 variants), mlorange, mlgreen, mlred, mlgray, lightgray, midgray. Includes compactlist environment, bottomnote command, highlight command.

**Missing colors that must be added**:
- `dfteal` -- not defined in any .tex file in the repository. Must define as `\definecolor{dfteal}{RGB}{0,128,128}` (standard teal).
- `dfred` -- not defined in any .tex file. Must define as `\definecolor{dfred}{RGB}{180,30,30}` (dark warning red, distinct from mlred).

**Existing TikZ usage**: ZERO `\begin{tikzpicture}` in any slide file. All visuals are external chart.pdf files. This mini-lecture introduces TikZ inline graphics as a new capability. Must add `\usetikzlibrary{arrows.meta,positioning,shapes.callouts,decorations.pathreplacing}` for comics and diagrams.

**pgfplots usage**: ZERO inline pgfplots in any file. Must add `\usepackage{pgfplots}` and `\pgfplotsset{compat=1.18}`. Alternative: reference existing `01_knn_boundaries/chart.pdf` for slide 7.

**Available chart assets** (in `slides/L03_KNN_KMeans/`):
- `01_knn_boundaries/chart.pdf` -- KNN decision boundaries for varying K
- `02_distance_metrics/chart.pdf` -- Euclidean/Manhattan/Chebyshev unit balls
- `06_voronoi/chart.pdf` -- Voronoi diagram

**Available images**:
- `images/1838_machine_learning.png` -- XKCD #1838
- `images/2731_kmeans_clustering.png` -- XKCD #2731

**Block usage**: Only `\begin{block}` used in existing slides. No `exampleblock` or `alertblock`. The mini-lecture introduces `exampleblock` for slides 2 and 10.

**Column pattern**: `\begin{columns}[T]` with `\column{0.55\textwidth}` + `\column{0.42\textwidth}` is the established pattern.

---

## Work Objectives

### Core Objective
Produce a single standalone .tex file (`L03_knn_mini.tex`) containing exactly 10 content frames following the interleaved WHY-FEEL-WHAT-CASE-HOW-RISK-WHERE-IMPACT-SO WHAT-ACT arc, with 10 distinct visual types, all compilable with pdflatex without external dependencies beyond the existing chart PDFs.

### Deliverables
1. `slides/L03_KNN_KMeans/L03_knn_mini.tex` -- the complete 10-slide mini-lecture
2. Zero compilation errors with `pdflatex -interaction=nonstopmode`
3. Zero overfull hbox warnings (strict mode compliance)

### Definition of Done
- All 10 slides compile cleanly
- Every slide uses `\begin{frame}[t]` with two-column `[T]` layout (0.55 + 0.42)
- Every slide (except 2 and 10) has an insight `\begin{block}` at the bottom
- Slides 2 and 10 use `\begin{exampleblock}` instead
- Every slide has `\bottomnote{}`
- Every itemize uses `\compactlist`
- Font cascade respected: `\small` -> `\footnotesize` -> `\scriptsize`; `\tiny` only in TikZ
- 10 visually distinct slide types (no two consecutive slides share the same visual approach)
- No specific numbers, company names, or years in content

---

## Must Have / Must NOT Have

### Must Have
- Exact preamble from L03_deepdive.tex (lines 1-101, including \highlight and \mathbold commands) with these additions:
  - `\definecolor{dfteal}{RGB}{0,128,128}`
  - `\definecolor{dfred}{RGB}{180,30,30}`
  - `\usepackage{colortbl}` (required for \rowcolor in slide 3's comparison table)
  - `\usetikzlibrary{arrows.meta,positioning,shapes.callouts,decorations.pathreplacing}`
  - `\usepackage{pgfplots}` and `\pgfplotsset{compat=1.18}`
- Title block: `\title[KNN Mini-Lecture]{K-Nearest Neighbors}`, `\subtitle{A 10-Slide Mini-Lecture}`, `\author{Methods and Algorithms}`, `\institute{MSc Data Science}`, `\date{Spring 2026}`
- `\begin{document}` with no title page (all 10 slides are content frames)
- Relative paths to chart assets: `01_knn_boundaries/chart.pdf` etc.

### Must NOT Have
- No title slide or outline slide (the 10 slides ARE the entire deck)
- No `\section{}` or `\tableofcontents` commands
- No specific company names, dollar amounts, specific years, or named individuals
- No subplots or multi-panel figures within a single slide
- No `\large` or `\Large` font sizes in body text
- No bare `\begin{itemize}` without `\compactlist` wrapper (except inside blocks)

---

## All 10 Slide Titles

| # | Role | Title |
|---|------|-------|
| 1 | WHY | "Why Would a Loan Officer Want to Ask the Neighbors?" |
| 2 | FEEL | "Classifying a Stranger -- Did Similarity Cross Your Mind?" |
| 3 | WHAT | "What Makes KNN Different from Logistic Regression and Trees?" |
| 4 | CASE | "Follow One Applicant from Feature Space to Final Label" |
| 5 | HOW | "Who Should Measure Distance -- Euclid, Manhattan, or Cosine?" |
| 6 | RISK | "What Could Go Wrong If Every Dimension Votes Equally?" |
| 7 | WHERE | "Why Do So Many Practitioners Start with KNN?" |
| 8 | IMPACT | "Who Wins and Who Loses When KNN Replaces Rules?" |
| 9 | SO WHAT | "3 Questions That Reveal Whether KNN Is the Right Algorithm" |
| 10 | ACT | "Your Challenge: Evaluate a Real Classification Problem" |

---

## Slide-by-Slide Specification

---

### SLIDE 1: WHY -- TikZ Comic (Dilemma)

**Title**: "Why Would a Loan Officer Want to Ask the Neighbors?"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "The Dilemma"
- `\compactlist`:
  - A new applicant walks in with no credit history
  - The rulebook says nothing about this profile
  - But the database holds thousands of past applicants with known outcomes
- Transition line: "What if the answer is already in the data -- hiding among the neighbors?"

**Right column** (0.42, TikZ comic):
- `\begin{tikzpicture}[scale=0.75]`
- **Scene**: Two stick figures. Left figure (dfteal, labeled "Officer") stands at a desk. Right figure (mlpurple, labeled "Applicant") stands with a question mark above their head.
- **Speech bubble** (Officer, ellipse callout, dfteal fill!10): "Your profile matches no rules..."
- **Thought bubble** (Officer, thought bubble, mllavender4 fill): "...but it looks just like those five approved cases."
- Stick figures: simple lines + circles, `\tiny` labels
- **Punchline element**: Dotted arrow from Applicant to a cluster of 5 small dots (mlgreen) labeled "K=5 neighbors"

**Insight block**:
```
\begin{block}{Insight}
KNN formalizes human reasoning: when rules fail, look at the most similar past cases and follow their lead.
\end{block}
```

**Bottomnote**: "Instance-based learning stores all training data -- no model parameters, no training phase"

**Colors dominant**: dfteal (officer), mlpurple (applicant), mlgreen (neighbor dots)

---

### SLIDE 2: FEEL -- Text-Only with Prompt

**Title**: "Classifying a Stranger -- Did Similarity Cross Your Mind?"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "Think Before You Compute"
- Narrative paragraph (`\footnotesize`): "Imagine you meet someone at a conference. You know nothing about them. Within seconds, your brain classifies: academic or industry? Junior or senior? Friendly or reserved? You did not run a logistic regression. You compared them to people you already know."
- `\compactlist`:
  - How many "neighbors" did your brain consult?
  - Did you weight closer acquaintances more heavily?
  - What "features" did you use -- appearance, speech, context?

**Right column** (0.42, reflective prompt -- NO visual):
- `\footnotesize`
- Framed text box using `\fcolorbox{mlpurple}{mllavender4}{\parbox{0.85\columnwidth}{...}}`:
  - "Pause and reflect:"
  - "When you last recommended a restaurant to a friend, did you match their taste to similar friends who liked similar places?"
  - "That is KNN."

**Exampleblock** (instead of insight block):
```
\begin{exampleblock}{Reflection Prompt}
Write down one real decision you made this week by mentally consulting "similar past cases." What K did you use?
\end{exampleblock}
```

**Bottomnote**: "KNN mirrors how humans naturally classify: by analogy to known examples, not by learned rules"

**Colors**: mlpurple (frame border), mllavender4 (frame fill)

---

### SLIDE 3: WHAT -- Comparison Table

**Title**: "What Makes KNN Different from Logistic Regression and Trees?"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text + table):
- `\small` font
- Bold header: "Taxonomy of Classifiers"
- `\footnotesize` table using `\begin{tabular}{@{}l c c c@{}}` with `\toprule`, `\midrule`, `\bottomrule`:

| Property | KNN | Log. Reg. | Dec. Tree |
|----------|-----|-----------|-----------|
| Training phase | None | Optimize weights | Build tree |
| Decision boundary | Non-linear, local | Linear (global) | Axis-aligned |
| Interpretability | Low (black box) | High (coefficients) | High (rules) |
| Handles new classes | Naturally | Retrain needed | Retrain needed |
| Memory at predict | All data | Model only | Model only |

- **Pattern to notice** (bold after table): "KNN trades training speed for prediction cost -- the opposite of parametric models"

**Right column** (0.42, structured summary):
- `\footnotesize`
- Three color-coded mini-boxes (using `\colorbox`):
  - `\colorbox{dfteal!15}` -- "KNN: Lazy, local, non-parametric"
  - `\colorbox{mlorange!15}` -- "LogReg: Eager, global, parametric"
  - `\colorbox{mlpurple!15}` -- "Tree: Eager, local, non-parametric"

**Insight block**:
```
\begin{block}{Insight}
Lazy learners memorize; eager learners generalize. KNN defers all computation to prediction time, making it uniquely adaptable but expensive at scale.
\end{block}
```

**Bottomnote**: "Non-parametric means the model complexity grows with the data -- no fixed number of parameters"

---

### SLIDE 4: CASE -- Step Diagram / Timeline

**Title**: "Follow One Applicant from Feature Space to Final Label"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "One Prediction, Step by Step"
- `\compactlist`:
  - An applicant arrives with feature vector (income, debt ratio, employment length)
  - All features are standardized to zero mean and unit variance
  - The algorithm computes distance to every stored example
  - The K closest examples "vote" on the label
  - Majority wins; ties broken by distance weighting

**Right column** (0.42, TikZ step diagram):
- `\begin{tikzpicture}[scale=0.75]`
- **5 numbered nodes** arranged vertically, connected by arrows:
  1. `\node[draw, rounded corners, fill=mllavender4]` -- "Standardize features"
  2. `\node[draw, rounded corners, fill=mllavender4]` -- "Compute all distances"
  3. `\node[draw, rounded corners, fill=dfteal!20]` -- "Select K nearest"
  4. `\node[draw, rounded corners, fill=mlorange!20]` -- "Majority vote"
  5. `\node[draw, rounded corners, fill=mlgreen!20, thick]` -- "Output: Approved"
- Arrows between nodes using `[-{Stealth[length=3mm]}]`
- **Decision diamond** between nodes 4 and 5: "Tie?" with two branches: "No -> direct" and "Yes -> weight by 1/d"
- `\tiny` labels on arrows: "O(nd)", "sort top K", "argmax"

**Insight block**:
```
\begin{block}{Insight}
Feature standardization is not optional -- without it, high-magnitude features dominate the distance and K neighbors become meaningless.
\end{block}
```

**Bottomnote**: "Complexity per query: O(nd) for brute force, O(n log n) with KD-trees when d is small"

---

### SLIDE 5: HOW -- Side-by-Side Architecture

**Title**: "Who Should Measure Distance -- Euclid, Manhattan, or Cosine?"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "Three Distance Philosophies"
- `\compactlist`:
  - **Euclidean** (L2): straight-line distance, default for dense numerical data
  - **Manhattan** (L1): city-block distance, robust to outliers in individual features
  - **Cosine**: measures angle not magnitude, ideal for sparse high-dimensional data (text, embeddings)
- Transition: "The choice of metric reshapes which points count as neighbors -- and therefore changes the prediction"

**Right column** (0.42, TikZ side-by-side):
- `\begin{tikzpicture}[scale=0.75]`
- **Two sub-diagrams** stacked vertically:
  - **Top**: "Dense features (finance)" -- draw a circle (Euclidean ball, dfteal line) and a diamond (Manhattan ball, mlorange line) overlaid on the same center point, with 3 data points. Label which metric selects which neighbors differently.
  - **Bottom**: "Sparse features (text)" -- draw two vectors from origin with a small angle between them (mlpurple lines). Label "cosine = small angle = high similarity". Show a third vector far in magnitude but same angle: "same cosine, different Euclidean."
- `\tiny` annotations

**Insight block**:
```
\begin{block}{Insight}
Euclidean distance assumes all features are equally scaled and equally important. When that assumption fails, Manhattan or Cosine often outperform it.
\end{block}
```

**Bottomnote**: "Also consider: Mahalanobis distance when features are correlated, Hamming for binary features"

---

### SLIDE 6: RISK -- TikZ Comic (Failure)

**Title**: "What Could Go Wrong If Every Dimension Votes Equally?"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "Three Ways KNN Fails Silently"
- `\compactlist`:
  - **Curse of dimensionality**: in high dimensions, all points become equidistant -- neighbors lose meaning
  - **Wrong K**: too small captures noise, too large washes out local structure
  - **Imbalanced classes**: majority class dominates the vote even when the minority class is the correct answer
- Each failure tagged with a consequence: "misclassification", "overfitting/underfitting", "systematic bias"

**Right column** (0.42, TikZ comic -- DIFFERENT emotional register from slide 1):
- `\begin{tikzpicture}[scale=0.75]`
- **Scene**: A single stick figure (dfred color, labeled "Model") surrounded by a fog/cloud effect (light gray shading). Three data points nearby are ALL equidistant (shown with dashed lines of equal length, labeled "d ~ d ~ d").
- **Speech bubble** (Model, ellipse callout, dfred!10 fill): "Everyone is the same distance away... I cannot distinguish anyone!"
- **Visual element**: A large dfred "X" stamped over the scene with `\tiny` label "High-D Failure"
- **Emotional register**: Confusion and helplessness (vs. slide 1's contemplation and hope). The stick figure has "?" and "!" marks.

**Insight block**:
```
\begin{block}{Insight}
The curse of dimensionality is not theoretical trivia -- in production, adding irrelevant features silently degrades KNN accuracy without any warning from the algorithm.
\end{block}
```

**Bottomnote**: "Mitigation: feature selection, PCA for dimensionality reduction, distance-weighted voting for imbalance"

**Colors dominant**: dfred (failure stick figure, X stamp), mlgray (fog), dashed lines

---

### SLIDE 7: WHERE -- pgfplots Chart

**Title**: "Why Do So Many Practitioners Start with KNN?"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "KNN as a Baseline Classifier"
- `\compactlist`:
  - KNN requires no assumptions about data distribution
  - It naturally handles multi-class problems
  - Decision boundaries adapt to local data density
  - Fast to prototype: no hyperparameter tuning beyond K
- Sentence: "The chart shows how boundaries smooth as K increases -- the visual signature of the bias-variance tradeoff"

**Right column** (0.42, pgfplots chart OR external chart.pdf):
- **Primary option**: Include existing chart via `\includegraphics[width=\textwidth]{01_knn_boundaries/chart.pdf}`
- **Fallback option** (if inline pgfplots preferred): Create a simple scatter plot with `\begin{axis}[width=7cm, height=4.5cm]` showing two classes of points (dfteal and mlorange markers) with a shaded decision region
- **Axes**: x = "Feature 1 (standardized)", y = "Feature 2 (standardized)"
- **Data pattern**: Two clusters with slight overlap, boundary region shaded in mllavender4
- **Annotations**: Arrow pointing to boundary labeled "Smoother as K increases"

**Implementation note**: Using the existing `01_knn_boundaries/chart.pdf` is strongly recommended for visual consistency with the rest of L03. The pgfplots fallback should only be used if a self-contained file is explicitly required.

**Insight block**:
```
\begin{block}{Insight}
KNN decision boundaries are not computed -- they emerge from the data. This makes KNN the natural first-look tool before committing to a parametric model.
\end{block}
```

**Bottomnote**: "KNN with K=1 achieves asymptotic error at most twice the Bayes optimal rate (Cover-Hart theorem)"

---

### SLIDE 8: IMPACT -- Stakeholder Map

**Title**: "Who Wins and Who Loses When KNN Replaces Rules?"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "Stakeholder Analysis"
- `\compactlist`:
  - **Winners**: Risk teams (better default prediction), medical teams (diagnosis by similarity), marketing (customer segmentation)
  - **Losers**: Compliance officers (KNN is hard to explain to regulators), IT operations (prediction latency scales with data size), anyone expecting a simple "why" for a decision
- Sentence: "KNN shifts power from those who write rules to those who curate data"

**Right column** (0.42, TikZ stakeholder map):
- `\begin{tikzpicture}[scale=0.75]`
- **Center node**: Large rounded rectangle, mlpurple fill, white text: "KNN Prediction"
- **4 surrounding actor nodes** arranged in a diamond/cross:
  - Top: "Risk Analyst" (mlgreen fill!20) with arrow TO center labeled "curates data"
  - Right: "Applicant" (dfteal fill!20) with arrow FROM center labeled "gets decision"
  - Bottom: "Regulator" (dfred fill!20) with arrow FROM center labeled "demands explanation"
  - Left: "IT Ops" (mlorange fill!20) with arrow TO center labeled "manages latency"
- **Edge annotations** (`\tiny`): win/lose indicators using checkmarks and warning triangles
- **Flow direction**: Arrows show information/power flow, not just connections

**Insight block**:
```
\begin{block}{Insight}
KNN's Achilles heel in regulated industries is not accuracy -- it is explainability. A model that says "because these five past cases" may not satisfy a regulator who wants a causal story.
\end{block}
```

**Bottomnote**: "Explainability techniques: show the K neighbors and their features as the 'reason' for classification"

---

### SLIDE 9: SO WHAT -- Metaphor Visual (Balance Scale)

**Title**: "3 Questions That Reveal Whether KNN Is the Right Algorithm"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "The Decision Framework"
- Numbered list (1-3), each with a question and a diagnostic:
  1. **"Is the data low-dimensional?"** -- If d > 20 without feature selection, distances lose meaning. KNN struggles.
  2. **"Is the training set small enough to store?"** -- KNN stores everything. If n > 1M, consider approximate methods or switch algorithms.
  3. **"Can you live without a global model?"** -- KNN explains by example, not by formula. If regulators demand a formula, look elsewhere.
- Concluding sentence: "If all three answers are 'yes,' KNN is a strong candidate."

**Right column** (0.42, TikZ balance scale):
- `\begin{tikzpicture}[scale=0.75]`
- **Fulcrum**: Triangle at bottom center (mlgray)
- **Beam**: Horizontal line tilted slightly left (indicating "use KNN" is heavier/winning)
- **Left pan** (dfteal): labeled "Use KNN" with three small rectangles inside representing the 3 "yes" answers, mlgreen fill
- **Right pan** (dfred): labeled "Avoid KNN" with three small rectangles representing "no" answers, mlred fill
- **Tilt**: Beam tilted 10-15 degrees toward the left (KNN side) -- showing a slight advantage when conditions are met
- **Question mark**: Large "?" above the fulcrum in mlpurple, representing the decision moment
- `\tiny` labels on each rectangle in the pans

**Insight block**:
```
\begin{block}{Insight}
No algorithm is universally best. KNN excels in its niche -- low dimensions, moderate data, local patterns -- and fails gracefully when you monitor these three diagnostics.
\end{block}
```

**Bottomnote**: "The 'No Free Lunch' theorem guarantees no single algorithm dominates across all possible datasets"

---

### SLIDE 10: ACT -- Activity Frame

**Title**: "Your Challenge: Evaluate a Real Classification Problem"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "The Scenario"
- `\footnotesize` narrative: "A retail bank wants to predict which customers will default on personal loans. They have a dataset of past customers with features: income, age, employment length, debt-to-income ratio, number of open accounts. The dataset has moderate size and all features are numerical."
- `\compactlist`:
  - Apply the 3-question framework from slide 9
  - Decide: Is KNN appropriate here?
  - If yes: recommend K and a distance metric with justification
  - If no: name a better algorithm and explain why

**Right column** (0.42, structured activity):
- `\footnotesize`
- Framework table using `\begin{tabular}{@{}l p{3.5cm}@{}}`:

| Question | Your Answer |
|----------|-------------|
| Low-dimensional? | \_\_\_\_\_\_\_ |
| Storable data? | \_\_\_\_\_\_\_ |
| Example-based OK? | \_\_\_\_\_\_\_ |
| Verdict | \_\_\_\_\_\_\_ |
| Recommended K | \_\_\_\_\_\_\_ |
| Distance metric | \_\_\_\_\_\_\_ |

**Exampleblock** (instead of insight block):
```
\begin{exampleblock}{Deliverable}
Fill in the table. Be prepared to defend your verdict to a skeptical risk manager who asks: "Why not just use logistic regression?"
\end{exampleblock}
```

**Bottomnote**: "Hint: consider the dimensionality, the data size, and the regulatory environment for your recommendation"

---

## TikZ Comic Descriptions (Detailed)

### Slide 1 Comic (Dilemma -- dfteal dominant)

**Characters**:
- **Officer** (left, x=0, y=0): Stick figure drawn with dfteal lines. Circle head (radius 0.3cm), body line, two arm lines, two leg lines. Label "Officer" below in `\tiny`.
- **Applicant** (right, x=4, y=0): Stick figure drawn with mlpurple lines. Same construction. Label "Applicant" below. Large "?" above head in mlorange.

**Dialogue**:
- Speech bubble from Officer (ellipse callout, pointing right, fill=dfteal!10, draw=dfteal): "Your profile matches no rules..."
- Thought bubble from Officer (ellipse callout above head with 2-3 small leading circles for thought-bubble styling, fill=mllavender4, draw=mlpurple): "...but it looks like those five approved cases."

**Environment**:
- Small desk between them (simple rectangle, mlgray fill)
- Cluster of 5 small filled circles (mlgreen) at x=5, y=2.5, with a dotted arc connecting Applicant to the cluster, labeled "K=5"

**Punchline**: The visual contrast between the empty speech bubble (no rules) and the rich thought bubble (neighbor-based reasoning) carries the message.

### Slide 6 Comic (Failure -- dfred dominant, DIFFERENT register)

**Characters**:
- **Model** (center, x=2.5, y=2): Single stick figure in dfred. Head has "?" on left and "!" on right. Body slightly hunched (shorter body line). Label "Model" below.

**Environment**:
- 6 data points arranged in a rough circle around Model, ALL at approximately equal distance. Dashed lines (mlgray) from Model to each point, each labeled "d" in `\tiny`.
- Light gray cloud/fog behind everything: `\fill[mlgray!15, rounded corners=10pt] (0,0) rectangle (5,4);`
- Large dfred "X" overlaid diagonally across the scene: `\draw[dfred, line width=3pt] (0.5,0.5) -- (4.5,3.5); \draw[dfred, line width=3pt] (0.5,3.5) -- (4.5,0.5);`
- `\tiny` label at bottom-right: "High-D Failure"

**Speech bubble**: Ellipse callout from Model (fill=dfred!10, draw=dfred): "Everyone is the same distance... I cannot distinguish anyone!"

**Emotional register contrast with Slide 1**: Slide 1 is contemplative and hopeful (the officer has a solution in mind). Slide 6 is confused and alarmed (the model has no solution, all distances collapsed).

---

## pgfplots Chart Spec (Slide 7)

**Recommended approach**: Use existing `01_knn_boundaries/chart.pdf` for visual consistency.

**Fallback inline pgfplots spec** (if self-contained required):
```
\begin{axis}[
    width=7cm, height=4.5cm,
    xlabel={Feature 1}, ylabel={Feature 2},
    xmin=-3, xmax=3, ymin=-3, ymax=3,
    legend pos=north east,
    axis lines=middle,
    tick label style={font=\tiny},
    label style={font=\scriptsize}
]
```
- **Class A** (dfteal): 15-20 scatter points centered around (-1, 1)
- **Class B** (mlorange): 15-20 scatter points centered around (1, -1)
- **Overlap region**: 4-5 points near origin where classes intermingle
- **Annotation**: Arrow from (2, 2.5) pointing to overlap zone, labeled "Boundary shifts with K" in `\tiny`
- **No fitted boundary line** -- the point is that the boundary is implicit

---

## Comparison Table Spec (Slide 3)

**Columns**: Property | KNN | Logistic Regression | Decision Tree

**Rows** (6 rows):
1. Training phase: None | Optimize weights | Build tree
2. Decision boundary: Non-linear, local | Linear, global | Axis-aligned, local
3. Interpretability: Low | High (coefficients) | High (rules)
4. New class handling: Naturally | Retrain | Retrain
5. Memory at prediction: All training data | Parameters only | Tree structure only
6. Prediction speed: Slow (O(nd)) | Fast (O(d)) | Fast (O(depth))

**Pattern to notice**: KNN is the only classifier where the model IS the data. This is the defining property that drives all its strengths and weaknesses.

**Formatting**: Use `\rowcolor{mllavender4}` on alternating rows. Bold the KNN column header in dfteal. Use `\footnotesize` for table text.

---

## Step Diagram Spec (Slide 4)

**5 numbered nodes**, vertical flow, top to bottom:

1. **"Standardize features"** -- mllavender4 fill, rounded corners
   - Arrow down, labeled "zero mean, unit var" (`\tiny`)
2. **"Compute all distances"** -- mllavender4 fill
   - Arrow down, labeled "O(nd)" (`\tiny`)
3. **"Select K nearest"** -- dfteal!20 fill (highlighted as the core step)
   - Arrow down, labeled "sort top K" (`\tiny`)
4. **"Majority vote"** -- mlorange!20 fill
   - **Decision diamond** branching from bottom of node 4:
     - Left branch: "Tie? Yes" -> small node "Weight by 1/d" (mlgray fill) -> merges back
     - Right branch: "Tie? No" -> continues down
5. **"Output label"** -- mlgreen!20 fill, thick border

**Layout**: Nodes at y = 4, 3, 2, 1, 0 (top to bottom). Decision diamond at y = 0.5, offset right.

---

## Architecture Diagram Spec (Slide 5)

**Two sub-diagrams** stacked vertically within the TikZ picture:

**Top sub-diagram** ("Dense numerical features"):
- Center point at (0,0) as a black dot
- Circle (radius 1.5cm, dfteal, dashed) = Euclidean neighborhood
- Diamond (rotated square, radius 1.5cm, mlorange, dashed) = Manhattan neighborhood
- 5 data points scattered: 2 inside both shapes, 1 inside circle only, 1 inside diamond only, 1 outside both
- Labels: "Euclidean selects these" (dfteal), "Manhattan selects these" (mlorange)

**Bottom sub-diagram** ("Sparse / directional features"):
- Origin at (0, -3)
- Two vectors from origin: one at 20 degrees (length 3cm, mlpurple), one at 25 degrees (length 1.5cm, mlpurple)
- Arc between them labeled "small angle = similar" (dfteal)
- Third vector at 70 degrees (length 3cm, dfred dashed), labeled "large angle = dissimilar"
- Caption: "Cosine cares about direction, not magnitude"

---

## Stakeholder Map Spec (Slide 8)

**Central node**: Rounded rectangle (3cm x 1.5cm), mlpurple fill, white text: "KNN Prediction"

**4 actor nodes** (diamond arrangement):
- **Top** (y=2.5): "Risk Analyst" -- rounded rect, mlgreen!20 fill, mlgreen border
  - Arrow TO center, labeled "curates training data" (`\tiny`)
  - Checkmark icon (mlgreen)
- **Right** (x=3.5): "Applicant" -- rounded rect, dfteal!20 fill, dfteal border
  - Arrow FROM center, labeled "receives decision" (`\tiny`)
  - Neutral indicator
- **Bottom** (y=-2.5): "Regulator" -- rounded rect, dfred!20 fill, dfred border
  - Arrow FROM center, labeled "demands explanation" (`\tiny`)
  - Warning triangle (dfred)
- **Left** (x=-3.5): "IT Operations" -- rounded rect, mlorange!20 fill, mlorange border
  - Arrow TO center, labeled "manages compute/latency" (`\tiny`)
  - Warning triangle (mlorange)

**Edge style**: Arrows with `[-{Stealth}]`, mlgray color, label midway

---

## Balance Scale Spec (Slide 9)

**Fulcrum**: Equilateral triangle at (2.5, 0), mlgray fill, pointing up, apex at (2.5, 1.8)

**Support strut**: Vertical line from fulcrum apex (2.5, 1.8) up to beam pivot (2.5, 1.8) -- beam rests directly on fulcrum

**Beam**: Line from (0.3, 1.5) to (4.7, 2.1) -- tilted ~10 degrees toward left (KNN side is heavier/lower), pivoting at (2.5, 1.8)

**Left pan** ("Use KNN"):
- Suspended from left end of beam by two short lines
- Rectangular tray (2cm x 0.8cm), dfteal!20 fill, dfteal border
- 3 small rectangles inside (0.5cm x 0.3cm each), mlgreen fill, labeled in `\tiny`: "Low d", "Small n", "Local OK"
- Label below pan: "Use KNN" in `\small` dfteal

**Right pan** ("Avoid KNN"):
- Suspended from right end of beam (higher because lighter)
- Same tray dimensions, dfred!20 fill, dfred border
- 3 small rectangles inside, mlred fill, labeled: "High d", "Huge n", "Need formula"
- Label below pan: "Avoid KNN" in `\small` dfred

**Question mark**: Large "?" (font size `\Large`) at (2.5, 3.5) in mlpurple, directly above fulcrum

---

## Activity Spec (Slide 10)

**Case description** (left column):
- Scenario: Retail bank, personal loan default prediction
- Features: income, age, employment length, debt-to-income, open accounts (d=5)
- Dataset: moderate size, all numerical, labeled outcomes available
- Students apply the 3-question framework

**Framework table** (right column):

| Question | Your Answer |
|----------|-------------|
| Low-dimensional? (d < 20) | \_\_\_\_ |
| Storable training set? | \_\_\_\_ |
| Example-based explanation OK? | \_\_\_\_ |
| **Verdict: KNN appropriate?** | \_\_\_\_ |
| If yes: recommended K | \_\_\_\_ |
| If yes: distance metric | \_\_\_\_ |

**Exampleblock text**: "Fill in the table. Be prepared to defend your verdict to a skeptical risk manager who asks: 'Why not just use logistic regression?'"

**Design intent**: The table forces structured thinking. The defense question forces them to articulate KNN's unique value proposition (local, non-parametric, no distributional assumptions) versus logistic regression's advantages (interpretable, fast, regulatory-friendly).

---

## File Location and Compilation

**File**: `slides/L03_KNN_KMeans/L03_knn_mini.tex`

**Compilation**:
```bash
cd slides/L03_KNN_KMeans
pdflatex -interaction=nonstopmode L03_knn_mini.tex
pdflatex -interaction=nonstopmode L03_knn_mini.tex
mkdir temp 2>nul & move *.aux *.log *.nav *.out *.snm *.toc temp/
```

Two passes required for page numbers. The file references `01_knn_boundaries/chart.pdf` via relative path from its own directory.

**Dependencies**:
- pdflatex with TikZ, pgfplots (standard TeX Live / MiKTeX)
- `01_knn_boundaries/chart.pdf` must exist (already present in repo)
- No other external files required (TikZ graphics are all inline)

---

## Task Flow and Dependencies

```
Task 1: Create file with preamble (no dependencies)
   |
   v
Task 2: Write slides 1-5 (depends on Task 1)
   |
   v
Task 3: Write slides 6-10 (depends on Task 1, can parallel with Task 2 if careful)
   |
   v
Task 4: Compile and fix overflow (depends on Tasks 2+3)
   |
   v
Task 5: Verify against checklist (depends on Task 4)
```

### Detailed TODOs

**TODO 1: Create preamble and file skeleton**
- Copy preamble from L03_deepdive.tex lines 1-101 (including \highlight and \mathbold commands)
- Add `\definecolor{dfteal}{RGB}{0,128,128}` and `\definecolor{dfred}{RGB}{180,30,30}`
- Add `\usetikzlibrary{arrows.meta,positioning,shapes.callouts,decorations.pathreplacing}`
- Add `\usepackage{pgfplots}` and `\pgfplotsset{compat=1.18}`
- Set title/subtitle/author/institute/date
- Create `\begin{document}` ... `\end{document}` with 10 empty frame placeholders
- **Acceptance**: File compiles with 10 empty frames, no errors

**TODO 2: Implement slides 1-2 (WHY + FEEL)**
- Slide 1: TikZ comic with stick figures, speech/thought bubbles, neighbor cluster
- Slide 2: Text-only with fcolorbox prompt and exampleblock
- **Acceptance**: Both slides compile, TikZ renders without errors, slide 2 uses exampleblock

**TODO 3: Implement slides 3-4 (WHAT + CASE)**
- Slide 3: Comparison table with booktabs, color-coded summary boxes
- Slide 4: TikZ step diagram with 5 nodes, decision diamond, arrows
- **Acceptance**: Table renders with correct alignment, step diagram flows top-to-bottom

**TODO 4: Implement slides 5-6 (HOW + RISK)**
- Slide 5: Side-by-side TikZ architecture (Euclidean vs Manhattan vs Cosine)
- Slide 6: TikZ failure comic with dfred dominant, different register from slide 1
- **Acceptance**: Both TikZ diagrams render, slide 6 uses dfred not dfteal

**TODO 5: Implement slides 7-8 (WHERE + IMPACT)**
- Slide 7: Include 01_knn_boundaries/chart.pdf via includegraphics
- Slide 8: TikZ stakeholder map with 4 actors and directional arrows
- **Acceptance**: Chart.pdf included at correct size, stakeholder map has all 4 actors

**TODO 6: Implement slides 9-10 (SO WHAT + ACT)**
- Slide 9: TikZ balance scale with tilted beam, labeled pans, question mark
- Slide 10: Activity frame with case description and framework table, exampleblock
- **Acceptance**: Scale tilts correctly, table has blank answer cells, slide 10 uses exampleblock

**TODO 7: Compile and fix overflow**
- Run `pdflatex -interaction=nonstopmode L03_knn_mini.tex` twice
- Check for overfull hbox warnings
- Fix any overflow by adjusting font sizes, rewording, or reducing content
- **Acceptance**: Zero overfull hbox warnings on strict validation

**TODO 8: Final verification against checklist**
- Run full checklist (see below)
- **Acceptance**: All checklist items pass

---

## Commit Strategy

**Single commit** after all TODOs complete:
```
Add KNN mini-lecture: 10-slide standalone with TikZ visuals

New file L03_knn_mini.tex following the WHY-FEEL-WHAT-CASE-HOW-RISK-
WHERE-IMPACT-SO WHAT-ACT interleaved arc. Includes inline TikZ comics,
step diagrams, stakeholder map, balance scale metaphor, and comparison
table. Reuses existing 01_knn_boundaries chart. Self-contained and
compilable with standard pdflatex.
```

---

## Success Criteria

### Checklist Verification (Both Skills)

**Mini-Lecture Generator Compliance:**
- [ ] Exactly 10 content frames (no title slide, no outline)
- [ ] Correct arc order: WHY, FEEL, WHAT, CASE, HOW, RISK, WHERE, IMPACT, SO WHAT, ACT
- [ ] Odd slides (1,3,5,7,9) form conceptual spine
- [ ] Even slides (2,4,6,8,10) provide deepening
- [ ] All titles are questions (except slide 9 which is a numbered promise)
- [ ] 10 different visual types, no consecutive repetition
- [ ] Slide 1: TikZ comic (dilemma, dfteal dominant)
- [ ] Slide 2: Text-only with prompt (visual pause)
- [ ] Slide 3: Comparison table (structured taxonomy)
- [ ] Slide 4: Step diagram with numbered nodes and arrows
- [ ] Slide 5: Side-by-side architecture (two models compared)
- [ ] Slide 6: TikZ comic (failure, dfred dominant, DIFFERENT register from slide 1)
- [ ] Slide 7: pgfplots/chart (quantitative evidence)
- [ ] Slide 8: Stakeholder map (multi-actor TikZ diagram)
- [ ] Slide 9: Metaphor visual (balance scale with tilted beam)
- [ ] Slide 10: Activity frame (structured text with exampleblock)

**Beamer Slide Creator Compliance:**
- [ ] Every frame uses `\begin{frame}[t]`
- [ ] Every frame uses `\begin{columns}[T]` with 0.55 + 0.42
- [ ] Font cascade: `\small` -> `\footnotesize` -> `\scriptsize`, `\tiny` only in TikZ
- [ ] Every slide has `\bottomnote{}`
- [ ] Slides 1,3,4,5,6,7,8,9 have `\begin{block}{Insight}...\end{block}`
- [ ] Slides 2 and 10 have `\begin{exampleblock}` instead
- [ ] Every `\begin{itemize}` uses `\compactlist` (except inside blocks)
- [ ] Color palette: mlpurple, dfteal, mlorange, dfred, mlgray, mllavender4
- [ ] No specific numbers, company names, or years
- [ ] TikZ comics at scale=0.75
- [ ] pgfplots (if inline) at width=7cm, height=4.5cm
- [ ] Zero overfull hbox warnings
- [ ] File compiles cleanly with pdflatex

**Content Accuracy:**
- [ ] KNN algorithm correctly described (lazy learner, majority vote, distance-based)
- [ ] Distance metrics correctly distinguished (Euclidean, Manhattan, Cosine)
- [ ] Curse of dimensionality correctly explained
- [ ] Bias-variance tradeoff correctly tied to K
- [ ] Comparison with logistic regression and decision trees is fair and accurate
- [ ] 3-question framework is actionable and correct
- [ ] Activity scenario is realistic for MSc Data Science students

---

PLAN_READY
