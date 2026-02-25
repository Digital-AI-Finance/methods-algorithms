"""
Chart 10: Bias-Variance Visual - K=1 vs K=15 Decision Boundaries
Overlaid contourf showing jagged (K=1) vs smooth (K=15) boundaries.
"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons

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

# Generate 80 training points with partial overlap
X, y = make_moons(n_samples=80, noise=0.25, random_state=42)

# Create mesh for decision boundary
h = 0.02
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
grid = np.c_[xx.ravel(), yy.ravel()]

# Fit K=1 and K=15
knn1 = KNeighborsClassifier(n_neighbors=1).fit(X, y)
knn15 = KNeighborsClassifier(n_neighbors=15).fit(X, y)
Z1 = knn1.predict(grid).reshape(xx.shape)
Z15 = knn15.predict(grid).reshape(xx.shape)

# --- Plot ---
fig, ax = plt.subplots(figsize=(10, 6))

# K=1 boundary (red, jagged)
ax.contourf(xx, yy, Z1, alpha=0.15, levels=1,
            colors=[COLORS['red'], '#FFFFFF'], zorder=1)
ax.contour(xx, yy, Z1, levels=[0.5], colors=[COLORS['red']],
           linewidths=1.5, linestyles='--', zorder=2)

# K=15 boundary (blue, smooth)
ax.contourf(xx, yy, Z15, alpha=0.15, levels=1,
            colors=[COLORS['blue'], '#FFFFFF'], zorder=1)
ax.contour(xx, yy, Z15, levels=[0.5], colors=[COLORS['blue']],
           linewidths=2.0, linestyles='-', zorder=2)

# Scatter training points
mask0 = y == 0
mask1 = y == 1
ax.scatter(X[mask0, 0], X[mask0, 1], color=COLORS['blue'], s=50,
           edgecolors='black', linewidths=0.5, zorder=3, label='Class 0')
ax.scatter(X[mask1, 0], X[mask1, 1], color=COLORS['orange'], s=50,
           edgecolors='black', linewidths=0.5, zorder=3, label='Class 1')

# Text annotations
ax.annotate('K=1: Overfitting\n(follows noise)',
            xy=(0.5, -0.3), fontsize=12, fontweight='bold',
            color=COLORS['red'],
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor=COLORS['red'], alpha=0.9))
ax.annotate('K=15: Underfitting\n(too smooth)',
            xy=(-0.3, 1.0), fontsize=12, fontweight='bold',
            color=COLORS['blue'],
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor=COLORS['blue'], alpha=0.9))

# Legend entries for boundaries
ax.plot([], [], color=COLORS['red'], linestyle='--', linewidth=1.5, label='K=1 boundary')
ax.plot([], [], color=COLORS['blue'], linestyle='-', linewidth=2.0, label='K=15 boundary')

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_title('Bias-Variance: K=1 vs K=15')
ax.legend(loc='upper right', framealpha=0.9)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig(Path(__file__).parent / 'chart.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to: {output_path}")
