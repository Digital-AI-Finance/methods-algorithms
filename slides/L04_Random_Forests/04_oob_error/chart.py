"""Out-of-Bag Error - OOB vs Test Error comparison"""
import matplotlib.pyplot as plt

# Chart metadata for QR code generation
CHART_METADATA = {
    'title': 'OOB Error Estimation',
    'description': 'Out-of-bag error convergence with tree count',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/04_oob_error'
}
import numpy as np
from pathlib import Path

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

# Simulate OOB error vs number of trees
n_trees = np.arange(1, 501, 5)

# OOB error decreases and stabilizes
oob_error = 0.35 * np.exp(-n_trees / 50) + 0.08 + np.random.normal(0, 0.008, len(n_trees))
oob_error = np.clip(oob_error, 0.06, 0.4)

# Test error follows similar pattern
test_error = 0.33 * np.exp(-n_trees / 55) + 0.075 + np.random.normal(0, 0.01, len(n_trees))
test_error = np.clip(test_error, 0.055, 0.38)

# Training error (much lower, overfitting)
train_error = 0.05 * np.exp(-n_trees / 30) + 0.01 + np.random.normal(0, 0.002, len(n_trees))
train_error = np.clip(train_error, 0.005, 0.1)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(n_trees, train_error, color=MLGREEN, linewidth=2, label='Training Error', alpha=0.8)
ax.plot(n_trees, oob_error, color=MLBLUE, linewidth=2.5, label='OOB Error')
ax.plot(n_trees, test_error, color=MLRED, linewidth=2, linestyle='--', label='Test Error')

# Highlight convergence region
ax.axvspan(200, 500, alpha=0.1, color='gray')
ax.text(350, 0.32, 'Stable Region', fontsize=11, ha='center', style='italic', color='gray')

# Add horizontal line at final OOB error
final_oob = np.mean(oob_error[-20:])
ax.axhline(y=final_oob, color=MLBLUE, linestyle=':', alpha=0.5)
ax.text(505, final_oob, f'{final_oob:.1%}', fontsize=10, va='center', color=MLBLUE)

ax.set_xlabel('Number of Trees', fontweight='bold')
ax.set_ylabel('Error Rate', fontweight='bold')
ax.set_title('Out-of-Bag Error vs Number of Trees', fontsize=16, fontweight='bold')
ax.legend(loc='upper right', framealpha=0.9)

ax.set_xlim(0, 520)
ax.set_ylim(0, 0.4)
ax.grid(True, alpha=0.3)

# Format y-axis as percentage
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0%}'))

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 04_oob_error/chart.pdf")
