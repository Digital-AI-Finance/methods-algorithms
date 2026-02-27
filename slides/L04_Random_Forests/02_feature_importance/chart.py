"""Feature Importance - Random Forest for fraud detection"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from pathlib import Path

# Chart metadata for QR code generation
CHART_METADATA = {
    'title': 'Feature Importance',
    'description': 'Random Forest feature importance ranking',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/02_feature_importance'
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
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLORANGE = '#FF7F0E'

np.random.seed(42)

# Generate classification data and fit RandomForest with sklearn
X, y = make_classification(n_samples=500, n_features=8, n_informative=4, random_state=42)
features = ['Amount', 'Time', 'IP_Risk', 'Velocity', 'Country', 'Device', 'History', 'Age']
rf = RandomForestClassifier(n_estimators=100, random_state=42).fit(X, y)
importances = rf.feature_importances_
# Compute std from individual tree importances
std = np.std([tree.feature_importances_ for tree in rf.estimators_], axis=0)

# Sort by importance
indices = np.argsort(importances)
features = [features[i] for i in indices]
importances = importances[indices]
std = std[indices]

# Colors based on importance
colors = [MLBLUE if imp > 0.1 else MLORANGE if imp > 0.05 else 'gray'
          for imp in importances]

fig, ax = plt.subplots(figsize=(10, 6))

y_pos = np.arange(len(features))
bars = ax.barh(y_pos, importances, xerr=std, align='center',
               color=colors, edgecolor='black', linewidth=1, capsize=3)

ax.set_yticks(y_pos)
ax.set_yticklabels(features)
ax.set_xlabel('Mean Decrease in Impurity', fontweight='bold')
ax.set_title('Random Forest Feature Importance', fontsize=16, fontweight='bold')

# Add value labels
for i, (imp, s) in enumerate(zip(importances, std)):
    ax.text(imp + s + 0.01, i, f'{imp:.2f}', va='center', fontsize=11)

# Add legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=MLBLUE, edgecolor='black', label='High (>10%)'),
    Patch(facecolor=MLORANGE, edgecolor='black', label='Medium (5-10%)'),
    Patch(facecolor='gray', edgecolor='black', label='Low (<5%)')
]
ax.legend(handles=legend_elements, loc='lower right', title='Importance Level')

ax.set_xlim(0, 0.38)
ax.grid(True, axis='x', alpha=0.3)

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 02_feature_importance/chart.pdf")
