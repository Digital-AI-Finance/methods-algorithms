"""Instructor guide generator - creates teaching guides from templates."""
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

PROJECT_ROOT = Path(__file__).parent.parent.parent
TEMPLATE_PATH = PROJECT_ROOT / "templates" / "instructor_guide_template.md"


def generate_instructor_guide(topic: dict, verbose: bool = False) -> str:
    """
    Generate instructor guide for a topic.

    Args:
        topic: Topic dictionary from manifest
        verbose: Show detailed output

    Returns:
        Guide markdown string
    """
    topic_id = topic.get("id", "LXX")
    title = topic.get("title", "Topic")
    finance_case = topic.get("finance_case", "TBD")

    # Get learning objectives
    objectives = topic.get("learning_objectives", [])
    obj_texts = [obj.get("text", "TBD") for obj in objectives[:3]]
    while len(obj_texts) < 3:
        obj_texts.append("TBD")

    # Get decision framework
    decision = topic.get("decision_framework", {})
    when_use = decision.get("when_to_use", ["TBD", "TBD", "TBD"])[:3]
    when_not = decision.get("when_not_to_use", ["TBD", "TBD", "TBD"])[:3]

    # Get assets
    assets = topic.get("assets", {})
    notebook = assets.get("notebook", {}).get("file", "TBD")
    dataset = assets.get("dataset", {}).get("file", "TBD")

    # Get prerequisites
    prereqs = topic.get("prerequisites", ["Python", "Statistics", "Linear Algebra"])

    guide = f"""# Instructor Guide: {topic_id} - {title}

## Session Overview

| Aspect | Details |
|--------|---------|
| **Duration** | 3 hours |
| **Topic** | {title} |
| **Finance Case** | {finance_case} |
| **Prerequisites** | {', '.join(prereqs)} |

## Learning Objectives

By the end of this session, students will be able to:

1. {obj_texts[0]}
2. {obj_texts[1]}
3. {obj_texts[2]}

## PMSP Structure (Problem-Method-Solution-Practice)

### Problem Phase (15 min)

**Motivation**: Present the real-world finance problem that motivates this method.

**Key Questions to Ask**:
- Why do existing methods fail for this problem?
- What characteristics of the data make this approach suitable?

**Discussion Points**:
- Connect to students' prior knowledge
- Highlight real-world applications in finance

### Method Phase (45 min)

**Core Concepts to Cover**:

1. **Mathematical Foundation**
   - Key formulas and derivations
   - Intuition behind the math

2. **Algorithm Steps**
   - Step-by-step walkthrough
   - Complexity analysis

3. **Assumptions & Limitations**
   - When the method works well
   - When it fails

**Common Misconceptions**:
- Address typical student confusions
- Clarify notation and terminology

### Solution Phase (45 min)

**Implementation Walkthrough**:

1. **From Scratch (NumPy)**
   - Show core algorithm implementation
   - Emphasize key steps

2. **Using Libraries (scikit-learn)**
   - Standard workflow
   - Important parameters

**Live Coding Tips**:
- Start with simple example
- Build complexity gradually
- Pause for questions at key points

### Practice Phase (75 min)

**Hands-on Notebook**:
- Students work through {notebook}
- Circulate to help with questions

**Exercise Difficulty Progression**:
1. Basic application (guided)
2. Intermediate analysis (semi-guided)
3. Challenge problem (open-ended)

## Decision Framework

### When to Use {title}

| Use When | Don't Use When |
|----------|----------------|
| {when_use[0] if len(when_use) > 0 else 'TBD'} | {when_not[0] if len(when_not) > 0 else 'TBD'} |
| {when_use[1] if len(when_use) > 1 else 'TBD'} | {when_not[1] if len(when_not) > 1 else 'TBD'} |
| {when_use[2] if len(when_use) > 2 else 'TBD'} | {when_not[2] if len(when_not) > 2 else 'TBD'} |

## Materials Checklist

- [ ] Slides: {topic_id}_overview.pdf
- [ ] Slides: {topic_id}_deepdive.pdf
- [ ] Notebook: {notebook}
- [ ] Dataset: {dataset}
- [ ] All charts compiled

## Timing Guide

| Phase | Duration | Notes |
|-------|----------|-------|
| Problem | 15 min | Keep engaging, connect to finance |
| Method | 45 min | Don't rush math, check understanding |
| Solution | 45 min | Live coding, encourage questions |
| **Break** | 15 min | |
| Practice | 60 min | Hands-on notebook work |
| Q&A | 15 min | Wrap-up, preview next session |

## Common Student Questions

**Q: How do I choose between this method and alternatives?**
A: Refer to the decision framework - consider data characteristics, interpretability needs, and computational constraints.

**Q: What are the most important hyperparameters?**
A: Focus on the parameters that most affect model performance in this domain.

## Additional Resources

- ISLR textbook sections
- Relevant academic papers
- Online tutorials and videos

## Post-Session Notes

*Space for instructor notes after delivering the session*

---

*Last updated: {datetime.now().strftime('%Y-%m-%d')}*
"""

    return guide


def generate_all_guides(manifest: dict, verbose: bool = False) -> Dict[str, Path]:
    """
    Generate instructor guides for all topics.

    Args:
        manifest: Course manifest
        verbose: Show detailed output

    Returns:
        Dictionary of topic_id -> output path
    """
    print("Generating instructor guides...")
    outputs = {}

    for topic in manifest.get("topics", []):
        topic_id = topic["id"]
        title = topic["title"].replace(" ", "_").replace("&", "").replace("/", "_")
        topic_dir = PROJECT_ROOT / "slides" / f"{topic_id}_{title}"

        if not topic_dir.exists():
            if verbose:
                print(f"  [SKIP] {topic_id} - directory not found")
            continue

        guide_content = generate_instructor_guide(topic, verbose)
        guide_path = topic_dir / f"{topic_id}_instructor_guide.md"

        with open(guide_path, 'w', encoding='utf-8') as f:
            f.write(guide_content)

        outputs[topic_id] = guide_path
        print(f"  [X] {topic_id}: {guide_path.name}")

    return outputs


def update_guide_from_feedback(guide_path: Path, feedback: str) -> None:
    """
    Append feedback to instructor guide's post-session notes.

    Args:
        guide_path: Path to instructor guide
        feedback: Feedback text to append
    """
    if not guide_path.exists():
        return

    content = guide_path.read_text()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')

    # Find post-session notes section and append
    if "## Post-Session Notes" in content:
        insert_pos = content.find("## Post-Session Notes")
        insert_pos = content.find("\n", insert_pos) + 1

        feedback_entry = f"\n**{timestamp}**: {feedback}\n"
        content = content[:insert_pos] + feedback_entry + content[insert_pos:]

        with open(guide_path, 'w', encoding='utf-8') as f:
            f.write(content)
