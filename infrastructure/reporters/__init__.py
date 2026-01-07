"""Report generators for course progress and quality."""
from .progress_report import generate_progress_report
from .build_report import generate_build_report
from .coverage_report import generate_coverage_report
from .quality_report import generate_quality_report
from .html_dashboard import generate_html_dashboard

__all__ = [
    "generate_progress_report",
    "generate_build_report",
    "generate_coverage_report",
    "generate_quality_report",
    "generate_html_dashboard",
]
