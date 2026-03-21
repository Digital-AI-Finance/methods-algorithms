"""Bias-Variance Tradeoff vs Tree Depth"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'Decision Tree: Bias-Variance Tradeoff',
    'description': 'Train and test error as a function of tree depth',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/17_bias_variance_depth'
}


# Generate dataset
X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

depths = range(1, 21)
train_errors = []
test_errors = []

for d in depths:
    dt = DecisionTreeClassifier(max_depth=d, random_state=42)
    dt.fit(X_train, y_train)
    train_errors.append(1 - dt.score(X_train, y_train))
    test_errors.append(1 - dt.score(X_test, y_test))

fig, ax = plt.subplots(figsize=(10, 6))

# Shaded zones
ax.axvspan(1, 5, alpha=0.08, color=MLBLUE, label='_nolegend_')
ax.axvspan(12, 20, alpha=0.08, color=MLRED, label='_nolegend_')

ax.plot(list(depths), train_errors, color=MLBLUE, linewidth=2.5, marker='o', markersize=5, label='Train error')
ax.plot(list(depths), test_errors, color=MLRED, linewidth=2.5, marker='s', markersize=5, label='Test error')

ax.set_xlabel('Max Depth', fontweight='bold')
ax.set_ylabel('Error Rate', fontweight='bold')
ax.set_title('Decision Tree: Bias-Variance Tradeoff', fontsize=16, fontweight='bold')
ax.legend(loc='upper right', fontsize=12)
ax.grid(True, alpha=0.3)

# Zone labels
ax.text(3, max(test_errors) * 0.92, 'Underfitting', fontsize=12, ha='center', color=MLBLUE, fontweight='bold', alpha=0.8)
ax.text(16, max(test_errors) * 0.92, 'Overfitting', fontsize=12, ha='center', color=MLRED, fontweight='bold', alpha=0.8)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: 17_bias_variance_depth/chart.pdf")
