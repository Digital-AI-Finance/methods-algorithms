"""Single Tree Variance - High variance in single decision tree predictions"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from pathlib import Path

# Chart metadata for QR code generation
CHART_METADATA = {
    'title': 'Single Tree Variance',
    'description': 'High variance in single decision tree predictions',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/06a_single_tree_variance'
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

# Generate true function
x = np.linspace(0, 10, 200)
y_true = np.sin(x) + 0.5 * np.cos(2*x)

# Generate training data
n_train = 30
x_train = np.random.uniform(0, 10, n_train)
y_train = np.sin(x_train) + 0.5 * np.cos(2*x_train) + np.random.normal(0, 0.3, n_train)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot training data
ax.scatter(x_train, y_train, c=MLBLUE, s=60, alpha=0.7, label='Training data', zorder=5)
ax.plot(x, y_true, 'k--', linewidth=2.5, label='True function', alpha=0.6)

# Fit multiple single decision trees on bootstrap samples (high variance)
for i in range(7):
    idx = np.random.choice(n_train, n_train, replace=True)
    tree = DecisionTreeRegressor(max_depth=5, random_state=i)
    tree.fit(x_train[idx].reshape(-1, 1), y_train[idx])
    y_pred = tree.predict(x.reshape(-1, 1))
    ax.plot(x, y_pred, color=MLRED, alpha=0.4, linewidth=1.5)

ax.plot([], [], color=MLRED, alpha=0.6, linewidth=2, label='Individual trees')

ax.set_xlabel('x', fontweight='bold')
ax.set_ylabel('y', fontweight='bold')
ax.set_title('Single Decision Trees: High Variance', fontsize=16, fontweight='bold')
ax.legend(loc='upper right', fontsize=12)
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2.5)
ax.grid(True, alpha=0.3)

# Add annotation
ax.annotate('Predictions vary\nwidely between trees',
            xy=(7, 1.5), fontsize=11, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='gray', alpha=0.8))

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 06a_single_tree_variance/chart.pdf")
