# Presentation Ultra-Deep Review Work Plan

## Context

### Original Request
Ultra-deep review of all 12 presentations (6 overview + 6 deepdive) covering:
1. Template compliance verification
2. Content structure review (PMSP framework, slide counts, chart references)
3. Chart compilation verification (51 chart.py scripts)
4. Per-presentation JSON inventory generation

### Codebase Structure
```
slides/
  L01_Introduction_Linear_Regression/
    L01_overview.tex (~17 slides)
    L01_deepdive.tex (~30 slides)
    01_simple_regression/chart.py -> chart.pdf
    02_multiple_regression_3d/chart.py -> chart.pdf
    ... (8 charts total)
  L02_Logistic_Regression/
    L02_overview.tex
    L02_deepdive.tex
    01_sigmoid_function/chart.py -> chart.pdf
    ... (7 charts total)
  L03_KNN_KMeans/
    L03_overview.tex
    L03_deepdive.tex
    ... (7 charts total)
  L04_Random_Forests/
    L04_overview.tex
    L04_deepdive.tex
    ... (8 charts: includes 06a/06b pair)
  L05_PCA_tSNE/
    L05_overview.tex
    L05_deepdive.tex
    ... (11 charts: includes 04a/04b/04c, 05a/05b, 06a/06b/06c)
  L06_Embeddings_RL/
    L06_overview.tex
    L06_deepdive.tex
    ... (7 charts total)
```

### Template Requirements (from templates/beamer_template.tex)
- **Document class**: `\documentclass[8pt,aspectratio=169]{beamer}`
- **Theme**: `\usetheme{Madrid}` with `\usecolortheme{default}`
- **Colors defined**:
  - MLPurple: RGB{51,51,178} = #3333B2
  - MLBlue: RGB{0,102,204} = #0066CC
  - MLOrange: RGB{255,127,14} = #FF7F0E
  - MLGreen: RGB{44,160,44} = #2CA02C
  - MLRed: RGB{214,39,40} = #D62728
- **Footer**: Three boxes (Methods and Algorithms | MSc Data Science | page X/Y)
- **Commands**: `\bottomnote{}`, `\highlight{}`, `\mathbold{}`
- **PMSP Sections**: Problem, Method, Solution, Practice, Decision Framework, Summary
- **Chart widths**: 0.55\textwidth (with text) or 0.65\textwidth (chart-only slides)

### Chart Requirements (from templates/chart_template.py)
- `figsize=(10, 6)`
- `figure.dpi=150`
- Font sizes: 14 (general), 14 (labels), 16 (title), 13 (ticks, legend)
- ONE figure per chart (NO subplots)
- Output: `chart.pdf` in same directory
- Color palette: COLORS dict with primary (#3333B2), secondary (#0066CC), accent (#FF7F0E), success (#2CA02C), danger (#D62728)

---

## Work Objectives

### Core Objective
Comprehensive quality audit of all 12 presentations ensuring template compliance, content completeness, and chart functionality.

### Deliverables
1. **Template Compliance Report** - Per-presentation checklist of template adherence
2. **Content Audit Report** - Slide counts, PMSP structure, chart references, learning objectives
3. **Chart Compilation Report** - Execution status of all 51 chart.py scripts with PDF verification
4. **Per-Presentation Inventories** - JSON files at `.omc/inventories/L0X_{overview|deepdive}.json`

### Definition of Done
- All 12 .tex files validated against template requirements
- All PMSP sections identified and documented
- All 51 chart.py scripts executed successfully with PDF output verified
- 12 JSON inventory files created in `.omc/inventories/`
- Summary report generated at `.omc/reports/ultradeep_review.md`

---

## Must Have / Must NOT Have

### Must Have
- Exact RGB color value verification (not just color name presence)
- Frame count verification (frame environments, not just \begin{frame})
- Chart reference validation (verify referenced PDFs exist)
- Finance use case identification in each presentation
- Learning objectives extraction from overview presentations

### Must NOT Have
- Modification of any .tex files (read-only audit)
- Modification of any chart.py files
- Re-generation of charts if they already exist and are valid
- LaTeX compilation (just source analysis, unless explicitly needed)

---

## Task Flow and Dependencies

```
PHASE 1: Template Compliance (Parallel - 6 topics)
   |
   +-> Task 1.1: L01 template check
   +-> Task 1.2: L02 template check
   +-> Task 1.3: L03 template check
   +-> Task 1.4: L04 template check
   +-> Task 1.5: L05 template check
   +-> Task 1.6: L06 template check
   |
   v
PHASE 2: Content Review (Parallel - 12 presentations)
   |
   +-> Task 2.1-2.6: Overview presentations (extract learning objectives, slide counts)
   +-> Task 2.7-2.12: Deepdive presentations (verify PMSP, chart refs)
   |
   v
PHASE 3: Chart Compilation (Parallel - 6 batches by topic)
   |
   +-> Task 3.1: L01 charts (8 scripts)
   +-> Task 3.2: L02 charts (7 scripts)
   +-> Task 3.3: L03 charts (7 scripts)
   +-> Task 3.4: L04 charts (8 scripts)
   +-> Task 3.5: L05 charts (11 scripts)
   +-> Task 3.6: L06 charts (7 scripts)
   |
   v
PHASE 4: Inventory Generation (Sequential)
   |
   +-> Task 4.1: Generate 12 JSON inventory files
   +-> Task 4.2: Generate summary report
```

---

## Detailed TODOs

### PHASE 1: Template Compliance Verification

#### Task 1.1-1.6: Per-Topic Template Check
**Executor**: architect-low (haiku) - 6 parallel agents
**Files**: All .tex files in each topic folder

**Checklist to verify in each .tex file:**
```
[ ] Document class: \documentclass[8pt,aspectratio=169]{beamer}
[ ] Theme: \usetheme{Madrid}
[ ] Color definitions present:
    [ ] MLPurple: RGB{51,51,178}
    [ ] MLBlue: RGB{0,102,204}
    [ ] MLOrange: RGB{255,127,14}
    [ ] MLGreen: RGB{44,160,44}
    [ ] MLRed: RGB{214,39,40}
[ ] Footer template with three beamercolorboxes
[ ] Navigation symbols disabled: \setbeamertemplate{navigation symbols}{}
[ ] Custom commands: \bottomnote, \highlight
[ ] Title/author metadata set correctly
[ ] Date: Spring 2026
```

**Acceptance Criteria:**
- Each item marked PASS/FAIL with line number reference
- List any deviations from template

---

### PHASE 2: Content Review

#### Task 2.1-2.6: Overview Presentations
**Executor**: explore (haiku) - 6 parallel agents
**Target**: L01-L06 `*_overview.tex`

**Extract and verify:**
```
[ ] Frame count (target: ~17, acceptable: 15-22)
[ ] Learning objectives slide present
[ ] Learning objectives text extracted
[ ] Finance use case slide present
[ ] Finance use case text extracted
[ ] PMSP sections identified:
    [ ] Problem section
    [ ] Method section
    [ ] Solution section
    [ ] Practice section (or Hands-on)
    [ ] Decision Framework section
    [ ] Summary section
[ ] Chart references (list all \includegraphics paths)
[ ] Key Takeaways slide present
[ ] References slide present
```

**Acceptance Criteria:**
- JSON output with all extracted data
- Flag any missing PMSP sections
- Verify chart paths exist on disk

#### Task 2.7-2.12: Deepdive Presentations
**Executor**: explore (haiku) - 6 parallel agents
**Target**: L01-L06 `*_deepdive.tex`

**Extract and verify:**
```
[ ] Frame count (target: ~30, acceptable: 25-40)
[ ] Section structure (list all \section{} titles)
[ ] Mathematical content present (equations, align environments)
[ ] Chart references (list all \includegraphics paths)
[ ] Summary slides present
[ ] References slide present
[ ] "Next Session" reference present
```

**Acceptance Criteria:**
- JSON output with all extracted data
- Cross-reference chart paths with Phase 3 results

---

### PHASE 3: Chart Compilation Verification

#### Task 3.1-3.6: Per-Topic Chart Compilation
**Executor**: executor (sonnet) - 6 parallel agents
**Method**: Execute each chart.py and verify PDF output

**Per-chart verification:**
```python
# For each chart.py:
1. Check chart.py exists
2. Execute: python chart.py
3. Verify chart.pdf exists
4. Verify chart.pdf size > 0 bytes
5. Record execution time
6. Capture any warnings/errors
```

**Charts per topic:**
| Topic | Charts | IDs |
|-------|--------|-----|
| L01 | 8 | 01-08 (decision_flowchart) |
| L02 | 7 | 01-07 |
| L03 | 7 | 01-07 |
| L04 | 8 | 01-07 + 06a/06b |
| L05 | 11 | 01-07 + 04a/04b/04c, 05a/05b, 06a/06b/06c |
| L06 | 7 | 01-07 |

**Absolute paths for chart.py files:**
```
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\01_simple_regression\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\02_multiple_regression_3d\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\03_residual_plots\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\04_gradient_descent\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\05_learning_curves\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\06_regularization_comparison\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\07_bias_variance\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\08_decision_flowchart\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L02_Logistic_Regression\01_sigmoid_function\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L02_Logistic_Regression\02_decision_boundary\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L02_Logistic_Regression\03_log_loss\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L02_Logistic_Regression\04_roc_curve\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L02_Logistic_Regression\05_precision_recall\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L02_Logistic_Regression\06_confusion_matrix\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L02_Logistic_Regression\07_decision_flowchart\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L03_KNN_KMeans\01_knn_boundaries\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L03_KNN_KMeans\02_distance_metrics\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L03_KNN_KMeans\03_kmeans_iteration\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L03_KNN_KMeans\04_elbow_method\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L03_KNN_KMeans\05_silhouette\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L03_KNN_KMeans\06_voronoi\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L03_KNN_KMeans\07_decision_flowchart\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L04_Random_Forests\01_decision_tree\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L04_Random_Forests\02_feature_importance\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L04_Random_Forests\03_bootstrap\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L04_Random_Forests\04_oob_error\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L04_Random_Forests\05_ensemble_voting\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L04_Random_Forests\06a_single_tree_variance\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L04_Random_Forests\06b_random_forest_variance\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L04_Random_Forests\07_decision_flowchart\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\01_scree_plot\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\02_principal_components\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\03_reconstruction\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\04a_tsne_perplexity_5\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\04b_tsne_perplexity_30\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\04c_tsne_perplexity_100\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\05a_pca_swiss_roll\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\05b_tsne_swiss_roll\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\06a_original_clusters\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\06b_pca_cluster_projection\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\06c_tsne_cluster_projection\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\07_decision_flowchart\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L06_Embeddings_RL\01_word_embedding_space\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L06_Embeddings_RL\02_similarity_heatmap\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L06_Embeddings_RL\03_rl_loop\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L06_Embeddings_RL\04_q_learning_grid\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L06_Embeddings_RL\05_reward_curves\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L06_Embeddings_RL\06_policy_viz\chart.py
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L06_Embeddings_RL\07_decision_flowchart\chart.py
```

**Command to execute:**
```bash
python "D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\01_simple_regression\chart.py"
```

**Acceptance Criteria:**
- All 51 chart.py scripts execute without error
- All 51 chart.pdf files exist with size > 0
- Execution log with timestamps

---

### PHASE 4: Inventory Generation

#### Task 4.1: Generate JSON Inventories
**Executor**: executor (sonnet)
**Output**: `.omc/inventories/` directory with 12 JSON files

**JSON Schema per presentation:**
```json
{
  "presentation_id": "L01_overview",
  "topic_id": "L01",
  "topic_title": "Introduction & Linear Regression",
  "type": "overview",
  "file_path": "slides/L01_Introduction_Linear_Regression/L01_overview.tex",
  "audit_timestamp": "2026-01-28T...",
  "template_compliance": {
    "document_class": true,
    "theme_madrid": true,
    "colors_defined": true,
    "footer_correct": true,
    "commands_defined": true
  },
  "content": {
    "frame_count": 17,
    "sections": ["Learning Objectives", "The Business Problem", ...],
    "pmsp_coverage": {
      "problem": true,
      "method": true,
      "solution": true,
      "practice": true,
      "decision_framework": true,
      "summary": true
    },
    "learning_objectives": [
      "Understand the ordinary least squares (OLS) framework",
      "Apply gradient descent for parameter optimization",
      "Interpret regression coefficients in business contexts"
    ],
    "finance_use_case": "House price prediction, factor models"
  },
  "charts": {
    "referenced": [
      "01_simple_regression/chart.pdf",
      "02_multiple_regression_3d/chart.pdf",
      ...
    ],
    "all_exist": true,
    "missing": []
  },
  "issues": []
}
```

**Inventory files to create:**
```
.omc/inventories/L01_overview.json
.omc/inventories/L01_deepdive.json
.omc/inventories/L02_overview.json
.omc/inventories/L02_deepdive.json
.omc/inventories/L03_overview.json
.omc/inventories/L03_deepdive.json
.omc/inventories/L04_overview.json
.omc/inventories/L04_deepdive.json
.omc/inventories/L05_overview.json
.omc/inventories/L05_deepdive.json
.omc/inventories/L06_overview.json
.omc/inventories/L06_deepdive.json
```

#### Task 4.2: Generate Summary Report
**Executor**: writer (haiku)
**Output**: `.omc/reports/ultradeep_review.md`

**Report structure:**
```markdown
# Ultra-Deep Presentation Review Report

Generated: 2026-01-28

## Executive Summary
- Total presentations: 12
- Template compliant: X/12
- Charts compiled: X/51
- Issues found: N

## Per-Topic Summary
| Topic | Overview | Deepdive | Charts | Issues |
|-------|----------|----------|--------|--------|
| L01   | PASS     | PASS     | 8/8    | 0      |
...

## Detailed Findings
### L01: Introduction & Linear Regression
- Overview: 17 frames, all PMSP sections present
- Deepdive: 30 frames, 6 sections
- Charts: 8/8 compiled successfully

[continues for all topics]

## Issues Summary
[list any issues found]

## Recommendations
[any suggested improvements]
```

---

## Commit Strategy

This is a read-only audit plan. No commits expected unless:
1. Inventory JSON files are new (commit to `.omc/inventories/`)
2. Reports are generated (commit to `.omc/reports/`)

**Commit message template:**
```
Add ultra-deep presentation review inventories and report

- Generate 12 per-presentation JSON inventory files
- Create comprehensive review report
- Verify 51 chart compilations

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

---

## Success Criteria

| Criterion | Target | Verification Method |
|-----------|--------|---------------------|
| Template compliance | 12/12 presentations | JSON inventories |
| PMSP coverage | All sections in all presentations | Content extraction |
| Chart compilation | 51/51 scripts pass | Execution + PDF check |
| Inventory files | 12 JSON files created | File existence |
| Summary report | 1 MD file created | File existence |
| Zero blocking issues | No critical failures | Issue count in report |

---

## Execution Notes

### Parallel Execution Strategy
- Phase 1 (Template): 6 parallel agents (one per topic)
- Phase 2 (Content): 12 parallel agents (one per presentation)
- Phase 3 (Charts): 6 parallel agents (one per topic, each handling 7-11 charts sequentially)
- Phase 4 (Inventory): Sequential (depends on Phase 1-3 results)

### Error Handling
- If a chart.py fails: Log error, continue with next chart, mark in inventory
- If a .tex file is missing: Log as critical issue, continue with others
- If a chart.pdf is missing after execution: Mark as FAIL in inventory

### Existing Infrastructure
Use existing validators where possible:
- `infrastructure/validators/latex_validator.py` - For compilation checks
- `infrastructure/validators/chart_validator.py` - For chart execution
- `infrastructure/auditors/audit_system.py` - For report generation patterns

---

## File Paths Reference

### Input Files (Read-Only)
```
D:\Joerg\Research\slides\Methods_and_Algorithms\templates\beamer_template.tex
D:\Joerg\Research\slides\Methods_and_Algorithms\templates\chart_template.py
D:\Joerg\Research\slides\Methods_and_Algorithms\manifest.json
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L0X_*\L0X_overview.tex
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L0X_*\L0X_deepdive.tex
D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L0X_*\*\chart.py
```

### Output Files (Write)
```
D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\inventories\L01_overview.json
D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\inventories\L01_deepdive.json
D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\inventories\L02_overview.json
D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\inventories\L02_deepdive.json
D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\inventories\L03_overview.json
D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\inventories\L03_deepdive.json
D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\inventories\L04_overview.json
D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\inventories\L04_deepdive.json
D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\inventories\L05_overview.json
D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\inventories\L05_deepdive.json
D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\inventories\L06_overview.json
D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\inventories\L06_deepdive.json
D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\reports\ultradeep_review.md
```
