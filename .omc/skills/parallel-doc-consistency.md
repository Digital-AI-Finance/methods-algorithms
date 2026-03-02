---
id: parallel-doc-consistency
name: Cross-Document Consistency in Parallel Agent Creation
description: When parallel agents create related documents from a single plan, they drift on shared values (thresholds, percentages, counts). Architect verification must check cross-file consistency, not just per-file correctness.
source: session-2026-02-07-group-assignment
triggers:
  - parallel executor agents creating documents
  - multiple markdown files from one plan
  - rubric and specification consistency
  - cross-document values mismatch
  - contribution survey threshold
quality: high
---

# Cross-Document Consistency in Parallel Agent Creation

## The Insight

When multiple executor agents create related documents in parallel from a single source plan, they each independently interpret shared values. Even with detailed prompts, agents will **drift on specific numbers** (thresholds, percentages, counts) because they're generating text, not copying it verbatim. The drift is always on "secondary" values — the main structure is correct, but supporting details diverge.

## Why This Matters

In this project, two blocking issues were caught by Architect verification:
- `contribution_survey.md` said ">1.0 points lower" while `group_assignment_specification.md` said ">1.5 standard deviations" (same concept, different thresholds)
- `contribution_survey.md` said "+/- 15%" while the plan and spec both said "+/- 10%"
- `group_assignment_specification.md` said "6 quizzes" while the plan said "3 quizzes"

Students reading both documents simultaneously would see contradictory policies — causing confusion and potential grade appeals.

## Recognition Pattern

This applies whenever you:
- Launch 2+ parallel executor agents that create related files (spec + rubric + form + survey)
- Have a single source-of-truth plan with specific numbers that must appear consistently across files
- Create student-facing or policy documents where contradictions have real consequences

## The Approach

1. **In agent prompts**: For shared values (thresholds, percentages, point totals, grade scales), include the EXACT text to use — not a description of the value, but the literal string.
2. **In verification**: Architect must explicitly check cross-file consistency for: point totals, grade tables, policy thresholds, deadline penalties, and any value that appears in 2+ files.
3. **Post-fix pattern**: After fixing consistency issues, re-verify with Architect specifically asking to cross-reference the fixed values across all documents.

## Example

BAD prompt: "Include the contribution survey trigger threshold from the plan"
GOOD prompt: "The trigger is: 'more than 1.5 standard deviations below the group mean'. Use this EXACT phrasing. The grade adjustment is +/- 10% (not 15%, not 5%)."
