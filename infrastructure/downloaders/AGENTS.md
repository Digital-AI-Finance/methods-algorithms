<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-03-21 | Updated: 2026-03-21 -->

# infrastructure/downloaders/

**Parent**: [../AGENTS.md](../AGENTS.md) (infrastructure/)

## Purpose

Downloads and manages course reference materials (textbooks, papers, datasets) from remote URLs. Maintains a local resource registry with checksums for cache validity.

## Key Files

| File | Description |
|------|-------------|
| `pdf_downloader.py` | Downloads PDFs (textbooks, papers) defined in `DEFAULT_RESOURCES`; verifies checksums; stores files in `resources/`; maintains a `resource_registry.json` for cache tracking |
| `__init__.py` | Package init |

## For AI Agents

### Working In This Directory

- Downloads go to `{project_root}/resources/` (not in this directory)
- Registry is stored at `infrastructure/downloaders/resource_registry.json`
- Default resources include ISLR v2 (textbook) and topic-specific papers
- Run from project root: `python -m infrastructure.downloaders.pdf_downloader`
- Uses stdlib only (`urllib`, `hashlib`) — no extra dependencies
- SSL verification uses default context; some institutional firewalls may block downloads
