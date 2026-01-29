"""Decision Flowchart - When to use PCA vs t-SNE"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

CHART_METADATA = {
    'title': 'PCA vs t-SNE Decision Guide',
    'description': 'Flowchart for choosing between PCA and t-SNE',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/07_decision_flowchart'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLORANGE = '#FF7F0E'

fig, ax = plt.subplots(figsize=(10, 6))

def draw_diamond(ax, x, y, text, color=MLBLUE):
    diamond = mpatches.RegularPolygon((x, y), numVertices=4, radius=0.12,
                                       orientation=0, facecolor=color,
                                       edgecolor='black', linewidth=2)
    ax.add_patch(diamond)
    ax.text(x, y, text, ha='center', va='center', fontsize=9,
            fontweight='bold', color='white', wrap=True)

def draw_box(ax, x, y, text, color=MLGREEN, width=0.18, height=0.1):
    box = mpatches.FancyBboxPatch((x - width/2, y - height/2), width, height,
                                   boxstyle="round,pad=0.02,rounding_size=0.02",
                                   facecolor=color, edgecolor='black', linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=9,
            fontweight='bold', color='white')

def draw_arrow(ax, start, end, label='', color='gray'):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=2))
    if label:
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        ax.text(mid_x + 0.03, mid_y, label, fontsize=9, fontweight='bold', color=color)

# Start
draw_box(ax, 0.5, 0.92, 'Dimensionality\nReduction', MLPURPLE, width=0.18, height=0.1)

# First decision: Purpose?
draw_diamond(ax, 0.5, 0.75, 'Purpose?')
draw_arrow(ax, (0.5, 0.87), (0.5, 0.82))

# Left branch: Feature extraction / Preprocessing
draw_arrow(ax, (0.42, 0.75), (0.2, 0.60), 'Preprocess')
draw_diamond(ax, 0.2, 0.52, 'Need\nreversible?')

# Reversible - Yes -> PCA
draw_arrow(ax, (0.2, 0.44), (0.2, 0.32), 'Yes')
draw_box(ax, 0.2, 0.25, 'PCA', MLGREEN, width=0.12, height=0.08)

# Reversible - No
draw_arrow(ax, (0.12, 0.52), (0.02, 0.52))
ax.text(-0.02, 0.52, 'No: Many options', fontsize=9, va='center')

# Right branch: Visualization
draw_arrow(ax, (0.58, 0.75), (0.8, 0.60), 'Visualize')
draw_diamond(ax, 0.8, 0.52, 'Linear\nstructure?')

# Linear - Yes -> PCA
draw_arrow(ax, (0.8, 0.44), (0.6, 0.32), 'Yes')
draw_box(ax, 0.6, 0.25, 'PCA', MLGREEN, width=0.12, height=0.08)

# Linear - No -> t-SNE
draw_arrow(ax, (0.88, 0.52), (0.95, 0.32), 'No')
draw_box(ax, 0.95, 0.25, 't-SNE', MLORANGE, width=0.12, height=0.08)

# Comparison table
ax.text(0.5, 0.12, 'PCA: Fast, linear, reversible, for preprocessing',
        ha='center', fontsize=10, style='italic', color='gray')
ax.text(0.5, 0.06, 't-SNE: Slow, non-linear, visualization only, preserves local structure',
        ha='center', fontsize=10, style='italic', color='gray')

ax.set_xlim(-0.1, 1.1)
ax.set_ylim(0, 1.0)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('When to Use PCA vs t-SNE', fontsize=16, fontweight='bold', y=0.98)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 07_decision_flowchart/chart.pdf")
