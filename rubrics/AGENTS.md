# rubrics/

<!-- Parent: ../AGENTS.md -->

**Generated**: 2026-01-25
**Purpose**: Grading rubrics for course assessments (capstone project and presentations)

---

## Overview

This directory contains **detailed grading rubrics** for major course assessments. Rubrics provide:
- Clear evaluation criteria for students
- Consistent grading standards for instructors
- Transparent breakdown of point allocations
- Quick-reference checklists for efficient grading

All rubrics follow a **criterion-based scoring** approach with predefined performance levels.

---

## Key Files

| File | Assessment Type | Total Points | Grading Time |
|------|-----------------|--------------|--------------|
| `capstone_rubric.md` | Final capstone project (written report) | 100 | ~15 min/report |
| `presentation_rubric.md` | Capstone presentation | 50 | ~5 min/presentation |

---

## For AI Agents

### Rubric Structure

Each rubric file contains:

1. **Header**: Course info, deliverable format, total points
2. **Quick Grading Guide**: Overview for instructors
3. **Criteria Sections**: Each criterion with:
   - Performance levels (Excellent, Good, Adequate, Needs Work)
   - Point values per level
   - Checklist of required elements
4. **Total Score Calculation**: Summary table
5. **Grade Conversion**: Points-to-letter-grade mapping
6. **Bonus Points**: Optional extra credit
7. **Deductions**: Penalties for violations (late submission, plagiarism)
8. **Feedback Template**: Space for qualitative comments

---

### capstone_rubric.md

**Purpose**: Grading the final written capstone project (10-15 page report)

**Criteria** (5 criteria × 20 points each = 100 points total):

| Criterion | Points | Evaluates |
|-----------|--------|-----------|
| **Problem Definition** | 20 | Clarity of business problem, motivation, success criteria |
| **Method Selection** | 20 | Justification of ML methods, decision framework usage, alternatives considered |
| **Implementation** | 20 | Code correctness, preprocessing, hyperparameter tuning, reproducibility |
| **Results Interpretation** | 20 | Business insights, model comparison, feature importance, limitations |
| **Report Quality** | 20 | Writing, structure, citations, figures/tables, professionalism |

**Performance Levels** (per criterion):

| Level | Points | Description |
|-------|--------|-------------|
| Excellent | 20 | Exceeds expectations, professional quality |
| Good | 15 | Meets expectations, minor issues |
| Adequate | 10 | Meets minimum requirements, some gaps |
| Needs Work | 5 | Below expectations, major issues |

**Example criterion structure**:

```markdown
## Criterion 1: Problem Definition (20 points)

| Level | Points | Description |
|-------|--------|-------------|
| Excellent | 20 | Clear, well-motivated business problem with specific success criteria |
| Good | 15 | Clear problem statement, adequate motivation |
| Adequate | 10 | Problem stated but vague or poorly motivated |
| Needs Work | 5 | Unclear problem, no business context |

**Score: _____ / 20**

**Checklist:**
- [ ] Business context explained
- [ ] Problem clearly stated
- [ ] Success criteria defined
- [ ] Relevance to course topics evident
```

**Bonus Points** (up to 5):
- Novel problem or creative approach (+2)
- Exceptional visualization (+1)
- Deployment-ready code (+2)

**Deductions**:
- Late submission: -10 per day (max -30)
- Over page limit (>18 pages): -5
- Under page limit (<8 pages): -10
- Plagiarism detected: -100 (automatic fail)

**Grade Conversion**:

| Score Range | Letter Grade |
|-------------|--------------|
| 90-100 | A |
| 80-89 | B |
| 70-79 | C |
| 60-69 | D |
| <60 | F |

---

### presentation_rubric.md

**Purpose**: Grading the capstone project oral presentation (10-15 minutes)

**Criteria** (5 criteria × 10 points each = 50 points total):

| Criterion | Points | Evaluates |
|-----------|--------|-----------|
| **Content** | 10 | Problem clarity, methods explained, results presented |
| **Clarity** | 10 | Organization, logical flow, slide design |
| **Delivery** | 10 | Pace, eye contact, confidence, engagement |
| **Visuals** | 10 | Chart quality, readability, relevance |
| **Q&A** | 10 | Ability to answer questions, defend choices |

**Performance Levels** (per criterion):

| Level | Points | Description |
|-------|--------|-------------|
| Excellent | 10 | Professional, polished, engaging |
| Good | 8 | Solid performance, minor issues |
| Adequate | 6 | Meets expectations, room for improvement |
| Needs Work | 4 | Below expectations, major issues |

**Time Penalties**:
- Under 8 minutes: -5 points
- Over 17 minutes: -5 points

**Bonus**:
- Exceptional visualization or demo: +3 points

---

### How to Use Rubrics

#### For Instructors

**Grading workflow**:

```
1. Open rubric file (capstone_rubric.md)
2. Print or use digital copy with PDF annotator
3. For each criterion:
   - Circle/highlight appropriate performance level
   - Mark checklist items
   - Add brief qualitative notes
4. Calculate total score
5. Apply bonus/deductions if applicable
6. Write feedback summary (strengths, areas for improvement, overall comments)
7. Transfer score to LMS gradebook
8. Share rubric + feedback with student
```

**Typical grading time**: 15 minutes per capstone report (with rubric)

**Calibration** (recommended for multiple graders):
```
1. All graders independently grade 2-3 sample reports
2. Meet to compare scores and discuss discrepancies
3. Agree on interpretation of performance levels
4. Adjust scores if needed for consistency
5. Proceed with grading remaining reports
```

#### For Students

**Use rubrics to**:
- Understand evaluation criteria before starting work
- Self-assess work before submission
- Identify areas needing improvement
- Prepare targeted questions for instructor

**Self-assessment checklist** (from rubric):
```
Problem Definition:
☐ Business context explained clearly
☐ Problem statement is specific and measurable
☐ Success criteria defined
☐ Relevance to course topics evident

Method Selection:
☐ At least 2 methods from course applied
☐ Justification for method selection provided
☐ Alternatives considered and compared
☐ Decision framework reasoning used
...
```

---

### Updating Rubrics

**When to update**:
- After first use (based on instructor feedback)
- When course content changes
- When new assessment requirements added
- When grade distribution is unexpected (too harsh/lenient)

**Update protocol**:

```bash
# 1. Document reason for change
# Example: "Updated Problem Definition criterion to require quantitative success metrics"

# 2. Edit rubric file
# - Modify criterion descriptions
# - Adjust point values if needed
# - Update checklists

# 3. Review with teaching team
# - Get feedback from other instructors
# - Ensure consistency across criteria

# 4. Test with sample work
# - Grade 2-3 sample reports with new rubric
# - Verify scoring makes sense

# 5. Update this AGENTS.md file
# - Document changes made
# - Update examples

# 6. Commit changes
git add rubrics/capstone_rubric.md rubrics/AGENTS.md
git commit -m "Update capstone rubric: require quantitative success metrics"
```

**Version control**: Keep old versions for reference (useful if re-grading or handling appeals).

---

### Validation Checklist

Before using a rubric:

- [ ] **Total points add up correctly** (5 criteria × 20 = 100 for capstone)
- [ ] **Performance levels are clearly distinct** (no overlap in descriptions)
- [ ] **Point values are consistent** (same point spread for all criteria)
- [ ] **Checklists are exhaustive** (cover all key elements)
- [ ] **Grade conversion is standard** (A=90+, B=80+, etc.)
- [ ] **Deductions are fair and documented** (clear policies)
- [ ] **Feedback template is included** (space for qualitative comments)

---

### Common Rubric Issues

| Issue | Problem | Solution |
|-------|---------|----------|
| **Inconsistent scoring** | Different graders interpret levels differently | Calibration session with sample work |
| **Unclear descriptions** | "Good" vs "Adequate" hard to distinguish | Add specific examples or quantitative thresholds |
| **Checklist mismatch** | Checklist items don't align with point values | Review each criterion, ensure alignment |
| **Too harsh/lenient** | Grade distribution skewed | Adjust performance level descriptions |
| **Missing criteria** | Important aspect not evaluated | Add new criterion or expand existing one |
| **Overlapping criteria** | Two criteria evaluate same thing | Merge or clarify distinction |

---

### Creating New Rubric

**Step-by-step**:

```markdown
# 1. Define assessment details
- Type: (quiz, project, presentation, etc.)
- Deliverable format: (report, slides, code, etc.)
- Total points: (typically 50 or 100)

# 2. Identify criteria (typically 4-6)
- What are the key aspects to evaluate?
- Are they independent (non-overlapping)?
- Do they cover all important elements?

# 3. Define performance levels
- How many levels? (typically 4: Excellent, Good, Adequate, Needs Work)
- What distinguishes each level?
- What point values for each level?

# 4. Create checklists
- What specific elements must be present for each criterion?
- Can be checked yes/no

# 5. Add bonus/deductions
- What warrants extra credit?
- What violations require penalties?

# 6. Add feedback template
- Space for strengths
- Space for areas for improvement
- Space for overall comments

# 7. Test with sample work
- Grade 2-3 samples
- Check if scoring makes sense
- Adjust as needed
```

**Example new rubric** (for quiz presentation rubric):

```markdown
# Quiz Presentation Rubric

**Course**: Methods and Algorithms - MSc Data Science
**Deliverable**: 5-minute explanation of quiz solution
**Total Points**: 20

## Criterion 1: Correctness (10 points)

| Level | Points | Description |
|-------|--------|-------------|
| Excellent | 10 | Solution is completely correct with clear reasoning |
| Good | 8 | Solution is mostly correct with minor errors |
| Adequate | 6 | Solution has correct approach but significant errors |
| Needs Work | 4 | Solution is incorrect or incomplete |

**Score: _____ / 10**

## Criterion 2: Explanation Clarity (10 points)

| Level | Points | Description |
|-------|--------|-------------|
| Excellent | 10 | Explanation is clear, well-organized, and easy to follow |
| Good | 8 | Explanation is generally clear with minor confusion |
| Adequate | 6 | Explanation is understandable but lacks organization |
| Needs Work | 4 | Explanation is unclear or hard to follow |

**Score: _____ / 10**

## Total Score: _____ / 20
```

---

### Integration with Course Assessment

**Capstone project workflow**:

```
Week 1-4: In-class lectures + notebooks
Week 5: Capstone project introduced
     - Review specification.md
     - Review capstone_rubric.md
     - Students brainstorm topics
Week 6: Topic proposal due (1-page)
     - Instructor feedback using mini-rubric
Week 7-8: Students work on project
     - Office hours for questions
Week 9: Final report due
     - Grading using capstone_rubric.md
Week 9-10: Presentations (optional)
     - Grading using presentation_rubric.md
```

**Rubric transparency**:
- Share rubrics with students at project introduction
- Post rubrics on Moodle course page
- Reference rubric criteria in office hours discussions
- Return graded rubrics with scores and feedback

---

### Grade Distribution Analysis

After grading, analyze score distribution to evaluate rubric effectiveness:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load scores
scores = pd.DataFrame({
    'student_id': range(1, 31),
    'problem_def': [18, 15, 12, ...],  # Criterion 1 scores
    'method_selection': [16, 14, 18, ...],  # Criterion 2 scores
    # ... other criteria
})

# Calculate total scores
scores['total'] = scores[['problem_def', 'method_selection', ...]].sum(axis=1)

# Plot distribution
plt.hist(scores['total'], bins=10, edgecolor='black')
plt.xlabel('Total Score')
plt.ylabel('Number of Students')
plt.title('Capstone Project Score Distribution')
plt.show()

# Summary statistics
print(f"Mean: {scores['total'].mean():.1f}")
print(f"Median: {scores['total'].median():.1f}")
print(f"Std Dev: {scores['total'].std():.1f}")
print(f"Min: {scores['total'].min()}")
print(f"Max: {scores['total'].max()}")
```

**Expected distribution** (for well-calibrated rubric):
- Mean: 75-80 (B-/B range)
- Standard deviation: 10-15
- Range: 50-100 (few fails, few perfect scores)

**If distribution is unexpected**:
- Too harsh: Mean <70 → Consider adjusting performance level descriptions
- Too lenient: Mean >85 → Raise standards or add stricter checklist items
- Low variance: Std <8 → Rubric may not differentiate well; add more nuanced levels

---

## Related Files

- **Parent hierarchy**: `../AGENTS.md` (project root)
- **Capstone spec**: `../capstone/specification.md` (project requirements that rubric evaluates)
- **Report template**: `../capstone/report_template.tex` (students use this for structure)
- **Manifest**: `../manifest.json` (tracks rubric versions)
- **CLI**: `python infrastructure/course_cli.py inventory list` (shows rubric files)
