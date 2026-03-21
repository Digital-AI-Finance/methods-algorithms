<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-03-21 | Updated: 2026-03-21 -->

# infrastructure/trackers/

**Parent**: [../AGENTS.md](../AGENTS.md) (infrastructure/)

## Purpose

Activity logging for course development. Tracks all file creation, modification, CLI commands, validation runs, build runs, and errors into a structured JSON log.

## Key Files

| File | Description |
|------|-------------|
| `activity_log.py` | Records development events (file_created, file_modified, cli_command, validation_run, build_run, download_attempt, git_operation, error, info) to `activity_log.json`; each event has a UUID, timestamp, event type, and metadata dict |
| `__init__.py` | Package init |

## For AI Agents

### Working In This Directory

- Log file is written to `infrastructure/trackers/activity_log.json` (local, not project root)
- Use the `@contextmanager` `log_activity()` to wrap operations that should be recorded
- Event types: `file_created`, `file_modified`, `file_deleted`, `cli_command`, `validation_run`, `build_run`, `download_attempt`, `git_operation`, `error`, `info`
- The log is append-only; do not truncate or delete it during normal operations
- Used by the audit system (`run_audit.py`) to produce activity summaries
