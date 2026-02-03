"""Gradient Descent Visualization - Loss landscape with optimization path"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# QuantLet branding metadata
CHART_METADATA = {
    "title": "Gradient Descent Optimization",
    "description": "Contour plot with optimization path showing gradient descent",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L01_Introduction_Linear_Regression/04_gradient_descent"
}

# Chart settings for Beamer
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False
})

# Colors
MLPURPLE = '#3333B2'
MLORANGE = '#FF7F0E'
MLRED = '#D62728'

# Create loss surface (quadratic bowl)
beta0 = np.linspace(-2, 4, 100)
beta1 = np.linspace(-1, 3, 100)
B0, B1 = np.meshgrid(beta0, beta1)

# True optimum at (1, 1)
Loss = (B0 - 1)**2 + 2*(B1 - 1)**2

# Gradient descent path
path_b0 = [3.5]
path_b1 = [2.5]
lr = 0.15

for i in range(15):
    grad_b0 = 2 * (path_b0[-1] - 1)
    grad_b1 = 4 * (path_b1[-1] - 1)
    path_b0.append(path_b0[-1] - lr * grad_b0)
    path_b1.append(path_b1[-1] - lr * grad_b1)

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Contour plot
levels = np.logspace(-1, 2, 20)
contour = ax.contour(B0, B1, Loss, levels=levels, cmap='viridis', alpha=0.7)
ax.contourf(B0, B1, Loss, levels=levels, cmap='viridis', alpha=0.3)

# Optimization path
ax.plot(path_b0, path_b1, 'o-', color=MLRED, markersize=8, linewidth=2, label='Gradient descent path')
ax.plot(path_b0[0], path_b1[0], 's', color=MLRED, markersize=12, label='Start')
ax.plot(1, 1, '*', color=MLORANGE, markersize=20, label='Optimum')

# Labels
ax.set_xlabel(r'$\beta_0$ (intercept)')
ax.set_ylabel(r'$\beta_1$ (slope)')
ax.set_title('Gradient Descent: Finding Optimal Coefficients')
ax.legend(loc='upper right')

# Colorbar
cbar = plt.colorbar(contour, ax=ax)
cbar.set_label('Loss (MSE)')

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 04_gradient_descent/chart.pdf")
