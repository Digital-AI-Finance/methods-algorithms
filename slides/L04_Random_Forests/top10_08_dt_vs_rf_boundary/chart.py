"""Ensemble Smoothing: One Tree vs Many"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_moons
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

CHART_METADATA = {
    'title': 'Ensemble Smoothing: One Tree vs Many',
    'description': 'Side-by-side decision boundaries of a single DT vs Random Forest on moons data',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/top10_08_dt_vs_rf_boundary'
}


X, y = make_moons(n_samples=300, noise=0.3, random_state=42)

dt = DecisionTreeClassifier(max_depth=None, random_state=42)
dt.fit(X, y)

rf = RandomForestClassifier(n_estimators=200, max_depth=None, random_state=42)
rf.fit(X, y)

x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300), np.linspace(y_min, y_max, 300))
grid = np.c_[xx.ravel(), yy.ravel()]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6), sharey=True)

from matplotlib.colors import ListedColormap
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()
cmap_bg = ListedColormap([MLBLUE, MLORANGE])

for ax, model, title in [(ax1, dt, "Single Decision Tree"), (ax2, rf, "Random Forest (200 Trees)")]:
    Z = model.predict(grid).reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.3, colors=[MLBLUE, MLORANGE], levels=[-0.5, 0.5, 1.5])
    ax.scatter(X[y == 0, 0], X[y == 0, 1], c=MLBLUE, edgecolors='k', s=20, linewidths=0.5, label='Class 0')
    ax.scatter(X[y == 1, 0], X[y == 1, 1], c=MLORANGE, edgecolors='k', s=20, linewidths=0.5, label='Class 1')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel("Feature 1")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

ax1.set_ylabel("Feature 2")
plt.suptitle("Ensemble Smoothing: One Tree vs Many", fontsize=16, fontweight='bold', y=1.02)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_08_dt_vs_rf_boundary/chart.pdf")
