"""
Chart 11: Customer Segments - RFM Analysis with K-Means
Scatter of 200 customers colored by cluster, annotated segment names.
"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.cluster import KMeans

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

# Generate 200 synthetic customers with clustered RFM data
# 4 clusters with distinct characteristics
n = 200
# Champions: low recency, high monetary
c1 = np.column_stack([
    np.random.uniform(5, 60, 50),
    np.random.uniform(5000, 10000, 50),
    np.random.uniform(15, 30, 50),
])
# At Risk: high recency, low monetary
c2 = np.column_stack([
    np.random.uniform(250, 365, 50),
    np.random.uniform(10, 2000, 50),
    np.random.uniform(1, 8, 50),
])
# New Customers: low recency, low monetary
c3 = np.column_stack([
    np.random.uniform(5, 80, 50),
    np.random.uniform(10, 2000, 50),
    np.random.uniform(1, 5, 50),
])
# Hibernating: high recency, mid monetary
c4 = np.column_stack([
    np.random.uniform(200, 350, 50),
    np.random.uniform(2000, 6000, 50),
    np.random.uniform(5, 15, 50),
])

data = np.vstack([c1, c2, c3, c4])
recency = data[:, 0]
monetary = data[:, 1]
frequency = data[:, 2]

# Cluster with KMeans on recency and monetary
X_cluster = np.column_stack([recency, monetary])
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_cluster)
centers = kmeans.cluster_centers_

# Map cluster labels to segment names based on center positions
# Sort clusters by (recency, monetary) to assign meaningful names
cluster_colors = [COLORS['blue'], COLORS['orange'], COLORS['green'], COLORS['purple']]
segment_names = {}
for c_id in range(4):
    cr, cm = centers[c_id]
    if cr < 150 and cm > 4000:
        segment_names[c_id] = 'Champions'
    elif cr > 150 and cm < 3000:
        segment_names[c_id] = 'At Risk'
    elif cr < 150 and cm < 3000:
        segment_names[c_id] = 'New Customers'
    else:
        segment_names[c_id] = 'Hibernating'

# --- Plot ---
fig, ax = plt.subplots(figsize=(10, 6))

# Size proportional to frequency (scaled for visibility)
sizes = 15 + (frequency - frequency.min()) / (frequency.max() - frequency.min()) * 120

for c_id in range(4):
    mask = labels == c_id
    ax.scatter(recency[mask], monetary[mask] / 1000, c=cluster_colors[c_id],
               s=sizes[mask], alpha=0.7, edgecolors='white', linewidths=0.3,
               label=segment_names.get(c_id, f'Cluster {c_id}'), zorder=2)

# Cluster centers (black diamonds)
ax.scatter(centers[:, 0], centers[:, 1] / 1000, color='black', marker='D',
           s=150, zorder=5, edgecolors='white', linewidths=1.2, label='Centroids')

# Annotate centers with segment names
for c_id in range(4):
    name = segment_names.get(c_id, f'Cluster {c_id}')
    offset_x = 15 if centers[c_id, 0] < 200 else -15
    ha = 'left' if centers[c_id, 0] < 200 else 'right'
    ax.annotate(name, xy=(centers[c_id, 0], centers[c_id, 1] / 1000),
                xytext=(centers[c_id, 0] + offset_x, centers[c_id, 1] / 1000 + 0.5),
                fontsize=12, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                          edgecolor='black', alpha=0.85),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.2),
                zorder=6)

ax.set_xlabel('Recency (days since last purchase)')
ax.set_ylabel('Monetary ($k)')
ax.set_title('Customer Segments: RFM Analysis with K-Means')
ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), framealpha=0.9)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig(Path(__file__).parent / 'chart.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to: {output_path}")
