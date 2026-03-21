# Chart Quality Overhaul: Textbook-Level Polish for All 162 Charts

## Context

### Original Request
Improve the visual quality of ALL charts across L01-L06 to textbook-level (ISLR/Bishop ML style). Four quality dimensions: visual polish, Beamer readability, data presentation, professional appearance.

### Interview Summary
Direct assignment via ralplan -- no interview conducted. Requirements are fully specified in the task brief.

### Research Findings

**Current state (162 chart.py files):**

| Topic | Chart Count |
|-------|-------------|
| L01 | 8 |
| L02 | 7 |
| L03 | 24 (13 core + 11 top10) |
| L04 | 41 (27 core + 13 top10 + 1 extra) |
| L05 | 50 (13 core + 12 top10 + 20 top20 + 5 numbered) |
| L06 | 32 (19 core + 13 top10) |
| **Total** | **162** |

**Current patterns observed across all 162 charts:**
- ALL charts define rcParams inline (copy-pasted block in every file)
- ALL charts define color constants inline (MLPURPLE, MLBLUE, etc.) -- no shared import
- 71 of 162 charts have `ax.grid()` calls, 91 do NOT
- 24 of 162 charts set `facecolor='white'` in savefig, 138 do NOT
- ALL 162 charts remove top/right spines (either via rcParams or manual `set_visible`)
- 156 charts use `Path(__file__).parent / 'chart.pdf'` for output; 6 use `os.path.join(os.path.dirname(...))`
- 7 charts use subplots (side-by-side comparisons) -- these are deliberate design choices, not violations:
  1. `L04/top10_08_dt_vs_rf_boundary` (1,2)
  2. `L03/top10_10_kmeans_failure_cases` (1,2)
  3. `L05/top10_12_kernel_pca` (1,2)
  4. `L05/top10_11_scaling_effect` (1,2)
  5. `L05/top10_20_tsne_perplexity_grid` (2,2)
  6. `L05/top10_13_tsne_iterations` (1,3)
  7. `L05/top10_19_pca_whitening` (1,3)
- No chart currently imports from any shared style module
- The existing `templates/chart_template.py` is a copy-template, not an importable module

**Key inconsistencies to fix:**
1. Font sizes: all use 14/14/16/13/13/13 -- need bump for projection readability
2. Grid lines: present in 44% of charts, absent in 56%
3. White background: only 15% explicitly set it
4. Line widths: vary wildly (1.0 to 3.0)
5. Edge colors on scatter/bar: some have `edgecolor='black'`, some `edgecolor='white'`, some none
6. Legend placement: mixed (some overlap data)
7. URL text: some use `ax.text()`, some use `plt.figtext()` -- inconsistent positioning

---

## Work Objectives

### Core Objective
Create a shared style module and systematically apply it to all 162 charts, achieving consistent textbook-quality appearance without changing any chart's data, algorithm, or meaning.

### Deliverables
1. **`templates/chart_style.py`** -- importable style module with rcParams, colors, helper functions
2. **`tools/patch_charts.py`** -- batch script to inject the style import into all 162 charts
3. **All 162 chart.py files updated** -- importing shared style, with per-chart manual fixes where needed
4. **All 162 chart.pdf files regenerated** -- verifying no breakage
5. **Updated `templates/chart_template.py`** -- reflecting new style for future charts

### Definition of Done
- Every chart.py imports from `chart_style.py` (verified by grep)
- Every chart.pdf regenerates without error (verified by running chart builder)
- Visual consistency: all charts have grid lines, white backgrounds, consistent fonts
- No chart semantics changed (data, algorithms, labels remain identical)
- CLAUDE.md updated with new chart standard

---

## Guardrails

### Must Have
- Shared style module at `templates/chart_style.py`
- ALL 162 charts importing from the shared module
- Spine removal (top/right) on every chart
- Subtle grid lines on every chart (light gray, alpha=0.3)
- Bumped font sizes for projection readability
- White backgrounds on all chart PDFs
- Consistent line widths
- `facecolor='white'` in all savefig calls
- Each chart.py still runnable standalone (self-contained with the import)

### Must NOT Have
- Changes to chart data generation or algorithm logic
- Changes to figsize (must remain 10,6)
- New subplots where none existed
- Removal of existing subplots (7 charts use them deliberately -- see research findings for full list)
- Changes to chart titles, axis labels, or legend text content
- New dependencies beyond matplotlib/numpy/sklearn/scipy
- Any chart that fails to regenerate

---

## Task Flow

```
[T1: Create style module] --> [T2: Create patch script] --> [T3: Run patch script]
                                                                    |
                                                          [T4: Manual per-topic fixes]
                                                                    |
                                                          [T5: Regenerate all PDFs]
                                                                    |
                                                          [T6: Update template + docs]
```

T1 and T2 can be done in parallel. T3 depends on both. T4 depends on T3. T5 depends on T4. T6 depends on T5.

---

## Detailed TODOs

### T1: Create Shared Style Module (`templates/chart_style.py`)

**File:** `templates/chart_style.py`
**Acceptance:** Module importable from any chart.py via `sys.path` manipulation; defines all style constants and helper functions.

Create the module with these components:

```
1.1 - RCPARAMS dict (bumped font sizes):
      font.size: 14 -> 15
      axes.labelsize: 14 -> 16
      axes.titlesize: 16 -> 18
      xtick.labelsize: 13 -> 14
      ytick.labelsize: 13 -> 14
      legend.fontsize: 13 -> 13 (keep -- legends are smaller by design)
      figure.figsize: (10, 6) (unchanged)
      figure.dpi: 150 (unchanged)
      axes.spines.top: False
      axes.spines.right: False
      axes.grid: True
      axes.grid.axis: 'both'   (but many charts override to 'x' or 'y' only)
      grid.alpha: 0.3
      grid.linestyle: '--'
      grid.color: '#CCCCCC'
      figure.facecolor: 'white'
      axes.facecolor: 'white'
      savefig.facecolor: 'white'
      savefig.bbox: 'tight'
      lines.linewidth: 2.0
      scatter.edgecolors: 'white'   # NOTE: charts with deliberate black edges must override

1.2 - COLOR PALETTE dict (unchanged from CLAUDE.md canonical values):
      MLPurple: '#3333B2'
      MLBlue: '#0066CC'
      MLOrange: '#FF7F0E'
      MLGreen: '#2CA02C'
      MLRed: '#D62728'
      MLLavender: '#ADADE0'
      MLGray: '#808080'
      Also export individual names: MLPURPLE, MLBLUE, etc. for backward compat
      NOTE: Colors are NOT muted -- they match CLAUDE.md exactly. Textbook
      quality comes from typography, grid, spacing, and spines -- not color changes.

1.3 - apply_style() function:
      Calls plt.rcParams.update(RCPARAMS)
      Returns the COLORS dict for convenience

1.4 - save_chart(fig, file_path=None) helper:
      If file_path is None, auto-detect from __file__ of caller (using inspect)
      Calls plt.tight_layout()
      Calls fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
      Calls plt.close(fig)
      Prints confirmation

1.5 - add_url(ax_or_fig, url) helper:
      Standardized URL placement (bottom-right, fontsize=7, gray, alpha=0.7)
      Uses plt.figtext for consistency

1.6 - PATH RESOLUTION: The module must work when imported from any chart.py
      at any depth. Add a function: get_chart_dir(caller_file) that returns
      Path(caller_file).parent for the output path.
```

**Import mechanism:** Each chart.py will add this near the top:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, save_chart
apply_style()
```

This works because every chart is at depth `slides/LXX_Topic/NN_name/chart.py`:
- `parents[0]` = `NN_name/` (chart folder)
- `parents[1]` = `LXX_Topic/` (topic folder)
- `parents[2]` = `slides/` (slides directory)
- `parents[3]` = repo root (where `templates/` lives)

top10/top20 charts follow the same depth, so `parents[3]` works universally.

**Verification:** `python -c "import sys; sys.path.insert(0, 'templates'); from chart_style import apply_style; apply_style(); print('OK')"`

---

### T2: Create Batch Patch Script (`tools/patch_charts.py`)

**File:** `tools/patch_charts.py`
**Acceptance:** Script that modifies all 162 chart.py files to: (a) add the style import, (b) remove inline rcParams block, (c) remove inline color constant definitions, (d) update savefig calls to include facecolor='white'.

Patch logic per file:

```
2.1 - Insert import block after the existing imports (after last `import` or `from` line):
      import sys
      sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
      from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
      apply_style()

2.2 - Remove the inline plt.rcParams.update({...}) block (regex match the entire block)

2.3 - Remove inline color constant lines:
      Lines matching: MLPURPLE = '#...'
      Lines matching: MLBLUE = '#...'
      Lines matching: MLORANGE = '#...'
      etc.
      BUT: Only remove if they match the standard palette values.
      If a chart defines a CUSTOM color not in the palette, KEEP IT.

2.4 - Update savefig calls:
      If missing facecolor='white', add it
      If missing bbox_inches='tight', add it

2.5 - Normalize URL placement:
      Leave existing URL code alone (too varied to auto-patch safely)

2.6 - Add grid line if completely missing:
      If the chart has NO ax.grid() call AND no plt.grid() call,
      do NOT auto-add (some charts like heatmaps/flowcharts shouldn't have grids).
      The rcParams default handles most cases.
```

**Safety:** The script must:
- Create a backup of each file before patching (`.chart.py.bak`)
- Run in dry-run mode by default (`--dry-run` flag)
- Log every change made
- Skip files that already have the import

---

### T3: Run Patch Script on All 162 Charts

**Command:** `python tools/patch_charts.py --dry-run` first, then `python tools/patch_charts.py`
**Acceptance:** All 162 files patched. Grep confirms: 162 files contain `from chart_style import`.

Steps:
```
3.1 - Run dry-run and review output for anomalies
3.2 - Run actual patch
3.3 - Verify with: grep -r "from chart_style import" slides/ | wc -l  (expect 162)
3.4 - Verify no inline rcParams remain: grep -r "plt.rcParams.update" slides/**/chart.py (expect 0)
3.5 - Spot-check 5 charts (one per topic) to verify clean patching
```

---

### T4: Manual Per-Topic Polish Pass

After the batch patch handles the 80% (fonts, grids, spines, colors, backgrounds), do a manual pass per topic for chart-specific issues. This is the "20%" that requires human judgment.

**T4.1 - L01 (8 charts):** Check legend placement, annotation arrows, axis label units. These are the simplest charts -- should need minimal manual work.

**T4.2 - L02 (7 charts):** ROC curve and precision-recall charts need careful legend placement (lower-right for ROC, upper-right for PR). Confusion matrix chart may need grid suppressed (heatmap).

**T4.3 - L03 (24 charts):** KMeans iteration chart needs clean centroid markers. Voronoi chart may need grid suppressed. Decision flowchart is TikZ-like (likely needs grid suppressed). Worked example chart has multi-panel layout.

**T4.4 - L04 (41 charts):** Largest batch. Decision tree visualization may need grid suppressed. SHAP waterfall chart has specific formatting needs. Feature importance bar chart needs value labels aligned. Many boosting charts share similar line-plot structure -- check consistency.

**T4.5 - L05 (50 charts):** Largest batch. Scree plot has dual y-axes (grid on left axis only). t-SNE perplexity comparisons (04a/04b/04c) must look identical except for data. Swiss roll plots (05a/05b) are 3D-ish. Top20 charts are supplementary -- lower priority for manual polish.

**T4.6 - L06 (32 charts):** RL loop and DQN architecture are diagram-style (suppress grid). FinBERT bars and reward curves are standard. Q-learning grid is a heatmap (suppress grid). Static vs contextual embedding has manual spine handling.

**Per-chart manual fixes (common patterns):**
- Suppress grid on heatmaps: `ax.grid(False)`
- Suppress grid on flowcharts/diagrams: `ax.grid(False)`
- Fix legend overlap: move to `bbox_to_anchor` if data obscured
- Add `zorder=3` to data elements that should be above grid
- Ensure scatter `edgecolors='white'` with `linewidth=0.5` for clean separation
- Bump annotation font sizes from 10-11 to 12

**Acceptance per topic:** All charts in the topic regenerate without error and have consistent styling.

---

### T5: Regenerate All Chart PDFs

**Command:** `python infrastructure/course_cli.py build charts --topic all`
**Acceptance:** All 162 chart.pdf files regenerated, zero errors.

```
5.1 - Run the chart builder for all topics
5.2 - Check output for any Python errors or warnings
5.3 - Verify all 162 chart.pdf files have recent timestamps
5.4 - Spot-check 10 PDFs visually (2 per topic) for correct rendering
```

---

### T6: Update Documentation and Template

```
6.1 - Update templates/chart_template.py:
      Replace inline rcParams with import from chart_style
      Replace inline colors with import
      Update comments to reference the style module

6.2 - Update CLAUDE.md chart section:
      Document the new chart_style.py import pattern
      Update font size table to reflect new values
      Add note about chart_style.py location and usage
      Color palette hex values are unchanged -- just document the chart_style.py import pattern

6.3 - Remove .chart.py.bak files:
      After successful verification, delete all backup files
```

---

## Commit Strategy

| Commit | Contents | Message |
|--------|----------|---------|
| 1 | `templates/chart_style.py` + `tools/patch_charts.py` | "Add shared chart style module and batch patch script" |
| 2 | All 162 patched chart.py files | "Apply shared style to all 162 charts for textbook-quality polish" |
| 3 | Manual per-topic fixes (L01-L03) | "Manual chart polish: L01-L03 (legend, grid, annotation fixes)" |
| 4 | Manual per-topic fixes (L04-L06) | "Manual chart polish: L04-L06 (legend, grid, annotation fixes)" |
| 5 | All 162 regenerated chart.pdf files | "Regenerate all 162 chart PDFs with textbook styling" |
| 6 | Updated template + CLAUDE.md + cleanup | "Update chart template and docs for new style module" |

---

## Success Criteria

1. **Consistency:** `grep -r "from chart_style import" slides/ | wc -l` returns 162
2. **No inline rcParams:** `grep -r "plt.rcParams.update" slides/**/chart.py | wc -l` returns 0
3. **All regenerate:** `python infrastructure/course_cli.py build charts --topic all` exits 0 with 162 PDFs
4. **No semantic changes:** Diff of chart.py files shows ONLY style-related changes (imports, rcParams removal, color constant removal, savefig updates)
5. **Visual spot-check:** 12 randomly selected PDFs (2 per topic) show: grid lines, larger fonts, white backgrounds, no spine clutter

---

## Execution Notes

**Critical risks and mitigations:**

1. **Import path resolution:** The `parents[3]` approach assumes chart depth is exactly 3 levels below repo root (`slides/LXX/NN_name/chart.py`). Verified: all 162 charts follow this pattern.

2. **Charts with custom colors:** Some charts define additional colors beyond the ML palette (e.g., `'gray'`, custom hex values for specific elements). The patch script must ONLY remove the 6 standard ML color constants, not any custom ones.

3. **Grid on heatmaps/diagrams:** The rcParams default enables grid globally. Charts that use `imshow`/`pcolormesh`/heatmaps MUST add `ax.grid(False)`. Complete list (20+ charts):

   **Heatmap-style (imshow/pcolormesh) -- 11 charts:**
   - `L02/06_confusion_matrix`
   - `L03/top10_16_cluster_centers_heatmap`
   - `L03/top10_20_knn_confusion_matrix`
   - `L04/top10_14_confusion_matrix`
   - `L04/top10_16_probability_heatmap`
   - `L04/top10_18_ensemble_diversity`
   - `L04/top10_20_proximity_matrix`
   - `L04/22_correlation_variance_surface`
   - `L05/top10_14_explained_var_heatmap`
   - `L06/02_similarity_heatmap`
   - `L06/top10_15_state_action_heatmap`

   **Diagram-style (ax.axis('off') or plot_tree) -- 16 charts:**
   - `L01/08_decision_flowchart`
   - `L02/07_decision_flowchart`
   - `L03/07_decision_flowchart`
   - `L04/01_decision_tree`
   - `L04/03_bootstrap`
   - `L04/05_ensemble_voting`
   - `L04/07_decision_flowchart`
   - `L04/top10_05_tree_structure` (uses plot_tree -- needs explicit ax.grid(False))
   - `L05/07_decision_flowchart`
   - `L06/03_rl_loop`
   - `L06/04_q_learning_grid`
   - `L06/07_decision_flowchart`
   - `L06/08_skipgram_architecture`
   - `L06/09_dqn_architecture`
   - `L06/10_negative_sampling`
   - `L06/14_rag_pipeline_flow`
   - `L06/18_rlhf_pipeline`

   The T4 manual pass MUST verify every chart in this list has `ax.grid(False)`.

4. **Dual-axis charts:** ALL charts with `twinx()` need `ax2.grid(False)` on the secondary axis. Complete list (4 charts):
   - `L05/01_scree_plot`
   - `L06/top10_18_embedding_pca_variance`
   - `L05/top10_18_intrinsic_dimensionality`
   - `L03/top10_15_minibatch_kmeans`

5. **7 subplot charts:** These already work and should continue to work. The style module sets figure-level defaults that apply to all subplots within a figure. See research findings for the complete list of 7 charts.

6. **6 charts using os.path instead of Path:** These are all in L06 (charts 14-19). The patch script must handle both import patterns for output path.

7. **Color values:** Colors are kept at CLAUDE.md canonical values (no muting). Visual improvement comes from typography, grid, spacing, and spine removal -- not color changes.

**Execution order recommendation:** T1 and T2 in parallel, then T3-T6 sequentially. Total estimated effort: T1 (30 min), T2 (45 min), T3 (15 min), T4 (2-3 hours across all topics), T5 (30 min), T6 (15 min).

---

## Critic Issue Resolution Log

**Iteration 1 → 2 fixes applied:**

| Issue | Resolution |
|-------|-----------|
| FATAL: `parents[2]` wrong -- should be `parents[3]` | **Fixed:** All occurrences updated to `parents[3]`. Added explicit parent chain documentation showing parents[0]-[3] mapping. |
| Subplot count wrong (5 vs actual 7) | **Fixed:** Updated to 7 with complete named list of all subplot charts. |
| Incomplete heatmap/diagram grid-suppress list (8 vs 20) | **Fixed:** Expanded to complete list: 11 heatmap-style + 9 diagram-style charts, all named explicitly. |
| twinx charts undercounted (1 vs 4) | **Fixed:** Expanded to all 4 twinx charts by name. |
| Color muting contradicts CLAUDE.md | **Fixed:** Removed all color muting. Palette now uses CLAUDE.md canonical hex values exactly. Textbook quality comes from typography/grid/spacing, not color changes. |
| `save_chart()` used dpi=300 vs standard dpi=150 | **Fixed:** Updated to dpi=150 to match CLAUDE.md standard. |
| scatter.edgecolors global default could break some charts | **Fixed:** Added note that charts with deliberate black edges must override. |
