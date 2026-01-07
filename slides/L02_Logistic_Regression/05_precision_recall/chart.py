"""Precision-Recall Curve - Classification metrics tradeoff"""
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

# Simulate PR curves
def generate_pr_curve(ap_target, n_points=100):
    """Generate precision-recall curve with target average precision."""
    recall = np.linspace(0, 1, n_points)
    # Higher AP means precision stays high longer as recall increases
    precision = ap_target + (1 - ap_target) * (1 - recall ** (1/ap_target))
    precision = np.clip(precision + np.random.normal(0, 0.02, n_points), 0, 1)
    return recall, precision

recall_good, prec_good = generate_pr_curve(0.88)
recall_med, prec_med = generate_pr_curve(0.72)
recall_poor, prec_poor = generate_pr_curve(0.55)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot PR curves
ax.plot(recall_good, prec_good, color=MLGREEN, linewidth=3,
        label='Good Model (AP = 0.88)')
ax.plot(recall_med, prec_med, color=MLORANGE, linewidth=3,
        label='Medium Model (AP = 0.72)')
ax.plot(recall_poor, prec_poor, color=MLRED, linewidth=3,
        label='Poor Model (AP = 0.55)')

# Fill area
ax.fill_between(recall_good, 0, prec_good, alpha=0.15, color=MLGREEN)

# Annotations for key points
ax.annotate('High Precision\nLow Recall', xy=(0.15, 0.92), fontsize=11,
            ha='center', color=MLPURPLE)
ax.annotate('High Recall\nLower Precision', xy=(0.85, 0.55), fontsize=11,
            ha='center', color=MLPURPLE)

# Trade-off arrow
ax.annotate('', xy=(0.7, 0.6), xytext=(0.3, 0.88),
            arrowprops=dict(arrowstyle='->', color='gray', lw=2,
                          connectionstyle='arc3,rad=0.2'))
ax.text(0.5, 0.82, 'Trade-off', fontsize=11, color='gray', ha='center')

ax.set_xlabel('Recall (Sensitivity)')
ax.set_ylabel('Precision')
ax.set_title('Precision-Recall Curves: Model Comparison')
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(0, 1.05)
ax.legend(loc='lower left')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 05_precision_recall/chart.pdf")
