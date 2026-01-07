#!/usr/bin/env python
"""Run the course audit and generate all reports."""
import sys
from pathlib import Path

# Add infrastructure to path
sys.path.insert(0, str(Path(__file__).parent / "infrastructure"))

from auditors.audit_system import run_full_audit
from auditors.report_generator import generate_all_reports

if __name__ == "__main__":
    print("Running full audit...")
    result = run_full_audit(include_functional=True)

    print("\nGenerating all reports...")
    reports = generate_all_reports(result)

    print("\nAudit complete!")
    print(f"  - Console output shown above")
    print(f"  - JSON: audit_report.json")
    print(f"  - Markdown: audit_report.md")
    print(f"  - HTML: audit_dashboard.html")
