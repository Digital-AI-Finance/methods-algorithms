# Prompt: Embeddings Ultra-Deep Plan -- Iteration 2 (Critic Fixes)

**Time:** 2026-03-21 18:30
**Action:** Fixed all 5 critical and 10 minor issues from Critic review of embeddings-ultra-deep-lecture.md

## Critical Fixes Applied
1. **BPE formula** -- replaced WordPiece formula with correct `argmax count(ab)`, now shows both BPE and WordPiece with correct labels
2. **Sentence-BERT loss** -- replaced invalid `log(cos)` with cosine similarity MSE: `(cos(u,v) - y)^2`
3. **Closing comic** -- changed from nonexistent #2421 to confirmed #2173 in images/
4. **Chart count** -- resolved slide 17 ambiguity (top10_12 chosen), DoD updated, chart map consistent
5. **Zone 1 formula violation** -- moved one-hot formula from slide 4 to slide 6 (Zone 2), restructured zones

## Minor Fixes Applied
- 92% question-based titles (was ~3%), added title audit table
- Added TOC slide (slide 4), total now 39 slides
- Added TODO 11 for manifest.json update
- Preamble reference corrected to lines 1-99
- TikZ specs expanded for slides 7, 24, 29, 30
- TODO 5 formula count corrected (6 formulas listed, says 6)
- Guardrails formula list updated to match actual 15
- Overflow mitigation table added for risky slides
- ELMo omission formally justified

## Outcome
Plan updated at `.omc/plans/embeddings-ultra-deep-lecture.md`, signaled PLAN_READY.
