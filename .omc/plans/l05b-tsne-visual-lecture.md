# Plan: L05b_tsne_simple.tex -- t-SNE Visual Deep Dive

## Context

### Original Request
Create a standalone 18-slide t-SNE visual lecture (`L05b_tsne_simple.tex`) following the single-topic discovery arc pattern. The lecture explains what every t-SNE formula DOES using TikZ visual diagrams instead of displaying formulas. Five key formulas each get a dedicated TikZ intuition diagram.

### Relationship to Existing Files
| File | Role | Status |
|------|------|--------|
| `L05_pca_tsne_simple.tex` | Combined PCA+t-SNE visual guide (25 slides). Covers t-SNE in ~6 slides (13-18) SUPERFICIALLY. | DO NOT MODIFY |
| `L05_overview.tex` | Full overview with formulas | DO NOT MODIFY |
| `L05_deepdive.tex` | Full deepdive with all t-SNE math (slides 22-34) | DO NOT MODIFY |

L05b goes deeper than the simple guide: the visual-formula diagrams explain the INTUITION behind every key formula, making it a bridge between the simple visual guide and the deepdive.

### Research Findings
- L06b_rl_simple.tex is the reference single-topic discovery arc (17 slides, 5 charts, 3 TikZ comics). Pattern: Title + XKCD + LOs + Comic1 + table + charts + Comic2 + charts + gotchas + finance + code + Comic3+takeaways + XKCD.
- L05_pca_tsne_simple.tex preamble (lines 1-99) provides the exact template including `dfteal`, `dfred` colors, `\compactlist`, `\highlight{}`, `\bottomnote{}`.
- L05_deepdive.tex slides 22-29 contain the formal t-SNE math: p_{j|i} (slide 23), q_{ij} (slide 23), KL divergence + gradient (slide 25), crowding problem (slide 24), perplexity (slides 26-29).

---

## Work Objectives

### Core Objective
Create `slides/L05_PCA_tSNE/L05b_tsne_simple.tex` -- an 18-slide formula-free visual lecture on t-SNE with 5 charts, 3 TikZ comics, and 5 TikZ formula-visual diagrams.

### Deliverables
1. `L05b_tsne_simple.tex` -- the LaTeX file (18 slides)
2. `L05b_tsne_simple.pdf` -- compiled PDF
3. Updated `manifest.json` -- add `tsne_simple_slides` entry under L05
4. Updated `docs/index.html` -- add download card for L05b
5. PDF copied to `docs/slides/pdf/L05b_tsne_simple.pdf`

### Definition of Done
- 18 slides, 5 charts, 3 TikZ comics, 5 TikZ formula-visual diagrams
- `\bottomnote{}` on every content slide (slides 2-18 = 17 bottomnotes)
- Zero `$$` or `\[...\]` formula blocks
- Zero Overfull warnings
- Compiles cleanly with pdflatex

---

## Must Have / Must NOT Have

### Must Have
- Preamble copied from L05_pca_tsne_simple.tex lines 1-99 (with new title/subtitle block after)
- All 5 formula-visual TikZ diagrams (p_{j|i}, q_{ij}, KL divergence, gradient, perplexity)
- 3 TikZ comics at structural transition points (ACT 1, ACT 2, CLOSING)
- 5 charts from existing chart folders
- `\bottomnote{}` on every content slide
- `\compactlist` for all bullet lists
- `\highlight{}` for key phrases
- Finance application slide

### Must NOT Have
- Any displayed formulas (`$$`, `\[`, `\begin{equation}`, `\begin{align}`)
- Inline math beyond simple variable names (e.g., `$k$` is ok, `$\sum_{i}$` is not)
- Newly created subplots or multi-panel figures (existing charts like `top10_20_tsne_perplexity_grid` that are multi-panel are allowed since they are reused, not created)
- References to PCA (this is t-SNE only)
- Modification of any existing file except manifest.json and docs/index.html

---

## Chart Curation Table

| Slot | Chart Path | Why Chosen |
|------|-----------|------------|
| Chart 1 (slide 6) | `05b_tsne_swiss_roll/chart.pdf` | Swiss roll is the canonical "t-SNE wins" demo. Shows t-SNE succeeds where linear methods fail. |
| Chart 2 (slide 8) | `06c_tsne_cluster_projection/chart.pdf` | Shows t-SNE's primary use case: clean cluster separation from high-D data. |
| Chart 3 (slide 12) | `top10_20_tsne_perplexity_grid/chart.pdf` | 2x2 grid showing perplexity effect visually. Best single chart for "perplexity matters". |
| Chart 4 (slide 13) | `top10_13_tsne_iterations/chart.pdf` | Shows optimization convergence over iterations. Connects to gradient/forces intuition. |
| Chart 5 (slide 14) | `top10_16_tsne_distance_preservation/chart.pdf` | Quantifies what t-SNE preserves. Supports "local yes, global no" gotcha message. |

**Rejected alternatives and reasons:**
- `04a/04b/04c_tsne_perplexity_*`: Individual perplexity charts are redundant when `top10_20` shows all in one grid.
- `top10_17_pca_vs_tsne_runtime`: This is a PCA comparison chart; this lecture is t-SNE only.
- `05a_pca_swiss_roll`: PCA content; excluded from t-SNE-only lecture.

---

## TikZ Comic Descriptions

### Comic C1 (slide 4) -- "The Crowded Room"
**Position:** ACT 1 opener (why t-SNE exists)
**Scene:** Left panel: a room viewed from above with 20+ dots (people) in a complex arrangement (some clustered, some spread). A stick figure looks in from a doorway with "?!?" above head. Speech bubble: "Who is near whom?" Right panel: same dots projected onto a single line at the bottom -- all dots overlap. Caption below: "Squashing to fewer dimensions loses the neighborhood structure."
**Colors:** dots in mlblue/mlorange/mlgreen clusters, room walls in mlgray, stick figure in black, speech bubble white with rounded corners.
**Size:** scale=0.75, fits in ~15 TikZ lines.

### Comic C2 (slide 7) -- "The Spring System"
**Position:** ACT 2 opener (how t-SNE works)
**Scene:** 6 labeled points (A-F) connected by springs. Close neighbors (A-B, B-C) have thick short springs (mlgreen). Distant pairs (A-F) have thin stretched springs (mlred, dashed). A stick figure pulls point D with a speech bubble: "Neighbors pull close, strangers push apart!"
**Colors:** points in mlblue, close springs mlgreen, far springs mlred, stick figure black.
**Size:** scale=0.8, fits in ~18 TikZ lines.

### Comic C3 (slide 16) -- "The Cartographer"
**Position:** CLOSING (comic-only slide, takeaways on separate slide 17)
**Scene:** A stick figure at a desk with a magnifying glass looking at a 2D map. On the wall behind: a tangled high-D cloud (scribble). An arrow labeled "t-SNE" points from the wall to the desk map. The map shows clean clusters. Speech bubble: "The neighborhoods are preserved!"
**Colors:** wall cloud in mlgray, map clusters in mlblue/mlorange/mlgreen, arrow in mlpurple, magnifying glass in mlorange.
**Size:** scale=0.75, fits in ~16 TikZ lines.

---

## Visual Formula Specifications

Each diagram replaces a formula with a visual explanation. All use the same framing: a centered TikZ picture at scale=0.7-0.8, max 25 TikZ lines, with a 2-3 bullet `\compactlist` below.

### VF1: p_{j|i} -- Gaussian Similarity in High-D (slide 9, left column)
**What it shows:** A central point (mlblue, labeled "i") with a Gaussian bell curve drawn as a shaded circle fading from mlpurple (center) to white (edges) around it. Three nearby points at varying distances. Dashed lines from center to each point. Labels on the dashed lines: "high prob" (short line), "medium" (medium), "low prob" (long line, near edge of bubble).
**Caption/bullets:** "In high-D, each point sees its neighbors through a Gaussian lens. Close = high probability. Far = low."
**Colors:** center point mlblue, bubble fill mlpurple!20 fading, probability labels mlorange.
**TikZ approach:** `\shade[inner color=mlpurple!20, outer color=white]` for the Gaussian bubble. Points as filled circles. Dashed lines with annotations.

### VF2: q_{ij} -- Student-t Similarity in Low-D (slide 9, right column)
**What it shows:** Same layout as VF1 but the bubble is wider and has heavier tails (drawn as a flatter, wider shaded region using `inner color=mlblue!15`). The "low prob" point that was at the edge in VF1 is now comfortably OUTSIDE the bubble. Label: "heavy tails = more room to spread out".
**Caption/bullets:** "In 2D, t-SNE uses a wider lens (Student-t). Far points get pushed much farther apart."
**Colors:** center point mlblue, bubble fill mlblue!15, labels mlorange.
**TikZ approach:** Wider `\shade` ellipse. Same point positions but different probability labels showing the contrast.

### VF3: KL Divergence Objective (slide 10, full width)
**What it shows:** Two panels side by side. LEFT panel labeled "High-D Neighborhoods": 3 points (A, B, C) with connection lines of varying thickness (thick A-B = high p, thin A-C = low p). RIGHT panel labeled "2D Layout": same 3 points rearranged, with connection lines of different thickness (representing q). A double-headed arrow between panels labeled "Mismatch?" in mlorange. Below the arrow: "t-SNE minimizes the mismatch between these two pictures."
**Colors:** left panel connections mlpurple, right panel connections mlblue, mismatch arrow mlorange.
**TikZ approach:** Two groups of 3 points with 3 connection lines each = 6 `\fill` + 6 `\draw` + labels + arrow = ~18 TikZ lines. Well within 25-line budget. NO gauge/meter element (removed to stay under budget).

### VF4: Gradient -- Attract/Repel Forces (slide 11)
**What it shows:** A central point (mlblue) with 4 surrounding points. Two nearby points have GREEN arrows pointing INWARD toward center (attractive force, labeled "pull closer"). Two distant points have RED arrows pointing OUTWARD away from center (repulsive force, labeled "push apart"). Center label: "Each point feels forces from all others."
**Colors:** center mlblue, attractive arrows mlgreen, repulsive arrows mlred, distant points mlgray.
**TikZ approach:** `\draw[-{Stealth}]` arrows with color coding. Simple and under 15 lines.

VF3 and VF4 are on separate slides (10 and 11 respectively).

### VF5: Perplexity -- Neighborhood Size Control (slide 12, alongside perplexity grid chart)
**What it shows:** Three versions of the same point with concentric circles around it. LEFT: small circle (perplexity=5, label "5 neighbors"), only 2 dots inside. MIDDLE: medium circle (perplexity=30, label "30 neighbors"), 5 dots inside. RIGHT: large circle (perplexity=100, label "100 neighbors"), 8 dots inside. Caption: "Perplexity controls how many neighbors each point considers."
**Colors:** circles in mlpurple (dashed), center points mlblue, neighbor dots mlgray.
**TikZ approach:** Three `\draw[dashed]` circles at increasing radii with scattered fill dots. Under 15 lines.

---

## Slide-by-Slide Breakdown

### FRONT MATTER (Slides 1-3)

**Slide 1: Title Page**
- `\begin{frame}[plain] \titlepage \end{frame}`
- Title: "t-SNE: A Visual Deep Dive"
- Subtitle: "Understanding Neighbor Embedding Without Formulas"

**Slide 2: XKCD Opening**
- Image: `images/2048_curve_fitting.png` (0.55\textheight, left column)
- Right column text: "You have 50 features. You need 2 axes. But you also need to keep the neighborhoods intact. How?"
- `\bottomnote{XKCD \#2048 by Randall Munroe (CC BY-NC 2.5)}`

**Slide 3: Learning Objectives**
- Title: "What You Will Learn Today"
- 3 LOs as numbered list:
  1. Explain what t-SNE does and why it exists
  2. Describe how t-SNE preserves neighborhoods (visually)
  3. Recognize when t-SNE results are trustworthy vs misleading
- `\bottomnote{Everything is explained with pictures, analogies, and visual diagrams --- zero formulas.}`

### `\section{}` Structure

The following `\section{}` commands create navigation dots in the Beamer footer:
- Before slide 4: `\section{The Problem}`
- Before slide 6: `\section{How t-SNE Works}`
- Before slide 12: `\section{Going Deeper}`
- Before slide 14: `\section{Application}`
- Before slide 16: `\section{Closing}`

### ACT 1: THE PROBLEM (Slides 4-5)

**Slide 4: TikZ Comic C1 -- "The Crowded Room"**
- Title: "The Problem: Who Is Near Whom?"
- TikZ comic C1 (see description above)
- Text below: "Dimensionality reduction must preserve which points are neighbors."
- `\bottomnote{t-SNE was invented specifically to solve this: preserve local neighborhoods when flattening to 2D.}`

**Slide 5: Why t-SNE Exists + What It Does**
- Title: "What t-SNE Does (One Sentence)"
- Two-column layout:
  - Left: comparison table (3 rows): Linear methods = "preserve global distances" / t-SNE = "preserve local neighborhoods" / Result = "clusters become visible"
  - Right: small TikZ showing high-D tangle --> arrow --> 2D clusters
- `\highlight{t-SNE keeps nearby points nearby. That is the entire idea.}`
- `\bottomnote{van der Maaten \& Hinton, 2008. The ``t'' is for Student's t-distribution; ``SNE'' = Stochastic Neighbor Embedding.}`

### ACT 2: HOW IT WORKS (Slides 6-11)

**Slide 6: CHART 1 -- Swiss Roll Success**
- Title: "t-SNE Unrolls What Linear Methods Cannot"
- Chart: `05b_tsne_swiss_roll/chart.pdf` at 0.65\textwidth
- 2-bullet compactlist: "Data spirals in 3D like a rolled carpet" / "t-SNE preserves the neighborhood order along the spiral"
- `\bottomnote{Compare with PCA on the same data: PCA smashes the spiral flat, mixing distant points.}`

**Slide 7: TikZ Comic C2 -- "The Spring System"**
- Title: "How t-SNE Works: A Spring System"
- TikZ comic C2 (see description above)
- Text below: "t-SNE connects every pair of points with a spring. Neighbors get strong springs. Strangers get weak ones."
- `\bottomnote{The ``springs'' are probability-based: high probability = strong pull, low probability = weak push.}`

**Slide 8: CHART 2 -- Cluster Separation**
- Title: "The Payoff: Clean Cluster Separation"
- Chart: `06c_tsne_cluster_projection/chart.pdf` at 0.60\textwidth
- 3-bullet compactlist: "Each color is a different group in the original high-D data" / "t-SNE pulls clusters apart so you can see them" / "Warning: distances BETWEEN clusters are not meaningful"
- `\bottomnote{t-SNE excels at revealing IF clusters exist. It does NOT tell you how far apart they are.}`

**Slide 9: Visual Formulas VF1 + VF2 -- Two Lenses**
- Title: "Two Different Lenses for Measuring Similarity"
- Two-column layout:
  - Left column header: "In High-D: Gaussian Lens" + VF1 TikZ diagram
  - Right column header: "In 2D: Student-t Lens" + VF2 TikZ diagram
- 2-bullet compactlist below both columns: "High-D uses a narrow Gaussian bubble --- only close neighbors matter" / "2D uses a wider Student-t bubble --- far points get pushed much farther apart"
- `\bottomnote{The wider t-distribution lens in 2D solves the ``crowding problem'': it gives clusters room to breathe.}`

**Slide 10: Visual Formula VF3 -- KL Divergence**
- Title: "The Goal: Make Both Pictures Match"
- VF3 TikZ diagram (two panels + mismatch arrow), full width
- 2-bullet compactlist: "Left = neighborhoods in the original data. Right = layout in 2D." / "t-SNE moves points until the 2D layout matches the original neighborhoods as closely as possible."
- `\bottomnote{Technically this is KL divergence minimization, but visually it is just ``make these two pictures agree.''}`

**Slide 11: Visual Formula VF4 -- Attract/Repel Forces**
- Title: "The Engine: Attract Neighbors, Repel Strangers"
- VF4 TikZ diagram (central point with force arrows), centered
- 3-bullet compactlist: "Green arrows: neighbors that are too far apart get pulled closer" / "Red arrows: non-neighbors that are too close get pushed apart" / "Every point feels these forces from every other point, every iteration"
- `\bottomnote{This is gradient descent in disguise: the forces ARE the gradient. Hundreds of iterations until equilibrium.}`

### ACT 3: GOING DEEPER (Slides 12-13)

**Slide 12: VF5 + CHART 3 -- Perplexity**
- Title: "The One Knob You Must Tune: Perplexity"
- Two-column layout:
  - Left column: VF5 TikZ (three concentric-circle diagrams showing perplexity 5/30/100)
  - Right column: `top10_20_tsne_perplexity_grid/chart.pdf` at \textwidth (column width)
- 1-bullet below: "Perplexity controls how many neighbors each point considers. Always try multiple values."
- `\bottomnote{Default perplexity = 30 in sklearn. Try 5, 30, and 100 to see if your clusters are robust.}`

**Slide 13: CHART 4 + Gotchas**
- Title: "Watch It Converge --- and Three Gotchas"
- Top: `top10_13_tsne_iterations/chart.pdf` at 0.55\textwidth
- Below chart, 3-item numbered list with `\textcolor{mlred}{\textbf{!}}` prefix:
  1. "Distances between clusters mean nothing --- only within-cluster structure is real"
  2. "Different random seeds produce different layouts --- run it multiple times"
  3. "Slow on big data --- use PCA to 50 dims first, then t-SNE"
- `\bottomnote{If your clusters disappear when you change the random seed, they are probably not real.}`

### ACT 4: APPLICATION (Slides 14-15)

**Slide 14: CHART 5 + Finance Application**
- Title: "What t-SNE Preserves --- and Where It Shines"
- Top: `top10_16_tsne_distance_preservation/chart.pdf` at 0.55\textwidth
- Below, block titled "Finance Applications":
  - "Fraud detection: t-SNE reveals anomalous transaction clusters"
  - "Credit risk: visualize borrower segments in high-dimensional feature space"
  - "Market regimes: identify hidden market states from return data"
- `\bottomnote{t-SNE is for exploration and visualization. Never feed t-SNE coordinates into a classifier.}`

**Slide 15: Try It Yourself**
- Title: "Try It Yourself: 4 Lines of Python"
- Code block (ttfamily, scriptsize):
  ```
  from sklearn.manifold import TSNE
  tsne = TSNE(n_components=2, perplexity=30)
  X_2d = tsne.fit_transform(X)
  plt.scatter(X_2d[:, 0], X_2d[:, 1])
  ```
- `\highlight{That is it. Four lines. sklearn does the heavy lifting.}`
- `\bottomnote{Always scale your data first with StandardScaler. For large datasets, reduce to 50 dims with PCA before t-SNE.}`

### CLOSING (Slides 16-18)

**Slide 16: TikZ Comic C3 -- "The Cartographer"**
- Title: "The Cartographer's Map"
- TikZ comic C3 (see description above)
- Below comic: "t-SNE turns high-dimensional tangles into readable maps --- if you tune it right."
- `\bottomnote{t-SNE: your best tool for seeing if clusters exist in high-dimensional data.}`

**Slide 17: Key Takeaways**
- Title: "Three Things to Remember"
- 3-item numbered list with `\setlength{\itemsep}{6pt}`:
  1. "t-SNE preserves local neighborhoods when flattening high-D data to 2D"
  2. "It works like a spring system: neighbors attract, strangers repel"
  3. "Always tune perplexity and run multiple seeds before trusting the layout"
- `\bottomnote{For preprocessing and speed, use PCA first. For visualization and cluster discovery, use t-SNE.}`

**Slide 18: XKCD Closing**
- Title: "Go Find the Hidden Clusters"
- Image: `images/2400_statistics.png` at 0.55\textheight, centered
- `\bottomnote{XKCD \#2400 by Randall Munroe (CC BY-NC 2.5). Next: try the Jupyter notebook with real financial data!}`

---

## Task Flow and Detailed TODOs

### Task 1: Create L05b_tsne_simple.tex
**File:** `slides/L05_PCA_tSNE/L05b_tsne_simple.tex`
**Depends on:** Nothing
**Acceptance criteria:**
- Preamble copied from L05_pca_tsne_simple.tex lines 1-99 (colors, theme, footer, compactlist, highlight, bottomnote, mathbold)
- Title block changed to: `\title[L05b: t-SNE Visual]{t-SNE: A Visual Deep Dive}` / `\subtitle{Understanding Neighbor Embedding Without Formulas}`
- 18 frames total
- 5 `\includegraphics` referencing chart.pdf files (paths verified to exist)
- 3 TikZ comics (C1 on slide 4, C2 on slide 7, C3 on slide 16)
- 5 TikZ formula-visual diagrams (VF1+VF2 on slide 9, VF3 on slide 10, VF4 on slide 11, VF5 on slide 12)
- Each VF diagram is under 25 TikZ lines
- `\bottomnote{}` on slides 2 through 18 (17 bottomnotes)
- Zero `$$`, `\[`, `\begin{equation}`, `\begin{align}`
- Inline math limited to simple variable names only

### Task 2: Compile and Verify
**Depends on:** Task 1
**Commands:**
```bash
cd D:/Joerg/Research/slides/Methods_and_Algorithms/slides/L05_PCA_tSNE
pdflatex -interaction=nonstopmode L05b_tsne_simple.tex
pdflatex -interaction=nonstopmode L05b_tsne_simple.tex
```
**Acceptance criteria:**
- Exit code 0 on both passes
- `grep -c "Overfull" L05b_tsne_simple.log` returns 0
- `L05b_tsne_simple.pdf` exists and is non-empty
- Move aux files: `mkdir -p temp && mv L05b_tsne_simple.aux L05b_tsne_simple.log L05b_tsne_simple.nav L05b_tsne_simple.out L05b_tsne_simple.snm L05b_tsne_simple.toc temp/ 2>/dev/null`

### Task 3: Content Verification
**Depends on:** Task 2
**Checks:**
```bash
# Count slides
grep -c '\\begin{frame}' L05b_tsne_simple.tex
# Expected: 18

# Count charts
grep -c 'includegraphics.*chart.pdf' L05b_tsne_simple.tex
# Expected: 5

# Count bottomnotes
grep -c '\\bottomnote' L05b_tsne_simple.tex
# Expected: 17

# Count TikZ pictures
grep -c '\\begin{tikzpicture}' L05b_tsne_simple.tex
# Expected: 8-12 (3 comics + 5 VF diagrams + inline mini-TikZ possible)

# Zero formula blocks
grep -c '\$\$\|\\begin{equation}\|\\begin{align}\|\\\[' L05b_tsne_simple.tex
# Expected: 0

# Zero Overfull
grep -c 'Overfull' temp/L05b_tsne_simple.log 2>/dev/null || grep -c 'Overfull' L05b_tsne_simple.log
# Expected: 0
```

### Task 4: Update manifest.json
**File:** `manifest.json` (project root)
**Depends on:** Task 2
**Change:** Add entry after `pca_tsne_simple_slides` closing brace. Add a trailing comma to the existing closing `}` of `pca_tsne_simple_slides` before inserting:
```json
        },
        "tsne_simple_slides": {
          "file": "slides/L05_PCA_tSNE/L05b_tsne_simple.tex",
          "status": "complete"
        }
```
Note: The `,` on the first line is added to the EXISTING closing brace of `pca_tsne_simple_slides` to make valid JSON.
**Acceptance criteria:** `python infrastructure/course_cli.py validate --all` passes (or at least no new errors)

### Task 5: Deploy PDF to docs/
**Depends on:** Task 2
**Commands:**
```bash
cp D:/Joerg/Research/slides/Methods_and_Algorithms/slides/L05_PCA_tSNE/L05b_tsne_simple.pdf D:/Joerg/Research/slides/Methods_and_Algorithms/docs/slides/pdf/L05b_tsne_simple.pdf
```

### Task 6: Update docs/index.html
**File:** `docs/index.html`
**Depends on:** Task 5
**Change:** After the existing L05 "Visual Guide" card (line 304), add:
```html
<a class="ccard" href="slides/pdf/L05b_tsne_simple.pdf" download><div class="ccard-icon">PDF</div>t-SNE Visual Deep Dive<div class="ccard-label">18-slide formula-free t-SNE</div></a>
```
**Acceptance criteria:** Card appears in L05 section of index.html

---

## Commit Strategy

Single commit after all tasks complete:
```
Add L05b t-SNE visual deep dive lecture (18 slides, 5 charts, 5 formula-visual diagrams)
```

Files in commit:
- `slides/L05_PCA_tSNE/L05b_tsne_simple.tex` (new)
- `slides/L05_PCA_tSNE/L05b_tsne_simple.pdf` (new)
- `manifest.json` (modified)
- `docs/index.html` (modified)
- `docs/slides/pdf/L05b_tsne_simple.pdf` (new)

---

## Risk Mitigation

### TikZ Complexity
- **Risk:** Visual formula diagrams exceed 25 lines and cause Overfull warnings.
- **Mitigation:** Each VF diagram uses `scale=0.7` and simple primitives only (`\fill`, `\draw`, `\shade`, `\node`). No `calc` library. No complex path operations. If a VF exceeds 25 lines during implementation, simplify by removing decorative elements first, then reduce point count.

### Overfull Warnings
- **Risk:** Text-heavy slides (especially slides 9, 12, 13) overflow.
- **Mitigation:** Use `\scriptsize` for code blocks, `\compactlist` for all bullets, max 3 bullets per slide. Slide 9 (two-column VF1+VF2) uses `\small` text and `scale=0.65` if needed. Slide 12 (VF5+chart) uses compact 0.45/0.50 column split.

### Chart Path Correctness
- **Risk:** Chart paths are wrong and compilation shows missing file warnings.
- **Mitigation:** All 5 chart paths verified against `ls` output:
  - `05b_tsne_swiss_roll/chart.pdf` -- confirmed exists
  - `06c_tsne_cluster_projection/chart.pdf` -- confirmed exists
  - `top10_20_tsne_perplexity_grid/chart.pdf` -- confirmed exists
  - `top10_13_tsne_iterations/chart.pdf` -- confirmed exists
  - `top10_16_tsne_distance_preservation/chart.pdf` -- confirmed exists

---

## Success Criteria

| Criterion | Target | Verification |
|-----------|--------|-------------|
| Slide count | 18 | `grep -c '\\begin{frame}' L05b_tsne_simple.tex` |
| Chart count | 5 | `grep -c 'includegraphics.*chart.pdf' L05b_tsne_simple.tex` |
| TikZ comic count | 3 | Manual: slides 4, 7, 16 |
| TikZ formula-visual count | 5 | Manual: VF1+VF2 on slide 9, VF3 on slide 10, VF4 on slide 11, VF5 on slide 12 |
| Bottomnote count | 17 | `grep -c '\\bottomnote' L05b_tsne_simple.tex` (slides 2-18) |
| Formula blocks | 0 | `grep -cE '\$\$\|\\begin\{equation\}\|\\begin\{align\}\|\\\[' L05b_tsne_simple.tex` |
| Overfull warnings | 0 | `grep -c 'Overfull' L05b_tsne_simple.log` |
| PDF exists | yes | `test -f L05b_tsne_simple.pdf` |
| manifest.json updated | yes | `grep 'tsne_simple_slides' manifest.json` |
| docs card added | yes | `grep 'L05b_tsne_simple' docs/index.html` |

---

## Verification Commands (Copy-Paste Ready)

```bash
cd D:/Joerg/Research/slides/Methods_and_Algorithms/slides/L05_PCA_tSNE

# Compile (2 passes for references)
pdflatex -interaction=nonstopmode L05b_tsne_simple.tex
pdflatex -interaction=nonstopmode L05b_tsne_simple.tex

# Check compilation success
echo "--- Overfull warnings ---"
grep -c "Overfull" L05b_tsne_simple.log

# Content counts
echo "--- Slide count (expect 18) ---"
grep -c '\\begin{frame}' L05b_tsne_simple.tex
echo "--- Chart count (expect 5) ---"
grep -c 'includegraphics.*chart.pdf' L05b_tsne_simple.tex
echo "--- Bottomnote count (expect 17) ---"
grep -c '\\bottomnote' L05b_tsne_simple.tex
echo "--- Formula blocks (expect 0) ---"
grep -cE '\$\$|\\begin\{equation\}|\\begin\{align\}|\\\[' L05b_tsne_simple.tex

# Clean up aux files
mkdir -p temp
mv L05b_tsne_simple.aux L05b_tsne_simple.log L05b_tsne_simple.nav L05b_tsne_simple.out L05b_tsne_simple.snm L05b_tsne_simple.toc temp/ 2>/dev/null

# Deploy
cp L05b_tsne_simple.pdf ../../docs/slides/pdf/L05b_tsne_simple.pdf
```
