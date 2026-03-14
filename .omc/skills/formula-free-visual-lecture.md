---
id: formula-free-visual-lecture
name: "Formula-Free Visual Lecture Creator"
description: >
  Complete pattern for creating ultra-simple, beginner-friendly Beamer lectures that teach
  complex technical concepts with zero formulas. Uses curated subsets of existing charts,
  TikZ stick-figure comics at structural points, real-world visual analogies, and dramatic
  narrative arcs. Supports 4 arc types: contrast (A vs B), parallel (A + B), single-topic
  (focused), and evolution (old -> new). Proven across 7 implementations: L05 simple,
  L06 combined, L06a/b split, L06c LLM evolution.
source: Extracted from L05_pca_tsne_simple.tex gold standard + 6 additional implementations (Mar 2026)
triggers:
  - "simple lecture"
  - "visual guide"
  - "no formulas"
  - "beginner friendly"
  - "ultra simple"
  - "comics"
  - "visual analogies"
  - "subset of charts"
  - "reuse charts"
  - "create lecture"
  - "new slides"
  - "formula-free"
  - "TikZ stick figure"
quality:
  googleable: false
  codebase_specific: true
  actionable: true
  hard_won: true
---

# Formula-Free Visual Lecture Creator

## The Insight

Complex technical concepts can be taught effectively in 16-25 slides with ZERO formulas
by combining three elements:

1. **Curated chart subset** from existing pool (don't create new charts)
2. **TikZ stick-figure comics** at structural transition points
3. **Dramatic narrative arc** chosen from 4 proven patterns

The key constraint that makes it work: **max 25 lines of TikZ per comic, stick figures only**.
This forces simplicity and prevents TikZ overflow disasters.

## Why This Matters

Full technical lectures contain eigenvalue equations, Lagrangian derivations, and matrix
notation. Some audiences (executives, first-week students, cross-discipline collaborators)
need the intuition without the math. Creating a formula-free version from scratch is slow;
creating one by curating existing charts and adding comics is fast and effective.

## Recognition Pattern

Use this skill when:
- User asks for "simple", "visual", "beginner-friendly", "no formulas", or "visual guide"
- An existing lecture has 10+ charts available to curate from
- The audience doesn't need to compute anything, just understand concepts
- You need a complement to an existing technical lecture, not a replacement

## The Approach

### Step 1: Choose Your Narrative Arc

| Arc | When to Use | Slides | Charts | Comics | Example |
|-----|-------------|--------|--------|--------|---------|
| **Contrast** | Two methods, one fails where other succeeds | 25 | 6-8 | 4 | L05 PCA/t-SNE |
| **Parallel** | Two independent topics presented side-by-side | 25-26 | 8-10 | 4 | L06 Embeddings+RL |
| **Single-topic** | Focused lecture on one method | 16-17 | 5 | 3 | L06a, L06b |
| **Evolution** | Historical progression (old -> limit -> new) | 25 | 7 | 4+3 diagrams | L06c LLMs |

#### Arc A: Contrast (Gold Standard)

```
FRONT MATTER (3 slides)
  1. Title page
  2. XKCD opening + framing question
  3. Learning objectives (3 bullets, plain English)

ACT 1: THE PROBLEM (3 slides)
  4. TikZ comic: the problem personified
  5. CHART: proof the solution works (before/after)
  6. Text slide: why the naive approach fails

ACT 2: METHOD A (6 slides)
  7. TikZ comic: visual analogy for method A
  8. CHART: core visualization
  9. TikZ flowchart: 3-step recipe (no formulas)
  10. CHART: diagnostic
  11. CHART: method A on realistic data
  12. Transition: "but method A has a limit..."

ACT 3: METHOD B (6 slides)
  13. TikZ comic: visual analogy for method B
  14. CHART: method A FAILS on this data
  15. CHART: method B SUCCEEDS on same data
  16. Plain English explanation (3 numbered steps)
  17. CHART: method B on realistic data
  18. Gotchas / warnings (3 items max)

ACT 4: COMPARISON (4 slides)
  19. Comparison table (5 rows max)
  20. CHART: decision flowchart
  21. Domain application teaser
  22. Code recipe (3-5 lines per method)

CLOSING (3 slides)
  23. TikZ comic: resolution (same character, happy)
  24. Key takeaways (5 bullets)
  25. XKCD closing
```

#### Arc B: Single-Topic Discovery

```
FRONT MATTER (3 slides)    1-3
ACT 1: PROBLEM (2)         4-5   (comic + why naive fails)
ACT 2: HOW IT WORKS (5)    6-10  (comic + 3 charts + flowchart)
ACT 3: DEEPER PROOF (2)    11-12 (2 charts proving it works)
ACT 4: APPLICATION (2)     13-14 (domain use + code)
CLOSING (2)                15-16 (comic+takeaways, XKCD)
Total: 16-17 slides, 5 charts, 3 comics
```

#### Arc C: Evolution

```
FRONT MATTER (3 slides)
ACT 1: PROBLEM + RECAP (5)      Old method works (compressed recap)
ACT 2: GOING DEEPER + LIMIT (5) Bridge charts + "the big problem" failure
ACT 3: NEW METHOD (5)           New approach + diagrams (attention, etc.)
ACT 4: REVOLUTION + APPS (4)    Scaling story + applications
CLOSING (3 slides)
Total: 25 slides, 7 charts, 4 comics + 3 diagrams
```

**Evolution arc notes** (from L06c):
- Charts shared with other lectures for recap MUST be documented
- Bridge charts MUST include explicit framing text connecting old-scale to new-scale
- Slide explaining new method MUST have bottomnote clarifying simplifications

#### Arc D: Parallel Topics

```
FRONT MATTER (3 slides)
ACT 1: TOPIC A (7 slides)       Problem + method + 3 charts + comic
TRANSITION (1 slide)             TikZ: "Understanding vs Action" pivot
ACT 2: TOPIC B (7 slides)       Problem + method + 3 charts + comic
ACT 3: COMPARISON (4 slides)    Table + flowchart + apps + code
CLOSING (3 slides)
Total: 25-26 slides, 8-10 charts, 4 comics
```

### Step 2: Chart Curation

**Golden Rule**: Reuse existing charts. Do NOT create new chart.py files.

**Selection Heuristic**: If a chart needs >2 sentences to explain, it's too complex. Skip it.

**Story-driven selection**:

| Story Beat | Chart Type | Example |
|------------|-----------|---------|
| "Look, it works!" | Before/after | high_dim_before_after |
| "Here's how" | Core visualization | principal_components |
| "How much is enough?" | Diagnostic | scree_plot |
| "But it has limits" | Failure case | pca_swiss_roll |
| "Something better" | Success case | tsne_swiss_roll |
| "When to use what" | Decision aid | decision_flowchart |
| "Words have math" | Wow moment | word_analogy |
| "Watch it learn" | Training progress | reward_curves |

**Chart slide template** (proven pattern from L05 gold standard):
```latex
\begin{frame}{Question-Based Title?}
\centering
\includegraphics[width=0.60\textwidth]{XX_chart_name/chart.pdf}

\begin{compactlist}
  \item First observation (what the chart shows)
  \item Second observation (what it means)
  \item Third observation (what to do about it)
\end{compactlist}
\bottomnote{One-line insight or attribution.}
\end{frame}
```

**Chart widths**: `0.55\textwidth` (with side text), `0.60\textwidth` (standard), `0.65\textwidth` (max visibility)

### Step 3: TikZ Stick-Figure Comics

**Placement by arc type**:

| Arc | Comic 1 | Comic 2 | Comic 3 | Comic 4 |
|-----|---------|---------|---------|---------|
| Contrast | Slide 4 (problem) | Slide 7 (method A) | Slide 13 (method B) | Slide 23 (resolution) |
| Single | Slide 4 (problem) | Slide 7 (analogy) | Slide 15 (resolution) | -- |
| Evolution | Slide 4 (problem) | Slide 8 (old method) | Slide 15 (new method) | Slide 23 (resolution) |

**Budget Rules (STRICT)**:
- Max **25 lines** of TikZ per comic
- **Stick figures ONLY**: circle head, line body, line limbs
- **Geometric shapes ONLY**: rectangles, circles, arrows
- No realistic objects
- Use `scale=0.75` or `scale=0.8` to prevent overflow
- `\scriptsize` or `\tiny` for all labels inside TikZ

**Proven Comic Patterns**:

**1. "Character with Problem" (opening)**:
```latex
\begin{tikzpicture}[scale=0.8]
  % Stick figure
  \draw[thick] (-0.5,1.8) circle (0.3);
  \draw[thick] (-0.5,1.5) -- (-0.5,0.5);
  \draw[thick] (-0.5,1.2) -- (-1.0,0.8);
  \draw[thick] (-0.5,1.2) -- (0.0,0.8);
  \draw[thick] (-0.5,0.5) -- (-0.9,0);
  \draw[thick] (-0.5,0.5) -- (-0.1,0);
  \node[font=\small] at (-0.5,2.3) {?!?};
  \node[draw,rounded corners,fill=white,font=\scriptsize,anchor=west]
    at (0.1,2.3) {I can't see the patterns!};
  % Problem visual: stack of rectangles
  \foreach \i/\lab in {0/F1,0.3/F2,0.6/F3,1.2/...,1.5/F49,1.8/F50} {
    \fill[white] (0.8,\i) rectangle (2.2,\i+0.25);
    \draw[mlpurple] (0.8,\i) rectangle (2.2,\i+0.25);
    \node[font=\tiny] at (1.5,\i+0.125) {\lab};
  }
\end{tikzpicture}
```

**2. "Shadow/Projection Analogy" (method A)**:
```latex
\begin{tikzpicture}[scale=0.75]
  % Sun with rays
  \fill[mlorange] (-3.5,3.5) circle (0.4);
  \foreach \a in {0,45,...,315} {
    \draw[mlorange,thick] (-3.5,3.5) -- ++(\a:0.6);
  }
  % 3D cube
  \fill[mllavender4,opacity=0.5] (0,0)--(2,0)--(2,2)--(0,2)--cycle;
  \draw[mlpurple,thick] (0,0)--(2,0)--(2,2)--(0,2)--cycle;
  \node[font=\scriptsize,mlpurple] at (1,-0.4) {3D Object};
  % Wall + shadow
  \fill[lightgray] (5,0) rectangle (5.2,3.5);
  \fill[mlgray,opacity=0.4] (5.01,0.5) rectangle (5.19,2.5);
  \node[font=\scriptsize] at (5.9,1.0) {Shadow};
  % Arrow: "Best angle"
  \draw[-{Stealth},thick,mlorange] (3.0,1.5) -- (4.8,1.5);
  \node[font=\scriptsize,above] at (3.9,1.5) {Best angle};
\end{tikzpicture}
```

**3. "Before/After Panels" (resolution)**:
```latex
\begin{tikzpicture}[scale=0.75]
  % Left: confused (gray dots, X-face stick figure)
  \draw[mlgray,thick] (-5.5,-1) rectangle (-1.5,3);
  \foreach \x/\y in {-4.8/1.2,-4.2/0.5,-3.5/2.1,-2.8/0.8,-3.0/1.6} {
    \fill[mlgray!60] (\x,\y) circle (2pt);
  }
  \draw[thick] (-3.5,-0.3) circle (0.25);
  \node[font=\tiny] at (-3.5,-0.3) {X};
  \node[font=\scriptsize,below] at (-3.5,-1.3) {\textcolor{mlred}{Before}};
  % Arrow
  \draw[-{Stealth},very thick,mlpurple] (-1.2,1.0) -- (0.2,1.0);
  % Right: clear (colored clusters, smile)
  \draw[mlgray,thick] (0.5,-1) rectangle (4.5,3);
  \fill[mlblue] (1.3,2.0) circle (3pt);
  \fill[mlblue] (1.6,2.3) circle (3pt);
  \fill[mlorange] (3.0,2.1) circle (3pt);
  \fill[mlorange] (3.3,1.8) circle (3pt);
  \fill[mlgreen] (2.2,0.5) circle (3pt);
  \fill[mlgreen] (2.5,0.3) circle (3pt);
  \draw[thick] (2.5,-0.3) circle (0.25);
  \draw[thick] (2.35,-0.35) arc (210:250:0.15);
  \node[font=\scriptsize,below] at (2.5,-1.3) {\textcolor{mlgreen}{After}};
\end{tikzpicture}
```

**4. "3-Step Flowchart" (method explanation)**:
```latex
\begin{tikzpicture}[
  box/.style={draw=mlpurple, fill=mllavender4, rounded corners=4pt,
              minimum width=3.2cm, minimum height=1.2cm, align=center,
              font=\scriptsize},
  arr/.style={-{Stealth}, thick, mlpurple}
]
  \node[box] (s1) at (0,0) {\textbf{1. Step}\\Description};
  \node[box] (s2) at (5,0) {\textbf{2. Step}\\Description};
  \node[box] (s3) at (10,0) {\textbf{3. Step}\\Description};
  \draw[arr] (s1) -- (s2);
  \draw[arr] (s2) -- (s3);
\end{tikzpicture}
```

### Step 4: Preamble (Copy, Don't Create)

Copy lines 1-107 from the most recent lecture in the same topic folder.
Key elements that MUST be present:
- `\documentclass[8pt,aspectratio=169]{beamer}` + `\usetheme{Madrid}`
- TikZ libraries: `arrows.meta,positioning,shapes.callouts,shapes.geometric,decorations.pathreplacing`
- Custom commands: `\bottomnote{}`, `\compactlist`, `\highlight{}`
- ML color palette: mlblue, mlpurple, mlorange, mlgreen, mlred, mlgray, mllavender (4 shades)
- 3-column footer: "Methods and Algorithms | MSc Data Science | page/total"

### Step 5: Writing Rules

| Rule | Why |
|------|-----|
| Zero `$$` display math | The whole point is no formulas |
| Every title is a **question or action** | "How Many Components?" not "Scree Plot" |
| Max **3 bullets** per chart slide | Chart is the star, not the text |
| `\bottomnote{}` on **every** content slide | Course standard + depth without clutter |
| `\compactlist` for all bullet lists | Prevents Overfull vbox warnings |
| `\highlight{}` for key insight phrases | Orange bold draws eye to the payoff |
| XKCD bookends (opening + closing) | Engagement + framing |
| `\section{}` before each act | Navigation dots in footer |
| `\texttt{}` for code, not `lstlisting` | Simpler, matches existing style |
| "sklearn does it" instead of equations | Acknowledges math without displaying it |

**XKCD Opening pattern**:
```latex
\begin{frame}{Framing Question Here}
\begin{columns}[T]
\begin{column}{0.55\textwidth}
\centering
\includegraphics[height=0.55\textheight]{images/XXXX_name.png}
\end{column}
\begin{column}{0.42\textwidth}
\vspace{8mm}
Context sentence 1.\\[4mm]
Context sentence 2.\\[4mm]
\highlight{The framing question?}
\end{column}
\end{columns}
\bottomnote{XKCD \#XXXX by Randall Munroe (CC BY-NC 2.5)}
\end{frame}
```

**XKCD Closing pattern**:
```latex
\begin{frame}{Call to Action}
\centering
\includegraphics[height=0.55\textheight]{images/XXXX_name.png}
\bottomnote{XKCD \#XXXX by Randall Munroe (CC BY-NC 2.5). Next: [what to do]!}
\end{frame}
```

**Key slide templates**:

Two-column comparison:
```latex
\begin{frame}{Why Not [Naive Approach]?}
\begin{columns}[T]
\begin{column}{0.47\textwidth}
\begin{block}{\textcolor{mlred}{Bad Approach}}
\begin{compactlist}
  \item Problem 1
  \item Problem 2
\end{compactlist}
\end{block}
\end{column}
\begin{column}{0.47\textwidth}
\begin{block}{\textcolor{mlgreen}{Better Approach}}
\begin{compactlist}
  \item Solution 1
  \item Solution 2
\end{compactlist}
\end{block}
\end{column}
\end{columns}
\vspace{4mm}
\centering
\highlight{Key insight.}
\bottomnote{Detail.}
\end{frame}
```

Comparison table (5 rows max):
```latex
\begin{frame}{A vs B: Quick Comparison}
\centering
\begin{tabular}{lll}
\toprule
\textbf{Aspect} & \textbf{A} & \textbf{B} \\
\midrule
Row 1-5 \\
\bottomrule
\end{tabular}
\vspace{5mm}
\highlight{Complementary tools, not competitors.}
\bottomnote{Practical advice.}
\end{frame}
```

Code recipe (side-by-side):
```latex
\begin{frame}{Try It: N Lines of Python}
\begin{columns}[T]
\begin{column}{0.47\textwidth}
\begin{block}{Method A}
\ttfamily\scriptsize
from sklearn.X import Y\\
result = Y().fit\_transform(X)
\end{block}
\end{column}
\begin{column}{0.47\textwidth}
\begin{block}{Method B}
\ttfamily\scriptsize
from sklearn.X import Z\\
result = Z().fit\_transform(X)
\end{block}
\end{column}
\end{columns}
\vspace{5mm}
\centering
\highlight{That's it. Three lines each.}
\bottomnote{Preprocessing tip.}
\end{frame}
```

### Step 6: Verification

```bash
# From the topic folder:
pdflatex -interaction=nonstopmode FILE.tex

# Move aux files:
mkdir -p temp && mv *.aux *.log *.nav *.out *.snm *.toc temp/ 2>/dev/null

# ALL must pass:
grep -c "begin{frame" FILE.tex           # Expected count per arc
grep -c "chart.pdf" FILE.tex             # Expected chart count
grep -c "bottomnote" FILE.tex            # >= (slides - 1)
grep -c '\$\$' FILE.tex                  # 0
grep -c "begin{tikzpicture}" FILE.tex    # >= comic count
grep -c "Overfull" temp/FILE.log         # MUST be 0
```

**Expected counts by arc**:

| Arc | Frames | Charts | Bottomnotes | TikZ pictures |
|-----|--------|--------|-------------|---------------|
| Contrast | 25 | 6-8 | >= 24 | >= 7 |
| Single-topic | 16-17 | 5 | >= 15 | >= 5 |
| Evolution | 25 | 7 | >= 24 | >= 7 |
| Parallel | 25-26 | 8-10 | >= 24 | >= 8 |

**Overfull fixes**: Reduce chart width -> `\compactlist` -> `\vspace{-2mm}` -> reduce TikZ scale -> split slide

### Step 7: Deployment

```bash
# Copy PDF to docs:
cp FILE.pdf ../../docs/slides/pdf/

# Add to docs/index.html (in topic's cgrid block):
# <a class="ccard" href="slides/pdf/FILE.pdf" download>
#   <div class="ccard-icon">PDF</div>TITLE
#   <div class="ccard-label">DESCRIPTION</div>
# </a>

# Update manifest.json with new entry
```

## Anti-Patterns

- **Don't create new chart.py files** -- reuse existing charts
- **Don't "simplify" formulas** -- either show the formula or don't
- **Don't use >8 charts** in a 25-slide lecture -- gallery, not story
- **Don't skip opening/closing comics** -- they create emotional arc
- **Don't use TikZ for realistic objects** -- geometric shapes and stick figures ONLY
- **Don't exceed 25 lines per TikZ comic** -- forces simplicity
- **Don't put >3 bullets on a chart slide** -- chart is the star
- **Don't duplicate XKCD images without different framing text**
- **Don't create a new preamble** -- always copy from existing

## Visual Formula Diagrams (VF Pattern)

When a lecture needs to teach *what a formula does* without showing the formula itself, use
**Visual Formula Diagrams** — TikZ illustrations that convey the intuition behind each
mathematical concept using geometric shapes, arrows, and labels.

### When to Use

- The lecture is formula-free but the topic has important formulas students need to understand conceptually
- You want to show *what* a formula computes, not *how* it computes it
- The audience needs intuition (e.g., "similarity shrinks with distance") rather than notation

### VF Budget Rules

| Rule | Value |
|------|-------|
| Max TikZ lines per VF | 25 (same as comics) |
| Labels | `\scriptsize` or `\tiny` only |
| Scale | `0.7`–`0.8` |
| Shapes | Circles (points), arrows (relationships), rectangles (containers) |
| Text inside TikZ | Plain English, no Greek letters, no subscripts |

### Proven VF Templates

**VF-A: "Two Lenses" (side-by-side comparison of two similarity measures)**

Use when two methods compute the same concept differently (e.g., Gaussian vs Student-t).

```latex
\begin{tikzpicture}[scale=0.7]
  % Left panel label
  \node[font=\scriptsize\bfseries,mlpurple] at (-3.5,3.2) {Method A};
  % Center point
  \fill[mlpurple] (-3.5,1.5) circle (4pt);
  \node[font=\tiny,below] at (-3.5,1.3) {center};
  % Nearby point (strong connection)
  \fill[mlblue] (-2.3,2.0) circle (3pt);
  \draw[mlpurple,very thick] (-3.5,1.5) -- (-2.3,2.0);
  \node[font=\tiny] at (-2.3,2.3) {near};
  % Far point (very weak connection)
  \fill[mlgray] (-4.8,0.3) circle (3pt);
  \draw[mlgray,thin,dashed] (-3.5,1.5) -- (-4.8,0.3);
  \node[font=\tiny] at (-4.8,0.0) {far};
  % Key difference annotation
  \node[draw,rounded corners,fill=white,font=\tiny,text width=2.2cm,align=center]
    at (-3.5,-0.5) {Far points get\\almost zero weight};

  % Right panel label
  \node[font=\scriptsize\bfseries,mlorange] at (3.5,3.2) {Method B};
  % Same layout but different connection weights
  \fill[mlorange] (3.5,1.5) circle (4pt);
  \fill[mlblue] (4.7,2.0) circle (3pt);
  \draw[mlorange,very thick] (3.5,1.5) -- (4.7,2.0);
  \fill[mlgray] (2.2,0.3) circle (3pt);
  \draw[mlorange,thick] (3.5,1.5) -- (2.2,0.3); % thicker than Method A
  \node[draw,rounded corners,fill=white,font=\tiny,text width=2.2cm,align=center]
    at (3.5,-0.5) {Far points keep\\some weight};
\end{tikzpicture}
```

**VF-B: "Mismatch Arrow" (divergence/loss between two distributions)**

Use when a formula measures how different two things are (KL divergence, MSE, etc.).

```latex
\begin{tikzpicture}[scale=0.7]
  % Left: original arrangement
  \node[font=\scriptsize\bfseries,mlpurple] at (-3,3.2) {Original};
  \fill[mlblue] (-3.8,2) circle (3pt); \fill[mlblue] (-3.2,2.3) circle (3pt);
  \fill[mlorange] (-2.5,1.2) circle (3pt); \fill[mlorange] (-3.5,0.8) circle (3pt);
  % Right: current map
  \node[font=\scriptsize\bfseries,mlorange] at (3,3.2) {Map};
  \fill[mlblue] (2.5,1.5) circle (3pt); \fill[mlorange] (3.5,1.8) circle (3pt);
  \fill[mlblue] (2.8,0.8) circle (3pt); \fill[mlorange] (3.2,2.5) circle (3pt);
  % Mismatch arrow
  \draw[-{Stealth},very thick,mlred] (-0.5,1.5) -- (1.5,1.5);
  \node[font=\scriptsize,above,mlred] at (0.5,1.5) {Mismatch?};
  % Bottom annotation
  \node[draw,rounded corners,fill=white,font=\tiny,text width=5cm,align=center]
    at (0,-0.3) {Big mismatch = clusters wrong. Small mismatch = good map.};
\end{tikzpicture}
```

**VF-C: "Push/Pull Forces" (gradient-based optimization intuition)**

Use when a formula creates attractive and repulsive forces.

```latex
\begin{tikzpicture}[scale=0.7]
  % Central point
  \fill[mlpurple] (0,1.5) circle (5pt);
  \node[font=\tiny,above] at (0,1.8) {point};
  % Attract: similar points pulled in
  \fill[mlblue] (-2,2.5) circle (3pt);
  \draw[-{Stealth},thick,mlgreen] (-2,2.5) -- (-0.5,1.8);
  \fill[mlblue] (2,0.5) circle (3pt);
  \draw[-{Stealth},thick,mlgreen] (2,0.5) -- (0.5,1.2);
  \node[font=\tiny,mlgreen] at (-2.5,1.8) {pull};
  % Repel: different points pushed away
  \fill[mlorange] (1.5,2.8) circle (3pt);
  \draw[-{Stealth},thick,mlred] (0.3,1.8) -- (1.2,2.5);
  \fill[mlorange] (-1.5,0.2) circle (3pt);
  \draw[-{Stealth},thick,mlred] (-0.3,1.2) -- (-1.2,0.5);
  \node[font=\tiny,mlred] at (2.5,2.8) {push};
  % Annotation
  \node[draw,rounded corners,fill=white,font=\tiny,text width=4cm,align=center]
    at (0,-0.5) {Similar = pull together. Different = push apart.};
\end{tikzpicture>
```

**VF-D: "Dial/Slider" (hyperparameter intuition)**

Use when a parameter controls a tradeoff (perplexity, learning rate, k, etc.).

```latex
\begin{tikzpicture}[scale=0.7]
  % Slider bar
  \draw[thick,mlgray] (-4,0) -- (4,0);
  % Left extreme
  \fill[mlblue] (-4,0) circle (3pt);
  \node[font=\tiny,below] at (-4,-0.3) {Low};
  \node[font=\tiny,above,text width=2cm,align=center] at (-3.5,0.5) {Few\\neighbors};
  % Right extreme
  \fill[mlorange] (4,0) circle (3pt);
  \node[font=\tiny,below] at (4,-0.3) {High};
  \node[font=\tiny,above,text width=2cm,align=center] at (3.5,0.5) {Many\\neighbors};
  % Sweet spot
  \fill[mlgreen] (0.5,0) circle (5pt);
  \node[font=\scriptsize,above,mlgreen] at (0.5,0.5) {Sweet spot};
  % Arrow pointing to sweet spot
  \draw[-{Stealth},thick,mlgreen] (0.5,1.2) -- (0.5,0.5);
\end{tikzpicture}
```

### VF Placement in Slide Plan

Visual formula diagrams go in the **method explanation section** (typically Act 2), grouped
on consecutive slides. Use 1-2 VFs per slide. The typical pattern:

```
Slide N:   VF-A (two lenses) — how similarity is computed
Slide N+1: VF-B (mismatch) — how the algorithm measures error
Slide N+2: VF-C (forces) — how the algorithm improves
Slide N+3: VF-D (dial) — what the user controls
```

Each VF slide should have:
- A question-based title: "How Does [Method] Measure Similarity?"
- The TikZ VF diagram centered
- 2-3 bullet points explaining what the diagram shows in plain English
- A `\bottomnote{}` linking to the technical lecture: "The math lives in L0X\_deepdive."

### Reference Implementation

`L05_PCA_tSNE/L05b_tsne_simple.tex` — 5 visual formula diagrams (VF1-VF5) across slides 9-12,
teaching Gaussian similarity, Student-t similarity, KL divergence, gradient forces, and perplexity
without a single formula.

## Reference Implementations

| File | Arc | Slides | Charts | TikZ | Status |
|------|-----|--------|--------|------|--------|
| `L05_PCA_tSNE/L05_pca_tsne_simple.tex` | Contrast | 25 | 8 | 10 | Gold standard |
| `L06_Embeddings_RL/L06_embeddings_rl_simple.tex` | Parallel | 26 | 10 | 8 | Proven |
| `L06_Embeddings_RL/L06a_embeddings_simple.tex` | Single | 16 | 5 | 6 | Proven |
| `L06_Embeddings_RL/L06b_rl_simple.tex` | Single | 17 | 5 | 6 | Proven |
| `L05_PCA_tSNE/L05b_tsne_simple.tex` | Single+VF | 18 | 5 | 9 | Proven (VF pattern) |
| `L06_Embeddings_RL/L06c_embeddings_llm_simple.tex` | Evolution | 25 | 7 | 7 | Proven |
