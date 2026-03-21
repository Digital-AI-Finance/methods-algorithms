"""Leaf Node Purity Distribution: Shallow vs Deep Trees"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'Leaf Node Purity Distribution: Shallow vs Deep Trees',
    'description': 'Histogram of leaf Gini impurities for shallow vs deep decision trees',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/top10_19_leaf_purity'
}


X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)

# Shallow tree
shallow = DecisionTreeClassifier(max_depth=3, random_state=42)
shallow.fit(X, y)
shallow_leaf_mask = shallow.tree_.children_left == -1
shallow_impurities = shallow.tree_.impurity[shallow_leaf_mask]

# Deep tree
deep = DecisionTreeClassifier(max_depth=None, random_state=42)
deep.fit(X, y)
deep_leaf_mask = deep.tree_.children_left == -1
deep_impurities = deep.tree_.impurity[deep_leaf_mask]

fig, ax = plt.subplots(figsize=(10, 6))

bins = np.linspace(0, 0.5, 25)
ax.hist(shallow_impurities, bins=bins, color=MLBLUE, alpha=0.7, edgecolor='white',
        label=f'Shallow (depth=3, {len(shallow_impurities)} leaves)')
ax.hist(deep_impurities, bins=bins, color=MLORANGE, alpha=0.7, edgecolor='white',
        label=f'Deep (unlimited, {len(deep_impurities)} leaves)')

ax.axvline(x=np.mean(shallow_impurities), color=MLBLUE, linestyle='--', linewidth=2, alpha=0.8)
ax.axvline(x=np.mean(deep_impurities), color=MLORANGE, linestyle='--', linewidth=2, alpha=0.8)

ax.set_xlabel("Gini Impurity at Leaf Node")
ax.set_ylabel("Number of Leaves")
ax.set_title("Leaf Node Purity Distribution: Shallow vs Deep Trees", fontsize=16, fontweight='bold')
ax.legend(loc='upper right', framealpha=0.9)
ax.grid(True, alpha=0.3, axis='y')

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_19_leaf_purity/chart.pdf")
