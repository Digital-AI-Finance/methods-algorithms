# Ultra Deep Presentation Review Plan

## Context

### Original Request
Ultra deep review of each presentation. Follow beamer template. Check content. Check charts compile. Create inventory for each presentation as JSON.

### Course Structure
- **Course**: Methods and Algorithms - MSc Data Science
- **Topics**: 6 lectures (L01-L06)
- **Presentations per topic**: 2 (overview ~17 slides, deepdive ~30 slides)
- **Total .tex files**: 12
- **Total chart.py files**: 51

### Beamer Template Requirements
| Requirement | Specification |
|-------------|---------------|
| Document class | `\documentclass[8pt,aspectratio=169]{beamer}` |
| Theme | Madrid with default color theme |
| Colors | MLPurple (#3333B2), MLBlue (#0066CC), MLOrange (#FF7F0E), MLGreen (#2CA02C), MLRed (#D62728) |
| Chart widths | 0.55\textwidth (with text) or 0.65\textwidth (chart-only) |
| Bullets | Max 3-4 per slide |
| Overflow | ZERO warnings allowed |
| Footer | Methods and Algorithms | MSc Data Science | Page X / Y |

### Chart Template Requirements
| Requirement | Specification |
|-------------|---------------|
| Figure size | figsize=(10, 6) |
| Output | chart.pdf in same directory |
| Font size | 14pt base, scaled for Beamer |
| Colors | Same ML palette as slides |
| URL | GitHub URL in bottom-right corner |

---

## Work Objectives

### Core Objective
Perform comprehensive audit of all 12 .tex files and 51 chart.py files, validating template compliance, content quality, and chart compilation. Generate JSON inventory per presentation.

### Deliverables
1. **Content Audit Report** - Per-file validation of template compliance
2. **Chart Compilation Report** - Verification that all 51 charts compile
3. **JSON Inventories** - 12 inventory files (one per .tex file)
4. **Issue Summary** - Consolidated list of all issues found

### Definition of Done
- [ ] All 12 .tex files reviewed against beamer template
- [ ] All 51 chart.py files executed successfully
- [ ] All 12 JSON inventories created
- [ ] Zero critical issues remaining
- [ ] Final summary report generated

---

## Guardrails

### Must Have
- Verify document class matches template exactly
- Check all 5 ML colors are defined correctly
- Validate chart width specifications
- Confirm no overflow warnings when compiled
- Verify all referenced chart.pdf files exist
- Run each chart.py and confirm it produces chart.pdf

### Must NOT Have
- Skip any .tex file
- Skip any chart.py file
- Modify source files during review (read-only audit)
- Accept overflow warnings as acceptable
- Approve missing chart.pdf references

---

## JSON Inventory Schema

```json
{
  "presentation": {
    "id": "L01_overview",
    "topic": "L01",
    "type": "overview|deepdive",
    "file": "slides/L01_Introduction_Linear_Regression/L01_overview.tex",
    "title": "Introduction & Linear Regression",
    "subtitle": "Overview"
  },
  "template_compliance": {
    "document_class_correct": true,
    "theme_correct": true,
    "colors_defined": ["MLPurple", "MLBlue", "MLOrange", "MLGreen", "MLRed"],
    "footer_configured": true,
    "navigation_symbols_removed": true
  },
  "content_metrics": {
    "total_frames": 18,
    "frames_with_charts": 8,
    "frames_with_equations": 4,
    "frames_with_columns": 2,
    "max_bullets_per_slide": 4,
    "overflow_warnings": 0
  },
  "charts": [
    {
      "id": "01_simple_regression",
      "folder": "01_simple_regression",
      "chart_py_exists": true,
      "chart_pdf_exists": true,
      "chart_py_compiles": true,
      "width_used": "0.50\\textwidth",
      "frame_title": "Simple Linear Regression"
    }
  ],
  "sections": [
    "Learning Objectives",
    "The Business Problem",
    "Method",
    "Decision Framework",
    "Key Takeaways"
  ],
  "issues": [
    {
      "severity": "warning|error|info",
      "type": "overflow|missing_chart|width_violation|etc",
      "location": "frame N",
      "description": "Description of the issue"
    }
  ],
  "audit_timestamp": "2026-01-28T12:00:00Z"
}
```

---

## Task Flow

```
Phase 1: Template Compliance Check (12 tasks)
    |
    v
Phase 2: Chart Compilation (51 tasks, parallelizable by topic)
    |
    v
Phase 3: Content Analysis (12 tasks)
    |
    v
Phase 4: JSON Inventory Generation (12 tasks)
    |
    v
Phase 5: Consolidation & Summary Report
```

---

## Detailed Tasks

### Phase 1: Template Compliance Check

| Task ID | File | Acceptance Criteria |
|---------|------|---------------------|
| T1.01 | `L01_overview.tex` | Document class = `[8pt,aspectratio=169]{beamer}`, theme = Madrid, all 5 colors defined, footer configured |
| T1.02 | `L01_deepdive.tex` | Same criteria as T1.01 |
| T1.03 | `L02_overview.tex` | Same criteria as T1.01 |
| T1.04 | `L02_deepdive.tex` | Same criteria as T1.01 |
| T1.05 | `L03_overview.tex` | Same criteria as T1.01 |
| T1.06 | `L03_deepdive.tex` | Same criteria as T1.01 |
| T1.07 | `L04_overview.tex` | Same criteria as T1.01 |
| T1.08 | `L04_deepdive.tex` | Same criteria as T1.01 |
| T1.09 | `L05_overview.tex` | Same criteria as T1.01 |
| T1.10 | `L05_deepdive.tex` | Same criteria as T1.01 |
| T1.11 | `L06_overview.tex` | Same criteria as T1.01 |
| T1.12 | `L06_deepdive.tex` | Same criteria as T1.01 |

### Phase 2: Chart Compilation

Execute all chart.py files and verify chart.pdf output.

**L01 Charts (8 files)**
| Task ID | Chart | Path |
|---------|-------|------|
| T2.01 | 01_simple_regression | `slides/L01_Introduction_Linear_Regression/01_simple_regression/chart.py` |
| T2.02 | 02_multiple_regression_3d | `slides/L01_Introduction_Linear_Regression/02_multiple_regression_3d/chart.py` |
| T2.03 | 03_residual_plots | `slides/L01_Introduction_Linear_Regression/03_residual_plots/chart.py` |
| T2.04 | 04_gradient_descent | `slides/L01_Introduction_Linear_Regression/04_gradient_descent/chart.py` |
| T2.05 | 05_learning_curves | `slides/L01_Introduction_Linear_Regression/05_learning_curves/chart.py` |
| T2.06 | 06_regularization_comparison | `slides/L01_Introduction_Linear_Regression/06_regularization_comparison/chart.py` |
| T2.07 | 07_bias_variance | `slides/L01_Introduction_Linear_Regression/07_bias_variance/chart.py` |
| T2.08 | 08_decision_flowchart | `slides/L01_Introduction_Linear_Regression/08_decision_flowchart/chart.py` |

**L02 Charts (7 files)**
| Task ID | Chart | Path |
|---------|-------|------|
| T2.09 | 01_sigmoid_function | `slides/L02_Logistic_Regression/01_sigmoid_function/chart.py` |
| T2.10 | 02_decision_boundary | `slides/L02_Logistic_Regression/02_decision_boundary/chart.py` |
| T2.11 | 03_log_loss | `slides/L02_Logistic_Regression/03_log_loss/chart.py` |
| T2.12 | 04_roc_curve | `slides/L02_Logistic_Regression/04_roc_curve/chart.py` |
| T2.13 | 05_precision_recall | `slides/L02_Logistic_Regression/05_precision_recall/chart.py` |
| T2.14 | 06_confusion_matrix | `slides/L02_Logistic_Regression/06_confusion_matrix/chart.py` |
| T2.15 | 07_decision_flowchart | `slides/L02_Logistic_Regression/07_decision_flowchart/chart.py` |

**L03 Charts (7 files)**
| Task ID | Chart | Path |
|---------|-------|------|
| T2.16 | 01_knn_boundaries | `slides/L03_KNN_KMeans/01_knn_boundaries/chart.py` |
| T2.17 | 02_distance_metrics | `slides/L03_KNN_KMeans/02_distance_metrics/chart.py` |
| T2.18 | 03_kmeans_iteration | `slides/L03_KNN_KMeans/03_kmeans_iteration/chart.py` |
| T2.19 | 04_elbow_method | `slides/L03_KNN_KMeans/04_elbow_method/chart.py` |
| T2.20 | 05_silhouette | `slides/L03_KNN_KMeans/05_silhouette/chart.py` |
| T2.21 | 06_voronoi | `slides/L03_KNN_KMeans/06_voronoi/chart.py` |
| T2.22 | 07_decision_flowchart | `slides/L03_KNN_KMeans/07_decision_flowchart/chart.py` |

**L04 Charts (8 files)**
| Task ID | Chart | Path |
|---------|-------|------|
| T2.23 | 01_decision_tree | `slides/L04_Random_Forests/01_decision_tree/chart.py` |
| T2.24 | 02_feature_importance | `slides/L04_Random_Forests/02_feature_importance/chart.py` |
| T2.25 | 03_bootstrap | `slides/L04_Random_Forests/03_bootstrap/chart.py` |
| T2.26 | 04_oob_error | `slides/L04_Random_Forests/04_oob_error/chart.py` |
| T2.27 | 05_ensemble_voting | `slides/L04_Random_Forests/05_ensemble_voting/chart.py` |
| T2.28 | 06a_single_tree_variance | `slides/L04_Random_Forests/06a_single_tree_variance/chart.py` |
| T2.29 | 06b_random_forest_variance | `slides/L04_Random_Forests/06b_random_forest_variance/chart.py` |
| T2.30 | 07_decision_flowchart | `slides/L04_Random_Forests/07_decision_flowchart/chart.py` |

**L05 Charts (12 files)**
| Task ID | Chart | Path |
|---------|-------|------|
| T2.31 | 01_scree_plot | `slides/L05_PCA_tSNE/01_scree_plot/chart.py` |
| T2.32 | 02_principal_components | `slides/L05_PCA_tSNE/02_principal_components/chart.py` |
| T2.33 | 03_reconstruction | `slides/L05_PCA_tSNE/03_reconstruction/chart.py` |
| T2.34 | 04a_tsne_perplexity_5 | `slides/L05_PCA_tSNE/04a_tsne_perplexity_5/chart.py` |
| T2.35 | 04b_tsne_perplexity_30 | `slides/L05_PCA_tSNE/04b_tsne_perplexity_30/chart.py` |
| T2.36 | 04c_tsne_perplexity_100 | `slides/L05_PCA_tSNE/04c_tsne_perplexity_100/chart.py` |
| T2.37 | 05a_pca_swiss_roll | `slides/L05_PCA_tSNE/05a_pca_swiss_roll/chart.py` |
| T2.38 | 05b_tsne_swiss_roll | `slides/L05_PCA_tSNE/05b_tsne_swiss_roll/chart.py` |
| T2.39 | 06a_original_clusters | `slides/L05_PCA_tSNE/06a_original_clusters/chart.py` |
| T2.40 | 06b_pca_cluster_projection | `slides/L05_PCA_tSNE/06b_pca_cluster_projection/chart.py` |
| T2.41 | 06c_tsne_cluster_projection | `slides/L05_PCA_tSNE/06c_tsne_cluster_projection/chart.py` |
| T2.42 | 07_decision_flowchart | `slides/L05_PCA_tSNE/07_decision_flowchart/chart.py` |

**L06 Charts (7 files)**
| Task ID | Chart | Path |
|---------|-------|------|
| T2.43 | 01_word_embedding_space | `slides/L06_Embeddings_RL/01_word_embedding_space/chart.py` |
| T2.44 | 02_similarity_heatmap | `slides/L06_Embeddings_RL/02_similarity_heatmap/chart.py` |
| T2.45 | 03_rl_loop | `slides/L06_Embeddings_RL/03_rl_loop/chart.py` |
| T2.46 | 04_q_learning_grid | `slides/L06_Embeddings_RL/04_q_learning_grid/chart.py` |
| T2.47 | 05_reward_curves | `slides/L06_Embeddings_RL/05_reward_curves/chart.py` |
| T2.48 | 06_policy_viz | `slides/L06_Embeddings_RL/06_policy_viz/chart.py` |
| T2.49 | 07_decision_flowchart | `slides/L06_Embeddings_RL/07_decision_flowchart/chart.py` |

### Phase 3: Content Analysis

For each .tex file, analyze:

| Task ID | File | Analysis Items |
|---------|------|----------------|
| T3.01-T3.12 | All .tex files | Count frames, count chart inclusions, verify chart references exist, check bullet counts, extract sections, identify potential overflow issues |

### Phase 4: JSON Inventory Generation

| Task ID | Output File | Source Files |
|---------|-------------|--------------|
| T4.01 | `.omc/inventories/L01_overview.json` | L01_overview.tex + L01 charts |
| T4.02 | `.omc/inventories/L01_deepdive.json` | L01_deepdive.tex + L01 charts |
| T4.03 | `.omc/inventories/L02_overview.json` | L02_overview.tex + L02 charts |
| T4.04 | `.omc/inventories/L02_deepdive.json` | L02_deepdive.tex + L02 charts |
| T4.05 | `.omc/inventories/L03_overview.json` | L03_overview.tex + L03 charts |
| T4.06 | `.omc/inventories/L03_deepdive.json` | L03_deepdive.tex + L03 charts |
| T4.07 | `.omc/inventories/L04_overview.json` | L04_overview.tex + L04 charts |
| T4.08 | `.omc/inventories/L04_deepdive.json` | L04_deepdive.tex + L04 charts |
| T4.09 | `.omc/inventories/L05_overview.json` | L05_overview.tex + L05 charts |
| T4.10 | `.omc/inventories/L05_deepdive.json` | L05_deepdive.tex + L05 charts |
| T4.11 | `.omc/inventories/L06_overview.json` | L06_overview.tex + L06 charts |
| T4.12 | `.omc/inventories/L06_deepdive.json` | L06_deepdive.tex + L06 charts |

### Phase 5: Consolidation

| Task ID | Description | Output |
|---------|-------------|--------|
| T5.01 | Aggregate all issues from inventories | `.omc/reports/issues_summary.md` |
| T5.02 | Generate chart compilation report | `.omc/reports/chart_compilation.md` |
| T5.03 | Generate final audit summary | `.omc/reports/audit_summary.md` |

---

## Commit Strategy

### Commit 1: Create inventory structure
```
feat(audit): initialize presentation review infrastructure

- Create .omc/inventories directory
- Create .omc/reports directory
```

### Commit 2: Generate inventories (batch by topic)
```
feat(audit): generate L01-L03 presentation inventories

- L01_overview.json, L01_deepdive.json
- L02_overview.json, L02_deepdive.json
- L03_overview.json, L03_deepdive.json
```

### Commit 3: Generate remaining inventories
```
feat(audit): generate L04-L06 presentation inventories

- L04_overview.json, L04_deepdive.json
- L05_overview.json, L05_deepdive.json
- L06_overview.json, L06_deepdive.json
```

### Commit 4: Generate summary reports
```
feat(audit): generate audit summary reports

- issues_summary.md
- chart_compilation.md
- audit_summary.md
```

---

## Success Criteria

| Criterion | Metric | Target |
|-----------|--------|--------|
| Template compliance | All 12 .tex files pass | 100% |
| Chart compilation | All 51 charts produce PDF | 100% |
| Inventory generation | All 12 JSON files created | 100% |
| Issue documentation | All issues catalogued | 100% |
| Critical issues | Must be zero | 0 |

---

## File References

### .tex Files (12 total)
```
slides/L01_Introduction_Linear_Regression/L01_overview.tex
slides/L01_Introduction_Linear_Regression/L01_deepdive.tex
slides/L02_Logistic_Regression/L02_overview.tex
slides/L02_Logistic_Regression/L02_deepdive.tex
slides/L03_KNN_KMeans/L03_overview.tex
slides/L03_KNN_KMeans/L03_deepdive.tex
slides/L04_Random_Forests/L04_overview.tex
slides/L04_Random_Forests/L04_deepdive.tex
slides/L05_PCA_tSNE/L05_overview.tex
slides/L05_PCA_tSNE/L05_deepdive.tex
slides/L06_Embeddings_RL/L06_overview.tex
slides/L06_Embeddings_RL/L06_deepdive.tex
```

### Template Files
```
templates/beamer_template.tex
templates/chart_template.py
```

### Output Directories
```
.omc/inventories/  - JSON inventory files
.omc/reports/      - Summary reports
```

---

## Execution Notes

1. **Parallelization**: Phase 2 (chart compilation) can run in parallel by topic
2. **Dependencies**: Phase 3 depends on Phase 2 (need chart.pdf existence info)
3. **Tool Usage**: Use CLI commands where available:
   - `python infrastructure/course_cli.py build charts --topic LXX`
   - `python infrastructure/course_cli.py validate latex --strict`
4. **Error Handling**: Log all errors but continue processing to get full picture
