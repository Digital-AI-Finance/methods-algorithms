"""Distance Metrics Comparison - Euclidean vs Manhattan"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    "title": "Distance Metrics Comparison",
    "description": "Euclidean vs Manhattan distance visualization",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L03_KNN_KMeans/02_distance_metrics"
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

fig, ax = plt.subplots(figsize=(10, 6))

# Two points
p1 = np.array([1, 1])
p2 = np.array([5, 4])

# Plot points
ax.scatter(*p1, s=200, c=MLBLUE, zorder=5, label='Point A (1, 1)')
ax.scatter(*p2, s=200, c=MLRED, zorder=5, label='Point B (5, 4)')
ax.text(p1[0]-0.3, p1[1]+0.3, 'A', fontsize=14, fontweight='bold')
ax.text(p2[0]+0.2, p2[1]+0.2, 'B', fontsize=14, fontweight='bold')

# Euclidean distance (straight line)
eucl_dist = np.sqrt(np.sum((p2 - p1)**2))
ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=MLGREEN, linewidth=3,
        linestyle='-', label=f'Euclidean: {eucl_dist:.2f}')

# Manhattan distance (L-shape)
manh_dist = np.sum(np.abs(p2 - p1))
ax.plot([p1[0], p2[0], p2[0]], [p1[1], p1[1], p2[1]], color=MLORANGE,
        linewidth=3, linestyle='--', label=f'Manhattan: {manh_dist:.0f}')

# Add annotations
ax.annotate('', xy=(p2[0], p1[1]), xytext=(p1[0], p1[1]),
            arrowprops=dict(arrowstyle='->', color=MLORANGE, lw=2))
ax.annotate('', xy=(p2[0], p2[1]), xytext=(p2[0], p1[1]),
            arrowprops=dict(arrowstyle='->', color=MLORANGE, lw=2))
ax.text(3, 0.6, '4 units', fontsize=11, color=MLORANGE, ha='center')
ax.text(5.4, 2.5, '3 units', fontsize=11, color=MLORANGE, ha='left')

# Formula box
formula_text = (r'$d_{Eucl} = \sqrt{\sum(x_i - y_i)^2}$' + '\n'
                r'$d_{Manh} = \sum|x_i - y_i|$')
ax.text(0.02, 0.98, formula_text, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

ax.set_xlabel('X coordinate')
ax.set_ylabel('Y coordinate')
ax.set_title('Distance Metrics: Euclidean vs Manhattan')
ax.legend(loc='lower right')
ax.set_xlim(0, 7)
ax.set_ylim(0, 5.5)
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 02_distance_metrics/chart.pdf")
