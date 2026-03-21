# Plan: Ultra-Simple PCA + t-SNE Lecture with Comics & Visual Analogies

## Task
Create `L05_pca_tsne_simple.tex` — a beginner-friendly, visually-rich lecture covering PCA and t-SNE with TikZ comics, visual analogies, and a curated subset of existing charts. Target: ~25 slides, zero formulas on screen unless absolutely essential.

## Requirements
1. **Ultra simple**: No matrix notation, no eigenvalue equations. Concepts via pictures only. Do NOT port formula slides (variance, covariance matrix, eigenvalue equation, Lagrangian derivation) from L05_pca_simple.tex. This lecture achieves the same concepts through visuals only.
2. **Comics**: TikZ stick-figure comics at opening, closing, and key transition points (min 4 comics). All comics use simple stick figures and geometric shapes only. No realistic objects. Target max 25 lines of TikZ per comic. If C2 (shadow) is too complex, replace dinosaur with a simple 3D cube.
3. **Visual analogies**: Real-world metaphors (shadow projection, map distortion, neighborhood preservation).
4. **Chart subset**: 8 carefully chosen charts from existing 42+ pool.
5. **PCA + t-SNE**: Both topics covered with roughly equal slide count; chart count skews 4:2 toward PCA because PCA requires more visual setup. (Existing L05_pca_simple.tex is PCA-only.)
6. **Course standards**: Madrid theme, 8pt, 16:9, `\bottomnote{}` on every slide, XKCD bookends.
7. **Standalone file**: This is a standalone supplementary lecture. It does not replace L05_pca_simple.tex, L05_overview.tex, or L05_deepdive.tex.

## Acceptance Criteria
- [ ] AC1: .tex file compiles with 0 errors, 0 Overfull
- [ ] AC2: ~25 slides (22-28 range)
- [ ] AC3: At least 4 TikZ comics/cartoons (opening + closing + 2 internal)
- [ ] AC4: At least 3 visual analogy slides (shadow, map, neighborhood)
- [ ] AC5: Exactly 8 reused charts (no new chart.py files needed)
- [ ] AC6: Zero matrix notation / eigenvalue equations visible on slides
- [ ] AC7: Both PCA and t-SNE covered with roughly equal weight
- [ ] AC8: `\bottomnote{}` on every content slide
- [ ] AC9: XKCD image at opening and closing (bookend rule)

## Chart Selection (8 from existing pool)

| # | Chart Path | Purpose in Lecture |
|---|------------|-------------------|
| 1 | `08_high_dim_before_after` | "Before/After" — shows compression works |
| 2 | `02_principal_components` | PC arrows on scatter — "PCA finds these directions" |
| 3 | `01_scree_plot` | "How many components?" — the elbow |
| 4 | `06b_pca_cluster_projection` | PCA on clusters — "pretty good but..." |
| 5 | `05a_pca_swiss_roll` | PCA FAILS on curved data |
| 6 | `05b_tsne_swiss_roll` | t-SNE SUCCEEDS on curved data |
| 7 | `06c_tsne_cluster_projection` | t-SNE on clusters — "much better!" |
| 8 | `07_decision_flowchart` | When to use PCA vs t-SNE |

**Why these 8**: They tell a complete story (compress → directions → how many → limits → t-SNE saves the day → when to use what) without requiring any math knowledge.

## TikZ Comics (4 planned)

| # | Title | Description |
|---|-------|-------------|
| C1 | "Drowning in Dimensions" | Stick figure at desk buried under spreadsheet columns labeled "Feature 1...Feature 50". Speech bubble: "Help! I can't see the patterns!" |
| C2 | "Shadow on the Wall" (PCA Analogy) | 3D dinosaur toy casting shadow on wall. Shadow = 2D PCA projection. Caption: "PCA = best shadow" |
| C3 | "The Neighborhood Rule" (t-SNE Analogy) | Village on hillside → flat map. Houses stay near their neighbors. Caption: "t-SNE = keep neighbors close" |
| C4 | "Now I See!" | Same stick figure from C1, now with magnifying glass, clear 2D scatter plot on screen. Speech bubble: "PCA + t-SNE = my visualization toolkit!" |

## Visual Analogy Slides (3 planned)

| # | Analogy | Concept | Implementation |
|---|---------|---------|----------------|
| A1 | Shadow Projection | PCA = projecting 3D onto 2D | TikZ: cube with light source, shadow on wall, label "best angle" |
| A2 | Globe → Flat Map | Dimensionality reduction = flattening | TikZ: sphere with countries → Mercator rectangle, "some distortion is inevitable" |
| A3 | Moving Cities | t-SNE neighborhood | TikZ: people in village → people in new neighborhood, "your neighbors stay your neighbors" |

Note: A1-A3 overlap with C2-C3 comics above. The comics ARE the analogies — we use 4 comic slides total, 3 of which serve as analogies.

## Slide Plan (~25 slides)

### Front Matter (3 slides)
1. **Title page**
2. **XKCD Opening** — `images/2048_curve_fitting.png` with question framing
3. **Learning Objectives** — 3 bullet points: (1) Explain what PCA does without formulas, (2) Describe when t-SNE beats PCA, (3) Choose the right method for a given dataset

### Act 1: The Problem (3 slides)
4. **TikZ Comic C1: "Drowning in Dimensions"** — The problem visualized
5. **CHART: Before/After** (`08_high_dim_before_after`) — "Look! Compression works!"
6. **Why not just pick 2 features?** — Simple text slide with cherry-picking vs PCA comparison

### Act 2: PCA = Best Shadow (6 slides)
7. **TikZ Comic C2: "Shadow on the Wall"** — PCA = finding the best angle for the shadow
8. **CHART: Principal Components** (`02_principal_components`) — "These are the best directions"
9. **Three Steps of PCA** — Simple recipe: Center → Find directions → Project (TikZ flowchart, no formulas)
10. **CHART: Scree Plot** (`01_scree_plot`) — "How many components? Look for the elbow"
11. **CHART: PCA Clusters** (`06b_pca_cluster_projection`) — "PCA does a decent job..."
12. **But PCA Has a Limit** — Transition slide: "What if data curves?"

### Act 3: t-SNE = Keep Neighbors Close (6 slides)
13. **TikZ Comic C3: "The Neighborhood Rule"** — t-SNE analogy
14. **CHART: PCA Swiss Roll FAIL** (`05a_pca_swiss_roll`) — "PCA crushes the curve"
15. **CHART: t-SNE Swiss Roll WIN** (`05b_tsne_swiss_roll`) — "t-SNE unrolls it!"
16. **t-SNE in Plain English** — What it does in 3 bullets (no KL divergence)
17. **CHART: t-SNE Clusters** (`06c_tsne_cluster_projection`) — "Much better separation!"
18. **t-SNE Gotchas** — 3 warnings (not for distances, random seed matters, slow on big data)

### Act 4: When to Use What (4 slides)
19. **PCA vs t-SNE Side-by-Side** — Simple comparison table (speed, type, output, use case)
20. **CHART: Decision Flowchart** (`07_decision_flowchart`) — "Follow this tree"
21. **Finance Teaser** — 1 slide: "3 PCA factors explain 98% of bond market moves" (no formulas, just the fact)
22. **The 5-Line Python Recipe** — `sklearn.decomposition.PCA` and `sklearn.manifold.TSNE` code snippets

### Closing (3 slides)
23. **TikZ Comic C4: "Now I See!"** — Resolution of opening comic
24. **Key Takeaways** — 5 bullet point summary
25. **XKCD Closing** — `images/2400_statistics.png`

**Total: 25 slides, 8 charts, 4 TikZ comics, 0 formulas**

## Implementation Steps

| Step | Description | Files |
|------|-------------|-------|
| 1 | Create `L05_pca_tsne_simple.tex` with full preamble (copy from L05_pca_simple.tex) | `slides/L05_PCA_tSNE/L05_pca_tsne_simple.tex` |
| 2 | Write all 25 slides following the slide plan above | same file |
| 3 | Create 4 TikZ comics inline (no external files needed) | same file |
| 4 | Compile and verify 0 errors, 0 Overfull | `L05_pca_tsne_simple.pdf` |
| 5 | Update manifest.json with new entry | `manifest.json` |

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| TikZ comics overflow frames | Use `\scriptsize` for text, keep comics compact, test each frame |
| Swiss roll charts may be confusing without explanation | Add "What you're seeing" callout text on each chart slide |
| "Too simple" criticism | This is intentional — it's a gateway lecture, not the deepdive |
| Missing XKCD images | Both `2048_curve_fitting.png` and `2400_statistics.png` already exist in `images/` |

## Verification
1. `pdflatex -interaction=nonstopmode L05_pca_tsne_simple.tex` → 0 errors
2. `grep -c "Overfull" *.log` → 0
3. Count frames → 22-28 range
4. Visual review: all 8 charts render, all 4 comics visible

---
PLAN_READY: .omc/plans/l05-simple-lecture.md
