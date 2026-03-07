"""Ensemble Diversity: Tree Disagreement Matrix"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

CHART_METADATA = {
    'title': 'Ensemble Diversity: Tree Disagreement Matrix',
    'description': 'Pairwise disagreement rates among first 20 trees in a random forest',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/top10_18_ensemble_diversity'
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

X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = RandomForestClassifier(n_estimators=50, random_state=42)
clf.fit(X_train, y_train)

n_trees = 20
predictions = np.array([clf.estimators_[i].predict(X_test) for i in range(n_trees)])

disagreement = np.zeros((n_trees, n_trees))
n_test = X_test.shape[0]
for i in range(n_trees):
    for j in range(n_trees):
        disagreement[i, j] = np.mean(predictions[i] != predictions[j])

fig, ax = plt.subplots(figsize=(10, 6))

from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list('disagree', ['#FFFFFF', MLPURPLE])

im = ax.imshow(disagreement, cmap=cmap, vmin=0, interpolation='nearest')
cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label('Disagreement Rate', fontsize=13)

ax.set_xlabel("Tree Index")
ax.set_ylabel("Tree Index")
ax.set_title("Ensemble Diversity: Tree Disagreement Matrix", fontsize=16, fontweight='bold')
ax.set_xticks(range(0, n_trees, 2))
ax.set_yticks(range(0, n_trees, 2))
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_18_ensemble_diversity/chart.pdf")
