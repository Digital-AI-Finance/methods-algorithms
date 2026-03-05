"""Boosting Learning Rate - Effect of learning rate on convergence"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from pathlib import Path

CHART_METADATA = {
    'title': 'Gradient Boosting: Effect of Learning Rate',
    'description': 'Test error convergence for different learning rates',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/15_boosting_learning_rate'
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
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

# Generate dataset
X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

learning_rates = [0.01, 0.1, 1.0]
colors = [MLBLUE, MLGREEN, MLRED]

fig, ax = plt.subplots(figsize=(10, 6))

for lr, color in zip(learning_rates, colors):
    gbc = GradientBoostingClassifier(n_estimators=200, learning_rate=lr, max_depth=3, random_state=42)
    gbc.fit(X_train, y_train)
    test_errors = [1 - accuracy_score(y_test, pred) for pred in gbc.staged_predict(X_test)]
    iterations = np.arange(1, len(test_errors) + 1)
    ax.plot(iterations, test_errors, color=color, linewidth=2.5, label=f'lr = {lr}')

ax.set_xlabel('Boosting Iteration', fontweight='bold')
ax.set_ylabel('Test Error', fontweight='bold')
ax.set_title('Gradient Boosting: Effect of Learning Rate', fontsize=16, fontweight='bold')
ax.legend(loc='upper right', fontsize=12)
ax.grid(True, alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 15_boosting_learning_rate/chart.pdf")
