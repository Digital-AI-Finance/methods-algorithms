<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-03-21 | Updated: 2026-03-21 -->

# skills/

**Parent**: [../AGENTS.md](../AGENTS.md) (Methods_and_Algorithms root)

## Purpose

Reusable AI skill definitions (prompt engineering recipes) for lecture construction. These are course-local skill files that define standardized workflows for AI agents working on this repository.

## Key Files

| File | Description |
|------|-------------|
| `formula-free-visual-lecture.md` | Skill definition for creating formula-free visual companion lectures: zero display math, TikZ stick-figure comics, XKCD bookends, `\bottomnote{}` on every slide. Used to produce L05 simple variants and all 5 L06 companion lectures (L06a-L06e) |

## For AI Agents

### Working In This Directory

- Skills here are **course-local** — they complement the global skills at `~/.claude/skills/omc-learned/`
- The `formula-free-visual-lecture.md` skill documents the pattern used for visual lectures: no Greek symbols, narrative storylines, TikZ comics, XKCD bookends
- When creating a new skill file, follow the same structure: purpose, trigger conditions, step-by-step recipe, quality checklist
- The master Beamer slide creation skill is at `~/.claude/skills/omc-learned/beamer-slide-creator.md` (global, not here)
