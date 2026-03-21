"""Calibration Curve: Are Predicted Probabilities Reliable?"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.calibration import calibration_curve
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'Calibration Curve: Are Predicted Probabilities Reliable?',
    'description': 'Calibration plots for DT and RF with probability histograms',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/top10_15_calibration_curve'
}


X, y = make_classification(n_samples=2000, n_features=10, n_informative=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

dt = DecisionTreeClassifier(max_depth=5, random_state=42)
dt.fit(X_train, y_train)
dt_proba = dt.predict_proba(X_test)[:, 1]

rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
rf_proba = rf.predict_proba(X_test)[:, 1]

dt_frac, dt_mean = calibration_curve(y_test, dt_proba, n_bins=10)
rf_frac, rf_mean = calibration_curve(y_test, rf_proba, n_bins=10)

fig, ax = plt.subplots(figsize=(10, 6))

# Perfect calibration
ax.plot([0, 1], [0, 1], '--', color='gray', linewidth=1.5, alpha=0.7, label='Perfect Calibration')

# Calibration curves
ax.plot(dt_mean, dt_frac, '-o', color=MLBLUE, linewidth=2.5, markersize=7, label='Decision Tree')
ax.plot(rf_mean, rf_frac, '-s', color=MLORANGE, linewidth=2.5, markersize=7, label='Random Forest')

# Inset histogram of predicted probabilities
ax_inset = ax.inset_axes([0.55, 0.05, 0.4, 0.25])
ax_inset.hist(dt_proba, bins=20, alpha=0.5, color=MLBLUE, density=True, label='DT')
ax_inset.hist(rf_proba, bins=20, alpha=0.5, color=MLORANGE, density=True, label='RF')
ax_inset.set_xlabel('Predicted P', fontsize=9)
ax_inset.set_ylabel('Density', fontsize=9)
ax_inset.tick_params(labelsize=8)
ax_inset.legend(fontsize=8)
ax_inset.set_title('Probability Distribution', fontsize=9)

ax.set_xlabel("Mean Predicted Probability")
ax.set_ylabel("Fraction of Positives")
ax.set_title("Calibration Curve: Are Predicted Probabilities Reliable?", fontsize=16, fontweight='bold')
ax.legend(loc='upper left', framealpha=0.9)
ax.grid(True, alpha=0.3)
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.02, 1.02)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_15_calibration_curve/chart.pdf")
