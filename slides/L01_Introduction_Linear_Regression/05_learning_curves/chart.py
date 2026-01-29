"""Learning Curves - Training vs Validation Error"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# QuantLet branding metadata
CHART_METADATA = {
    "title": "Learning Curves",
    "description": "Training vs validation error curves for model diagnostics",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L01_Introduction_Linear_Regression/05_learning_curves"
}

# Chart settings for Beamer
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})

# Colors
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'

# Generate learning curve data
np.random.seed(42)
train_sizes = np.array([10, 20, 40, 60, 80, 100, 150, 200, 300, 400, 500])

# Training error decreases then plateaus
train_error = 0.1 + 0.4 * np.exp(-train_sizes / 50) + np.random.normal(0, 0.01, len(train_sizes))

# Validation error starts high, decreases, then plateaus (slightly higher than train)
val_error = 0.15 + 0.5 * np.exp(-train_sizes / 80) + np.random.normal(0, 0.015, len(train_sizes))

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot curves
ax.plot(train_sizes, train_error, 'o-', color=MLBLUE, markersize=8, linewidth=2, label='Training error')
ax.plot(train_sizes, val_error, 's-', color=MLORANGE, markersize=8, linewidth=2, label='Validation error')

# Fill between (generalization gap)
ax.fill_between(train_sizes, train_error, val_error, alpha=0.2, color='gray', label='Generalization gap')

# Add annotations
ax.annotate('More data helps', xy=(150, 0.22), fontsize=11, color='gray',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Labels
ax.set_xlabel('Training Set Size')
ax.set_ylabel('Mean Squared Error')
ax.set_title('Learning Curves: How Much Data Do We Need?')
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# Axis limits
ax.set_xlim(0, 520)
ax.set_ylim(0, 0.65)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 05_learning_curves/chart.pdf")
