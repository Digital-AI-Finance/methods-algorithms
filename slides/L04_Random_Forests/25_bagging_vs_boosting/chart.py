"""Bagging vs Boosting: Error Reduction Strategies"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'Bagging vs Boosting: Error Reduction Strategies',
    'description': 'Compares RF (bagging) vs GBM (boosting) test error as ensemble size grows',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/25_bagging_vs_boosting'
}


X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

max_estimators = 200

# --- Gradient Boosting: staged_predict for per-iteration test error ---
gb = GradientBoostingClassifier(n_estimators=max_estimators, learning_rate=0.1, random_state=42)
gb.fit(X_train, y_train)

gb_errors = []
for y_pred_staged in gb.staged_predict(X_test):
    gb_errors.append(1.0 - np.mean(y_pred_staged == y_test))

# --- Random Forest: warm_start loop ---
rf = RandomForestClassifier(warm_start=True, random_state=42)
rf_errors = []
n_range = list(range(1, max_estimators + 1))
for i in n_range:
    rf.n_estimators = i
    rf.fit(X_train, y_train)
    rf_errors.append(1.0 - rf.score(X_test, y_test))

fig, ax = plt.subplots()

ax.plot(n_range, rf_errors, color=MLBLUE, linewidth=1.8, label='Random Forest (Bagging)', alpha=0.9)
ax.plot(range(1, max_estimators + 1), gb_errors, color=MLORANGE, linewidth=1.8, label='Gradient Boosting', alpha=0.9)

# Annotations
ax.annotate('Variance reduction\n(averaging)', xy=(120, rf_errors[119]),
            xytext=(140, rf_errors[119] + 0.06),
            fontsize=11, color=MLBLUE, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=MLBLUE, lw=1.2))

ax.annotate('Bias reduction\n(sequential fitting)', xy=(60, gb_errors[59]),
            xytext=(25, gb_errors[59] + 0.07),
            fontsize=11, color=MLORANGE, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=MLORANGE, lw=1.2))

ax.set_xlabel('Number of Estimators')
ax.set_ylabel('Test Error Rate')
ax.set_title(CHART_METADATA['title'])
ax.legend(loc='upper right', framealpha=0.9)
ax.set_xlim([1, max_estimators])
ax.set_ylim(bottom=0)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: 25_bagging_vs_boosting/chart.pdf")
