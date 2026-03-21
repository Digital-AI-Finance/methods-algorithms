"""Decision Tree Structure (max_depth=3)"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, plot_tree
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'Decision Tree Structure (max_depth=3)',
    'description': 'Visualization of a fitted decision tree with fraud detection features',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/top10_05_tree_structure'
}


X, y = make_classification(n_samples=200, n_features=4, n_informative=3, n_redundant=0, random_state=42)
feature_names = ['Amount', 'Frequency', 'Distance', 'Time']

clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X, y)

fig, ax = plt.subplots(figsize=(10, 6))
plot_tree(clf, feature_names=feature_names, class_names=['Legit', 'Fraud'],
          filled=True, rounded=True, fontsize=10, ax=ax)
ax.grid(False)
ax.set_title("Decision Tree Structure (max_depth=3)", fontsize=16, fontweight='bold')

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_05_tree_structure/chart.pdf")
