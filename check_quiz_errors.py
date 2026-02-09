#!/usr/bin/env python3
"""
Quiz Error Detector — finds rendering issues in quiz HTML files.

Checks for:
  1. Missing or empty option text (A/B/C/D)
  2. Bare | in KaTeX math (should use \\lvert/\\rvert)
  3. Unpaired/stray $ delimiters
  4. Currency $ signs that KaTeX misinterprets (e.g. $5,000)
  5. renderMathInElement(document.body) — should be element-scoped
  6. Missing correct answer key
  7. Duplicate question IDs

Usage:
    python check_quiz_errors.py                  # Check all quiz files
    python check_quiz_errors.py docs/quiz/L01*   # Check specific file(s)
    python check_quiz_errors.py --json           # JSON output for CI
"""

import json
import re
import sys
from pathlib import Path


# ---------- parsers for the two quiz formats ----------

def extract_quiz_data_format1(html: str) -> list | None:
    """Format 1 (L01-L06): const quizData = { questions: [...] }
    Options are {A:"...", B:"...", C:"...", D:"..."}; correct is a letter.
    """
    match = re.search(
        r'const\s+quizData\s*=\s*\{[^}]*questions\s*:\s*(\[.*?\])\s*\}',
        html, re.DOTALL,
    )
    if not match:
        return None
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return None


def extract_quiz_data_format2(html: str) -> list | None:
    """Format 2 (quiz1/2/3): const questions = [...]
    Options are arrays; correct is an index. Normalize to format 1.
    """
    match = re.search(r'const\s+questions\s*=\s*(\[.*?\]);\s*\n', html, re.DOTALL)
    if not match:
        return None
    raw = match.group(1)
    # Convert JS object syntax to JSON: {q:"...", options:[...], correct:0, explanation:"..."}
    # Replace unquoted keys with quoted keys
    raw = re.sub(r'(?<=[{,])\s*(q|options|correct|explanation)\s*:', r' "\1":', raw)
    # Replace single quotes with double quotes (careful with contractions)
    # Only replace quotes that are string delimiters (at start/end of values)
    raw = raw.replace('\\"', '__ESCAPED_QUOTE__')
    try:
        questions = json.loads(raw)
    except json.JSONDecodeError:
        return None

    # Normalize to format 1
    normalized = []
    letters = ("A", "B", "C", "D")
    for i, q in enumerate(questions):
        opts_list = q.get("options", [])
        opts_dict = {}
        for j, opt in enumerate(opts_list):
            if j < 4:
                opts_dict[letters[j]] = opt
        correct_idx = q.get("correct", 0)
        correct_letter = letters[correct_idx] if correct_idx < 4 else "A"
        normalized.append({
            "id": i + 1,
            "question": q.get("q", ""),
            "options": opts_dict,
            "correct": correct_letter,
            "explanation": q.get("explanation", ""),
        })
    return normalized


def extract_quiz_data(html: str) -> list | None:
    """Try both formats."""
    result = extract_quiz_data_format1(html)
    if result is not None:
        return result
    return extract_quiz_data_format2(html)


# ---------- checks ----------

def check_option_text(questions: list) -> list:
    """Check for empty/missing option text."""
    errors = []
    for q in questions:
        qid = q.get("id", "?")
        opts = q.get("options", {})
        for letter in ("A", "B", "C", "D"):
            if letter not in opts:
                errors.append({
                    "type": "missing_option",
                    "severity": "ERROR",
                    "question": qid,
                    "detail": f"Option {letter} is missing entirely",
                })
            elif not opts[letter] or not opts[letter].strip():
                errors.append({
                    "type": "empty_option",
                    "severity": "ERROR",
                    "question": qid,
                    "detail": f"Option {letter} is empty or whitespace-only",
                })
    return errors


def check_bare_pipe_in_math(questions: list) -> list:
    """Check for bare | in math that should use \\lvert/\\rvert.

    Skips conditional probability P(a|s), \\pi(a|s), norm ||x||.
    """
    errors = []
    for q in questions:
        qid = q.get("id", "?")
        texts = []
        for letter in ("A", "B", "C", "D"):
            opt = q.get("options", {}).get(letter, "")
            if opt:
                texts.append((f"option {letter}", opt))
        expl = q.get("explanation", "")
        if expl:
            texts.append(("explanation", expl))
        question_text = q.get("question", "")
        if question_text:
            texts.append(("question", question_text))

        for location, text in texts:
            for m in re.finditer(r'\$([^$]+)\$', text):
                math = m.group(1)
                # Skip conditional probability: P(x|y), \pi(a|s), etc.
                if re.search(r'[\w}]\([^)]*\|[^)]*\)', math):
                    continue
                # Skip norm notation ||x||
                if '||' in math:
                    continue
                # Check for bare single | after removing safe patterns
                cleaned = re.sub(
                    r'\\lvert|\\rvert|\\lVert|\\rVert|\\left\||\\right\|',
                    '', math,
                )
                if '|' in cleaned:
                    errors.append({
                        "type": "bare_pipe",
                        "severity": "WARNING",
                        "question": qid,
                        "detail": (f"Bare | in math in {location}: "
                                   f"${math}$ — use \\lvert/\\rvert"),
                    })
    return errors


def _is_currency_dollar(text: str, pos: int) -> bool:
    """Detect if $ at `pos` is a currency sign, not a KaTeX delimiter.

    Currency pattern: $ followed by digit+comma+digits (e.g. $5,000 or $3,500.50)
    Valid math: $0.5$, $\\lambda$, $1 - x^2$ — these are KaTeX.
    """
    after = text[pos + 1:]
    # Currency: $X,XXX  or  $X,XXX.XX  (comma-separated thousands)
    if re.match(r'\d{1,3},\d{3}', after):
        return True
    return False


def check_dollar_signs(questions: list) -> list:
    """Check for stray/unpaired $ and currency $ signs."""
    errors = []
    for q in questions:
        qid = q.get("id", "?")
        texts = [
            ("question", q.get("question", "")),
            ("explanation", q.get("explanation", "")),
        ]
        for letter in ("A", "B", "C", "D"):
            opt = q.get("options", {}).get(letter, "")
            texts.append((f"option {letter}", opt))

        for location, text in texts:
            if not text:
                continue
            # Count $ signs
            dollar_count = text.count("$")
            if dollar_count % 2 != 0:
                errors.append({
                    "type": "unpaired_dollar",
                    "severity": "ERROR",
                    "question": qid,
                    "detail": (f"Odd number of $ ({dollar_count}) in "
                               f"{location}: {text[:80]}"),
                })

            # Check for currency $ (e.g. $5,000 — NOT $0.5$ which is math)
            for m in re.finditer(r'\$', text):
                if _is_currency_dollar(text, m.start()):
                    errors.append({
                        "type": "currency_dollar",
                        "severity": "ERROR",
                        "question": qid,
                        "detail": (f"Currency $ in {location} will break "
                                   f"KaTeX: ...{text[max(0,m.start()-10):m.start()+20]}..."),
                    })
                    break  # one per field is enough
    return errors


def check_correct_answer(questions: list) -> list:
    """Check that correct answer key exists and matches an option."""
    errors = []
    for q in questions:
        qid = q.get("id", "?")
        correct = q.get("correct")
        opts = q.get("options", {})
        if correct is None:
            errors.append({
                "type": "missing_correct",
                "severity": "ERROR",
                "question": qid,
                "detail": "No 'correct' key defined",
            })
        elif correct not in opts:
            errors.append({
                "type": "invalid_correct",
                "severity": "ERROR",
                "question": qid,
                "detail": (f"Correct answer '{correct}' not in "
                           f"options {list(opts.keys())}"),
            })
    return errors


def check_duplicate_ids(questions: list) -> list:
    """Check for duplicate question IDs."""
    errors = []
    seen = {}
    for q in questions:
        qid = q.get("id", "?")
        if qid in seen:
            errors.append({
                "type": "duplicate_id",
                "severity": "ERROR",
                "question": qid,
                "detail": f"Question ID {qid} appears multiple times",
            })
        seen[qid] = True
    return errors


def check_rendermath_scope(html: str) -> list:
    """Check if renderMathInElement targets document.body (should be scoped)."""
    errors = []
    if "renderMathInElement(document.body" in html:
        errors.append({
            "type": "body_scope_render",
            "severity": "WARNING",
            "question": "N/A",
            "detail": ("renderMathInElement(document.body) — should be scoped "
                       "to quiz content elements to prevent cross-element issues"),
        })
    return errors


# ---------- runner ----------

def check_quiz_file(filepath: Path) -> dict:
    """Run all checks on a single quiz HTML file."""
    html = filepath.read_text(encoding="utf-8")
    result = {
        "file": str(filepath.name),
        "path": str(filepath),
        "errors": [],
        "warnings": [],
    }

    # Check renderMath scope (HTML-level check)
    for issue in check_rendermath_scope(html):
        if issue["severity"] == "ERROR":
            result["errors"].append(issue)
        else:
            result["warnings"].append(issue)

    # Extract quiz data (tries both formats)
    questions = extract_quiz_data(html)
    if questions is None:
        result["errors"].append({
            "type": "parse_error",
            "severity": "ERROR",
            "question": "N/A",
            "detail": "Could not parse quiz data from HTML",
        })
        return result

    result["question_count"] = len(questions)

    # Run all question-level checks
    checkers = [
        check_option_text,
        check_bare_pipe_in_math,
        check_dollar_signs,
        check_correct_answer,
        check_duplicate_ids,
    ]
    for checker in checkers:
        for issue in checker(questions):
            if issue["severity"] == "ERROR":
                result["errors"].append(issue)
            else:
                result["warnings"].append(issue)

    return result


def main():
    json_output = "--json" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]

    if args:
        files = []
        for pattern in args:
            files.extend(Path(".").glob(pattern))
    else:
        quiz_dir = Path(__file__).parent / "docs" / "quiz"
        files = sorted(quiz_dir.glob("*.html"))

    if not files:
        print("No quiz files found.")
        sys.exit(1)

    all_results = []
    total_errors = 0
    total_warnings = 0

    for f in files:
        result = check_quiz_file(f)
        all_results.append(result)
        total_errors += len(result["errors"])
        total_warnings += len(result["warnings"])

    if json_output:
        print(json.dumps({
            "files": len(all_results),
            "total_errors": total_errors,
            "total_warnings": total_warnings,
            "results": all_results,
        }, indent=2))
    else:
        print("=" * 60)
        print("QUIZ ERROR DETECTOR")
        print("=" * 60)
        print()

        for result in all_results:
            errors = result["errors"]
            warnings = result["warnings"]
            icon = "PASS" if not errors else "FAIL"
            qcount = result.get("question_count", "?")
            print(f"  [{icon}] {result['file']} ({qcount}Q): "
                  f"{len(errors)} errors, {len(warnings)} warnings")

            for issue in errors:
                print(f"        ERROR  Q{issue['question']}: "
                      f"[{issue['type']}] {issue['detail']}")
            for issue in warnings:
                print(f"        WARN   Q{issue['question']}: "
                      f"[{issue['type']}] {issue['detail']}")

        print()
        print("=" * 60)
        print(f"Files: {len(all_results)} | "
              f"Errors: {total_errors} | "
              f"Warnings: {total_warnings} | "
              f"Status: {'PASSED' if total_errors == 0 else 'FAILED'}")
        print("=" * 60)

    sys.exit(1 if total_errors > 0 else 0)


if __name__ == "__main__":
    main()
