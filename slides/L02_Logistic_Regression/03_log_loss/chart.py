"""Log Loss (Cross-Entropy) - Loss function visualization"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    "title": "Binary Cross-Entropy Loss",
    "description": "Log loss curves for true positives and negatives",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L02_Logistic_Regression/03_log_loss"
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

# Predicted probability
p = np.linspace(0.001, 0.999, 200)

# Log loss for y=1: -log(p)
loss_y1 = -np.log(p)
# Log loss for y=0: -log(1-p)
loss_y0 = -np.log(1 - p)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(p, loss_y1, color=MLGREEN, linewidth=3, label='y=1: -log(p)')
ax.plot(p, loss_y0, color=MLRED, linewidth=3, label='y=0: -log(1-p)')

# Annotations
ax.annotate('Low loss when\np close to 1', xy=(0.9, 0.2), fontsize=11,
            color=MLGREEN, ha='center')
ax.annotate('High loss when\np close to 0', xy=(0.1, 2.5), fontsize=11,
            color=MLGREEN, ha='center')
ax.annotate('Low loss when\np close to 0', xy=(0.1, 0.2), fontsize=11,
            color=MLRED, ha='center')
ax.annotate('High loss when\np close to 1', xy=(0.9, 2.5), fontsize=11,
            color=MLRED, ha='center')

ax.set_xlabel('Predicted Probability (p)')
ax.set_ylabel('Loss')
ax.set_title('Binary Cross-Entropy Loss')
ax.set_xlim(0, 1)
ax.set_ylim(0, 5)
ax.legend(loc='upper center', fontsize=13)
ax.grid(True, alpha=0.3)

# Add formula
ax.text(0.5, 4.3, r'$\mathcal{L} = -[y \log(p) + (1-y) \log(1-p)]$',
        fontsize=14, ha='center', color=MLPURPLE,
        bbox=dict(boxstyle='round', facecolor='white', edgecolor=MLPURPLE, alpha=0.8))

# Add URL annotation
ax.text(0.99, 0.01, CHART_METADATA['url'],
        transform=ax.transAxes,
        fontsize=7,
        color='gray',
        ha='right',
        va='bottom',
        alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 03_log_loss/chart.pdf")
