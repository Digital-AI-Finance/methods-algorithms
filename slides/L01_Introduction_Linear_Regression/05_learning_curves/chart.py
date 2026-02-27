"""Learning Curves - Training vs Validation Error"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import learning_curve
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
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False
})

# Colors
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'

# Generate regression data and compute learning curves with sklearn
np.random.seed(42)
X_data = np.random.uniform(50, 200, 500).reshape(-1, 1)
y_data = 50000 + 2000 * X_data.ravel() + np.random.normal(0, 30000, 500)

train_sizes_abs, train_scores, val_scores = learning_curve(
    LinearRegression(), X_data, y_data,
    train_sizes=np.linspace(0.1, 1.0, 10),
    cv=5, scoring='neg_mean_squared_error', random_state=42)

# Convert neg MSE to positive and scale for readability
train_mse = -train_scores.mean(axis=1) / 1e9
train_std = train_scores.std(axis=1) / 1e9
val_mse = -val_scores.mean(axis=1) / 1e9
val_std = val_scores.std(axis=1) / 1e9

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot curves with std bands
ax.plot(train_sizes_abs, train_mse, 'o-', color=MLBLUE, markersize=8, linewidth=2, label='Training error')
ax.fill_between(train_sizes_abs, train_mse - train_std, train_mse + train_std,
                alpha=0.15, color=MLBLUE)
ax.plot(train_sizes_abs, val_mse, 's-', color=MLORANGE, markersize=8, linewidth=2, label='Validation error')
ax.fill_between(train_sizes_abs, val_mse - val_std, val_mse + val_std,
                alpha=0.15, color=MLORANGE)

# Fill between (generalization gap)
ax.fill_between(train_sizes_abs, train_mse, val_mse, alpha=0.1, color='gray', label='Generalization gap')

# Add annotations
ax.annotate('More data helps', xy=(train_sizes_abs[4], val_mse[4] * 1.05), fontsize=11, color='gray',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Labels
ax.set_xlabel('Training Set Size')
ax.set_ylabel(r'Mean Squared Error ($\times 10^9$)')
ax.set_title('Learning Curves: How Much Data Do We Need?')
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 05_learning_curves/chart.pdf")
