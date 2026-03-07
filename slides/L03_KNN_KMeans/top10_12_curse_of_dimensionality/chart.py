"""Curse of Dimensionality - KNN accuracy degrades as feature count increases."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score

CHART_METADATA = {
    "title": "Curse of Dimensionality: KNN Accuracy vs Feature Count",
    "description": "KNN 5-fold CV accuracy across increasing feature dimensions",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L03_KNN_KMeans/top10_12_curse_of_dimensionality"
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

dims = [2, 5, 10, 20, 50, 100, 200]
means = []
stds = []

for d in dims:
    X, y = make_classification(n_samples=500, n_features=d, n_informative=2,
                               n_redundant=0, n_repeated=0,
                               random_state=42)
    knn = KNeighborsClassifier(n_neighbors=5)
    scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
    means.append(scores.mean())
    stds.append(scores.std())

means = np.array(means)
stds = np.array(stds)

fig, ax = plt.subplots(figsize=(10, 6))

ax.fill_between(dims, means - stds, means + stds, alpha=0.2, color=MLBLUE)
ax.plot(dims, means, color=MLBLUE, marker='o', markersize=8, linewidth=2.5,
        markeredgecolor='white', markeredgewidth=1.5, zorder=5)

# Annotate best and worst
best_idx = np.argmax(means)
ax.annotate(f'{means[best_idx]:.3f}', (dims[best_idx], means[best_idx]),
            textcoords="offset points", xytext=(0, 15), ha='center',
            fontsize=12, fontweight='bold', color=MLGREEN)
ax.annotate(f'{means[-1]:.3f}', (dims[-1], means[-1]),
            textcoords="offset points", xytext=(0, -18), ha='center',
            fontsize=12, fontweight='bold', color=MLRED)

ax.set_xscale('log')
ax.set_xticks(dims)
ax.set_xticklabels([str(d) for d in dims])
ax.set_xlabel('Number of Features')
ax.set_ylabel('5-Fold CV Accuracy')
ax.set_title('Curse of Dimensionality: KNN Accuracy vs Feature Count', fontweight='bold')
ax.grid(True, alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_12_curse_of_dimensionality/chart.pdf")
