# Work Plan: Comprehensive Content Inventory & Gap Analysis

## Context

**Original Request:** Create a complete inventory of all course assets, verify existence on disk, cross-reference against manifest.json, and produce a gap analysis.

**Repository:** MSc Data Science - Methods and Algorithms (6 topics, L01-L06)

**Research Findings:**
- All 6 topic folders exist: L01_Introduction_Linear_Regression through L06_Embeddings_RL
- manifest.json tracks all 6 topics, 3 quizzes, and supporting assets - all marked "complete"
- Disk shows some assets NOT tracked in manifest (e.g., L04 has `06_bias_variance` folder not in manifest; L05 has `04_tsne_perplexity` and `05_pca_vs_tsne` parent folders not in manifest but sub-variants are)
- L06 has no `images/` folder unlike L01-L05
- Several `nul` files scattered (Windows artifact)
- Aux/log files not cleaned up in L02, L04

## Work Objectives

**Core Objective:** Produce a verified inventory of every asset with existence status and manifest tracking status.

**Deliverables:**
1. Per-topic asset inventory report (markdown)
2. Manifest accuracy report (mismatches between manifest and disk)
3. Gap analysis with actionable items

**Definition of Done:**
- Every expected asset type checked for all 6 topics
- Every manifest entry verified against disk
- Every disk asset checked for manifest tracking
- Report saved to `D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\reports\content-inventory-report.md`

## Guardrails

**Must Have:**
- Check all asset types: overview.tex, deepdive.tex, chart folders (chart.py + chart.pdf), instructor_guide.md, notebook, dataset
- Check quizzes, templates, infrastructure, capstone, rubrics, docs
- Verify chart.pdf exists alongside each chart.py
- Cross-reference manifest.json entries bidirectionally

**Must NOT Have:**
- Do NOT modify any source files
- Do NOT modify manifest.json (report only)
- Do NOT run chart.py scripts or compile LaTeX

## Task Flow

```
T1 (enumerate expected) --> T2 (verify disk) --> T3 (cross-ref manifest) --> T4 (report)
```

All tasks are sequential; each depends on the prior.

## Detailed Tasks

### T1: Enumerate Expected Assets Per Topic
**Agent:** explore
**Accept:** Complete list of expected assets per topic based on manifest.json and CLAUDE.md spec

Steps:
1. Parse manifest.json to extract all declared assets per topic
2. For each topic (L01-L06), list: overview_slides, deepdive_slides, charts[], notebook, dataset, instructor_guide
3. List quizzes, templates, infrastructure modules, capstone, rubrics, docs assets
4. Output structured checklist

### T2: Verify Each Asset Exists on Disk
**Agent:** explore-medium
**Accept:** Every expected file checked with exists/missing status

Steps:
1. For each file path in manifest.json, check if file exists on disk
2. For each chart entry, verify BOTH chart.py AND chart.pdf exist
3. For each .tex file, check if compiled .pdf exists
4. Scan each topic folder for files/folders NOT referenced in manifest (untracked assets)
5. Check supporting directories: templates/ (5 files), infrastructure/ (CLI + submodules), quizzes/ (3 XML), capstone/, rubrics/, docs/

Known items to verify specifically:
- L04: `06_bias_variance/` folder exists on disk but NOT in manifest (manifest has 06a_ and 06b_ instead)
- L05: `04_tsne_perplexity/` and `05_pca_vs_tsne/` and `06_cluster_preservation/` parent folders exist on disk but manifest only tracks sub-variants (04a/04b/04c, 05a/05b, 06a/06b/06c)
- L06: No `images/` folder (L01-L05 all have one)
- `nul` files in root, L01, L03 slide folders (Windows artifacts, should be cleaned)

### T3: Cross-Reference Manifest Against Disk
**Agent:** architect-low
**Accept:** Bidirectional diff: (1) manifest entries missing from disk, (2) disk assets missing from manifest

Steps:
1. For every manifest file path, confirm existence -> flag missing
2. For every numbered chart folder on disk, confirm manifest entry -> flag untracked
3. Check manifest status fields: are any marked "complete" but missing on disk?
4. Check for assets on disk that should be tracked but are not (e.g., compiled PDFs, images/ folders)
5. Identify naming inconsistencies (e.g., L04 `06_bias_variance` vs manifest `06a_`/`06b_`)

### T4: Produce Gap Analysis Report
**Agent:** writer
**Accept:** Markdown report at `.omc/reports/content-inventory-report.md`

Report sections:
1. **Executive Summary** - Overall completeness percentage, total assets counted
2. **Per-Topic Inventory Table** - Asset type x topic grid with status icons
3. **Manifest Accuracy** - List of discrepancies (untracked, missing, status mismatches)
4. **Untracked Assets** - Files on disk not in manifest
5. **Missing Assets** - Manifest entries not found on disk
6. **Cleanup Recommendations** - nul files, aux files, naming inconsistencies
7. **Action Items** - Prioritized list of fixes

## Commit Strategy

No commits needed - this is a read-only audit producing a report file.

## Success Criteria

- [ ] All 6 topics fully inventoried
- [ ] All manifest entries verified against disk
- [ ] All disk assets checked for manifest tracking
- [ ] Gap analysis report generated with actionable items
- [ ] Zero false positives in the report
