"""Decision Tree Structure (max_depth=3)"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, plot_tree

CHART_METADATA = {
    'title': 'Decision Tree Structure (max_depth=3)',
    'description': 'Visualization of a fitted decision tree with fraud detection features',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/top10_05_tree_structure'
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

X, y = make_classification(n_samples=200, n_features=4, n_informative=3, n_redundant=0, random_state=42)
feature_names = ['Amount', 'Frequency', 'Distance', 'Time']

clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X, y)

fig, ax = plt.subplots(figsize=(10, 6))
plot_tree(clf, feature_names=feature_names, class_names=['Legit', 'Fraud'],
          filled=True, rounded=True, fontsize=10, ax=ax)
ax.set_title("Decision Tree Structure (max_depth=3)", fontsize=16, fontweight='bold')

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_05_tree_structure/chart.pdf")
