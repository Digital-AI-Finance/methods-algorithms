"""Decision Flowchart - When to Use Logistic Regression"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

CHART_METADATA = {
    "title": "Logistic Regression Decision Guide",
    "description": "When to use flowchart",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L02_Logistic_Regression/07_decision_flowchart"
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False
})

MLBLUE = '#0066CC'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLORANGE = '#FF7F0E'
MLPURPLE = '#3333B2'

def draw_box(ax, x, y, text, color, width=1.8, height=0.6):
    """Draw a rounded rectangle with text."""
    box = mpatches.FancyBboxPatch((x - width/2, y - height/2), width, height,
                                   boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor=color, edgecolor='black', linewidth=1.5,
                                   alpha=0.8)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=10,
            fontweight='bold', wrap=True)

def draw_diamond(ax, x, y, text, color, size=0.8):
    """Draw a diamond shape with text."""
    diamond = mpatches.RegularPolygon((x, y), numVertices=4, radius=size/1.4,
                                       facecolor=color, edgecolor='black',
                                       linewidth=1.5, alpha=0.8)
    ax.add_patch(diamond)
    ax.text(x, y, text, ha='center', va='center', fontsize=9,
            fontweight='bold', wrap=True)

def draw_arrow(ax, x1, y1, x2, y2, label=None, label_pos=0.5):
    """Draw an arrow with optional label."""
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    if label:
        mid_x = x1 + (x2 - x1) * label_pos
        mid_y = y1 + (y2 - y1) * label_pos
        ax.text(mid_x + 0.15, mid_y, label, fontsize=9, color='gray')

fig, ax = plt.subplots(figsize=(10, 6))

# Question diamonds
draw_diamond(ax, 2, 4, 'Target\nbinary?', '#E6E6FA', 1.0)
draw_diamond(ax, 5, 4, 'Need\nprobs?', '#E6E6FA', 1.0)
draw_diamond(ax, 5, 2, 'Interpret-\nability?', '#E6E6FA', 1.0)

# Action boxes
draw_box(ax, 2, 2, 'Multiclass or\nRegression', MLRED, 1.6, 0.7)
draw_box(ax, 8, 4, 'Logistic\nRegression', MLGREEN, 1.6, 0.7)
draw_box(ax, 8, 2, 'Consider\nTree/SVM', MLORANGE, 1.6, 0.7)
draw_box(ax, 5, 0, 'Consider\nNeural Net', MLBLUE, 1.6, 0.7)

# Arrows
draw_arrow(ax, 2, 3.4, 2, 2.4, 'No')
draw_arrow(ax, 2.5, 4, 4.4, 4, 'Yes')
draw_arrow(ax, 5.6, 4, 7.2, 4, 'Yes')
draw_arrow(ax, 5, 3.4, 5, 2.6, 'No')
draw_arrow(ax, 5.6, 2, 7.2, 2, 'No')
draw_arrow(ax, 5, 1.4, 5, 0.4, 'Yes')

# Title
ax.text(5, 5.2, 'Logistic Regression Decision Guide', fontsize=14,
        ha='center', fontweight='bold', color=MLPURPLE)

ax.set_xlim(0, 10)
ax.set_ylim(-0.5, 5.5)
ax.set_aspect('equal')
ax.axis('off')

# Add URL annotation
ax.text(0.99, 0.01, CHART_METADATA['url'],
        transform=ax.transAxes,
        fontsize=7,
        color='gray',
        ha='right',
        va='bottom',
        alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 07_decision_flowchart/chart.pdf")
