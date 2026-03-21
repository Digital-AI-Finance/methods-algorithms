<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-03-21 | Updated: 2026-03-21 -->

# tools/

**Parent**: [../AGENTS.md](../AGENTS.md) (Methods_and_Algorithms root)

## Purpose

Utility scripts for batch maintenance and patching of course materials. Currently focused on migrating chart.py files to use the shared `chart_style.py` module.

## Key Files

| File | Description |
|------|-------------|
| `patch_charts.py` | Batch-patches all chart.py files under `slides/` to import from `templates/chart_style.py`, removes inline rcParams blocks and ML color constant definitions, and ensures `savefig` calls include `facecolor='white'` and `bbox_inches='tight'` |

## For AI Agents

### Working In This Directory

- **Dry-run by default**: `python tools/patch_charts.py` previews changes without modifying files
- **Apply patches**: `python tools/patch_charts.py --apply` patches files and creates `.bak` backups
- **No backup**: `python tools/patch_charts.py --apply --no-backup` patches without backups
- Run from the **project root**, not from within `tools/`
- After patching, rebuild charts to verify: `python infrastructure/course_cli.py build charts --topic all`

### What patch_charts.py Does

1. Inserts the `chart_style` import block at the top of each chart.py
2. Removes inline `plt.rcParams.update({...})` blocks
3. Removes individual ML color constant lines (`MLPURPLE = '#...'`, etc.)
4. Ensures `savefig` calls include `facecolor='white'` and `bbox_inches='tight'`

### When to Use

- After adding new charts that still use old inline styling
- When `chart_style.py` is updated and existing charts need to be re-synced
- As a one-time migration tool when the shared style module was introduced (Mar 2026)
