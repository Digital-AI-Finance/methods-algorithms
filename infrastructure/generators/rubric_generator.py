"""Rubric generator - creates easy-to-grade assessment rubrics."""
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

PROJECT_ROOT = Path(__file__).parent.parent.parent
RUBRICS_DIR = PROJECT_ROOT / "rubrics"


def generate_rubrics(verbose: bool = False) -> Dict[str, Path]:
    """
    Generate all rubrics.

    Args:
        verbose: Show detailed output

    Returns:
        Dictionary of rubric name -> output path
    """
    print("Generating rubrics...")
    RUBRICS_DIR.mkdir(parents=True, exist_ok=True)

    outputs = {}

    # Presentation rubric
    pres_path = generate_presentation_rubric(verbose)
    outputs["presentation"] = pres_path
    print(f"  [X] Presentation rubric: {pres_path.name}")

    # Capstone rubric
    cap_path = generate_capstone_rubric(verbose)
    outputs["capstone"] = cap_path
    print(f"  [X] Capstone rubric: {cap_path.name}")

    return outputs


def generate_presentation_rubric(verbose: bool = False) -> Path:
    """
    Generate the presentation rubric (15 min, 100 points).

    Args:
        verbose: Show detailed output

    Returns:
        Path to generated rubric file
    """
    RUBRICS_DIR.mkdir(parents=True, exist_ok=True)

    rubric = """# Presentation Rubric

**Duration**: 15 minutes | **Total Points**: 100

## Grading Criteria

| Criterion | Excellent (25) | Good (20) | Adequate (15) | Needs Work (10) | Score |
|-----------|----------------|-----------|---------------|-----------------|-------|
| **Content Accuracy** | All facts correct, sources cited | Minor errors, mostly cited | Some errors, few citations | Major errors, no citations | __/25 |
| **Clarity** | Crystal clear, logical flow | Clear, minor jumps | Somewhat clear | Confusing | __/25 |
| **Visuals** | Professional, aids understanding | Good, mostly helpful | Basic, some help | Poor or distracting | __/25 |
| **Timing** | 14-16 min, well-paced | 12-18 min, mostly paced | 10-20 min, uneven | <10 or >20 min | __/25 |

## Quick Grading Guide

1. **Content Accuracy** (25 points)
   - Are all technical facts correct?
   - Are sources properly cited?
   - Does the presentation demonstrate understanding?

2. **Clarity** (25 points)
   - Is the presentation easy to follow?
   - Is there a clear structure (intro, body, conclusion)?
   - Are technical concepts explained clearly?

3. **Visuals** (25 points)
   - Are slides readable and professional?
   - Do visuals support the content?
   - Is there appropriate use of charts/diagrams?

4. **Timing** (25 points)
   - Did the presentation fit the 15-minute slot?
   - Was the pacing appropriate?
   - Was there time for questions?

## Grading Summary

| Student | Content | Clarity | Visuals | Timing | **Total** |
|---------|---------|---------|---------|--------|-----------|
| | __/25 | __/25 | __/25 | __/25 | __/100 |

## Comments

_Space for feedback:_

---

*Grading time: ~5 minutes per student*

---
*Last updated: """ + datetime.now().strftime('%Y-%m-%d') + """*
"""

    output_path = RUBRICS_DIR / "presentation_rubric.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rubric)

    return output_path


def generate_capstone_rubric(verbose: bool = False) -> Path:
    """
    Generate the capstone project rubric (report only, 100 points).

    Args:
        verbose: Show detailed output

    Returns:
        Path to generated rubric file
    """
    RUBRICS_DIR.mkdir(parents=True, exist_ok=True)

    rubric = """# Capstone Project Rubric

**Deliverable**: Written Report (10-15 pages PDF) | **Total Points**: 100

## Grading Criteria

| Criterion | Excellent (20) | Good (15) | Adequate (10) | Needs Work (5) | Score |
|-----------|----------------|-----------|---------------|----------------|-------|
| **Problem Definition** | Clear, well-motivated business problem | Clear problem | Somewhat clear | Unclear | __/20 |
| **Method Selection** | Justified choice with alternatives considered | Justified choice | Choice stated | No justification | __/20 |
| **Implementation** | Correct, efficient, well-documented | Correct, documented | Works, basic docs | Errors or no docs | __/20 |
| **Results Interpretation** | Business insights, limitations discussed | Good interpretation | Basic interpretation | No interpretation | __/20 |
| **Report Quality** | Professional, well-structured | Good structure | Adequate | Poor | __/20 |

## Detailed Criteria

### 1. Problem Definition (20 points)

| Points | Description |
|--------|-------------|
| 18-20 | Business problem clearly stated, well-motivated, appropriate scope |
| 14-17 | Problem clear, motivation present, reasonable scope |
| 10-13 | Problem identifiable but vague or poorly motivated |
| 5-9 | Problem unclear or inappropriate for course methods |

### 2. Method Selection (20 points)

| Points | Description |
|--------|-------------|
| 18-20 | Method well-justified, alternatives considered, decision framework used |
| 14-17 | Method justified, some alternatives mentioned |
| 10-13 | Method stated but justification weak |
| 5-9 | Method choice unexplained or inappropriate |

### 3. Implementation (20 points)

| Points | Description |
|--------|-------------|
| 18-20 | Code correct, efficient, well-documented, reproducible |
| 14-17 | Code correct, adequately documented |
| 10-13 | Code works but poorly documented or inefficient |
| 5-9 | Code has errors or missing documentation |

### 4. Results Interpretation (20 points)

| Points | Description |
|--------|-------------|
| 18-20 | Clear business insights, limitations acknowledged, actionable recommendations |
| 14-17 | Good interpretation, some limitations discussed |
| 10-13 | Basic interpretation of results |
| 5-9 | Results presented without interpretation |

### 5. Report Quality (20 points)

| Points | Description |
|--------|-------------|
| 18-20 | Professional formatting, clear writing, proper citations, follows template |
| 14-17 | Good structure, minor formatting issues |
| 10-13 | Adequate structure, some formatting problems |
| 5-9 | Poor organization or significant formatting issues |

## Grading Summary

| Student | Problem | Methods | Implementation | Results | Quality | **Total** |
|---------|---------|---------|----------------|---------|---------|-----------|
| | __/20 | __/20 | __/20 | __/20 | __/20 | __/100 |

## Grade Conversion

| Score | Grade |
|-------|-------|
| 90-100 | A |
| 80-89 | B |
| 70-79 | C |
| 60-69 | D |
| <60 | F |

## Comments

_Space for feedback:_

---

*Grading time: ~15 minutes per student*

---
*Last updated: """ + datetime.now().strftime('%Y-%m-%d') + """*
"""

    output_path = RUBRICS_DIR / "capstone_rubric.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rubric)

    return output_path


def get_rubric_templates() -> Dict[str, str]:
    """Get rubric templates as strings."""
    return {
        "presentation": """
| Criterion | Excellent | Good | Adequate | Needs Work | Score |
|-----------|-----------|------|----------|------------|-------|
| Content | 25 | 20 | 15 | 10 | __ |
| Clarity | 25 | 20 | 15 | 10 | __ |
| Visuals | 25 | 20 | 15 | 10 | __ |
| Timing | 25 | 20 | 15 | 10 | __ |
| **Total** | | | | | __/100 |
""",
        "capstone": """
| Criterion | Excellent | Good | Adequate | Needs Work | Score |
|-----------|-----------|------|----------|------------|-------|
| Problem | 20 | 15 | 10 | 5 | __ |
| Methods | 20 | 15 | 10 | 5 | __ |
| Implementation | 20 | 15 | 10 | 5 | __ |
| Results | 20 | 15 | 10 | 5 | __ |
| Quality | 20 | 15 | 10 | 5 | __ |
| **Total** | | | | | __/100 |
"""
    }
