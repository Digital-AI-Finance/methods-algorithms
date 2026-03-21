"""Random Forest: Error Convergence vs Number of Trees"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'Random Forest: Error Convergence vs Number of Trees',
    'description': 'OOB and test error as number of trees grows, showing diminishing returns',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/27_rf_ntrees_convergence'
}


X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

n_values = list(range(10, 501, 10))
oob_errors = []
test_errors = []

rf = RandomForestClassifier(warm_start=True, oob_score=True, random_state=42)
for n in n_values:
    rf.n_estimators = n
    rf.fit(X_train, y_train)
    oob_errors.append(1.0 - rf.oob_score_)
    test_errors.append(1.0 - rf.score(X_test, y_test))

# Find diminishing returns point: where improvement drops below 0.1% (0.001)
diminishing_idx = None
for i in range(1, len(oob_errors)):
    improvement = oob_errors[i - 1] - oob_errors[i]
    if improvement < 0.001 and i > 5:
        diminishing_idx = i
        break

fig, ax = plt.subplots()

ax.plot(n_values, oob_errors, color=MLBLUE, linewidth=2.0, label='OOB Error')
ax.plot(n_values, test_errors, color=MLRED, linewidth=2.0, linestyle='--', label='Test Error')

# Shade recommended range
ax.axvspan(100, 300, alpha=0.1, color=MLGREEN, label='Recommended range (100-300)')

# Diminishing returns line
if diminishing_idx is not None:
    dim_n = n_values[diminishing_idx]
    ax.axvline(x=dim_n, color='gray', linestyle=':', linewidth=1.5, alpha=0.8)
    ax.annotate(f'Diminishing returns\n(n={dim_n})',
                xy=(dim_n, oob_errors[diminishing_idx]),
                xytext=(dim_n + 80, oob_errors[diminishing_idx] + 0.015),
                fontsize=11, color='gray', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.2))

ax.set_xlabel('Number of Trees')
ax.set_ylabel('Error Rate')
ax.set_title(CHART_METADATA['title'])
ax.legend(loc='upper right', framealpha=0.9)
ax.set_xlim([10, 500])
ax.set_ylim(bottom=0)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: 27_rf_ntrees_convergence/chart.pdf")
