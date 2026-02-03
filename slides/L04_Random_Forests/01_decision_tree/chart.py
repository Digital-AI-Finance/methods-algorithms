"""Decision Tree Structure - Fraud detection example"""
import matplotlib.pyplot as plt

# Chart metadata for QR code generation
CHART_METADATA = {
    'title': 'Decision Tree Structure',
    'description': 'Fraud detection decision rules visualization',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/01_decision_tree'
}
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLORANGE = '#FF7F0E'

fig, ax = plt.subplots(figsize=(10, 6))

# Node positions
nodes = {
    'root': (0.5, 0.9),
    'left1': (0.25, 0.6),
    'right1': (0.75, 0.6),
    'left2a': (0.1, 0.3),
    'left2b': (0.4, 0.3),
    'right2a': (0.6, 0.3),
    'right2b': (0.9, 0.3),
}

# Node labels and colors
node_info = {
    'root': ('Amount > $500?', MLBLUE, 'white'),
    'left1': ('Time < 2am?', MLBLUE, 'white'),
    'right1': ('Foreign IP?', MLBLUE, 'white'),
    'left2a': ('Normal\n(85%)', MLGREEN, 'white'),
    'left2b': ('Fraud\n(72%)', MLRED, 'white'),
    'right2a': ('Normal\n(65%)', MLGREEN, 'white'),
    'right2b': ('Fraud\n(91%)', MLRED, 'white'),
}

# Draw nodes
for name, (x, y) in nodes.items():
    label, color, textcolor = node_info[name]
    width = 0.18 if 'left2' in name or 'right2' in name else 0.22
    height = 0.12 if 'left2' in name or 'right2' in name else 0.1

    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.02,rounding_size=0.02",
                         facecolor=color, edgecolor='black', linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center', fontsize=11,
            color=textcolor, fontweight='bold')

# Draw edges
edges = [
    ('root', 'left1', 'No'),
    ('root', 'right1', 'Yes'),
    ('left1', 'left2a', 'No'),
    ('left1', 'left2b', 'Yes'),
    ('right1', 'right2a', 'No'),
    ('right1', 'right2b', 'Yes'),
]

for start, end, label in edges:
    x1, y1 = nodes[start]
    x2, y2 = nodes[end]

    # Adjust start/end points
    y1 -= 0.05
    y2 += 0.06

    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='gray', lw=2))

    # Edge label
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    offset = -0.05 if 'left' in end else 0.05
    ax.text(mid_x + offset, mid_y + 0.02, label, fontsize=10,
            color='gray', fontweight='bold')

ax.set_xlim(0, 1)
ax.set_ylim(0.15, 1.0)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Decision Tree for Fraud Detection', fontsize=16, fontweight='bold', pad=10)

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 01_decision_tree/chart.pdf")
