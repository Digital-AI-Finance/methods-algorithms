"""KNN Decision Boundaries - Effect of K on classification"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    "title": "KNN Decision Boundaries",
    "description": "Effect of K on classification decision boundaries",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L03_KNN_KMeans/01_knn_boundaries"
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

np.random.seed(42)

# Generate synthetic data
n_per_class = 50
X0 = np.random.randn(n_per_class, 2) * 0.8 + np.array([-1, 0])
X1 = np.random.randn(n_per_class, 2) * 0.8 + np.array([1, 0])
X2 = np.random.randn(n_per_class, 2) * 0.8 + np.array([0, 1.5])
X = np.vstack([X0, X1, X2])
y = np.array([0] * n_per_class + [1] * n_per_class + [2] * n_per_class)

# Create decision boundary mesh
h = 0.05
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

from sklearn.neighbors import KNeighborsClassifier

fig, ax = plt.subplots(figsize=(10, 6))

# Use K=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot decision regions
colors = [MLRED, MLGREEN, MLBLUE]
ax.contourf(xx, yy, Z, levels=[-0.5, 0.5, 1.5, 2.5], colors=colors, alpha=0.2)
ax.contour(xx, yy, Z, levels=[0.5, 1.5], colors='gray', linestyles='--', linewidths=2)

# Plot data points
for i, (color, label) in enumerate(zip(colors, ['Class A', 'Class B', 'Class C'])):
    ax.scatter(X[y == i, 0], X[y == i, 1], c=color, s=60, alpha=0.8,
               label=label, edgecolors='white', linewidth=0.5)

ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_title('KNN Decision Boundaries (K=5)')
ax.legend(loc='upper right')
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 01_knn_boundaries/chart.pdf")
