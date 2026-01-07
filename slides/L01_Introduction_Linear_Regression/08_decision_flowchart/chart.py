"""Decision Flowchart - When to Use Linear Regression"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# Chart settings
plt.rcParams.update({
    'font.size': 11, 'figure.figsize': (10, 6), 'figure.dpi': 150
})

# Colors
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

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Question boxes (diamonds)
draw_diamond(ax, 2, 4, 'Target\ncontinuous?', '#E6E6FA', 1.0)
draw_diamond(ax, 5, 4, 'Linear\nrelation?', '#E6E6FA', 1.0)
draw_diamond(ax, 5, 2, 'Interpret-\nability?', '#E6E6FA', 1.0)

# Action boxes (rectangles)
draw_box(ax, 2, 2, 'Use\nClassification', MLRED, 1.5, 0.7)
draw_box(ax, 8, 4, 'Linear\nRegression', MLGREEN, 1.6, 0.7)
draw_box(ax, 8, 2, 'Consider\nTree/NN', MLORANGE, 1.6, 0.7)
draw_box(ax, 5, 0, 'Polynomial\nor Splines', MLBLUE, 1.6, 0.7)

# Arrows
draw_arrow(ax, 2, 3.5, 2, 2.4, 'No')
draw_arrow(ax, 2.5, 4, 4.4, 4, 'Yes')
draw_arrow(ax, 5.6, 4, 7.2, 4, 'Yes')
draw_arrow(ax, 5, 3.4, 5, 2.6, 'No')
draw_arrow(ax, 5.6, 2, 7.2, 2, 'No')
draw_arrow(ax, 5, 1.4, 5, 0.4, 'Yes')

# Title
ax.text(5, 5.2, 'Linear Regression Decision Guide', fontsize=14,
        ha='center', fontweight='bold', color=MLPURPLE)

# Settings
ax.set_xlim(0, 10)
ax.set_ylim(-0.5, 5.5)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 08_decision_flowchart/chart.pdf")
