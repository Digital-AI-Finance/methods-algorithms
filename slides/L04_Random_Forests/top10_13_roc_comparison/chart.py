"""ROC Curve: Decision Tree vs Random Forest"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'ROC Curve: Decision Tree vs Random Forest',
    'description': 'ROC curves comparing DT and RF on imbalanced classification',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/top10_13_roc_comparison'
}


X, y = make_classification(n_samples=1000, n_features=10, weights=[0.7, 0.3], random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

dt = DecisionTreeClassifier(max_depth=5, random_state=42)
dt.fit(X_train, y_train)
dt_proba = dt.predict_proba(X_test)[:, 1]
dt_fpr, dt_tpr, _ = roc_curve(y_test, dt_proba)
dt_auc = auc(dt_fpr, dt_tpr)

rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
rf_proba = rf.predict_proba(X_test)[:, 1]
rf_fpr, rf_tpr, _ = roc_curve(y_test, rf_proba)
rf_auc = auc(rf_fpr, rf_tpr)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(dt_fpr, dt_tpr, color=MLBLUE, linewidth=2.5, label=f'Decision Tree (AUC={dt_auc:.2f})')
ax.plot(rf_fpr, rf_tpr, color=MLORANGE, linewidth=2.5, label=f'Random Forest (AUC={rf_auc:.2f})')
ax.plot([0, 1], [0, 1], '--', color='gray', linewidth=1.5, alpha=0.7, label='Random Baseline')

ax.set_xlabel("False Positive Rate")
ax.set_ylabel("True Positive Rate")
ax.set_title("ROC Curve: Decision Tree vs Random Forest", fontsize=16, fontweight='bold')
ax.legend(loc='lower right', framealpha=0.9, fontsize=13)
ax.grid(True, alpha=0.3)
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.02, 1.02)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_13_roc_comparison/chart.pdf")
