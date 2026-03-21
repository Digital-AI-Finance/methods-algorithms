"""t-SNE on Credit Risk Features."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "t-SNE on Credit Risk Features",
    "description": "t-SNE scatter plot of 600 credit applicants colored by credit class (Good, Borderline, Default).",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_39_credit_risk_tsne"
}


np.random.seed(42)

n_good, n_border, n_default = 300, 150, 150

def generate_class(n, income_params, dti_ab, util_range, employ_mean, late_lam, loan_params):
    annual_income = np.random.lognormal(income_params[0], income_params[1], n)
    debt_to_income = np.random.beta(dti_ab[0], dti_ab[1], n)
    credit_utilization = np.random.uniform(util_range[0], util_range[1], n)
    months_employed = np.random.exponential(employ_mean, n)
    num_late_payments = np.random.poisson(late_lam, n).astype(float)
    loan_amount = np.random.lognormal(loan_params[0], loan_params[1], n)
    return np.column_stack([annual_income, debt_to_income, credit_utilization,
                            months_employed, num_late_payments, loan_amount])

# Good: high income, low DTI, low utilization, long employment, few late payments
X_good = generate_class(n_good, (11, 0.5), (2, 8), (0.0, 0.4), 60, 0.5, (10, 0.3))
# Borderline: medium everything
X_border = generate_class(n_border, (11, 0.5), (4, 6), (0.3, 0.7), 30, 2.0, (10, 0.3))
# Default: lower income, high DTI, high utilization, short employment, many late payments
X_default = generate_class(n_default, (11, 0.5), (7, 3), (0.5, 1.0), 15, 5.0, (10, 0.3))

X = np.vstack([X_good, X_border, X_default])
labels = np.array([0]*n_good + [1]*n_border + [2]*n_default)

# Standardize and run t-SNE
X_scaled = StandardScaler().fit_transform(X)
tsne = TSNE(n_components=2, random_state=42, perplexity=30)
X_tsne = tsne.fit_transform(X_scaled)

fig, ax = plt.subplots()
for cls, color, name in [(0, MLGREEN, 'Good'), (1, MLORANGE, 'Borderline'), (2, MLRED, 'Default')]:
    mask = labels == cls
    ax.scatter(X_tsne[mask, 0], X_tsne[mask, 1], c=color, label=name,
               alpha=0.6, s=30, edgecolors='white', linewidths=0.3)

ax.set_xlabel('t-SNE Dimension 1')
ax.set_ylabel('t-SNE Dimension 2')
ax.set_title('t-SNE on Credit Risk Features')
ax.legend(frameon=True, fancybox=True, shadow=True, markerscale=1.5)
ax.grid(True, alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
