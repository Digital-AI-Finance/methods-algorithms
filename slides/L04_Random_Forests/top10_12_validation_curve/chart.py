"""Validation Curve: Optimal Tree Depth"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import validation_curve

CHART_METADATA = {
    'title': 'Validation Curve: Optimal Tree Depth',
    'description': 'Train and test scores as a function of max_depth for a decision tree',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/top10_12_validation_curve'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)

param_range = np.arange(1, 21)
train_scores, test_scores = validation_curve(
    DecisionTreeClassifier(random_state=42), X, y,
    param_name='max_depth', param_range=param_range,
    cv=5, scoring='accuracy'
)

train_mean = train_scores.mean(axis=1)
train_std = train_scores.std(axis=1)
test_mean = test_scores.mean(axis=1)
test_std = test_scores.std(axis=1)

optimal_depth = param_range[np.argmax(test_mean)]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(param_range, train_mean, '-o', color=MLBLUE, linewidth=2, markersize=5, label='Training Score')
ax.fill_between(param_range, train_mean - train_std, train_mean + train_std, color=MLBLUE, alpha=0.1)

ax.plot(param_range, test_mean, '--s', color=MLRED, linewidth=2, markersize=5, label='Validation Score')
ax.fill_between(param_range, test_mean - test_std, test_mean + test_std, color=MLRED, alpha=0.1)

ax.axvline(x=optimal_depth, color='gray', linestyle='--', linewidth=1.5, alpha=0.7,
           label=f'Optimal Depth = {optimal_depth}')

ax.set_xlabel("max_depth")
ax.set_ylabel("Accuracy")
ax.set_title("Validation Curve: Optimal Tree Depth", fontsize=16, fontweight='bold')
ax.legend(loc='lower right', framealpha=0.9)
ax.grid(True, alpha=0.3)
ax.set_xticks(param_range[::2])

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_12_validation_curve/chart.pdf")
