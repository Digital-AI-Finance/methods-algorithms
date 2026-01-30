#!/usr/bin/env python3
"""
Course CLI - Methods and Algorithms Course Management Tool

Usage:
    python course_cli.py <command> [options]

Commands:
    build       Build course components (slides, charts, notebooks, quizzes)
    validate    Run validation checks (latex, links, notebooks, charts)
    deploy      Deploy to GitHub/Colab
    status      Show progress dashboard
    inventory   Manage content inventory
    report      Generate reports (build, coverage, progress, quality)
    syllabus    Export syllabus (pdf, html, moodle)
"""
import argparse
import json
import sys
from pathlib import Path

# Add infrastructure to path
INFRASTRUCTURE_DIR = Path(__file__).parent
PROJECT_ROOT = INFRASTRUCTURE_DIR.parent
sys.path.insert(0, str(INFRASTRUCTURE_DIR))

from validators.latex_validator import validate_latex
from validators.link_validator import validate_links
from validators.notebook_validator import validate_notebooks
from validators.chart_validator import validate_charts
from builders.slide_builder import build_slides
from builders.chart_builder import build_charts
from builders.notebook_builder import build_notebooks
from builders.quiz_builder import build_quizzes
from reporters.progress_report import generate_progress_report


def load_manifest():
    """Load the course manifest."""
    manifest_path = PROJECT_ROOT / "manifest.json"
    with open(manifest_path, "r", encoding="utf-8") as f:
        return json.load(f)


def cmd_build(args):
    """Build course components."""
    manifest = load_manifest()

    if args.component == "slides":
        topic = args.topic if args.topic != "all" else None
        build_slides(manifest, topic=topic, verbose=args.verbose)
    elif args.component == "charts":
        topic = args.topic if args.topic != "all" else None
        build_charts(manifest, topic=topic, verbose=args.verbose)
    elif args.component == "notebooks":
        topic = args.topic if args.topic != "all" else None
        build_notebooks(manifest, topic=topic, verbose=args.verbose)
    elif args.component == "quizzes":
        quiz_id = args.topic if args.topic != "all" else None
        build_quizzes(manifest, quiz_id=quiz_id, verbose=args.verbose)
    elif args.component == "all":
        print("Building all components...")
        build_charts(manifest, verbose=args.verbose)
        build_slides(manifest, verbose=args.verbose)
        build_notebooks(manifest, verbose=args.verbose)
        build_quizzes(manifest, verbose=args.verbose)


def cmd_validate(args):
    """Run validation checks."""
    manifest = load_manifest()
    results = {}

    if args.check in ["latex", "all"]:
        print("\n=== Validating LaTeX ===")
        results["latex"] = validate_latex(manifest, strict=args.strict)

    if args.check in ["links", "all"]:
        print("\n=== Validating Links ===")
        results["links"] = validate_links(manifest, external=args.external)

    if args.check in ["notebooks", "all"]:
        print("\n=== Validating Notebooks ===")
        results["notebooks"] = validate_notebooks(manifest, execute=args.execute)

    if args.check in ["charts", "all"]:
        print("\n=== Validating Charts ===")
        results["charts"] = validate_charts(manifest, regenerate=args.regenerate)

    # Summary
    print("\n=== Validation Summary ===")
    all_passed = True
    for check, passed in results.items():
        status = "PASS" if passed else "FAIL"
        print(f"  {check}: {status}")
        if not passed:
            all_passed = False

    return 0 if all_passed else 1


def cmd_status(args):
    """Show progress dashboard."""
    manifest = load_manifest()
    report = generate_progress_report(manifest, detailed=args.detailed)
    print(report)


def cmd_inventory(args):
    """Manage content inventory."""
    manifest = load_manifest()

    if args.action == "list":
        if args.topic:
            # List assets for specific topic
            for topic in manifest["topics"]:
                if topic["id"] == args.topic:
                    print(f"\n=== {topic['id']}: {topic['title']} ===")
                    print(f"Status: {topic['status']}")
                    print("\nAssets:")
                    for asset_type, asset in topic["assets"].items():
                        if isinstance(asset, dict):
                            print(f"  {asset_type}: {asset.get('file', 'N/A')} [{asset.get('status', 'N/A')}]")
                        elif isinstance(asset, list):
                            print(f"  {asset_type}:")
                            for item in asset:
                                print(f"    - {item.get('id', 'N/A')}: {item.get('file', 'N/A')} [{item.get('status', 'N/A')}]")
                    break
        else:
            # List all topics
            print("\n=== Course Topics ===")
            for topic in manifest["topics"]:
                print(f"  {topic['id']}: {topic['title']} [{topic['status']}]")

    elif args.action == "add":
        print(f"Adding {args.type} to inventory...")
        # TODO: Implement add functionality


def cmd_report(args):
    """Generate reports."""
    manifest = load_manifest()

    if args.type == "progress":
        report = generate_progress_report(manifest, detailed=True)
        print(report)
    elif args.type == "build":
        print("Build report not yet implemented")
    elif args.type == "coverage":
        print("Coverage report not yet implemented")
    elif args.type == "quality":
        print("Quality report not yet implemented")


def cmd_syllabus(args):
    """Export syllabus."""
    print(f"Exporting syllabus to {args.format}...")
    # TODO: Implement syllabus generator


def main():
    parser = argparse.ArgumentParser(
        description="Methods and Algorithms Course Management CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Build command
    build_parser = subparsers.add_parser("build", help="Build course components")
    build_parser.add_argument("component", choices=["slides", "charts", "notebooks", "quizzes", "all"],
                              help="Component to build")
    build_parser.add_argument("--topic", default="all", help="Topic ID (e.g., L01) or 'all'")
    build_parser.set_defaults(func=cmd_build)

    # Validate command
    validate_parser = subparsers.add_parser("validate", help="Run validation checks")
    validate_parser.add_argument("check", nargs="?", default="all",
                                 choices=["latex", "links", "notebooks", "charts", "all"],
                                 help="Validation check to run")
    validate_parser.add_argument("--strict", action="store_true", help="Strict mode (fail on warnings)")
    validate_parser.add_argument("--external", action="store_true", help="Check external links")
    validate_parser.add_argument("--execute", action="store_true", help="Execute notebook cells")
    validate_parser.add_argument("--regenerate", action="store_true", help="Regenerate charts")
    validate_parser.set_defaults(func=cmd_validate)

    # Status command
    status_parser = subparsers.add_parser("status", help="Show progress dashboard")
    status_parser.add_argument("--detailed", action="store_true", help="Show detailed status")
    status_parser.set_defaults(func=cmd_status)

    # Inventory command
    inventory_parser = subparsers.add_parser("inventory", help="Manage content inventory")
    inventory_parser.add_argument("action", choices=["list", "add", "update", "remove"],
                                  help="Inventory action")
    inventory_parser.add_argument("--topic", help="Topic ID")
    inventory_parser.add_argument("--type", help="Asset type")
    inventory_parser.set_defaults(func=cmd_inventory)

    # Report command
    report_parser = subparsers.add_parser("report", help="Generate reports")
    report_parser.add_argument("type", choices=["build", "coverage", "progress", "quality"],
                               help="Report type")
    report_parser.set_defaults(func=cmd_report)

    # Syllabus command
    syllabus_parser = subparsers.add_parser("syllabus", help="Export syllabus")
    syllabus_parser.add_argument("--format", default="pdf", choices=["pdf", "html", "moodle"],
                                 help="Output format")
    syllabus_parser.set_defaults(func=cmd_syllabus)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
