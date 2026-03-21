# L05 PCA Pedagogy Review

## Context

### Original Request
Deep pedagogical content review of L05 PCA & t-SNE material. Three guiding questions:
1. Do we start simple, with motivation, example, visuals?
2. Do we really explain every term?
3. What else is needed to improve pedagogy?

### Scope
- Files: `L05_overview.tex` (429 lines, 24 slides) and `L05_deepdive.tex` (1126 lines, 48 slides)
- No changes to existing chart.py files
- New charts allowed (new chart.py + chart.pdf)
- Three-zone architecture in overview must be preserved
- 0 Overfull warnings required

### Existing Unused Assets
Two pre-built charts exist but are not referenced in either .tex file:
- `08_high_dim_before_after/chart.pdf` -- before/after PCA visualization
- `09_yield_curve_factors/chart.pdf` -- yield curve factor loadings

---

## Detailed Pedagogical Analysis

### FINDING 1: Overview Slides 9-10 -- Formula Dump Without Preparation

**Problem:** Overview slide 9 (line 207) jumps from the plain-English Zone 1 directly into covariance matrix, eigendecomposition, and EVR formulas with zero transition. Slide 10 then dumps t-SNE formulas. This is a back-to-back formula wall with no visual, no example, and no breather.

**Evidence:**
- Slide 8 (Business Problem) ends with words only
- Slide 9 opens with `$X_c = X - \bar{X}$`, covariance matrix, eigendecomposition equation, and EVR -- three distinct formulas on one slide
- Slide 10 immediately adds Gaussian kernel, Student-t kernel, and KL divergence
- The Scree Plot chart (slide 11) comes AFTER these formulas, when it should come BEFORE or alongside to motivate them

**Impact:** Students see 6 formulas across 2 consecutive slides before ANY visual or concrete example. Cognitive overload at the exact moment concepts are introduced.

### FINDING 2: Deepdive Slides 5-8 -- Four Consecutive Formula-Heavy Slides

**Problem:** Deepdive "PCA Foundations" opens with four consecutive formula-dense slides:
- Slide 5 (line 148): Mean-centering formula, PCA properties
- Slide 6 (line 170): Covariance matrix, eigendecomposition, projection formula
- Slide 7 (line 193): Lagrangian optimization, first-order condition
- Slide 8 (line 217): SVD decomposition, Gram matrix, eigenvalue relationship

No visual or worked example appears until slide 10 (Principal Components chart). That is 5 slides of continuous math.

**Impact:** Students who are shaky on linear algebra will disengage by slide 7. The Principal Components chart (slide 10) should appear much earlier to anchor the abstract math.

### FINDING 3: No "Gentle Lead-In" for PCA in Deepdive

**Problem:** The deepdive jumps straight from Learning Objectives (slide 4) to "Variance Maximization Objective" (slide 5) with formulas. There is no bridging slide that says: "Here is a simple 2D dataset. Watch what happens when we find the direction of greatest spread."

**What's missing:** A concrete, visual, numeric mini-example BEFORE the abstract formulation. Something like: "Here are 5 data points in 2D. The variance along this direction is X. Along this other direction, it's Y. PCA picks the direction with the highest variance."

### FINDING 4: Key Terms Not Explicitly Defined

Audit of critical terms:

| Term | Overview | Deepdive | Status |
|------|----------|----------|--------|
| Eigenvalue | Not defined | Used but not defined (slide 6, line 182: "$\lambda_k$ = eigenvalue (variance along that direction)") | PARTIAL -- labeled but not explained what an eigenvalue IS |
| Eigenvector | Not defined | Same pattern: "$\mathbf{v}_k$ = eigenvector (principal direction)" | PARTIAL -- labeled but no definition |
| Covariance matrix | Formula given (line 208-211) | Formula given (line 172-173) | FORMULA ONLY -- no intuition ("measures how features move together") |
| Mean-centering | Stated as formula (line 208) | Formula + "Required First Step" (line 152-155) | WHY is explained in deepdive bottomnote (line 166) but not in overview |
| Orthogonal | Not mentioned in overview | Used without definition (slide 5, line 149: "Find orthogonal directions") | MISSING -- never defined for students who forgot linear algebra |
| Variance | Assumed known | Assumed known | OK for MSc level, but a one-line reminder would help |
| KL divergence | Named but not explained (line 239) | Slide 20 gives formula + asymmetry explanation | OVERVIEW GAP -- overview just states "minimize KL(P||Q)" without saying what KL divergence means |
| Perplexity | Not in overview | Slide 24 gives formula + intuition ("effective number of neighbors") | OK in deepdive, MISSING in overview |
| Student's t-distribution | Named in overview (line 234) | Named in deepdive (line 435) | NEVER EXPLAINED -- why "Student's"? What shape? Why heavy tails help? |

### FINDING 5: Visuals Come AFTER Formulas Instead of BEFORE

| Concept | Formula Appears | Visual Appears | Gap |
|---------|----------------|----------------|-----|
| PCA (overview) | Slide 9 | Slide 11 (Scree Plot) | 2 slides late |
| PCA (deepdive) | Slide 5 | Slide 10 (Principal Components) | 5 slides late |
| Eigendecomposition (deepdive) | Slide 6 | Slide 10 | 4 slides late |
| Reconstruction (deepdive) | Slide 11 (formula) | Slide 12 (chart) | OK -- consecutive |
| t-SNE perplexity (deepdive) | Slide 24 (formula) | Slides 21-23 (charts) | REVERSED -- charts come first here, which is actually good |

The perplexity section accidentally demonstrates the correct pedagogy: show the charts first (slides 21-23), then explain the math (slide 24). The PCA sections do it backwards.

### FINDING 6: No Worked Numeric PCA Example in Overview

**Problem:** The overview has no "compute PCA by hand" example. Slide 9 (line 223) has a one-line example: "If the first eigenvalue explains 70% and the second 20%, then 2 components capture 90%." This is just arithmetic on percentages, not a PCA walkthrough.

The deepdive has a yield curve worked example (slide 14) with a loadings table, which is good. But the overview has nothing comparable.

### FINDING 7: Missing "What PCA is NOT" / Common Misconceptions

The deepdive has a "PCA Limitations" slide (slide 16, line 375), which covers when PCA fails. But there is no explicit "Common Misconceptions" content:
- Misconception: "PCA finds clusters" -- No, it finds directions of variance
- Misconception: "More components is always better" -- No, overfitting and noise
- Misconception: "PCA requires Gaussian data" -- partially addressed (line 165, 392) but scattered
- Misconception: "PCA results depend on scale" -- scale sensitivity is never mentioned in either file

### FINDING 8: Missing PCA Algorithm/Pseudocode

The deepdive has no pseudocode or step-by-step algorithm for PCA. The t-SNE section effectively has one (the gradient descent description), but PCA gets only math, never a numbered "Algorithm 1: PCA" box. For MSc students implementing PCA in their assignments, this is a gap.

### FINDING 9: Unused Charts That Should Be Integrated

Two pre-built charts sit unused:
- `08_high_dim_before_after/chart.pdf` -- This is exactly the "before/after PCA" visual that Finding 3 identifies as missing
- `09_yield_curve_factors/chart.pdf` -- A visual complement to the yield curve loadings table

### FINDING 10: Overview Slide 5 Analogies Are Good but Orphaned

The camera/wedding analogies (slide 5, line 143-153) are pedagogically sound. But they never connect forward to the formulas. Slide 9 could reference back: "Remember the 'best camera angle'? Mathematically, that's the eigenvector of the covariance matrix."

---

## Work Objectives

### Core Objective
Restructure L05 PCA content to follow "motivate -> visualize -> formalize" pedagogy in both overview and deepdive, explicitly define all key terms, and add concrete numeric examples before abstract math.

### Deliverables
1. Restructured overview with visual-first formula introduction
2. Restructured deepdive with gentle lead-in and term definitions
3. Integration of unused charts (08, 09)
4. Concrete mini-example slides
5. PCA algorithm pseudocode slide in deepdive

### Definition of Done
- [ ] Every formula has a preceding motivation ("why are we doing this?")
- [ ] Every key term from the audit table is explicitly defined
- [ ] At least one concrete numeric PCA example appears before abstract formulas
- [ ] Visual-first ordering: charts/diagrams appear before or alongside their formulas
- [ ] Both .tex files compile with 0 errors and 0 Overfull warnings
- [ ] Three-zone architecture in overview is preserved
- [ ] Overview slide count: 26 (currently 24 + 2 new = 26, within +/- 3)
- [ ] Deepdive slide count: 52 main+appendix (currently 48 + 4 new = 52). Exceeds +3, so merge existing slides 33-34 (PCA in sklearn + t-SNE/UMAP in Practice) into a single "Implementation: PCA, t-SNE, UMAP" slide to bring total to 51 (within +3)

---

## Must Have / Must NOT Have

### Must Have
- "Motivate -> Visualize -> Formalize" ordering for every concept
- Explicit definitions of: eigenvalue, eigenvector, covariance matrix, orthogonal, KL divergence, perplexity
- At least one concrete numeric mini-example for PCA (2D, 3-5 data points)
- Integration of chart 08 (high_dim_before_after) and chart 09 (yield_curve_factors)
- Connection between analogies (slide 5) and formulas (slide 9)
- PCA algorithm pseudocode in deepdive

### Must NOT Have
- Changes to any existing chart.py files
- Changes to files outside L05
- New sections that break the three-zone architecture
- Removal of any existing proofs (move to appendix if needed, don't delete)
- Bloom's level regression (keep at level 4-5)

---

## Task Flow and Dependencies

```
Task 1 (Overview restructure) ──┐
                                 ├── Task 5 (Compile & verify both)
Task 2 (Deepdive restructure) ──┤
                                 │
Task 3 (Term definitions) ───────┘  (can be done within Tasks 1 & 2)

Task 4 (New chart: PCA mini-example) ── independent, but Task 1 & 2
                                         reference its output path
```

Tasks 1 and 2 are the main bodies of work. Task 3 is woven into both. Task 4 is optional (a new chart.py for the numeric mini-example -- could also be done as a TikZ diagram instead). Task 5 is the verification gate.

---

## Detailed TODOs

### Task 1: Overview Restructure (L05_overview.tex)

**TODO 1.1: Add a "PCA in One Picture" slide before the formulas**
- Location: Insert new slide between current slide 8 (line 204) and slide 9 (line 206)
- Content: Include `08_high_dim_before_after/chart.pdf` showing a concrete before/after PCA visualization
- Title: "PCA in One Picture: Before and After"
- Bullets: 2-3 lines interpreting what the chart shows (100 dimensions -> 2 dimensions, structure preserved)
- Purpose: Visual anchor BEFORE any formula appears
- Acceptance: Chart displays, slide compiles, no Overfull

**TODO 1.2: Split slide 9 (Key Equations PCA) into motivation + formula**
- Location: Current slide 9 (lines 207-225)
- Change: Add a 2-line motivation at the top before the covariance formula: "To find the 'best camera angle' from slide 5, we need to measure how features move together (covariance) and find the direction of greatest spread (eigenvectors)."
- Also: Add one-line plain-English definition for each formula component:
  - Covariance matrix: "Measures how each pair of features varies together"
  - Eigendecomposition: "Finds the directions (eigenvectors) and magnitudes (eigenvalues) of greatest spread"
  - EVR: "What fraction of total information each direction captures"
- Acceptance: Slide compiles, each formula has a plain-English label, no Overfull

**TODO 1.3: Add yield curve factors chart to slide 12**
- Location: Current slide 12 (lines 253-264) -- Yield Curve PCA
- Change: This slide is text-only. Add `09_yield_curve_factors/chart.pdf` as a visual. Use a two-column layout: chart on left (0.55\textwidth), interpretation bullets on right.
- Acceptance: Chart displays alongside text, no Overfull

**TODO 1.4: Add KL divergence plain-English explanation to slide 10**
- Location: Current slide 10 (lines 228-241)
- Change: Before the KL divergence line, add: "KL divergence measures how different two probability distributions are -- here, how well the 2D map preserves the original neighborhood relationships."
- Acceptance: Definition present, no Overfull

**TODO 1.5: Connect analogies to formulas**
- Location: Current slide 9 (after restructure from TODO 1.2)
- Change: Add a callback line: "The 'best camera angle' from earlier IS the first eigenvector -- the direction capturing the most variance."
- Acceptance: Line present, reads naturally

**TODO 1.6: Keep Scree Plot in current position (no move needed)**
- Rationale: After TODO 1.1 inserts "PCA in One Picture" (chart 08) before the formula slides, students already see a PCA visual before any formula. The Scree Plot then serves as a second visual after the formulas, reinforcing the component selection concept. No reordering needed.
- Acceptance: At least one PCA chart appears before the eigendecomposition formula (satisfied by TODO 1.1)

**TODO 1.7: Add perplexity and Student's t intuition to overview slide 10**
- Location: Current slide 10 (lines 228-241), the t-SNE Key Equations slide
- Change: Before the formula for $q_{ij}$, add: "The Student's t-distribution (with 1 degree of freedom = Cauchy distribution) has heavier tails than the Gaussian, which prevents points from crowding together in 2D."
- Also add after the KL line: "Perplexity (typically 30) controls how many neighbors each point considers -- like adjusting the zoom level."
- Acceptance: Both perplexity and Student's t have 1-line intuitions in the overview

### Task 2: Deepdive Restructure (L05_deepdive.tex)

**TODO 2.1: Add "PCA Intuition" bridge slide before the math**
- Location: Insert between slide 4 (Learning Objectives, line 141) and slide 5 (Variance Maximization, line 148)
- Content: A new slide titled "PCA Intuition: Finding the Best View"
- Use `08_high_dim_before_after/chart.pdf` (currently unused). This avoids showing chart 02 twice and integrates an unused asset.
- Bullets:
  - "Imagine 2D data scattered in an ellipse"
  - "PC1 = the long axis of the ellipse (most spread)"
  - "PC2 = the short axis (remaining spread, perpendicular)"
  - "PCA generalizes this to any number of dimensions"
- Acceptance: Bridge slide present, chart 08 displayed, no formulas on this slide

**TODO 2.2: Add "Key Terms" definition block to slide 5 or as a new slide**
- Location: Either expand slide 5 (line 148) or insert a new slide after the bridge slide
- Content: Explicit definitions box:
  - **Variance**: How spread out data is along one direction; $\text{Var}(X) = \frac{1}{n-1}\sum(x_i - \bar{x})^2$
  - **Covariance matrix**: $p \times p$ matrix where entry $(i,j)$ measures how features $i$ and $j$ move together; diagonal = variances, off-diagonal = covariances
  - **Eigenvector**: A direction that a matrix only stretches (not rotates); $A\mathbf{v} = \lambda\mathbf{v}$
  - **Eigenvalue**: The stretch factor along that direction; larger = more variance
  - **Orthogonal**: Perpendicular; zero dot product; independent directions
  - **Mean-centering**: Subtracting the mean so data is centered at origin; required so PCA finds variance, not distance from origin
- Acceptance: All 6 terms have explicit plain-English + formula definitions

**TODO 2.2b: Overfull mitigation for TODO 2.2**
- If the 6-definition slide causes Overfull, split into two slides: "Key Terms: Linear Algebra" (variance, covariance, eigenvector, eigenvalue, orthogonal) and "Key Terms: Preprocessing" (mean-centering). This adds 1 more slide to the budget — acceptable since we merge slides 33-34 to compensate.
- Acceptance: Zero Overfull warnings on the definitions slide(s)

**TODO 2.3: Add concrete numeric mini-example**
- Location: Insert as a new slide after the definitions, before the formal variance maximization slide
- Title: "PCA by Hand: A 2D Mini-Example"
- Content: Walk through 4-5 data points in 2D:
  1. Show the data points: (1,2), (3,4), (5,6), (2,3), (4,5)
  2. Compute mean: (3, 4)
  3. Center: (-2,-2), (0,0), (2,2), (-1,-1), (1,1)
  4. Note: all centered points lie nearly on the line y=x
  5. Covariance matrix: $C = \begin{pmatrix} 2.5 & 2.5 \\ 2.5 & 2.5 \end{pmatrix}$
  6. Eigenvalues: $\lambda_1 = 5, \lambda_2 = 0$
  7. PC1 direction: $(1/\sqrt{2}, 1/\sqrt{2})$ -- the diagonal
  8. Conclusion: 100% of variance in 1 dimension (perfect linear relationship)
- Note: This is a deliberately simple example where PCA is obvious, building intuition
- Acceptance: Complete numeric walkthrough, all arithmetic correct

**TODO 2.4: Add "Why Eigenvectors?" motivation to slide 7**
- Location: Slide 7 (line 193), the proof slide
- Change: Add 2-line motivation at the very top: "We claimed PC1 is the eigenvector with the largest eigenvalue. But WHY? Could some other direction be better? The proof below shows: no. Eigenvectors are provably optimal."
- Acceptance: Motivation text present before the Lagrangian

**TODO 2.5: Add PCA Algorithm pseudocode slide**
- Location: Insert after slide 9 (Variance Explained, line 251) and before slide 10 (Principal Components chart)
- Content: Algorithm box using `algorithm`/`algorithmic` environment:
  ```
  Algorithm: PCA
  Input: Data matrix X (n x p), number of components k
  1. Center: X_c = X - mean(X)
  2. (Optional) Standardize if features have different scales
  3. Compute SVD: X_c = U S V^T
  4. Eigenvalues: lambda_k = s_k^2 / (n-1)
  5. Select top k columns of V as projection matrix W_k
  6. Project: Z = X_c * W_k
  Output: Z (n x k), eigenvalues, projection matrix
  ```
- Acceptance: Pseudocode present, uses algorithmic environment, compiles cleanly

**TODO 2.6: Add Student's t-distribution explanation**
- Location: Slide 19 (Crowding Problem, line 445) or slide 18 (Math Formulation, line 424)
- Change: Add 2-3 lines explaining the Student's t-distribution:
  - "Named after William Sealy Gosset who published under the pseudonym 'Student' in 1908"
  - "With 1 degree of freedom, it's also called the Cauchy distribution"
  - "Key property: heavier tails than Gaussian -- probability of extreme values decays as $1/(1+x^2)$ instead of $e^{-x^2}$"
- Acceptance: Student's t-distribution explained, heavy-tail property made explicit

**TODO 2.7: Move Principal Components chart earlier**
- Location: Currently slide 10 (line 254). Since TODO 2.1 uses chart 08 (not chart 02), chart 02 is free to move.
- Change: Move the Principal Components chart (slide 10) to immediately after the eigendecomposition slide (current slide 6). This provides visual anchoring right after the math.
- The moved chart becomes slide 7 (after new numbering from TODO 2.1-2.3 insertions); subsequent slides renumber.
- Acceptance: Principal Components chart appears within 1 slide of the eigendecomposition formula

**TODO 2.8: Add "Common Misconceptions" content**
- Location: Expand slide 16 (PCA Limitations, line 375) with a misconceptions subsection, or add a new slide before it
- Content:
  - "PCA finds clusters" -- No, PCA finds directions of maximum variance. Clusters may not align with high-variance directions. Use LDA for supervised separation.
  - "All features must be on the same scale" -- True for correlation-based PCA (StandardScaler first), but PCA on raw covariance is valid when features share units.
  - "Discarded components are 'noise'" -- Low-variance components may contain important signals for specific tasks. Always validate downstream.
- Acceptance: At least 3 misconceptions addressed

**TODO 2.9: Merge slides 33-34 into one "Implementation" slide**
- Location: Slides 33 (PCA in sklearn, line 759) and 34 (t-SNE/UMAP in Practice, line 782)
- Change: Combine into a single slide titled "Implementation: PCA, t-SNE, and UMAP" with the most essential API snippets from both. Move detailed API notes (sparse data, StandardScaler) to a bottomnote.
- Purpose: Reclaims 1 slide to offset the 4 new slides added, keeping deepdive within +3 tolerance.
- Acceptance: Single implementation slide compiles without Overfull

### Task 3: Term Definitions (woven into Tasks 1 and 2)

This is not a separate implementation task. The term definitions are delivered via:
- TODO 1.2 (overview: covariance, eigendecomposition, EVR plain-English labels)
- TODO 1.4 (overview: KL divergence explanation)
- TODO 2.2 (deepdive: full definitions block)
- TODO 2.6 (deepdive: Student's t-distribution)

Acceptance: Every term in the audit table (Finding 4) has an explicit definition in at least one file.

### Task 4: New Chart -- PCA Mini-Example (OPTIONAL)

**TODO 4.1: Create new chart `10_pca_mini_example/chart.py`**
- Purpose: Visual companion for TODO 2.3's numeric walkthrough
- Content: Plot the 5 data points in 2D, show the mean, draw PC1 and PC2 arrows, show the projected points on PC1
- Style: Follow standard chart template (figsize 10x6, ML color palette, font sizes)
- This is OPTIONAL because the mini-example slide (TODO 2.3) works with just numbers. A TikZ inline diagram could also work.
- Acceptance: chart.py runs without error, produces chart.pdf, follows template

**TODO 4.2: Update manifest.json if new chart created**
- If TODO 4.1 is implemented, add entry to L05 charts array:
  `{"id": "10_pca_mini_example", "file": "slides/L05_PCA_tSNE/10_pca_mini_example/chart.py", "status": "complete"}`
- Acceptance: manifest.json valid JSON, new chart entry present

### Task 5: Compile and Verify

**TODO 5.1: Compile L05_overview.tex**
- Command: `pdflatex -interaction=nonstopmode L05_overview.tex`
- Acceptance: 0 errors, 0 Overfull warnings (grep for "Overfull")

**TODO 5.2: Compile L05_deepdive.tex**
- Command: `pdflatex -interaction=nonstopmode L05_deepdive.tex`
- Acceptance: 0 errors, 0 Overfull warnings

**TODO 5.3: Slide count check**
- Overview target: 26 slides (currently 24 + 2 new = 26, within +/- 3)
- Deepdive target: 51 slides (currently 48 + 4 new - 1 merged = 51, within +/- 3)
- Acceptance: Overview = 26, Deepdive = 51 (or 52 if TODO 2.2b splits definitions into 2)

**TODO 5.4: Content consistency check**
- Verify: No duplicate definitions that contradict each other between overview and deepdive
- Verify: Yield curve numbers are consistent (85%/10%/3% = 98%) in both files
- Verify: All chart paths reference files that exist

---

## Commit Strategy

### Commit 1: Overview restructure
- TODOs 1.1, 1.2, 1.3, 1.4, 1.5, 1.6
- Message: "L05 overview: visual-first PCA intro, term definitions, integrate unused charts"

### Commit 2: Deepdive restructure
- TODOs 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8
- Message: "L05 deepdive: add PCA intuition bridge, term definitions, mini-example, algorithm pseudocode"

### Commit 3: Optional new chart + verification
- TODOs 4.1, 5.1, 5.2, 5.3, 5.4
- Message: "L05: add PCA mini-example chart, verify compilation clean"

---

## Success Criteria

1. **Simple Start**: PCA is introduced with a visual (chart 08 or 02) BEFORE any formula in both files
2. **Motivation First**: Every formula has a preceding "why" statement
3. **Terms Defined**: All 9 terms from the audit have explicit definitions
4. **Numeric Example**: A concrete "PCA by hand" walkthrough exists before abstract math
5. **Visual-Formula Ordering**: No formula appears more than 1 slide before its visual
6. **Compilation**: Both .tex files compile with 0 errors, 0 Overfull
7. **Slide Counts**: Overview = 26, Deepdive = 51 (within +/- 3 of current)
8. **Zone Architecture**: Overview three-zone structure preserved
