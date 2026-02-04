"""Decision Flowchart - When to use embeddings vs RL"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLORANGE = '#FF7F0E'

CHART_METADATA = {
    "title": "Embeddings & RL Decision Guide",
    "description": "When to use flowchart for embeddings and reinforcement learning",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/07_decision_flowchart"
}

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
draw_box(ax, 0.5, 0.92, 'ML Task', MLPURPLE, width=0.16, height=0.08)

# First decision: Data type?
draw_diamond(ax, 0.5, 0.75, 'Data\ntype?')
draw_arrow(ax, (0.5, 0.88), (0.5, 0.82))

# Left branch: Text/Categorical
draw_arrow(ax, (0.42, 0.75), (0.2, 0.60), 'Text')
draw_diamond(ax, 0.2, 0.52, 'Need\nsemantics?')

# Semantics - Yes -> Embeddings
draw_arrow(ax, (0.2, 0.44), (0.2, 0.32), 'Yes')
draw_box(ax, 0.2, 0.25, 'Embeddings', MLBLUE, width=0.14, height=0.08)

# Semantics - No -> One-hot
draw_arrow(ax, (0.12, 0.52), (0.02, 0.52))
ax.text(-0.02, 0.52, 'No: One-hot', fontsize=9, va='center')

# Right branch: Sequential decisions
draw_arrow(ax, (0.58, 0.75), (0.8, 0.60), 'Sequential')
draw_diamond(ax, 0.8, 0.52, 'Delayed\nreward?')

# Delayed reward - Yes -> RL
draw_arrow(ax, (0.8, 0.44), (0.8, 0.32), 'Yes')
draw_box(ax, 0.8, 0.25, 'RL', MLORANGE, width=0.12, height=0.08)

# Delayed reward - No -> Supervised
draw_arrow(ax, (0.88, 0.52), (0.98, 0.52))
ax.text(1.02, 0.52, 'No: Supervised', fontsize=9, va='center')

# Middle branch
draw_arrow(ax, (0.5, 0.68), (0.5, 0.45), 'Numeric')
ax.text(0.52, 0.56, 'Numeric', fontsize=9, color='gray')
draw_box(ax, 0.5, 0.38, 'Standard ML', '#808080', width=0.14, height=0.08)

# Bottom notes
ax.text(0.5, 0.12, 'Embeddings: Text, categorical -> dense vectors (Word2Vec, BERT)',
        ha='center', fontsize=10, style='italic', color='gray')
ax.text(0.5, 0.06, 'RL: Sequential decisions with delayed rewards (trading, games)',
        ha='center', fontsize=10, style='italic', color='gray')

ax.set_xlim(-0.1, 1.1)
ax.set_ylim(0, 1.0)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('When to Use Embeddings vs RL', fontsize=16, fontweight='bold', y=0.98)

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 07_decision_flowchart/chart.pdf")
