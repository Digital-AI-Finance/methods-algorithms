"""Scatter plot with axis-aligned decision boundaries from a depth-3 tree."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.inspection import DecisionBoundaryDisplay
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()


X, y = make_classification(n_samples=300, n_features=2, n_redundant=0,
                           n_clusters_per_class=2, random_state=42)
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X, y)

fig, ax = plt.subplots()
disp = DecisionBoundaryDisplay.from_estimator(
    clf, X, ax=ax, alpha=0.3, response_method='predict',
    cmap=plt.cm.coolwarm, grid_resolution=200
)

mask0 = y == 0
mask1 = y == 1
ax.scatter(X[mask0, 0], X[mask0, 1], c=MLBLUE, edgecolors='white',
           linewidth=0.5, s=30, label='Class 0', zorder=3)
ax.scatter(X[mask1, 0], X[mask1, 1], c=MLORANGE, edgecolors='white',
           linewidth=0.5, s=30, label='Class 1', zorder=3)

ax.annotate("Each rectangle = one leaf node", xy=(0.5, 0.95),
            xycoords='axes fraction', fontsize=12, fontweight='bold',
            color=MLPURPLE, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.set_title("Decision Tree: Axis-Aligned Decision Boundaries")
ax.legend(loc='lower right')

plt.tight_layout()
fig.savefig(Path(__file__).parent / "chart.pdf", bbox_inches='tight', facecolor='white')
plt.close(fig)
print("10_dt_decision_boundary/chart.pdf created")
