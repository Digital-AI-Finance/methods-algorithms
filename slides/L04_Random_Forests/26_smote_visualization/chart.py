"""SMOTE: Synthetic Minority Oversampling"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.neighbors import NearestNeighbors

CHART_METADATA = {
    'title': 'SMOTE: Synthetic Minority Oversampling',
    'description': 'Visualizes manual SMOTE implementation on 2D imbalanced data with interpolation lines',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/26_smote_visualization'
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

X, y = make_classification(n_samples=220, n_features=2, n_informative=2, n_redundant=0,
                           weights=[0.9, 0.1], random_state=42, n_clusters_per_class=1)

X_majority = X[y == 0]
X_minority = X[y == 1]

# Manual SMOTE implementation
np.random.seed(42)
k = 5
nn = NearestNeighbors(n_neighbors=k + 1)  # +1 because point itself is included
nn.fit(X_minority)
distances, indices = nn.kneighbors(X_minority)

synthetic_points = []
interpolation_lines = []  # Store (parent, synthetic) pairs for drawing lines
n_synthetic_per_point = max(1, len(X_majority) // len(X_minority) - 1)

for i in range(len(X_minority)):
    neighbors = indices[i, 1:]  # exclude self
    for _ in range(n_synthetic_per_point):
        neighbor_idx = neighbors[np.random.randint(0, k)]
        lam = np.random.uniform(0, 1)
        synthetic = X_minority[i] + lam * (X_minority[neighbor_idx] - X_minority[i])
        synthetic_points.append(synthetic)
        interpolation_lines.append((X_minority[i], synthetic, X_minority[neighbor_idx]))

synthetic_points = np.array(synthetic_points)

fig, ax = plt.subplots()

# Majority class
ax.scatter(X_majority[:, 0], X_majority[:, 1], c=MLBLUE, alpha=0.35, s=20,
           label=f'Majority (n={len(X_majority)})', zorder=2)

# Original minority
ax.scatter(X_minority[:, 0], X_minority[:, 1], c=MLRED, s=60, edgecolors='white',
           linewidth=0.5, label=f'Minority (n={len(X_minority)})', zorder=4)

# Synthetic minority
ax.scatter(synthetic_points[:, 0], synthetic_points[:, 1], c=MLORANGE, s=60,
           marker='D', edgecolors='white', linewidth=0.5,
           label=f'Synthetic (n={len(synthetic_points)})', zorder=3)

# Draw 4 example interpolation lines
rng = np.random.RandomState(123)
line_indices = rng.choice(len(interpolation_lines), size=min(4, len(interpolation_lines)), replace=False)
for idx in line_indices:
    parent, synth, neighbor = interpolation_lines[idx]
    ax.plot([parent[0], synth[0]], [parent[1], synth[1]],
            color='gray', linestyle='--', linewidth=1.2, alpha=0.7, zorder=1)

ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_title(CHART_METADATA['title'])
ax.legend(loc='best', framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 26_smote_visualization/chart.pdf")
