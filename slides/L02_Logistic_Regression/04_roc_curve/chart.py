"""ROC Curve - Receiver Operating Characteristic"""
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
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

np.random.seed(42)

# Simulate ROC curves for different models
def generate_roc(auc_target, n_points=100):
    """Generate ROC curve with approximately target AUC."""
    fpr = np.linspace(0, 1, n_points)
    # Use power function to create curve shape
    power = np.log(1 - auc_target + 0.5) / np.log(0.5)
    tpr = 1 - (1 - fpr) ** (1/max(power, 0.1))
    tpr = np.clip(tpr + np.random.normal(0, 0.02, n_points), 0, 1)
    tpr = np.sort(tpr)
    return fpr, tpr

fpr_good, tpr_good = generate_roc(0.92)
fpr_medium, tpr_medium = generate_roc(0.78)
fpr_poor, tpr_poor = generate_roc(0.62)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot ROC curves
ax.plot(fpr_good, tpr_good, color=MLGREEN, linewidth=3,
        label='Good Model (AUC = 0.92)')
ax.plot(fpr_medium, tpr_medium, color=MLORANGE, linewidth=3,
        label='Medium Model (AUC = 0.78)')
ax.plot(fpr_poor, tpr_poor, color=MLRED, linewidth=3,
        label='Poor Model (AUC = 0.62)')

# Random classifier line
ax.plot([0, 1], [0, 1], color='gray', linewidth=2, linestyle='--',
        label='Random (AUC = 0.50)')

# Fill AUC area for good model
ax.fill_between(fpr_good, 0, tpr_good, alpha=0.15, color=MLGREEN)

# Annotations
ax.annotate('AUC Area', xy=(0.6, 0.4), fontsize=12, color=MLGREEN)
ax.annotate('', xy=(0.3, 0.7), xytext=(0.3, 0.3),
            arrowprops=dict(arrowstyle='->', color=MLPURPLE, lw=2))
ax.text(0.35, 0.5, 'Better', fontsize=11, color=MLPURPLE, rotation=90, va='center')

ax.set_xlabel('False Positive Rate (FPR)')
ax.set_ylabel('True Positive Rate (TPR)')
ax.set_title('ROC Curves: Model Comparison')
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.02, 1.02)
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 04_roc_curve/chart.pdf")
