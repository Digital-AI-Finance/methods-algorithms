---
id: formula-free-visual-lecture
name: "Formula-Free Visual Lecture from Existing Charts"
description: >
  Pattern for creating ultra-simple, beginner-friendly Beamer lectures that teach
  complex technical concepts with zero formulas. Uses curated subsets of existing
  charts, TikZ stick-figure comics at structural points, real-world visual analogies,
  and a dramatic narrative arc (confusion -> method A -> limits -> method B -> clarity).
  Proven on L05_pca_tsne_simple.tex (25 slides, 10 TikZ pictures, 8 reused charts, 0 formulas, 0 Overfull).
source: Extracted from L05_pca_tsne_simple.tex creation (Mar 2026)
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
quality:
  googleable: false
  codebase_specific: true
  actionable: true
  hard_won: true
---

# Formula-Free Visual Lecture from Existing Charts

## The Insight

Complex technical concepts (PCA, t-SNE, neural networks, etc.) can be taught effectively
in 25 slides with ZERO formulas by combining three elements:

1. **Curated chart subset** from existing pool (don't create new charts)
2. **TikZ stick-figure comics** at 4 structural points (opening, 2 analogies, closing)
3. **Dramatic narrative arc**: confusion -> solution A -> limits -> solution B -> clarity

The key constraint that makes it work: **max 25 lines of TikZ per comic, stick figures only**.
This forces simplicity and prevents TikZ overflow disasters.

## Why This Matters

Full technical lectures (L05_overview, L05_deepdive) contain eigenvalue equations, Lagrangian
derivations, and matrix notation. Some audiences (executives, first-week students, cross-discipline
collaborators) need the intuition without the math. Creating a formula-free version from scratch
is slow; creating one by curating existing charts and adding comics is fast and effective.

Without this pattern, you either:
- Water down the full lecture (half-measures, still too complex)
- Create a slide deck that's "simple" but boring (just text bullets)
- Spend hours making new charts when existing ones already tell the story

## Recognition Pattern

Use this skill when:
- User asks for "simple", "ultra simple", "beginner-friendly", "no formulas", "visual" lecture
- An existing lecture has 15+ charts available to curate from
- The audience doesn't need to compute anything, just understand concepts
- You need a complement to an existing technical lecture, not a replacement

## The Approach

### Step 1: Chart Curation (Select 6-10 from existing pool)

Pick charts that tell a **story arc**, not charts that show the most math:

| Story Beat | Chart Type | Example |
|------------|-----------|---------|
| "Look, it works!" | Before/After | high_dim_before_after |
| "Here's how" | Core visualization | principal_components |
| "How much is enough?" | Diagnostic | scree_plot |
| "But it has limits" | Failure case | pca_swiss_roll |
| "Something better" | Success case | tsne_swiss_roll |
| "When to use what" | Decision aid | decision_flowchart |

**Selection heuristic**: If you need to explain what the chart shows for >2 sentences, it's too complex for this lecture. Skip it.

### Step 2: TikZ Comics at 4 Structural Points

| Position | Comic | Purpose |
|----------|-------|---------|
| Slide 4 (after LOs) | **Opening comic**: stick figure with the PROBLEM | Hook + empathy |
| Slide 7 (method intro) | **Analogy comic**: real-world metaphor for the method | Intuition building |
| Slide 13 (method B intro) | **Second analogy**: different metaphor for method B | Contrast |
| Slide 23 (before closing) | **Resolution comic**: same character, problem solved | Narrative closure |

**TikZ Budget Rules**:
- Max 25 lines of TikZ per comic
- Stick figures ONLY: circle head, line body, line limbs
- Geometric shapes ONLY: rectangles, circles, arrows
- No realistic objects (no dinosaurs, no buildings, no people)
- Use `scale=0.75` or `scale=0.8` to prevent overflow
- `\scriptsize` or `\tiny` for all labels inside TikZ

**Proven comic patterns** (from L05_pca_tsne_simple.tex):

1. **"Drowning in X"** (opening): Stick figure + tall stack of rectangles labeled F1..F50 + speech bubble "I can't see the patterns!"
2. **"Shadow on Wall"** (projection analogy): Cube + sun circle + wall + shadow + "Best angle" arrow
3. **"Neighborhood Preservation"** (embedding analogy): Labeled dots on curve + arrow + same dots on flat line, neighbor connections preserved
4. **"Before/After panels"** (resolution): Left panel (gray dots, confused face) + arrow + right panel (colored clusters, happy face)

### Step 3: Slide Structure (~25 slides)

```
FRONT MATTER (3 slides)
  1. Title page
  2. XKCD opening + framing question
  3. Learning objectives (3 bullets, plain English)

ACT 1: THE PROBLEM (3 slides)
  4. TikZ comic: the problem personified
  5. CHART: proof that the solution works (before/after)
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
  21. Domain application teaser (1 compelling fact)
  22. Code recipe (3-5 lines per method)

CLOSING (3 slides)
  23. TikZ comic: resolution (same character, happy)
  24. Key takeaways (5 bullets)
  25. XKCD closing
```

### Step 4: Writing Rules

| Rule | Why |
|------|-----|
| Zero `$$` display math | The whole point is no formulas |
| Every title is a question or action | "How Many Components?" not "Scree Plot" |
| Max 3 bullets per chart slide | Chart is the star, not the text |
| `\bottomnote{}` on every slide | Course standard + adds depth without cluttering |
| "sklearn does it" instead of showing equations | Acknowledges math exists without displaying it |
| XKCD bookends (opening + closing) | Bookend rule from course pedagogy |
| `\texttt{}` for code, not `lstlisting` | Simpler, no extra packages, matches existing style |

### Step 5: Verification

```bash
# Must all pass:
grep -c "begin{frame" FILE.tex           # 22-28
grep -c "chart.pdf" FILE.tex             # 6-10
grep -c "bottomnote" FILE.tex            # >= slides - 1
grep -c '\$\$' FILE.tex                  # 0
grep -c "begin{tikzpicture}" FILE.tex    # >= 4
pdflatex -interaction=nonstopmode FILE.tex
grep -c "Overfull" FILE.log              # 0
```

## Example

Reference implementation: `slides/L05_PCA_tSNE/L05_pca_tsne_simple.tex`

| Metric | Value |
|--------|-------|
| Slides | 25 |
| Charts (reused) | 8 |
| New charts created | 0 |
| TikZ pictures | 10 (4 comics + 6 diagrams) |
| `$$` formulas | 0 |
| Overfull warnings | 0 |
| PDF size | 649 KB |
| Narrative arc | Drowning -> Shadow (PCA) -> Neighborhood (t-SNE) -> Clarity |

## Anti-Patterns

- **Don't create new chart.py files** — the whole point is reusing existing charts
- **Don't "simplify" formulas** — either show the formula or don't; "simplified" formulas are the worst of both worlds
- **Don't use more than 8-10 charts** — too many charts = no narrative, just a gallery
- **Don't skip the opening/closing comics** — they provide the emotional arc that makes the lecture memorable
- **Don't use TikZ for anything realistic** — cubes, circles, arrows, stick figures only
