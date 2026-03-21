"""Random Forest: Prediction Probability Landscape"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_moons
from sklearn.ensemble import RandomForestClassifier

CHART_METADATA = {
    'title': 'Random Forest: Prediction Probability Landscape',
    'description': 'Continuous probability heatmap of RF predictions on moons dataset',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/top10_16_probability_heatmap'
}


X, y = make_moons(n_samples=300, noise=0.3, random_state=42)

clf = RandomForestClassifier(n_estimators=200, random_state=42)
clf.fit(X, y)

x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300), np.linspace(y_min, y_max, 300))
grid = np.c_[xx.ravel(), yy.ravel()]

Z = clf.predict_proba(grid)[:, 1].reshape(xx.shape)

# Custom colormap from MLBLUE to MLORANGE
from matplotlib.colors import LinearSegmentedColormap
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()
cmap = LinearSegmentedColormap.from_list('ml_prob', [MLBLUE, '#FFFFFF', MLORANGE])

fig, ax = plt.subplots(figsize=(10, 6))

pcm = ax.pcolormesh(xx, yy, Z, cmap=cmap, vmin=0, vmax=1, shading='auto')
ax.grid(False)
ax.scatter(X[y == 0, 0], X[y == 0, 1], c=MLBLUE, edgecolors='k', s=30, linewidths=0.7, label='Class 0', zorder=5)
ax.scatter(X[y == 1, 0], X[y == 1, 1], c=MLORANGE, edgecolors='k', s=30, linewidths=0.7, label='Class 1', zorder=5)

cbar = plt.colorbar(pcm, ax=ax, shrink=0.8)
cbar.set_label('P(Class = 1)', fontsize=13)

ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.set_title("Random Forest: Prediction Probability Landscape", fontsize=16, fontweight='bold')
ax.legend(loc='upper left', framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_16_probability_heatmap/chart.pdf")
