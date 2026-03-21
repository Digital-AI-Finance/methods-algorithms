"""
Shared chart style for Methods & Algorithms course.

Provides a single source of truth for rcParams, color palette, and save helper.
Import from any chart.py via:

    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
    from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
    apply_style()
"""

import inspect
import os
from pathlib import Path

import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# RC Parameters -- optimised for Beamer at 0.55-0.65 textwidth
# ---------------------------------------------------------------------------
RCPARAMS = {
    'font.size': 15,
    'axes.labelsize': 16,
    'axes.titlesize': 18,
    'xtick.labelsize': 14,
    'ytick.labelsize': 14,
    'legend.fontsize': 13,
    'figure.figsize': (10, 6),
    'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'axes.grid.axis': 'both',
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    'grid.color': '#CCCCCC',
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'savefig.facecolor': 'white',
    'savefig.bbox': 'tight',
    'lines.linewidth': 2.0,
    'scatter.edgecolors': 'white',
}

# ---------------------------------------------------------------------------
# Color palette (canonical values from CLAUDE.md)
# ---------------------------------------------------------------------------
MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLLAVENDER = '#ADADE0'
MLGRAY = '#808080'

COLORS = {
    'MLPurple': MLPURPLE,
    'MLBlue': MLBLUE,
    'MLOrange': MLORANGE,
    'MLGreen': MLGREEN,
    'MLRed': MLRED,
    'MLLavender': MLLAVENDER,
    'MLGray': MLGRAY,
}


def apply_style():
    """Apply course-wide rcParams and return the COLORS dict."""
    plt.rcParams.update(RCPARAMS)
    return COLORS


def save_chart(fig, file_path=None):
    """Save *fig* as PDF and close it.

    If *file_path* is None the output path is auto-detected from the
    caller's ``__file__`` attribute (writes ``chart.pdf`` next to the
    calling script).
    """
    if file_path is None:
        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename
        file_path = Path(caller_file).parent / 'chart.pdf'

    plt.tight_layout()
    fig.savefig(file_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"Chart saved to: {file_path}")


def add_url(fig, url):
    """Place a small URL in the bottom-right corner of *fig*."""
    plt.figtext(
        0.99, 0.01, url,
        fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7,
    )


def get_chart_dir(caller_file):
    """Return the directory containing *caller_file* as a Path."""
    return Path(caller_file).parent
