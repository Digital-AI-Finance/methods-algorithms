"""
Chart 12: K-Means Worked Example - Iteration 1
Shows 8 points, initial centroids, assignments, and centroid movement.
"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False,
})

COLORS = {
    'purple': '#3333B2', 'blue': '#0066CC', 'orange': '#FF7F0E',
    'green': '#2CA02C', 'red': '#D62728', 'lavender': '#ADADE0', 'gray': '#808080',
}

np.random.seed(42)

# 8 data points in 2 visible groups
group1 = np.array([[1.5, 2.0], [2.0, 3.0], [2.5, 2.5], [1.0, 3.5]])
group2 = np.array([[6.0, 6.5], [7.0, 5.5], [6.5, 7.0], [7.5, 6.0]])
X = np.vstack([group1, group2])

# Initial centroids (simulate K-Means++ style: one from each region but offset)
old_c0 = np.array([2.5, 3.5])   # near group 1 but offset
old_c1 = np.array([6.0, 5.5])   # near group 2 but offset

# Assign points to nearest old centroid
def assign(X, c0, c1):
    d0 = np.sqrt(np.sum((X - c0)**2, axis=1))
    d1 = np.sqrt(np.sum((X - c1)**2, axis=1))
    return (d1 < d0).astype(int)  # 0 = cluster 0, 1 = cluster 1

labels_old = assign(X, old_c0, old_c1)

# New centroids = mean of assigned points
new_c0 = X[labels_old == 0].mean(axis=0)
new_c1 = X[labels_old == 1].mean(axis=0)

# --- Plot ---
fig, ax = plt.subplots(figsize=(10, 6))

cluster_colors = [COLORS['blue'], COLORS['orange']]

# Data points colored by assignment
for c_id in [0, 1]:
    mask = labels_old == c_id
    ax.scatter(X[mask, 0], X[mask, 1], color=cluster_colors[c_id], s=150,
               edgecolors='black', linewidths=1.0, zorder=3,
               label=f'Cluster {c_id}')

# Old centroids (gray diamonds)
ax.scatter(*old_c0, color=COLORS['gray'], marker='D', s=200,
           edgecolors='black', linewidths=1.2, zorder=4, label='Old centroids')
ax.scatter(*old_c1, color=COLORS['gray'], marker='D', s=200,
           edgecolors='black', linewidths=1.2, zorder=4)

# New centroids (purple diamonds)
ax.scatter(*new_c0, color=COLORS['purple'], marker='D', s=200,
           edgecolors='black', linewidths=1.2, zorder=5, label='New centroids')
ax.scatter(*new_c1, color=COLORS['purple'], marker='D', s=200,
           edgecolors='black', linewidths=1.2, zorder=5)

# Dashed arrows from old to new centroids
ax.annotate('', xy=new_c0, xytext=old_c0,
            arrowprops=dict(arrowstyle='->', color=COLORS['red'],
                            linestyle='--', lw=2.0), zorder=4)
ax.annotate('', xy=new_c1, xytext=old_c1,
            arrowprops=dict(arrowstyle='->', color=COLORS['red'],
                            linestyle='--', lw=2.0), zorder=4)

# Text annotations
ax.text(0.5, 0.95, "Iteration 1: Assign $\\rightarrow$ Update $\\rightarrow$ Centroids move",
        transform=ax.transAxes, fontsize=13, fontweight='bold',
        ha='center', va='top',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                  edgecolor=COLORS['purple'], alpha=0.9))

ax.text(0.02, 0.02,
        "Initial centroids (K-Means++) $\\rightarrow$ After 1 iteration",
        transform=ax.transAxes, fontsize=11, color=COLORS['gray'],
        ha='left', va='bottom')

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_title('K-Means Worked Example: One Iteration')
ax.legend(loc='center right', framealpha=0.9)
ax.set_xlim(-0.5, 9.5)
ax.set_ylim(0.5, 8.5)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig(Path(__file__).parent / 'chart.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to: {output_path}")
