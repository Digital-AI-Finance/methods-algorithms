# Plan: K-Means Mini-Lecture (10-Slide Standalone)

## Context

### Original Request
Create a 10-slide standalone mini-lecture on K-Means Clustering following two simultaneous skill templates: the Mini-Lecture Generator (WHY-FEEL-WHAT-CASE-HOW-RISK-WHERE-IMPACT-SO WHAT-ACT arc) and the Beamer Slide Creator (two-column [T] layout, insight blocks, compactlist, TikZ comics, pgfplots).

### Core Tension
K-Means is the most intuitive clustering algorithm -- just "pick K centers, assign points, update, repeat" -- **but** that simplicity conceals brutal failure modes: wrong K, bad initialization, and non-spherical clusters can all produce confidently wrong groupings with no built-in warning signal.

### Research Findings (Codebase Exploration)

**Preamble source**: `slides/L03_KNN_KMeans/L03_knn_mini.tex` lines 1-106. This file IS the direct template. Its preamble includes all required colors (mlblue, mlpurple, mllavender 1-4, mlorange, mlgreen, mlred, mlgray, lightgray, midgray, dfteal, dfred), TikZ libraries, pgfplots, colortbl, compactlist environment, bottomnote command, highlight command.

**Preamble is IDENTICAL**: Copy the KNN mini-lecture preamble verbatim (lines 1-105), changing only:
- `\title[KNN Mini-Lecture]{K-Nearest Neighbors}` -> `\title[K-Means Mini-Lecture]{K-Means Clustering}`
- `\subtitle{A 10-Slide Mini-Lecture}` stays the same.

**Available chart assets** (all confirmed present in `slides/L03_KNN_KMeans/`):
- `03_kmeans_iteration/chart.pdf` -- K-Means iteration visualization (assign -> update -> repeat)
- `04_elbow_method/chart.pdf` -- Elbow method for choosing K
- `05_silhouette/chart.pdf` -- Silhouette scores for cluster quality
- `06_voronoi/chart.pdf` -- Voronoi diagram showing K-Means decision boundaries

**Available images**:
- `images/2731_kmeans_clustering.png` -- XKCD #2731 on K-Means

**Existing TikZ patterns in L03_knn_mini.tex**: Stick figures with circle heads, speech/thought bubbles via `rounded corners` and `ellipse` nodes (NOT `ellipse callout` -- the KNN file avoids callout shapes for compatibility), step diagrams with `stepnode` style, stakeholder maps with `actor` style, balance scales with manual coordinate geometry. All at `scale=0.75`.

**CRITICAL LESSON**: The KNN build used `rounded corners` rectangles and plain `ellipse` nodes for speech/thought bubbles instead of `shapes.callouts` library shapes. This proved more reliable for compilation. The K-Means build MUST follow the same pattern.

---

## Work Objectives

### Core Objective
Produce a single standalone .tex file (`L03_kmeans_mini.tex`) containing exactly 10 content frames following the interleaved WHY-FEEL-WHAT-CASE-HOW-RISK-WHERE-IMPACT-SO WHAT-ACT arc, with 10 distinct visual types, all compilable with pdflatex without external dependencies beyond the existing chart PDFs.

### Deliverables
1. `slides/L03_KNN_KMeans/L03_kmeans_mini.tex` -- the complete 10-slide mini-lecture
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
- Exact preamble from `L03_knn_mini.tex` (lines 1-99 = all definitions up to \mathbold; skip blank line 100; write new title block at lines 101-105; then \begin{document}) -- this already includes:
  - `\usepackage{colortbl}` for `\rowcolor` in slide 3's comparison table
  - `\definecolor{dfteal}{RGB}{0,128,128}` and `\definecolor{dfred}{RGB}{180,30,30}`
  - `\usetikzlibrary{arrows.meta,positioning,shapes.callouts,shapes.geometric,decorations.pathreplacing}`
  - `\usepackage{pgfplots}` and `\pgfplotsset{compat=1.18}`
  - compactlist environment, bottomnote command, highlight command
- Title block: `\title[K-Means Mini-Lecture]{K-Means Clustering}`, `\subtitle{A 10-Slide Mini-Lecture}`, `\author{Methods and Algorithms}`, `\institute{MSc Data Science}`, `\date{}`
- `\begin{document}` with NO title page (all 10 slides are content frames)
- Relative paths to chart assets: `03_kmeans_iteration/chart.pdf`, `04_elbow_method/chart.pdf`, `05_silhouette/chart.pdf`, `06_voronoi/chart.pdf`

### Must NOT Have
- No title slide or outline slide (the 10 slides ARE the entire deck)
- No `\section{}` or `\tableofcontents` commands
- No specific company names, dollar amounts, specific years, or named individuals
- No subplots or multi-panel figures within a single slide
- No `\large` or `\Large` font sizes in body text (only in TikZ accent elements like the "?" on slide 9)
- No bare `\begin{itemize}` without `\compactlist` wrapper (except inside blocks)
- No `ellipse callout` or `cloud callout` TikZ shapes (use plain `ellipse` nodes with rounded corners, matching the KNN pattern)

---

## All 10 Slide Titles

| # | Role | Title |
|---|------|-------|
| 1 | WHY | "Why Would a Marketing Team Want to Group Customers Without Labels?" |
| 2 | FEEL | "Sorting a Crowd -- Did Clustering Cross Your Mind?" |
| 3 | WHAT | "What Makes K-Means Different from DBSCAN, Hierarchical, and GMM?" |
| 4 | CASE | "Follow One Iteration from Random Centers to Stable Clusters" |
| 5 | HOW | "Who Should Pick the Starting Centers -- Random, K-Means++, or Both?" |
| 6 | RISK | "What Could Go Wrong If You Choose the Wrong K?" |
| 7 | WHERE | "Why Do So Many Practitioners Reach for K-Means First?" |
| 8 | IMPACT | "Who Wins and Who Loses When Clusters Replace Categories?" |
| 9 | SO WHAT | "3 Questions That Reveal Whether K-Means Is the Right Algorithm" |
| 10 | ACT | "Can You Evaluate This Real Clustering Problem?" |

---

## Slide-by-Slide Specification

---

### SLIDE 1: WHY -- TikZ Comic (Dilemma)

**Title**: "Why Would a Marketing Team Want to Group Customers Without Labels?"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "The Dilemma"
- `\compactlist`:
  - A bank has thousands of customers but no pre-defined categories
  - Management asks "which customers are similar?" but nobody agrees on the definition
  - The data has patterns -- but nobody has labeled them yet
- Transition line: "What if the structure is already in the data -- waiting to be discovered?"

**Right column** (0.42, TikZ comic):
- `\begin{tikzpicture}[scale=0.75]`
- **Scene**: Two stick figures. Left figure (dfteal, labeled "Analyst") stands at a desk. Right figure (mlpurple, labeled "Manager") stands with arms raised in frustration.
- **Speech bubble** (Manager, rounded corners rectangle, mlpurple fill!10): "How many customer segments do we have?"
- **Thought bubble** (Analyst, ellipse node, mllavender4 fill): "...the data probably knows, if I let it speak."
- Stick figures: simple lines + circles (SAME construction as KNN slide 1), `\tiny` labels
- **Punchline element**: Cluster of scattered dots below the figures: 3 color-coded groups (mlgreen, mlorange, dfteal) with dotted circles around each group, suggesting latent clusters
- Leading thought-bubble dots: 2-3 small filled circles in mlpurple

**Insight block**:
```
\begin{block}{Insight}
K-Means formalizes unsupervised discovery: let the algorithm find groups that the data itself defines, rather than imposing human categories.
\end{block}
```

**Bottomnote**: "Unsupervised learning finds structure without labels -- the algorithm discovers categories, not confirms them"

**Colors dominant**: dfteal (analyst), mlpurple (manager), mlgreen/mlorange/dfteal (cluster dots)

---

### SLIDE 2: FEEL -- Text-Only with Prompt

**Title**: "Sorting a Crowd -- Did Clustering Cross Your Mind?"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "Think Before You Compute"
- Narrative paragraph (`\footnotesize`): "Imagine walking into a large networking event. Within minutes, you mentally group people: the tech crowd by the coffee machine, the finance crowd near the bar, the academics huddled around the whiteboard. Nobody told you these groups existed. You found them by similarity."
- `\compactlist`:
  - How many groups did you identify? What made you pick that number?
  - What "features" separated the groups -- clothing, conversation, location?
  - Did some people seem to belong to two groups at once?

**Right column** (0.42, reflective prompt -- NO visual):
- `\footnotesize`
- Framed text box using `\fcolorbox{mlpurple}{mllavender4}{\parbox{0.85\columnwidth}{...}}`:
  - "Pause and reflect:"
  - "When you last organized files on your desktop, did you create folders by searching for natural groupings rather than following a predefined scheme?"
  - "That is K-Means."

**Exampleblock** (instead of insight block):
```
\begin{exampleblock}{Reflection Prompt}
Write down one situation this week where you mentally grouped things by similarity. How did you decide how many groups to create?
\end{exampleblock}
```

**Bottomnote**: "Clustering mirrors how humans naturally organize: by perceived similarity, not by assigned labels"

**Colors**: mlpurple (frame border), mllavender4 (frame fill)

---

### SLIDE 3: WHAT -- Comparison Table

**Title**: "What Makes K-Means Different from DBSCAN, Hierarchical, and GMM?"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text + table):
- `\small` font
- Bold header: "Taxonomy of Clustering Algorithms"
- `\footnotesize` table using `\begin{tabular}{@{}l c c c c@{}}` with `\toprule`, `\midrule`, `\bottomrule`:

| Property | K-Means | DBSCAN | Hier. | GMM |
|----------|---------|--------|-------|-----|
| Choose K? | Yes | No | Cut tree | Yes |
| Shape | Spherical | Arbitrary | Any | Elliptical |
| Outliers | Assigns all | Detects | Assigns all | Soft assign |
| Speed | O(nKt) | O(n log n) | O(n^2) | O(nK) |
| Output | Hard | Hard+noise | Dendrogram | Soft |

- **Pattern to notice** (bold after table): "K-Means is the fastest and simplest, but assumes spherical clusters and assigns every point -- no outlier detection."

**Right column** (0.42, structured summary):
- `\footnotesize`
- Four color-coded mini-boxes (using `\colorbox`):
  - `\colorbox{dfteal!15}` -- "K-Means: Fast, spherical, hard assignment"
  - `\colorbox{mlorange!15}` -- "DBSCAN: Density-based, arbitrary shapes"
  - `\colorbox{mlpurple!15}` -- "Hierarchical: Tree of merges, any K"
  - `\colorbox{mlgreen!15}` -- "GMM: Probabilistic, soft membership"

**Insight block**:
```
\begin{block}{Insight}
\scriptsize K-Means wins on speed and simplicity but pays a price: it cannot discover non-spherical clusters or flag outliers. Know the tradeoff before you choose.
\end{block}
```

**Bottomnote**: "Spherical assumption means K-Means minimizes within-cluster variance, equivalent to Voronoi tessellation"

---

### SLIDE 4: CASE -- Step Diagram / Timeline

**Title**: "Follow One Iteration from Random Centers to Stable Clusters"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "One Iteration, Step by Step"
- `\compactlist`:
  - Start with K randomly placed centroids in feature space
  - Assign every data point to the nearest centroid (Voronoi partition)
  - Recompute each centroid as the mean of its assigned points
  - Repeat assign-update until centroids stop moving
  - Convergence guaranteed: each step reduces within-cluster sum of squares

**Right column** (0.42, TikZ step diagram):
- `\begin{tikzpicture}[scale=0.75]`
- **4 numbered nodes** arranged vertically, connected by arrows (using `stepnode` style from KNN):
  1. `\node[stepnode, fill=mlorange!20]` -- "1. Initialize K centroids"
  2. `\node[stepnode, fill=mllavender4]` -- "2. Assign to nearest"
  3. `\node[stepnode, fill=dfteal!20]` -- "3. Recompute means"
  4. `\node[stepnode, fill=mlgreen!20, thick]` -- "4. Converged? Output"
- Arrows between nodes using `[-{Stealth[length=2mm]}]`
- **Feedback loop**: Curved arrow from the decision diamond's "Yes" branch back to node 2, labeled "repeat" in `\tiny`, using `dfred, densely dashed` style
- `\tiny` labels on arrows: "Voronoi", "centroid update", "WCSS check"
- **Decision diamond** between nodes 3 and 4: "Moved?" with two branches: "No -> output" and "Yes -> loop back"

**Insight block**:
```
\begin{block}{Insight}
\scriptsize K-Means always converges, but to a local minimum -- not necessarily the global one. The final clusters depend on where you started.
\end{block}
```

**Bottomnote**: "Each iteration is O(nKd): n points, K clusters, d dimensions. Typically converges in few iterations."

---

### SLIDE 5: HOW -- Side-by-Side Architecture

**Title**: "Who Should Pick the Starting Centers -- Random, K-Means++, or Both?"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "Three Initialization Strategies"
- `\compactlist`:
  - **Random**: Pick K points at random. Fast but high variance. May converge to poor local minimum.
  - **K-Means++**: First center random, then each next center chosen proportional to squared distance from nearest existing center. Spreads centers out.
  - **Multiple restarts**: Run K-Means R times with different random seeds, keep the result with lowest WCSS. The brute-force hedge.
- Transition: "K-Means++ is now the default in scikit-learn for good reason."

**Right column** (0.42, TikZ side-by-side):
- `\begin{tikzpicture}[scale=0.75]`
- **Two sub-diagrams** stacked vertically:
  - **Top** ("Random Init"): A rectangle region with scattered dots (mlgray). Three initial centroids (dfred, filled triangles or stars) placed randomly -- two are very close together, one is far away. Dotted lines showing poor Voronoi regions. Label: "Unlucky: two centers in same cluster" in `\tiny`.
  - **Bottom** ("K-Means++ Init"): Same data region with same scattered dots. Three centroids now well-spread (dfteal, filled triangles or stars). Dotted lines show balanced Voronoi regions. Label: "Spread out: better coverage" in `\tiny`.
- Accent arrow between top and bottom labeled "K-Means++ fixes this" in `\tiny dfteal`

**Insight block**:
```
\begin{block}{Insight}
\scriptsize K-Means++ initialization reduces both the expected WCSS and the number of iterations. It is a cheap insurance policy against bad starts.
\end{block}
```

**Bottomnote**: "K-Means++ guarantees O(log K)-competitive approximation to optimal WCSS (Arthur and Vassilvitskii)"

---

### SLIDE 6: RISK -- TikZ Comic (Failure)

**Title**: "What Could Go Wrong If You Choose the Wrong K?"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "Three Ways K-Means Fails Silently"
- `\compactlist`:
  - **Wrong K**: too few clusters merge distinct groups, too many split natural groups
  - **Non-spherical data**: K-Means forces round clusters onto elongated or crescent-shaped structure
  - **Bad initialization**: unlucky starting centroids trap the algorithm in a poor local minimum
- Each failure tagged with a consequence: "misleading segments", "artificial boundaries", "unstable results"

**Right column** (0.42, TikZ comic -- DIFFERENT emotional register from slide 1):
- `\begin{tikzpicture}[scale=0.75]`
- **Scene**: A single stick figure (dfred color, labeled "K-Means") stands in the center, arms outstretched. Around it are two crescent-shaped / banana-shaped point clouds (drawn as arcs of mlgreen and mlorange dots). A straight dotted line (dfred, thick) cuts through the middle, clearly splitting each crescent in half rather than separating the two crescents.
- **Speech bubble** (K-Means, rounded corners rectangle, dfred!10 fill): "I split everything into perfect circles... but the data is not round!"
- **Visual element**: A large dfred "X" stamped over the wrong boundary line with `\tiny` label "Wrong Assumption"
- **Emotional register**: Frustration and futility (vs. slide 1's curiosity and hope). The stick figure has "!" marks on both sides.

**Insight block**:
```
\begin{block}{Insight}
\scriptsize K-Means always finds K clusters, even when the true number is different. The algorithm never says "I don't know" -- silence is not confidence.
\end{block}
```

**Bottomnote**: "Diagnostics: elbow method for K, silhouette score for cluster quality, visual inspection for shape assumptions"

**Colors dominant**: dfred (failure stick figure, X stamp, wrong boundary), mlgreen/mlorange (crescent clouds)

---

### SLIDE 7: WHERE -- External Chart (PDF)

**Title**: "Why Do So Many Practitioners Reach for K-Means First?"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "K-Means as a Baseline Clusterer"
- `\compactlist`:
  - Scales linearly with data size -- handles millions of points
  - Simple to implement, explain, and debug
  - Results easy to interpret: each cluster has a centroid
  - Natural starting point before trying complex alternatives
- Sentence: "The chart shows how cluster boundaries emerge from the iteration process."

**Right column** (0.42, external chart):
- **Primary option**: `\includegraphics[width=\textwidth]{03_kmeans_iteration/chart.pdf}`
- This shows the K-Means iteration process visually, which directly supports the "how it works" narrative.
- **Rationale for chart choice**: The iteration chart (03) is the most pedagogically relevant for a slide about why K-Means is popular -- it shows the algorithm's elegant simplicity. The elbow chart (04) and silhouette chart (05) are better suited for the activity slide (10) or diagnostics discussion.

**Insight block**:
```
\begin{block}{Insight}
\scriptsize K-Means owes its popularity to the same property as linear regression: it is the simplest reasonable solution, making it the natural baseline.
\end{block}
```

**Bottomnote**: "K-Means with K=2 is equivalent to finding the optimal split of data along the first principal component direction"

---

### SLIDE 8: IMPACT -- Stakeholder Map

**Title**: "Who Wins and Who Loses When Clusters Replace Categories?"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "Stakeholder Analysis"
- `\compactlist`:
  - **Winners**: Marketing teams (data-driven segments), fraud detection (anomaly = far from all centroids), data preprocessing (dimensionality reduction via cluster features)
  - **Losers**: Domain experts (their intuitive categories may be overridden), interpretability advocates (cluster labels are arbitrary), anyone expecting stable segments (different runs may yield different groups)
- Sentence: "K-Means shifts power from domain intuition to data patterns -- for better and worse."

**Right column** (0.42, TikZ stakeholder map):
- `\begin{tikzpicture}[scale=0.75]`
- **Center node**: Rounded rectangle, mlpurple fill, white text: "K-Means Clusters" (using `actor` style from KNN)
- **4 surrounding actor nodes** arranged in diamond/cross (SAME layout as KNN slide 8):
  - Top: "Marketing" (mlgreen!20 fill, mlgreen border) with arrow TO center labeled "segments customers" (`\tiny`)
  - Right: "Fraud Team" (dfteal!20 fill, dfteal border) with arrow FROM center labeled "flags anomalies" (`\tiny`)
  - Bottom: "Domain Expert" (dfred!20 fill, dfred border) with arrow FROM center labeled "intuition overridden" (`\tiny`)
  - Left: "Data Engineer" (mlorange!20 fill, mlorange border) with arrow TO center labeled "preprocesses features" (`\tiny`)
- **Edge annotations** (`\tiny`): same `arr` style as KNN slide 8

**Insight block**:
```
\begin{block}{Insight}
\scriptsize K-Means clusters are not "real" categories -- they are mathematical artifacts. The business meaning must be assigned after the algorithm finishes.
\end{block}
```

**Bottomnote**: "Cluster interpretation requires domain expertise: the algorithm finds groups, humans name them"

---

### SLIDE 9: SO WHAT -- Metaphor Visual (Balance Scale)

**Title**: "3 Questions That Reveal Whether K-Means Is the Right Algorithm"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "The Decision Framework"
- Numbered list (1-3), each with a question and a diagnostic:
  1. **"Are the clusters roughly spherical?"** -- If the data has elongated, crescent, or nested shapes, K-Means will force round boundaries. Consider DBSCAN or spectral clustering.
  2. **"Do you know how many clusters to expect?"** -- K-Means requires K upfront. If you have no prior on K, use the elbow method or silhouette analysis, or consider hierarchical clustering.
  3. **"Is every point a member of exactly one group?"** -- K-Means does hard assignment. If overlap is natural, GMM gives soft (probabilistic) membership.
- Concluding sentence: "If all three answers are 'yes,' K-Means is a strong candidate."

**Right column** (0.42, TikZ balance scale):
- `\begin{tikzpicture}[scale=0.75]`
- **SAME STRUCTURE as KNN slide 9** -- fulcrum, tilted beam, two pans, question mark:
- **Fulcrum**: Triangle at bottom center (mlgray)
- **Beam**: Tilted slightly left (indicating "use K-Means" is heavier/winning)
- **Left pan** (dfteal): labeled "Use K-Means" with three small rectangles: "Spherical", "Known K", "Hard OK" in mlgreen fill
- **Right pan** (dfred): labeled "Avoid K-Means" with three small rectangles: "Elongated", "Unknown K", "Overlap" in mlred fill
- **Tilt**: Beam tilted ~10 degrees toward left
- **Question mark**: Large "?" above fulcrum in mlpurple

**Insight block**:
```
\begin{block}{Insight}
\scriptsize No clustering algorithm is universally best. K-Means excels on spherical, well-separated clusters with known K -- and fails gracefully when you monitor these three diagnostics.
\end{block}
```

**Bottomnote**: "The 'No Free Lunch' theorem applies to clustering too: no single algorithm dominates all data shapes"

---

### SLIDE 10: ACT -- Activity Frame

**Title**: "Can You Evaluate This Real Clustering Problem?"

**Layout**: Two-column [T], 0.55 + 0.42

**Left column** (0.55, text):
- `\small` font
- Bold header: "The Scenario"
- `\footnotesize` narrative: "A retail bank wants to segment its customer base for targeted marketing. Features: monthly income, average transaction amount, number of transactions, account tenure, credit utilization ratio. The bank suspects there are natural groupings but has no predefined categories. All features are numerical."
- `\compactlist`:
  - Apply the 3-question framework from the previous slide
  - Decide: Is K-Means appropriate here?
  - If yes: recommend a K and explain how you would validate it
  - If no: name a better algorithm and explain why

**Right column** (0.42, structured activity):
- `\footnotesize`
- Framework table using `\begin{tabular}{@{}l p{2.8cm}@{}}`:

| Question | Your Answer |
|----------|-------------|
| Spherical clusters? | \_\_\_\_\_\_\_ |
| Known K? | \_\_\_\_\_\_\_ |
| Hard assignment OK? | \_\_\_\_\_\_\_ |
| **Verdict** | \_\_\_\_\_\_\_ |
| Recommended K | \_\_\_\_\_\_\_ |
| Validation method | \_\_\_\_\_\_\_ |

**Exampleblock** (instead of insight block):
```
\begin{exampleblock}{Deliverable}
\scriptsize Fill in the table. Be prepared to defend your verdict to a skeptical marketing director who asks: "Why can't we just use our existing customer categories?"
\end{exampleblock}
```

**Bottomnote**: "Hint: consider the feature space shape, the business context, and how you would validate cluster quality"

---

## TikZ Comic Descriptions (Detailed)

### Slide 1 Comic (Dilemma -- dfteal dominant)

**Characters**:
- **Analyst** (left, x=1, y=2): Stick figure drawn with dfteal lines. Circle head (radius 0.15cm), body line, two arm lines, two leg lines. SAME construction as KNN Officer. Label "Analyst" below in `\tiny`.
- **Manager** (right, x=3.5, y=2): Stick figure drawn with mlpurple lines. Same construction. Label "Manager" below. "!" above head in mlorange (frustrated).

**Dialogue**:
- Speech bubble from Manager (rounded corners rectangle, fill=mlpurple!10, draw=mlpurple): "How many segments do we have?"
- Thought bubble from Analyst (ellipse node, fill=mllavender4, draw=mlpurple): "...the data probably knows." Plus 2-3 small leading circles in mlpurple.

**Environment**:
- Below the figures (y=0 to y=0.8): Scatter of ~15 small dots in 3 color groups:
  - 5 mlgreen dots clustered around (0.5, 0.4)
  - 5 mlorange dots clustered around (2.0, 0.6)
  - 5 dfteal dots clustered around (3.5, 0.3)
- Dotted circles around each group (matching color, dashed)

**Punchline**: The contrast between the manager's demand for a fixed answer and the analyst's realization that the data holds the answer.

### Slide 6 Comic (Failure -- dfred dominant, DIFFERENT register)

**Characters**:
- **K-Means** (center, x=2.5, y=2): Single stick figure in dfred. "!" on both sides of head. Label "K-Means" below.

**Environment**:
- Two crescent/banana shapes made of small dots:
  - Upper crescent: 5-7 mlgreen dots in an arc from (0.5, 3.0) to (4.0, 3.5)
  - Lower crescent: 5-7 mlorange dots in an arc from (1.0, 0.5) to (4.5, 1.0)
- A vertical dashed line (dfred, thick) at x=2.5 cutting through both crescents, showing the WRONG split
- Each crescent gets split in half by this line, illustrating how spherical assumption fails

**Speech bubble**: Rounded corners rectangle from K-Means (fill=dfred!10, draw=dfred): "I only know circles... but the data is curved!"

**Visual element**: Large dfred "X" overlaid diagonally. `\tiny` label "Wrong Assumption" at bottom-right.

**Emotional register contrast with Slide 1**: Slide 1 is curious and hopeful (the analyst has a path forward). Slide 6 is frustrated and trapped (the algorithm cannot handle the data shape). Different character, different color, different emotion.

---

## Chart Selection (Slide 7)

**Selected chart**: `03_kmeans_iteration/chart.pdf`

**Rationale**: This chart shows the K-Means iteration process (centroids moving, assignments changing), which is the most compelling visual for "why K-Means is popular" -- it demonstrates the algorithm's elegant simplicity and convergence.

**Rejected alternatives**:
- `04_elbow_method/chart.pdf`: Too diagnostic, better for validation discussion
- `05_silhouette/chart.pdf`: Too technical for a "why it's popular" narrative
- `06_voronoi/chart.pdf`: Shows the result but not the process

**Implementation**: `\includegraphics[width=\textwidth]{03_kmeans_iteration/chart.pdf}`

---

## Comparison Table Spec (Slide 3)

**Columns**: Property | K-Means | DBSCAN | Hierarchical | GMM

**Rows** (5 rows to fit in `\footnotesize`):
1. Choose K?: Yes | No | Cut tree | Yes
2. Cluster shape: Spherical | Arbitrary | Any | Elliptical
3. Outliers: Assigns all | Detects | Assigns all | Soft assign
4. Speed: O(nKt) | O(n log n) | O(n^2) | O(nK)
5. Output: Hard labels | Hard+noise | Dendrogram | Soft probabilities

**Pattern to notice**: K-Means is the fastest and simplest, but it assumes spherical clusters and assigns every point -- no outlier detection.

**Formatting**: Use `\rowcolor{mllavender4}` on rows 1, 3, 5 (alternating). Bold the K-Means column header in dfteal. Use `\footnotesize` for table text. Use abbreviated headers to prevent overflow: "K-M", "DBS", "Hier.", "GMM" if space requires it.

---

## Step Diagram Spec (Slide 4)

**4 numbered nodes**, vertical flow, top to bottom:

1. **"1. Initialize K centroids"** -- mlorange!20 fill, rounded corners
   - Arrow down, labeled "random or K-Means++" (`\tiny`)
2. **"2. Assign to nearest"** -- mllavender4 fill
   - Arrow down, labeled "Voronoi partition" (`\tiny`)
3. **"3. Recompute means"** -- dfteal!20 fill (highlighted as the core step)
   - Arrow down, labeled "centroid update" (`\tiny`)
4. **"4. Converged? Output"** -- mlgreen!20 fill, thick border

**Decision diamond** between nodes 3 and 4: "Moved?" with:
- "No" branch -> continue down to node 4
- "Yes" branch -> curved dashed arrow looping back to node 2

**Layout**: Nodes at y = 5.0, 3.9, 2.8, 1.2 (top to bottom). Decision diamond at y ~1.7, offset right. Feedback loop curves outside the main column.

---

## Architecture Diagram Spec (Slide 5)

**Two sub-diagrams** stacked vertically within the TikZ picture:

**Top sub-diagram** ("Random Init"):
- Gray rectangle region (mlgray!10 fill, 3cm x 2cm)
- ~8 small gray dots scattered as data points
- 3 centroid markers (dfred, filled circles or triangles): TWO placed close together in the left half, one alone on the right
- Dotted lines from centroids creating Voronoi regions -- clearly unbalanced
- `\tiny` label: "Unlucky: two centers overlap"

**Bottom sub-diagram** ("K-Means++ Init"):
- Same rectangle region, same data points
- 3 centroid markers (dfteal, filled circles or triangles): well spread across the region
- Dotted lines showing balanced Voronoi regions
- `\tiny` label: "Spread: better coverage"

**Accent**: Arrow from top to bottom with `\tiny dfteal` label "K-Means++ fixes this"

---

## Stakeholder Map Spec (Slide 8)

**SAME STRUCTURE as KNN slide 8** -- center node with 4 surrounding actors in diamond arrangement.

**Central node**: Rounded rectangle (1.4cm width), mlpurple fill, white text: "K-Means"

**4 actor nodes** (diamond arrangement, using `actor` style):
- **Top** (y=4.0): "Marketing" -- mlgreen!20 fill, mlgreen border
  - Arrow TO center, labeled "segments customers" (`\tiny`)
- **Right** (x=4.5): "Fraud Team" -- dfteal!20 fill, dfteal border
  - Arrow FROM center, labeled "flags anomalies" (`\tiny`)
- **Bottom** (y=0.4): "Domain Expert" -- dfred!20 fill, dfred border
  - Arrow FROM center, labeled "intuition overridden" (`\tiny`)
- **Left** (x=0): "Data Eng." -- mlorange!20 fill, mlorange border
  - Arrow TO center, labeled "preprocesses" (`\tiny`)

**Edge style**: `[-{Stealth[length=1.5mm]}, thick, mlgray]` -- identical to KNN slide 8

---

## Balance Scale Spec (Slide 9)

**SAME GEOMETRY as KNN slide 9** -- copy the coordinate structure exactly.

**Fulcrum**: Equilateral triangle at (2.5, 0.2), mlgray fill: `\fill[mlgray] (2.5,0.2) -- (2.1,0) -- (2.9,0) -- cycle;`

**Beam**: Line from (0.3,1.5) to (4.7,2.1) -- tilted ~10 degrees left (K-Means side heavier)

**Left pan** ("Use K-Means"):
- Suspension lines from (0.3,1.5) to (0.0,0.8) and (1.8,0.8)
- Rectangular tray: dfteal!20 fill, dfteal border, (0.0,0.3) to (1.8,0.8)
- 3 small rectangles (mlgreen fill): "Spherical", "Known K", "Hard OK"
- Label below: "Use K-Means" in `\tiny dfteal`

**Right pan** ("Avoid K-Means"):
- Suspension lines from (4.7,2.1) to (3.5,1.4) and (5.3,1.4)
- Rectangular tray: dfred!20 fill, dfred border, (3.5,0.9) to (5.3,1.4)
- 3 small rectangles (mlred fill): "Elongated", "Unknown K", "Overlap"
- Label below: "Avoid K-Means" in `\tiny dfred`

**Question mark**: `\node[mlpurple, font=\Large\bfseries] at (2.5,3.2) {?};`

---

## Activity Spec (Slide 10)

**Case description** (left column):
- Scenario: Retail bank, customer segmentation for targeted marketing
- Features: monthly income, avg transaction amount, number of transactions, account tenure, credit utilization (d=5)
- Dataset: moderate size, all numerical, no predefined categories
- Students apply the 3-question framework

**Framework table** (right column):

| Question | Your Answer |
|----------|-------------|
| Spherical clusters? | \_\_\_\_ |
| Known K? | \_\_\_\_ |
| Hard assignment OK? | \_\_\_\_ |
| **Verdict: K-Means appropriate?** | \_\_\_\_ |
| If yes: recommended K | \_\_\_\_ |
| Validation method | \_\_\_\_ |

**Exampleblock text**: "Fill in the table. Be prepared to defend your verdict to a skeptical marketing director who asks: 'Why can't we just use our existing customer categories?'"

**Design intent**: The table forces structured thinking about K-Means appropriateness. The defense question forces students to articulate K-Means' unique value proposition (data-driven discovery, no label bias) versus predefined categories' advantages (interpretable, stable, domain-grounded).

---

## File Location and Compilation

**File**: `slides/L03_KNN_KMeans/L03_kmeans_mini.tex`

**Compilation**:
```bash
cd slides/L03_KNN_KMeans
pdflatex -interaction=nonstopmode L03_kmeans_mini.tex
pdflatex -interaction=nonstopmode L03_kmeans_mini.tex
mkdir temp 2>nul & move *.aux *.log *.nav *.out *.snm *.toc temp/
```

Two passes required for page numbers. The file references `03_kmeans_iteration/chart.pdf` via relative path from its own directory.

**Dependencies**:
- pdflatex with TikZ, pgfplots (standard TeX Live / MiKTeX)
- `03_kmeans_iteration/chart.pdf` must exist (already present in repo, confirmed)
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
Task 3: Write slides 6-10 (depends on Task 1, can parallel with Task 2)
   |
   v
Task 4: Compile and fix overflow (depends on Tasks 2+3)
   |
   v
Task 5: Verify against checklist (depends on Task 4)
```

### Detailed TODOs

**TODO 1: Create preamble and file skeleton**
- Copy preamble from `L03_knn_mini.tex` lines 1-99 verbatim
- Change ONLY the title line: `\title[K-Means Mini-Lecture]{K-Means Clustering}`
- Keep `\subtitle{A 10-Slide Mini-Lecture}`, `\author{Methods and Algorithms}`, `\institute{MSc Data Science}`, `\date{}`
- Create `\begin{document}` ... `\end{document}` with 10 empty frame placeholders
- **Acceptance**: File compiles with 10 empty frames, no errors

**TODO 2: Implement slides 1-2 (WHY + FEEL)**
- Slide 1: TikZ comic with Analyst/Manager stick figures, speech/thought bubbles, scattered cluster dots below
- Slide 2: Text-only with fcolorbox prompt and exampleblock
- **Acceptance**: Both slides compile, TikZ renders without errors, slide 2 uses exampleblock

**TODO 3: Implement slides 3-4 (WHAT + CASE)**
- Slide 3: Comparison table with 4 algorithms, booktabs, alternating rowcolor, color-coded summary boxes
- Slide 4: TikZ step diagram with 4 nodes, decision diamond, feedback loop arrow
- **Acceptance**: Table renders with correct alignment and no overflow, step diagram flows top-to-bottom with visible loop-back

**TODO 4: Implement slides 5-6 (HOW + RISK)**
- Slide 5: Side-by-side TikZ showing random init (bad) vs K-Means++ init (good)
- Slide 6: TikZ failure comic with dfred dominant, crescent-shaped data, wrong boundary line
- **Acceptance**: Both TikZ diagrams render, slide 6 uses dfred not dfteal, different emotional register from slide 1

**TODO 5: Implement slides 7-8 (WHERE + IMPACT)**
- Slide 7: Include `03_kmeans_iteration/chart.pdf` via `\includegraphics[width=\textwidth]`
- Slide 8: TikZ stakeholder map with 4 actors (Marketing, Fraud Team, Domain Expert, Data Engineer) and directional arrows
- **Acceptance**: Chart.pdf included at correct size, stakeholder map has all 4 actors with labeled arrows

**TODO 6: Implement slides 9-10 (SO WHAT + ACT)**
- Slide 9: TikZ balance scale with SAME geometry as KNN slide 9, but K-Means labels (Spherical/Known K/Hard OK vs Elongated/Unknown K/Overlap)
- Slide 10: Activity frame with banking segmentation scenario and framework table, exampleblock
- **Acceptance**: Scale tilts correctly, table has blank answer cells, slide 10 uses exampleblock

**TODO 7: Compile and fix overflow**
- Run `pdflatex -interaction=nonstopmode L03_kmeans_mini.tex` twice
- Check for overfull hbox warnings
- Fix any overflow by adjusting font sizes, rewording, or reducing content
- **Known risk areas**: Slide 3 table (4 algorithm columns may be tight -- use abbreviated headers if needed), Slide 5 two-diagram TikZ (may need vertical compression)
- **Acceptance**: Zero overfull hbox warnings on strict validation

**TODO 8: Final verification against checklist**
- Run full checklist (see below)
- **Acceptance**: All checklist items pass

---

## Commit Strategy

**Single commit** after all TODOs complete:
```
Add K-Means mini-lecture: 10-slide standalone with TikZ visuals

New file L03_kmeans_mini.tex following the WHY-FEEL-WHAT-CASE-HOW-RISK-
WHERE-IMPACT-SO WHAT-ACT interleaved arc. Includes inline TikZ comics,
step diagrams, initialization comparison, stakeholder map, balance scale
metaphor, and clustering comparison table. Reuses existing
03_kmeans_iteration chart. Self-contained and compilable with pdflatex.
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
- [ ] Slide 4: Step diagram with numbered nodes and feedback loop
- [ ] Slide 5: Side-by-side architecture (random vs K-Means++ init)
- [ ] Slide 6: TikZ comic (failure, dfred dominant, DIFFERENT register from slide 1)
- [ ] Slide 7: External chart PDF (03_kmeans_iteration)
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
- [ ] Zero overfull hbox warnings
- [ ] File compiles cleanly with pdflatex

**Content Accuracy:**
- [ ] K-Means algorithm correctly described (iterative: assign to nearest centroid, recompute means, repeat)
- [ ] Convergence guaranteed (WCSS monotonically decreasing) but to local minimum only
- [ ] K-Means++ initialization correctly explained (distance-proportional sampling)
- [ ] Comparison with DBSCAN, hierarchical, GMM is fair and accurate
- [ ] Failure modes correctly identified: wrong K, non-spherical data, bad initialization
- [ ] 3-question framework is actionable (spherical? known K? hard assignment OK?)
- [ ] Activity scenario is realistic for MSc Data Science students

**Structural Matching with KNN Mini-Lecture:**
- [ ] Same preamble (lines 1-99 identical except title)
- [ ] Same TikZ construction patterns (stick figures, stepnode style, actor style, balance scale geometry)
- [ ] Same speech/thought bubble approach (rounded corners + ellipse nodes, NOT callout shapes)
- [ ] Same column widths (0.55 + 0.42)
- [ ] Same block placement pattern (insight blocks at bottom of left column)
- [ ] Same `\compactlist` usage throughout

---

PLAN_READY
