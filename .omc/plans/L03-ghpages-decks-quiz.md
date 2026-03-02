# Plan: L03 GH Pages Deployment, Deck Audit, Quiz Alignment (v2)

## Task
Three deliverables:
1. Deploy L03 accessible slides + new chart images to GitHub Pages
2. Audit supplementary slide decks vs established patterns across topics
3. Create L03 quiz aligned to accessible slide content

---

## Part 1: GitHub Pages Deployment

### 1A. Copy New PDFs to docs/slides/pdf/
```bash
cp slides/L03_KNN_KMeans/L03_overview_accessible.pdf docs/slides/pdf/
cp slides/L03_KNN_KMeans/L03_deepdive_accessible.pdf docs/slides/pdf/
```

### 1B. Generate Chart PNGs (Concrete Method)

Each chart.py currently saves only `chart.pdf`. To generate PNGs, add a `plt.savefig()` call for PNG in each of the 6 new chart.py files (08-13), then re-run them:

```python
# Add this line BEFORE plt.close() in each chart.py:
plt.savefig(Path(__file__).parent / 'chart.png', dpi=150, bbox_inches='tight', facecolor='white')
```

Then copy the PNGs to docs:
```bash
for num in 08 09 10 11 12 13; do
  name=$(ls -d slides/L03_KNN_KMeans/${num}_*/)
  basename=$(basename $name)
  cp ${name}chart.png docs/slides/images/L03_KNN_KMeans/${basename#*_}.png
done
```

Wait — the existing naming convention uses just the descriptive part without the number prefix. Checking existing names:
- `01_knn_boundaries.png` → file is named `01_knn_boundaries.png` (number included)

So the convention IS `{number}_{name}.png`. The copy commands:
```bash
cp slides/L03_KNN_KMeans/08_feature_scaling_effect/chart.png docs/slides/images/L03_KNN_KMeans/08_feature_scaling_effect.png
cp slides/L03_KNN_KMeans/09_knn_step_by_step/chart.png docs/slides/images/L03_KNN_KMeans/09_knn_step_by_step.png
cp slides/L03_KNN_KMeans/10_bias_variance_visual/chart.png docs/slides/images/L03_KNN_KMeans/10_bias_variance_visual.png
cp slides/L03_KNN_KMeans/11_rfm_scatter/chart.png docs/slides/images/L03_KNN_KMeans/11_rfm_scatter.png
cp slides/L03_KNN_KMeans/12_kmeans_worked_example/chart.png docs/slides/images/L03_KNN_KMeans/12_kmeans_worked_example.png
cp slides/L03_KNN_KMeans/13_cv_accuracy_curve/chart.png docs/slides/images/L03_KNN_KMeans/13_cv_accuracy_curve.png
```

### 1C. Update docs/index.html — L03 Section

**Step 1: Add accessible PDF cards** after the K-Means Mini-Lecture card (line 199):
```html
<a class="ccard" href="slides/pdf/L03_overview_accessible.pdf" download><div class="ccard-icon">PDF</div>Overview (Accessible)<div class="ccard-label">28-slide intro-level</div></a>
<a class="ccard" href="slides/pdf/L03_deepdive_accessible.pdf" download><div class="ccard-icon">PDF</div>Deep Dive (Accessible)<div class="ccard-label">29-slide intro-level</div></a>
```

**Step 2: Update L03 Charts header** (line 203 → shifts to ~205 after PDF insertion):
Change `Charts (7)` to `Charts (13)`.

**Step 3: Add 6 chart image cards** after 07_decision_flowchart card (adjust for line drift from step 1):
```html
<a class="ccard" href="slides/images/L03_KNN_KMeans/08_feature_scaling_effect.png" target="_blank"><img src="slides/images/L03_KNN_KMeans/08_feature_scaling_effect.png" alt="Feature Scaling" style="width:100%;height:80px;object-fit:contain;background:#fff;border-radius:3px;margin-bottom:4px" loading="lazy"><span class="ccard-name" style="font-size:9px">Feature Scaling</span></a>
<a class="ccard" href="slides/images/L03_KNN_KMeans/09_knn_step_by_step.png" target="_blank"><img src="slides/images/L03_KNN_KMeans/09_knn_step_by_step.png" alt="KNN Step by Step" style="width:100%;height:80px;object-fit:contain;background:#fff;border-radius:3px;margin-bottom:4px" loading="lazy"><span class="ccard-name" style="font-size:9px">KNN Step by Step</span></a>
<a class="ccard" href="slides/images/L03_KNN_KMeans/10_bias_variance_visual.png" target="_blank"><img src="slides/images/L03_KNN_KMeans/10_bias_variance_visual.png" alt="Bias vs Variance" style="width:100%;height:80px;object-fit:contain;background:#fff;border-radius:3px;margin-bottom:4px" loading="lazy"><span class="ccard-name" style="font-size:9px">Bias vs Variance</span></a>
<a class="ccard" href="slides/images/L03_KNN_KMeans/11_rfm_scatter.png" target="_blank"><img src="slides/images/L03_KNN_KMeans/11_rfm_scatter.png" alt="RFM Segments" style="width:100%;height:80px;object-fit:contain;background:#fff;border-radius:3px;margin-bottom:4px" loading="lazy"><span class="ccard-name" style="font-size:9px">RFM Segments</span></a>
<a class="ccard" href="slides/images/L03_KNN_KMeans/12_kmeans_worked_example.png" target="_blank"><img src="slides/images/L03_KNN_KMeans/12_kmeans_worked_example.png" alt="K-Means Worked Example" style="width:100%;height:80px;object-fit:contain;background:#fff;border-radius:3px;margin-bottom:4px" loading="lazy"><span class="ccard-name" style="font-size:9px">K-Means Worked</span></a>
<a class="ccard" href="slides/images/L03_KNN_KMeans/13_cv_accuracy_curve.png" target="_blank"><img src="slides/images/L03_KNN_KMeans/13_cv_accuracy_curve.png" alt="CV Accuracy Curve" style="width:100%;height:80px;object-fit:contain;background:#fff;border-radius:3px;margin-bottom:4px" loading="lazy"><span class="ccard-name" style="font-size:9px">CV Accuracy</span></a>
```

### 1D. Update Hero Stats Counters (line 116)

Current values → new values:
- `<b>12</b><small>PDFs</small>` → `<b>14</b><small>PDFs</small>` (+2 accessible PDFs)
- `<b>48</b><small>Charts</small>` → `<b>54</b><small>Charts</small>` (+6 new charts)
- `<b>165</b><small>Quiz Questions</small>` → `<b>185</b><small>Quiz Questions</small>` (+20 new quiz questions)

### 1E. Acceptance Criteria (Part 1)
1. `docs/slides/pdf/L03_overview_accessible.pdf` exists (file size > 100KB)
2. `docs/slides/pdf/L03_deepdive_accessible.pdf` exists (file size > 100KB)
3. 6 new PNG images in `docs/slides/images/L03_KNN_KMeans/` (08-13)
4. `docs/index.html` has `L03_overview_accessible.pdf` and `L03_deepdive_accessible.pdf` links
5. `docs/index.html` has image cards for all 13 charts
6. Hero stats: PDFs=14, Charts=54, Quiz Questions=185
7. L03 Charts header reads "Charts (13)"

---

## Part 2: Supplementary Slide Deck Audit

### Current Inventory (All Topics)

| Topic | Overview | Deepdive | Accessible O | Accessible D | Mini | Full | Self-Study |
|-------|----------|----------|--------------|--------------|------|------|------------|
| L01 | Y | Y | - | - | - | - | - |
| L02 | Y | Y | - | - | Y (logreg_mini) | Y (logreg_full, 31 slides) | Y (selfstudy + selfstudy_intro) |
| L03 | Y | Y | **Y (NEW)** | **Y (NEW)** | Y (knn_mini + kmeans_mini) | **- GAP** | **- GAP** |
| L04 | Y | Y | - | - | Y (rf_mini) | Y (rf_full, 31 slides) | - |
| L05 | Y | Y | - | - | - | - | - |
| L06 | Y | Y | - | - | - | - | - |

### Gap Analysis

**Pattern from L02 and L04:** Both have a "full technical lecture" (~31 slides) combining overview + deepdive highlights into a standalone deck. L02 additionally has self-study reading guides (5-page PDFs).

**L03 gaps vs L02/L04 pattern:**
1. **No full technical lecture** — L02 has `logreg_full` (31 slides), L04 has `rf_full` (31 slides). L03 has none.
2. **No self-study guide** — L02 has `selfstudy` + `selfstudy_intro`. L03 has none.

**Recommendation:** These supplementary decks are NOT required by the beamer-slide-restructure skill (which specifies only overview + deepdive). They were created as extra materials for L02 and L04. Whether to create them for L03 is a course design decision.

**This plan does NOT include creating these supplementary decks.** If the user wants them, a separate ralplan can be initiated. The accessible overview (28 slides) and deepdive (29 slides) already serve as intro-level alternatives.

### 2E. Acceptance Criteria (Part 2)
1. Gap audit presented to user (this table above) for informed decision
2. No new supplementary deck files created unless user separately requests them

---

## Part 3: L03 Quiz for Accessible Slides

### Current State
- `docs/quiz/L03_knn_kmeans.html` — 20 questions for MSc-level slides
- Skill Rule 6: "Quiz questions must reference actual content" from final slides
- Skill Gotcha 7: "Quiz-Slide Drift" — always write quiz AFTER finalizing slides

### Approach
Create a NEW quiz file `docs/quiz/L03_knn_kmeans_accessible.html` with 20 questions aligned to the accessible slides. Keep the existing quiz for MSc students.

**CRITICAL — Read accessible .tex files FIRST:** Before writing any quiz question, the executor MUST read `L03_overview_accessible.tex` and `L03_deepdive_accessible.tex` to extract testable concepts. Slide number references in the topic distribution below are approximate — verify against actual file content.

### Quiz Design Rules (from skill)
- Every question references a concept in the accessible .tex slides
- Questions test reasoning ("What would happen if...") not memorization
- Even distribution: ~10 KNN questions + ~10 K-Means questions
- Answer explanations cite specific slide content
- Use KaTeX for math rendering (matching existing quiz template)
- Three-column card layout (matching existing L03 quiz design)

### Question Topic Distribution (20 questions)
| Topic | Count | Approximate Source |
|-------|-------|--------------------|
| KNN basics (lazy learner, neighbors, voting) | 4 | Overview: classification intro, KNN steps, step-by-step chart |
| Distance metrics & feature scaling | 3 | Overview: Euclidean formula, distance chart; Deepdive: scaling chart |
| K selection & bias-variance | 3 | Overview: K boundaries; Deepdive: bias-variance, CV curve |
| K-Means algorithm & iterations | 3 | Overview: K-Means steps, iteration chart; Deepdive: objective, worked example |
| K-Means evaluation (elbow, silhouette) | 3 | Overview: elbow chart; Deepdive: silhouette, Voronoi |
| KNN vs K-Means comparison | 2 | Overview: comparison table, decision flowchart |
| Finance applications (RFM, fraud) | 2 | Overview: RFM scatter, class imbalance |

### Quiz HTML Structure
Copy `docs/quiz/L03_knn_kmeans.html` as template. Modifications:
- Title: "Quiz 3: KNN & K-Means (Accessible)"
- `quizData.questions`: 20 new questions as JSON array
- Navigation: Link back to dashboard

**KaTeX Initialization (CLAUDE.md gotcha):** The existing quiz uses `waitForKaTeX(renderMath)` at end of body, NOT inside `DOMContentLoaded`. The new quiz MUST preserve this pattern — call `renderMath()` directly at end of `<body>`, not inside a `DOMContentLoaded` listener. Copy the script section from the existing quiz verbatim and only change the `quizData` object.

### Update docs/index.html for Quiz

**Step 1: Add accessible quiz card** in Per-Lesson Quizzes section (after line 332, the existing L03 quiz card):
```html
<a class="lcard" href="quiz/L03_knn_kmeans_accessible.html" style="border-left:3px solid #FF7F0E;background:linear-gradient(135deg,#f5f3ff,#ede9fe)"><span class="lcard-num" style="background:#8b5cf6;color:white">L03</span><span class="lcard-title">KNN & K-Means (Accessible)</span><div style="font-size:9px;color:#7c3aed;margin-top:4px;font-weight:600">20 questions</div></a>
```

**Step 2: Update Per-Lesson Quizzes count** (line 328):
Change `Per-Lesson Quizzes (120 questions)` to `Per-Lesson Quizzes (140 questions)`.

**Step 3: Add sidebar navigation entry** (around line 101, after existing L03 quiz sidebar link):
```html
<li><a href="#per-lesson-quizzes">L03 KNN & K-Means (Accessible)</a></li>
```

### 3E. Acceptance Criteria (Part 3)
1. `docs/quiz/L03_knn_kmeans_accessible.html` exists with exactly 20 questions
2. Every question references content present in accessible .tex files (verified by reading both files first)
3. Zero references to MSc-only content (Cover & Hart, Mahalanobis, formal proofs, Hopkins statistic, Gap statistic, cosine similarity)
4. Even distribution (~10 KNN, ~10 K-Means)
5. KaTeX renders correctly (renderMath called at end of body, NOT in DOMContentLoaded)
6. `docs/index.html` has quiz card for accessible quiz
7. `docs/index.html` Per-Lesson Quizzes count updated to 140
8. `docs/index.html` sidebar has entry for accessible quiz

---

## Execution Steps (Ordered)

1. **Generate chart PNGs** — Add `plt.savefig(..., 'chart.png')` to each of the 6 new chart.py files (08-13), re-run them
2. **Copy files to docs** — 2 PDFs to `docs/slides/pdf/`, 6 PNGs to `docs/slides/images/L03_KNN_KMeans/`
3. **Read accessible .tex files** — Extract all testable concepts for quiz
4. **Write quiz** — Create `docs/quiz/L03_knn_kmeans_accessible.html` with 20 questions
5. **Update index.html** — All changes in single pass to avoid line-drift confusion:
   a. Hero stats: PDFs 12→14, Charts 48→54, Quiz Questions 165→185
   b. L03 section: add 2 PDF cards after kmeans_mini
   c. L03 Charts header: 7→13
   d. L03 Charts grid: add 6 image cards after 07_decision_flowchart
   e. Per-Lesson Quizzes header: 120→140
   f. Per-Lesson Quizzes grid: add accessible quiz card after L03
   g. Sidebar: add accessible quiz entry

**NOTE on line drift:** Steps 5a-5g modify index.html. Use string-matching (Edit tool with `old_string`) rather than line numbers to avoid drift issues from earlier insertions.

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Chart PNG conversion fails | Add plt.savefig PNG line, re-run; fallback: Python `from PIL import Image` convert |
| Quiz references MSc-only content | Executor reads accessible .tex first; Architect verification step |
| index.html line drift | Use Edit tool with exact string matching, not line numbers |
| KaTeX initialization bug | Copy script section verbatim from existing quiz, only change quizData |
| Hero stat counts wrong | Verify: `ls docs/slides/pdf/*.pdf | wc -l` for PDF count, etc. |

---

PLAN_READY: .omc/plans/L03-ghpages-decks-quiz.md
