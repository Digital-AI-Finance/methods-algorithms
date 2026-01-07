"""Feature Importance - Random Forest for fraud detection"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLORANGE = '#FF7F0E'

np.random.seed(42)

# Feature importance data (simulated)
features = [
    'Transaction Amount',
    'Time of Day',
    'Foreign IP',
    'Previous Fraud',
    'Account Age',
    'Transaction Frequency',
    'Device Change',
    'Location Distance'
]

importances = np.array([0.28, 0.18, 0.15, 0.12, 0.10, 0.08, 0.05, 0.04])
std = np.array([0.03, 0.02, 0.02, 0.015, 0.012, 0.01, 0.008, 0.006])

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
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 02_feature_importance/chart.pdf")
