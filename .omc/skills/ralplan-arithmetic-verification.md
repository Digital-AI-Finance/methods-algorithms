---
id: ralplan-arithmetic-verification
name: Arithmetic Consistency in Ralplan Scoring Systems
description: When designing point-based scoring systems in ralplan, arithmetic errors propagate through examples and references. The Critic catches these but only if the plan contains enough cross-references to expose inconsistencies.
source: session-2026-02-07-group-assignment
triggers:
  - ralplan scoring system
  - difficulty multiplier table
  - point totals across examples
  - arithmetic error in plan
  - critic rejection arithmetic
quality: high
---

# Arithmetic Consistency in Ralplan Scoring Systems

## The Insight

When designing point-based scoring/grading systems, the Planner creates a master table (e.g., difficulty multiplier) and then references those values in worked examples. The **references drift from the table** because the Planner is generating narrative text, not computing values. The Critic reliably catches these — but only across 2+ iterations, because the first iteration focuses on structural issues.

## Why This Matters

In the group assignment design:
- Iteration 0: Critic caught 15+ structural issues (perverse incentives, unrealistic examples, missing policies)
- Iteration 1: Critic caught arithmetic errors — every "remaining points" calculation in the examples was wrong by 1 point. Total possible was 13, but examples said "8 pts", "10 pts", "12 pts" instead of "9 pts", "11 pts", "12 pts"
- The multiplier table itself was correct; the error was in the narrative referencing it

Pattern: **Tables are usually correct. Prose references to tables are usually wrong.**

## Recognition Pattern

- Any plan with a scoring table AND worked examples that reference those scores
- Point totals, grade calculations, weighted averages in narrative text
- "Omits X (Y pts), remaining Z pts" — the Z is often wrong
- Multiple examples each computing from the same base table

## The Approach

1. **After creating the multiplier/scoring table**: Immediately compute ALL derived values (remaining points for each omission scenario) and write them explicitly. Don't leave them for narrative generation.
2. **In worked examples**: State the formula explicitly: "Total = 13, omitted = 4, remaining = 13 - 4 = 9" rather than just "remaining 9 pts"
3. **Self-check before Critic**: Run the arithmetic manually for every example. For each "remaining X pts" claim, verify: total (13) minus omitted topic points = claimed remaining.
4. **Expect 2 Critic iterations minimum**: First iteration catches design issues, second catches arithmetic. Budget for this in ralplan.

## Example

The multiplier table had L06 = 4 points, total = 13.
- WRONG (Iteration 0): "Omits L06, 8 difficulty pts" (where did 8 come from?)
- CORRECT (Iteration 2): "Omits L06 (4 pts), remaining 9 pts, multiplier 0.88"
- VERIFICATION: 13 - 4 = 9. Multiplier for 9 pts = 0.88. 50 x 0.88 = 44.0 max technical.
