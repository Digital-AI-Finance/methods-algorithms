"""Random Forest Proximity Matrix"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

CHART_METADATA = {
    'title': 'Random Forest Proximity Matrix',
    'description': 'Heatmap of sample co-occurrence in RF leaves, sorted by class',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/top10_20_proximity_matrix'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

X, y = make_classification(n_samples=100, n_features=10, n_informative=5, random_state=42)

clf = RandomForestClassifier(n_estimators=200, random_state=42)
clf.fit(X, y)

n_samples = X.shape[0]
n_estimators = len(clf.estimators_)
proximity = np.zeros((n_samples, n_samples))

for tree in clf.estimators_:
    leaves = tree.apply(X)
    for i in range(n_samples):
        same_leaf = leaves == leaves[i]
        proximity[i] += same_leaf

proximity /= n_estimators

# Sort by class label
sort_idx = np.argsort(y)
proximity_sorted = proximity[np.ix_(sort_idx, sort_idx)]
y_sorted = y[sort_idx]

fig, ax = plt.subplots(figsize=(10, 6))

from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list('prox', ['#FFFFFF', MLPURPLE, '#1a1a6e'])

im = ax.imshow(proximity_sorted, cmap=cmap, vmin=0, interpolation='nearest')
cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label('Proximity (co-occurrence rate)', fontsize=13)

# Mark class boundary
boundary = np.searchsorted(y_sorted, 1)
ax.axhline(y=boundary - 0.5, color=MLRED, linewidth=1.5, linestyle='--', alpha=0.8)
ax.axvline(x=boundary - 0.5, color=MLRED, linewidth=1.5, linestyle='--', alpha=0.8)

ax.set_xlabel("Sample Index (sorted by class)")
ax.set_ylabel("Sample Index (sorted by class)")
ax.set_title("Random Forest Proximity Matrix", fontsize=16, fontweight='bold')
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_20_proximity_matrix/chart.pdf")
