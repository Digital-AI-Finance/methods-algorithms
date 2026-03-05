"""RF Hyperparameter max_features - OOB error vs max_features"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from pathlib import Path

CHART_METADATA = {
    'title': 'Random Forest: OOB Error vs max_features',
    'description': 'Out-of-bag error as a function of max_features hyperparameter',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/18_rf_hyperparameter_maxfeatures'
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

# Generate dataset with 20 features
X, y = make_classification(n_samples=500, n_features=20, n_informative=10, random_state=42)

max_features_range = range(1, 21)
oob_errors = []

for k in max_features_range:
    rf = RandomForestClassifier(n_estimators=100, max_features=k, oob_score=True, random_state=42)
    rf.fit(X, y)
    oob_errors.append(1 - rf.oob_score_)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(list(max_features_range), oob_errors, color=MLBLUE, linewidth=2.5, marker='o', markersize=6, label='OOB Error')

# Vertical line at sqrt(p)
sqrt_p = np.sqrt(20)
ax.axvline(x=sqrt_p, color=MLPURPLE, linestyle='--', linewidth=2, label=f'$\\sqrt{{p}}$ = {sqrt_p:.1f}')

ax.set_xlabel('max_features', fontweight='bold')
ax.set_ylabel('OOB Error', fontweight='bold')
ax.set_title('Random Forest: OOB Error vs max_features', fontsize=16, fontweight='bold')
ax.legend(loc='upper right', fontsize=12)
ax.grid(True, alpha=0.3)
ax.set_xticks(range(1, 21, 2))

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 18_rf_hyperparameter_maxfeatures/chart.pdf")
