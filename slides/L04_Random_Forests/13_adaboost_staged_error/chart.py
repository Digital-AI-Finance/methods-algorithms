"""AdaBoost Staged Error - Train vs test error across boosting rounds"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from pathlib import Path

CHART_METADATA = {
    'title': 'AdaBoost: Training vs Test Error',
    'description': 'Train and test error rates across boosting rounds',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/13_adaboost_staged_error'
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

# Train AdaBoost
ada = AdaBoostClassifier(n_estimators=50, algorithm='SAMME', random_state=42)
ada.fit(X_train, y_train)

# Get staged scores (cumulative accuracy at each round)
train_errors = [1 - acc for acc in ada.staged_score(X_train, y_train)]
test_errors = [1 - acc for acc in ada.staged_score(X_test, y_test)]
n_rounds = np.arange(1, len(train_errors) + 1)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(n_rounds, train_errors, color=MLBLUE, linewidth=2.5, label='Train error')
ax.plot(n_rounds, test_errors, color=MLRED, linewidth=2.5, label='Test error')

ax.set_xlabel('Number of Estimators', fontweight='bold')
ax.set_ylabel('Error Rate', fontweight='bold')
ax.set_title('AdaBoost: Training vs Test Error', fontsize=16, fontweight='bold')
ax.legend(loc='upper right', fontsize=12)
ax.grid(True, alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 13_adaboost_staged_error/chart.pdf")
