# Prompt: /ralph all — Chart Quality Overhaul Execution

## Request
Execute the Critic-approved plan at `.omc/plans/chart-quality-overhaul.md` to upgrade all 162 charts to textbook-quality styling.

## Action
- Created shared style module + batch patch script (T1+T2)
- Patched 162 charts, fixed 14 edge cases (try-block imports, mid-file imports)
- Added grid suppression to 12 heatmap/diagram charts + 4 twinx charts
- Regenerated all 162 PDFs, updated docs
- Architect verified: APPROVED on all 10 criteria

## Outcome
162/162 charts upgraded. Shared style module at `templates/chart_style.py`.
