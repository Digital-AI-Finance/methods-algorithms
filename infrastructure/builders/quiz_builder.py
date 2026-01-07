"""Quiz builder - exports quizzes to Moodle XML format."""
import xml.etree.ElementTree as ET
from xml.dom import minidom
from pathlib import Path
from typing import Optional, List, Dict
import html

PROJECT_ROOT = Path(__file__).parent.parent.parent
TEMPLATE_PATH = PROJECT_ROOT / "templates" / "quiz_template.xml"


def build_quizzes(
    manifest: dict,
    quiz_id: Optional[str] = None,
    verbose: bool = False
) -> bool:
    """
    Build quizzes in Moodle XML format.

    Args:
        manifest: Course manifest
        quiz_id: Quiz ID to build (None for all)
        verbose: Show detailed output

    Returns:
        True if all builds succeed
    """
    all_passed = True
    quizzes = manifest.get("quizzes", [])
    quizzes_dir = PROJECT_ROOT / "quizzes"
    quizzes_dir.mkdir(parents=True, exist_ok=True)

    if quiz_id:
        quizzes = [q for q in quizzes if q.get("id") == quiz_id]

    for quiz in quizzes:
        passed = _build_quiz(quiz, quizzes_dir, verbose)
        if not passed:
            all_passed = False

    return all_passed


def _build_quiz(quiz: dict, output_dir: Path, verbose: bool) -> bool:
    """Build a single quiz to Moodle XML."""
    quiz_id = quiz.get("id", "unknown")
    output_file = quiz.get("file", f"{quiz_id}.xml")
    output_path = output_dir / output_file
    print(f"  Building {quiz_id}...")

    questions = quiz.get("questions", [])
    if not questions:
        print(f"    [SKIP] No questions defined")
        return True

    try:
        root = ET.Element("quiz")

        for q in questions:
            question_elem = _create_question_element(q)
            root.append(question_elem)

        # Pretty print XML
        xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
        # Remove empty lines
        xml_str = "\n".join(line for line in xml_str.split("\n") if line.strip())

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)

        print(f"    [PASS] {len(questions)} questions exported to {output_file}")
        return True

    except Exception as e:
        print(f"    [FAIL] {e}")
        return False


def _create_question_element(question: dict) -> ET.Element:
    """Create a Moodle question XML element."""
    q_type = question.get("type", "multichoice")
    q_elem = ET.Element("question", type=q_type)

    # Question name
    name = ET.SubElement(q_elem, "name")
    name_text = ET.SubElement(name, "text")
    name_text.text = question.get("name", "Question")

    # Question text
    qtext = ET.SubElement(q_elem, "questiontext", format="html")
    qtext_text = ET.SubElement(qtext, "text")
    qtext_text.text = f"<![CDATA[{question.get('text', '')}]]>"

    # Default grade
    default_grade = ET.SubElement(q_elem, "defaultgrade")
    default_grade.text = str(question.get("points", 1))

    # Penalty
    penalty = ET.SubElement(q_elem, "penalty")
    penalty.text = str(question.get("penalty", 0.3333333))

    # Single answer (for multichoice)
    if q_type == "multichoice":
        single = ET.SubElement(q_elem, "single")
        single.text = "true" if question.get("single", True) else "false"

        shuffle = ET.SubElement(q_elem, "shuffleanswers")
        shuffle.text = "true" if question.get("shuffle", True) else "false"

        numbering = ET.SubElement(q_elem, "answernumbering")
        numbering.text = question.get("numbering", "abc")

    # Answers
    for answer in question.get("answers", []):
        ans_elem = _create_answer_element(answer)
        q_elem.append(ans_elem)

    # General feedback
    if question.get("feedback"):
        fb = ET.SubElement(q_elem, "generalfeedback", format="html")
        fb_text = ET.SubElement(fb, "text")
        fb_text.text = f"<![CDATA[{question.get('feedback')}]]>"

    return q_elem


def _create_answer_element(answer: dict) -> ET.Element:
    """Create a Moodle answer XML element."""
    fraction = answer.get("fraction", 0)
    ans_elem = ET.Element("answer", fraction=str(fraction), format="html")

    text = ET.SubElement(ans_elem, "text")
    text.text = f"<![CDATA[{answer.get('text', '')}]]>"

    if answer.get("feedback"):
        fb = ET.SubElement(ans_elem, "feedback", format="html")
        fb_text = ET.SubElement(fb, "text")
        fb_text.text = f"<![CDATA[{answer.get('feedback')}]]>"

    return ans_elem


def create_quiz_from_template(
    quiz_name: str,
    topics: List[str],
    num_questions: int = 15
) -> dict:
    """Create a quiz structure from template."""
    return {
        "id": quiz_name.lower().replace(" ", "_"),
        "name": quiz_name,
        "topics": topics,
        "time_limit_minutes": 30,
        "attempts": 1,
        "questions": [],
        "file": f"{quiz_name.lower().replace(' ', '_')}.xml"
    }


def add_question(
    quiz: dict,
    name: str,
    text: str,
    answers: List[Dict],
    feedback: str = "",
    points: int = 1
) -> dict:
    """Add a question to a quiz structure."""
    question = {
        "type": "multichoice",
        "name": name,
        "text": text,
        "answers": answers,
        "feedback": feedback,
        "points": points,
        "single": True,
        "shuffle": True
    }
    quiz["questions"].append(question)
    return quiz


def create_answer(text: str, correct: bool = False, feedback: str = "") -> dict:
    """Create an answer structure."""
    return {
        "text": text,
        "fraction": 100 if correct else 0,
        "feedback": feedback
    }
