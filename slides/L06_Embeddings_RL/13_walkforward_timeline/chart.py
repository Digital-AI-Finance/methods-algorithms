"""
Chart: Walk-Forward Validation for RL Trading
4-fold expanding-window timeline with train/test blocks using broken_barh.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------
CHART_METADATA = {
    "title": "Walk-Forward Validation for RL Trading",
    "description": (
        "4-fold expanding-window walk-forward validation timeline. "
        "Train windows grow; test windows shift forward. Prevents look-ahead bias."
    ),
    "url": "https://digital-ai-finance.github.io/methods-algorithms/slides/L06_Embeddings_RL/13_walkforward_timeline",
}

# ---------------------------------------------------------------------------
# Style
# ---------------------------------------------------------------------------
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False
})

MLPURPLE = '#3333B2'
MLBLUE   = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN  = '#2CA02C'
MLRED    = '#D62728'

# ---------------------------------------------------------------------------
# Walk-forward data
# Encode years as floats for broken_barh; 2015 = 0, 2016 = 1, etc.
# ---------------------------------------------------------------------------
ALPHA = 0.85

# Each fold: (train_start, train_end, test_start, test_end) in year floats
folds = [
    (2015, 2017, 2017, 2018),  # Fold 1
    (2016, 2018, 2018, 2019),  # Fold 2
    (2017, 2019, 2019, 2020),  # Fold 3
    (2018, 2020, 2020, 2021),  # Fold 4
]

# Y positions: Fold 4 at bottom (y=0), Fold 1 at top (y=3)
# broken_barh: (xranges, yrange) where xranges = list of (xmin, xwidth)
BAR_HEIGHT = 0.6

fig, ax = plt.subplots()

for i, (tr_s, tr_e, te_s, te_e) in enumerate(folds):
    y_center = 3 - i          # Fold 1 at y=3, Fold 4 at y=0
    y_bottom = y_center - BAR_HEIGHT / 2

    # Training bar
    ax.broken_barh([(tr_s, tr_e - tr_s)], (y_bottom, BAR_HEIGHT),
                   facecolors=MLBLUE, alpha=ALPHA, zorder=2)

    # Test bar
    ax.broken_barh([(te_s, te_e - te_s)], (y_bottom, BAR_HEIGHT),
                   facecolors=MLORANGE, alpha=ALPHA, zorder=2)

    # Year range labels inside bars
    ax.text(tr_s + (tr_e - tr_s) / 2, y_center,
            f'{int(tr_s)}–{int(tr_e)}',
            ha='center', va='center', fontsize=11, color='white', fontweight='bold')
    ax.text(te_s + (te_e - te_s) / 2, y_center,
            f'{int(te_s)}–{int(te_e)}',
            ha='center', va='center', fontsize=11, color='white', fontweight='bold')

# ---------------------------------------------------------------------------
# Y-axis labels
# ---------------------------------------------------------------------------
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(['Fold 4', 'Fold 3', 'Fold 2', 'Fold 1'])
ax.set_ylim(-0.5, 3.7)

# ---------------------------------------------------------------------------
# X-axis: year ticks
# ---------------------------------------------------------------------------
ax.set_xlim(2014.7, 2021.5)
ax.set_xticks(range(2015, 2022))
ax.set_xticklabels([str(y) for y in range(2015, 2022)])

# ---------------------------------------------------------------------------
# Grid (x-axis only)
# ---------------------------------------------------------------------------
ax.grid(axis='x', alpha=0.3)

# ---------------------------------------------------------------------------
# Expanding window arrow annotation
# ---------------------------------------------------------------------------
ax.annotate('',
            xy=(2015, 0.5),
            xytext=(2015, 3.4),
            arrowprops=dict(arrowstyle='->', color='#555555', lw=1.5))
ax.text(2014.75, 1.9, 'Expanding\nwindow',
        ha='center', va='center', fontsize=10, color='#555555',
        rotation=90)

# ---------------------------------------------------------------------------
# "No look-ahead bias" annotation
# ---------------------------------------------------------------------------
ax.text(2021.4, 0.1, 'No look-ahead bias',
        ha='right', va='bottom', fontsize=11, color='#444444',
        style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFBE6',
                  edgecolor='#CCCC88', alpha=0.85))

# ---------------------------------------------------------------------------
# Legend
# ---------------------------------------------------------------------------
train_patch = mpatches.Patch(color=MLBLUE,   alpha=ALPHA, label='Train window')
test_patch  = mpatches.Patch(color=MLORANGE, alpha=ALPHA, label='Test window')
ax.legend(handles=[train_patch, test_patch], loc='upper right', framealpha=0.85)

# ---------------------------------------------------------------------------
# Labels, title, URL
# ---------------------------------------------------------------------------
ax.set_xlabel('Year')
ax.set_title('Walk-Forward Validation for RL Trading')

ax.text(0.99, 0.01, CHART_METADATA["url"],
        transform=ax.transAxes, fontsize=7, color='#AAAAAA',
        ha='right', va='bottom')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
