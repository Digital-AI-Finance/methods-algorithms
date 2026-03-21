"""Partial Dependence: How Features Affect Predictions"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import partial_dependence
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'Partial Dependence: How Features Affect Predictions',
    'description': 'PDP lines for top 2 features by importance with rug plots',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/top10_10_partial_dependence'
}


feature_names = ['Amount', 'Frequency', 'Distance', 'Time', 'Device', 'Country']
X, y = make_classification(n_samples=1000, n_features=6, n_informative=4, random_state=42)

clf = RandomForestClassifier(n_estimators=200, random_state=42)
clf.fit(X, y)

importances = clf.feature_importances_
top2_idx = np.argsort(importances)[-2:][::-1]

fig, ax = plt.subplots(figsize=(10, 6))

for i, (feat_idx, color) in enumerate(zip(top2_idx, [MLBLUE, MLORANGE])):
    pdp_result = partial_dependence(clf, X, features=[feat_idx], kind='average')
    pd_values = pdp_result['average'][0]
    feat_values = pdp_result['grid_values'][0]

    ax.plot(feat_values, pd_values, color=color, linewidth=2.5,
            label=f"{feature_names[feat_idx]} (importance={importances[feat_idx]:.3f})")

    # Rug plot
    ax.plot(X[:, feat_idx], np.full(len(X), ax.get_ylim()[0] if i == 0 else pd_values.min() - 0.02),
            '|', color=color, alpha=0.15, markersize=8)

# Redo rug after axis limits are set
ax.set_ylim(auto=True)
y_bottom = ax.get_ylim()[0]
for feat_idx, color in zip(top2_idx, [MLBLUE, MLORANGE]):
    ax.plot(X[:, feat_idx], np.full(len(X), y_bottom), '|', color=color, alpha=0.15, markersize=8)

ax.set_xlabel("Feature Value")
ax.set_ylabel("Partial Dependence")
ax.set_title("Partial Dependence: How Features Affect Predictions", fontsize=16, fontweight='bold')
ax.legend(loc='best', framealpha=0.9)
ax.grid(True, alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_10_partial_dependence/chart.pdf")
