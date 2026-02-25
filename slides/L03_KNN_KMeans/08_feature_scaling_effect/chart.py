"""
Chart 08: Feature Scaling Changes Your Neighbors
Shows how unscaled vs scaled features lead to different KNN neighbors.
"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False,
})

COLORS = {
    'purple': '#3333B2', 'blue': '#0066CC', 'orange': '#FF7F0E',
    'green': '#2CA02C', 'red': '#D62728', 'lavender': '#ADADE0', 'gray': '#808080',
}

np.random.seed(42)

# Generate 15 data points: Age (20-80), Income (20k-200k)
n_points = 15
ages = np.random.uniform(20, 80, n_points)
incomes = np.random.uniform(20000, 200000, n_points)
X = np.column_stack([ages, incomes])

# Query point
query_age, query_income = 45, 90000
query = np.array([[query_age, query_income]])

# Find 3 nearest neighbors WITHOUT scaling (dominated by income axis)
nn_unscaled = NearestNeighbors(n_neighbors=3)
nn_unscaled.fit(X)
dists_unscaled, idx_unscaled = nn_unscaled.kneighbors(query)
idx_unscaled = idx_unscaled[0]

# Find 3 nearest neighbors WITH scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
query_scaled = scaler.transform(query)
nn_scaled = NearestNeighbors(n_neighbors=3)
nn_scaled.fit(X_scaled)
dists_scaled, idx_scaled = nn_scaled.kneighbors(query_scaled)
idx_scaled = idx_scaled[0]

# --- Plot ---
fig, ax = plt.subplots(figsize=(10, 6))

# All points (lavender background)
ax.scatter(ages, incomes / 1000, color=COLORS['lavender'], s=80, zorder=2,
           edgecolors='white', linewidths=0.5)

# Highlight unscaled neighbors
for i in idx_unscaled:
    ax.plot([query_age, ages[i]], [query_income / 1000, incomes[i] / 1000],
            color=COLORS['gray'], linestyle='--', linewidth=1.8, zorder=3)
ax.scatter(ages[idx_unscaled], incomes[idx_unscaled] / 1000,
           color=COLORS['gray'], s=120, zorder=4, edgecolors='black',
           linewidths=1.0, label='Unscaled neighbors (dashed)')

# Highlight scaled neighbors
for i in idx_scaled:
    ax.plot([query_age, ages[i]], [query_income / 1000, incomes[i] / 1000],
            color=COLORS['blue'], linestyle='-', linewidth=2.0, zorder=3)
ax.scatter(ages[idx_scaled], incomes[idx_scaled] / 1000,
           color=COLORS['blue'], s=120, zorder=4, edgecolors='black',
           linewidths=1.0, label='Scaled neighbors (solid)')

# Query point
ax.scatter(query_age, query_income / 1000, color=COLORS['red'], s=250,
           marker='*', zorder=5, edgecolors='black', linewidths=0.8,
           label='Query point')

ax.set_xlabel('Age (years)')
ax.set_ylabel('Income ($k)')
ax.set_title('Feature Scaling Changes Your Neighbors')
ax.legend(loc='upper left', framealpha=0.9)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig(Path(__file__).parent / 'chart.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to: {output_path}")
