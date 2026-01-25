# Infrastructure Module - Course Management System

<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 -->

## Purpose

Python-based CLI infrastructure for managing the Methods and Algorithms course. Provides automated building, validation, reporting, and deployment of course materials (slides, charts, notebooks, quizzes).

**Central Entry Point:** `course_cli.py` - Command-line interface that orchestrates all subsystems.

## Key Files

| File | Purpose | Lines | Key Functions |
|------|---------|-------|---------------|
| `course_cli.py` | Main CLI entry point | 220 | `cmd_build()`, `cmd_validate()`, `cmd_status()`, `cmd_inventory()`, `cmd_report()` |

## Subdirectories

| Directory | Purpose | Module Count | Key Modules |
|-----------|---------|--------------|-------------|
| `validators/` | Content validation (LaTeX, links, notebooks, charts) | 5 | latex_validator, chart_validator, link_validator, notebook_validator |
| `builders/` | Content generation (slides, charts, notebooks, quizzes) | 5 | slide_builder, chart_builder, notebook_builder, quiz_builder |
| `reporters/` | Progress and quality reporting | 6 | progress_report, html_dashboard, build_report, coverage_report, quality_report |
| `auditors/` | Full course audit system | 3 | audit_system, report_generator |
| `generators/` | Generate syllabus, rubrics, guides | 3 | syllabus_generator, rubric_generator, guide_generator |
| `deployers/` | Deploy to GitHub/Colab | 2 | github_deployer, colab_deployer |
| `utils/` | Utility modules | 3 | retry_strategy, hash_utils |

## For AI Agents

### Working with the Infrastructure

The infrastructure follows a **hub-and-spoke pattern** where `course_cli.py` acts as the central orchestrator:

```
course_cli.py
    ├── validators/ (check content integrity)
    ├── builders/ (generate content)
    ├── reporters/ (status dashboards)
    ├── auditors/ (full audit)
    └── deployers/ (publish to GitHub/Colab)
```

**Entry Points:**
- **CLI:** `python infrastructure/course_cli.py <command> [options]`
- **Audit:** `python run_audit.py` (in project root)
- **Module Import:** `from validators import validate_latex`

### Common Workflows

**1. Build charts for a topic:**
```bash
python infrastructure/course_cli.py build charts --topic L01
```

**2. Validate all LaTeX with strict mode:**
```bash
python infrastructure/course_cli.py validate latex --strict
```

**3. Generate progress dashboard:**
```bash
python infrastructure/course_cli.py status --detailed
```

**4. Run full audit:**
```bash
python run_audit.py  # Generates JSON, MD, HTML reports
```

### Architecture Patterns

**1. Manifest-Driven Design:**
All modules read from `manifest.json` to discover content. The manifest is the single source of truth for:
- Topic IDs (L01-L06)
- Asset locations (charts, slides, notebooks)
- Completion status (pending, in_progress, complete)

**2. Functional Return Values:**
Validators and builders return `bool`:
- `True` = operation succeeded
- `False` = operation failed

**3. Subprocess Execution:**
External tools (pdflatex, python scripts) are invoked via `subprocess.run()` with:
- `capture_output=True` for silent operation
- `timeout=60/120` to prevent hangs
- `cwd=` set to appropriate working directory

**4. Path Management:**
All modules define `PROJECT_ROOT = Path(__file__).parent.parent.parent` to enable absolute path resolution.

### Testing Infrastructure Changes

**Before modifying infrastructure:**
1. Run `python infrastructure/course_cli.py status` to capture baseline
2. Make changes to a validator/builder/reporter
3. Test with `--topic L01` flag first (single topic)
4. Run full audit: `python run_audit.py`
5. Verify functional tests pass in audit output

**Functional tests include:**
- CLI help command
- Manifest JSON validity
- Module import checks
- Progress report generation

### Debugging Common Issues

**"Module not found" errors:**
- Check `__init__.py` exports in each subdirectory
- Verify `sys.path` includes `infrastructure/` directory
- Use absolute imports: `from validators.latex_validator import ...`

**"pdflatex not found" errors:**
- Validators/builders gracefully skip if LaTeX not installed
- Check return codes: `FileNotFoundError` → SKIP, not FAIL

**Subprocess timeout errors:**
- Chart scripts timeout at 60s, LaTeX at 120s
- Increase timeout values if needed for complex charts
- Check for infinite loops in chart.py scripts

### Extension Points

**Adding a new validator:**
1. Create `infrastructure/validators/new_validator.py`
2. Implement `validate_new(manifest: dict, **kwargs) -> bool`
3. Add to `validators/__init__.py` exports
4. Add command to `course_cli.py` in `cmd_validate()`

**Adding a new builder:**
1. Create `infrastructure/builders/new_builder.py`
2. Implement `build_new(manifest: dict, topic: str = None) -> bool`
3. Add to `builders/__init__.py` exports
4. Add command to `course_cli.py` in `cmd_build()`

**Adding a new reporter:**
1. Create `infrastructure/reporters/new_report.py`
2. Implement `generate_new_report(manifest: dict, **kwargs) -> str`
3. Add to `reporters/__init__.py` exports
4. Add to `course_cli.py` in `cmd_report()`

### Dependencies

**Internal:**
- `manifest.json` (required - single source of truth)
- `config.yaml` (optional - course configuration)
- `templates/` (required for builders)

**External Python Packages:**
- Standard library only (subprocess, json, pathlib, argparse, datetime)
- Optional: `nbformat`, `nbconvert` (for notebook execution)
- Optional: `yaml` (for config.yaml parsing)

**External Tools:**
- `pdflatex` (for LaTeX compilation) - optional, graceful degradation
- `pandoc` (for syllabus PDF export) - optional
- `git` (for GitHub deployment)

### Performance Considerations

**Parallel Execution:**
- Chart building can be parallelized (each chart is independent)
- LaTeX compilation must be sequential (due to aux file dependencies)
- Validators can run in parallel (read-only operations)

**Caching:**
- Chart PDFs are cached - regenerate only if chart.py changes
- LaTeX auxiliary files stored in `temp/` subdirectories
- Audit results can be cached for dashboard generation

### File Structure Conventions

**Naming:**
- Modules use underscore_case: `latex_validator.py`
- Classes use PascalCase: `RetryStrategy`
- Functions use snake_case: `validate_latex()`

**Return Values:**
- Validators return `bool`
- Builders return `bool`
- Reporters return `str` (formatted output)
- Generators return `str` or `Path`

**Error Handling:**
- Use try/except for subprocess calls
- Print status messages: `[PASS]`, `[FAIL]`, `[SKIP]`, `[WARN]`
- Return False on errors, don't raise exceptions (graceful degradation)

---

**MANUAL:** This file documents the infrastructure subsystem for course management. See subdirectory AGENTS.md files for detailed documentation of validators/, builders/, reporters/, auditors/, generators/, deployers/, and utils/.
