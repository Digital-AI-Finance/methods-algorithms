"""Learning Curves: Decision Tree vs Random Forest"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import learning_curve
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'Learning Curves: Decision Tree vs Random Forest',
    'description': 'Training and validation scores vs dataset size for DT and RF',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/top10_11_learning_curve'
}


X, y = make_classification(n_samples=2000, n_features=10, n_informative=5, random_state=42)

train_sizes = np.linspace(0.1, 1.0, 10)

dt = DecisionTreeClassifier(max_depth=5, random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42)

dt_sizes, dt_train, dt_val = learning_curve(dt, X, y, train_sizes=train_sizes, cv=5, scoring='accuracy', random_state=42)
rf_sizes, rf_train, rf_val = learning_curve(rf, X, y, train_sizes=train_sizes, cv=5, scoring='accuracy', random_state=42)

fig, ax = plt.subplots(figsize=(10, 6))

# Decision Tree
dt_train_mean, dt_train_std = dt_train.mean(axis=1), dt_train.std(axis=1)
dt_val_mean, dt_val_std = dt_val.mean(axis=1), dt_val.std(axis=1)
ax.plot(dt_sizes, dt_train_mean, '-', color=MLBLUE, linewidth=2, label='DT Train')
ax.plot(dt_sizes, dt_val_mean, '--', color=MLBLUE, linewidth=2, label='DT Validation')
ax.fill_between(dt_sizes, dt_train_mean - dt_train_std, dt_train_mean + dt_train_std, color=MLBLUE, alpha=0.1)
ax.fill_between(dt_sizes, dt_val_mean - dt_val_std, dt_val_mean + dt_val_std, color=MLBLUE, alpha=0.1)

# Random Forest
rf_train_mean, rf_train_std = rf_train.mean(axis=1), rf_train.std(axis=1)
rf_val_mean, rf_val_std = rf_val.mean(axis=1), rf_val.std(axis=1)
ax.plot(rf_sizes, rf_train_mean, '-', color=MLORANGE, linewidth=2, label='RF Train')
ax.plot(rf_sizes, rf_val_mean, '--', color=MLORANGE, linewidth=2, label='RF Validation')
ax.fill_between(rf_sizes, rf_train_mean - rf_train_std, rf_train_mean + rf_train_std, color=MLORANGE, alpha=0.1)
ax.fill_between(rf_sizes, rf_val_mean - rf_val_std, rf_val_mean + rf_val_std, color=MLORANGE, alpha=0.1)

ax.set_xlabel("Training Set Size")
ax.set_ylabel("Accuracy")
ax.set_title("Learning Curves: Decision Tree vs Random Forest", fontsize=16, fontweight='bold')
ax.legend(loc='lower right', framealpha=0.9)
ax.grid(True, alpha=0.3)
ax.set_ylim(0.6, 1.02)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_11_learning_curve/chart.pdf")
