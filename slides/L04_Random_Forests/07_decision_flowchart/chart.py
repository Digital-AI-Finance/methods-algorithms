"""Decision Flowchart - When to use Random Forests"""
import matplotlib.pyplot as plt

# Chart metadata for QR code generation
CHART_METADATA = {
    'title': 'Random Forest Decision Guide',
    'description': 'When to use Random Forests flowchart',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/07_decision_flowchart'
}
import matplotlib.patches as mpatches
from pathlib import Path

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
draw_box(ax, 0.5, 0.92, 'ML Problem', MLPURPLE, width=0.15, height=0.08)

# First decision: Classification or Regression?
draw_diamond(ax, 0.5, 0.75, 'Need\nfeature\nimportance?')
draw_arrow(ax, (0.5, 0.88), (0.5, 0.82))

# Yes branch - Feature importance needed
draw_arrow(ax, (0.58, 0.75), (0.78, 0.75), 'Yes')
draw_diamond(ax, 0.85, 0.75, 'Large\ndataset?')

# Large dataset - Yes
draw_arrow(ax, (0.85, 0.67), (0.85, 0.55), 'Yes')
draw_box(ax, 0.85, 0.48, 'Random\nForest', MLGREEN, width=0.14, height=0.1)

# Large dataset - No
draw_arrow(ax, (0.93, 0.75), (1.0, 0.75))
ax.text(1.02, 0.75, 'No: Single Tree', fontsize=9, ha='left', va='center')

# No branch - Interpretability focus
draw_arrow(ax, (0.5, 0.67), (0.5, 0.55), 'No')
draw_diamond(ax, 0.5, 0.48, 'High\naccuracy\nneeded?')

# High accuracy - Yes
draw_arrow(ax, (0.5, 0.4), (0.5, 0.28), 'Yes')
draw_diamond(ax, 0.5, 0.21, 'Non-linear\nrelations?')

# Non-linear - Yes
draw_arrow(ax, (0.58, 0.21), (0.72, 0.21), 'Yes')
draw_box(ax, 0.85, 0.21, 'Random\nForest', MLGREEN, width=0.14, height=0.1)

# Non-linear - No
draw_arrow(ax, (0.42, 0.21), (0.28, 0.21), 'No')
draw_box(ax, 0.15, 0.21, 'Linear/\nLogistic', MLORANGE, width=0.14, height=0.1)

# High accuracy - No (interpretability)
draw_arrow(ax, (0.42, 0.48), (0.2, 0.48), 'No')
draw_box(ax, 0.1, 0.48, 'Single Tree\nor Linear', MLORANGE, width=0.15, height=0.1)

# Legend
ax.text(0.02, 0.08, 'Key:', fontsize=10, fontweight='bold')
ax.text(0.02, 0.04, 'Random Forest: Best for accuracy + feature importance', fontsize=9)
ax.text(0.02, 0.00, 'Alternative: When interpretability is paramount', fontsize=9)

ax.set_xlim(-0.05, 1.1)
ax.set_ylim(-0.05, 1.0)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('When to Use Random Forests', fontsize=16, fontweight='bold', y=0.98)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 07_decision_flowchart/chart.pdf")
