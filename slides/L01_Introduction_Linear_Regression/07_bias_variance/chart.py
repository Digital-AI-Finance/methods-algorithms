"""Bias-Variance Tradeoff - Model Complexity vs Error"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

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
MLPURPLE = '#3333B2'

# Model complexity axis
complexity = np.linspace(0.5, 10, 100)

# Bias decreases with complexity
bias_squared = 2.5 * np.exp(-0.5 * complexity)

# Variance increases with complexity
variance = 0.1 + 0.15 * complexity**1.2

# Irreducible error (constant)
irreducible = 0.3 * np.ones_like(complexity)

# Total error
total_error = bias_squared + variance + irreducible

# Optimal complexity
optimal_idx = np.argmin(total_error)
optimal_complexity = complexity[optimal_idx]

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot components
ax.plot(complexity, bias_squared, '-', color=MLBLUE, linewidth=2.5, label=r'Bias$^2$')
ax.plot(complexity, variance, '-', color=MLORANGE, linewidth=2.5, label='Variance')
ax.plot(complexity, irreducible, '--', color='gray', linewidth=2, label='Irreducible error')
ax.plot(complexity, total_error, '-', color=MLPURPLE, linewidth=3, label='Total error')

# Mark optimal point
ax.axvline(x=optimal_complexity, color=MLGREEN, linestyle=':', linewidth=2)
ax.plot(optimal_complexity, total_error[optimal_idx], 'o', color=MLGREEN, markersize=12)

# Labels
ax.set_xlabel('Model Complexity')
ax.set_ylabel('Error')
ax.set_title('Bias-Variance Tradeoff')
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# Add annotations
ax.annotate('Underfitting\n(High Bias)', xy=(1.5, 2.5), fontsize=11,
            ha='center', color='gray')
ax.annotate('Overfitting\n(High Variance)', xy=(8.5, 2.0), fontsize=11,
            ha='center', color='gray')
ax.annotate('Optimal\nComplexity', xy=(optimal_complexity, 0.5), fontsize=11,
            ha='center', color=MLGREEN)

# Axis limits
ax.set_xlim(0, 10.5)
ax.set_ylim(0, 3.5)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 07_bias_variance/chart.pdf")
