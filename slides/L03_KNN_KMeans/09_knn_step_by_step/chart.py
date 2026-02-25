"""
Chart 09: KNN Step-by-Step with K=3 Voting
Shows query point, 3 nearest neighbors, voting annotation, neighborhood circle.
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

# 12 training points: 8 class A (blue), 4 class B (orange)
# Arrange so query at (5, 5) has 2 blue and 1 orange among 3 nearest
class_a_x = np.array([3.0, 4.0, 4.5, 6.5, 7.0, 2.0, 8.0, 3.5])
class_a_y = np.array([6.0, 4.5, 5.5, 6.0, 4.0, 3.0, 7.0, 7.5])
class_b_x = np.array([5.5, 6.0, 7.5, 8.0])
class_b_y = np.array([4.0, 2.5, 5.5, 3.0])

query = np.array([5.0, 5.0])

# Compute distances to query
all_x = np.concatenate([class_a_x, class_b_x])
all_y = np.concatenate([class_a_y, class_b_y])
labels = np.array([0]*8 + [1]*4)  # 0=A(blue), 1=B(orange)
dists = np.sqrt((all_x - query[0])**2 + (all_y - query[1])**2)

# 3 nearest neighbors
k = 3
nn_idx = np.argsort(dists)[:k]
nn_labels = labels[nn_idx]
radius = dists[nn_idx[-1]]  # distance to 3rd neighbor

# --- Plot ---
fig, ax = plt.subplots(figsize=(10, 6))

# Shaded neighborhood circle
circle = plt.Circle(query, radius * 1.05, color=COLORS['lavender'],
                    alpha=0.25, zorder=1)
ax.add_patch(circle)

# Training points
ax.scatter(class_a_x, class_a_y, color=COLORS['blue'], s=100, zorder=3,
           edgecolors='black', linewidths=0.8, label='Class A (Blue)')
ax.scatter(class_b_x, class_b_y, color=COLORS['orange'], s=100, zorder=3,
           edgecolors='black', linewidths=0.8, label='Class B (Orange)')

# Draw dashed lines to 3 nearest neighbors
for idx in nn_idx:
    ax.plot([query[0], all_x[idx]], [query[1], all_y[idx]],
            color=COLORS['gray'], linestyle='--', linewidth=1.5, zorder=2)

# Query point
ax.scatter(query[0], query[1], color=COLORS['red'], s=300, marker='*',
           zorder=5, edgecolors='black', linewidths=0.8, label='Query point')

# Vote annotation
n_blue = np.sum(nn_labels == 0)
n_orange = np.sum(nn_labels == 1)
vote_text = f"Vote: {n_blue} Blue, {n_orange} Orange\n$\\rightarrow$ Predict: Blue"
ax.annotate(vote_text, xy=(query[0], query[1]),
            xytext=(query[0] + 2.0, query[1] + 1.8),
            fontsize=13, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor=COLORS['blue'], alpha=0.9),
            arrowprops=dict(arrowstyle='->', color=COLORS['blue'], lw=1.5),
            zorder=6)

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_title('KNN Classification: K = 3 Voting')
ax.legend(loc='lower right', framealpha=0.9)
ax.set_xlim(0.5, 9.5)
ax.set_ylim(1.0, 9.0)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig(Path(__file__).parent / 'chart.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to: {output_path}")
