# Ralplan Iteration 2: RL Lecture Ultra Deep Plan

**Date:** 2026-03-20
**Prompt:** Fix 5 critical issues from Critic rejection (24/35) of rl-lecture-ultra-deep plan
**Action:** Rewrote plan addressing all 5 critical and 6 minor issues

## Critical Fixes Applied
1. **Slide budget**: Added concrete slide-by-slide accounting table. 3 merges (-3) + 5 additions (+5) = net +2 = 46 main... wait, recalculated to 45 main + 10 appendix = 55 exactly at cap. PPO math moved to L06_rl_full.
2. **TODO-05 subplots**: Redesigned as single-axes horizontal flow diagram with 3 connected zones, NOT plt.subplot panels.
3. **Stale counts**: All numbers replaced with verified grep counts (deepdive=54, overview=25, L06b=19, L06e=12, rl_full=25, rl_mini=10).
4. **TODO-13 ambiguity**: Resolved: appendix A7 and A9 STAY as-is. New main body slides are separate, lighter treatments. Explicit statement of what happens to each appendix slide.
5. **Phase 1 empty**: Removed Phase 1 "Structural Analysis" (analysis is in Context section). Renumbered phases starting at 1=Charts.

## Minor Fixes Applied
1. Charts 16-19 added to inventory (noted 16/17 are embeddings, not RL)
2. TODO-14 now specifies exact slide titles and line numbers
3. XKCD dedup expanded: both comics in both files, fix replaces BOTH L06e comics
4. TODO-20 (now TODO-19) clarified as REWRITE not copy
5. L06_rl_mini.tex added to inventory and TODO-23
6. Chart ratio verified (1:4 current, 1:3.2 after changes)

## Architect Questions Addressed
- PPO math -> L06_rl_full only (not deepdive)
- A7/A9 stay in appendix unchanged
- Direct answers in new "Architect Questions" section

**Outcome:** Updated plan saved to .omc/plans/rl-lecture-ultra-deep.md
