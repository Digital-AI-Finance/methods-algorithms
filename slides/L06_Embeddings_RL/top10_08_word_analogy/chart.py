"""Word Analogy Arithmetic - Visualizes king-man+woman=queen with PCA projection of synthetic embeddings."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA

CHART_METADATA = {
    "title": "Word Analogy Arithmetic",
    "description": "Visualizes king-man+woman=queen analogy with PCA-projected synthetic embeddings",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/top10_08_word_analogy"
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

np.random.seed(42)

# Create synthetic 50D embeddings encoding gender and royalty semantics
dim = 50
base = np.random.randn(8, dim) * 0.3

# Semantic offsets
gender_offset = np.random.randn(dim) * 1.5  # male -> female direction
royalty_offset = np.random.randn(dim) * 1.5  # commoner -> royal direction
youth_offset = np.random.randn(dim) * 1.0   # adult -> child direction

words = ['king', 'queen', 'man', 'woman', 'prince', 'princess', 'boy', 'girl']
# Assign: male+royal, female+royal, male, female, male+royal+young, female+royal+young, male+young, female+young
embeddings = np.zeros((8, dim))
embeddings[0] = base[0] + royalty_offset                          # king: male + royal
embeddings[1] = base[0] + royalty_offset + gender_offset          # queen: female + royal
embeddings[2] = base[0]                                           # man: male
embeddings[3] = base[0] + gender_offset                           # woman: female
embeddings[4] = base[0] + royalty_offset + youth_offset           # prince: male + royal + young
embeddings[5] = base[0] + royalty_offset + gender_offset + youth_offset  # princess: female + royal + young
embeddings[6] = base[0] + youth_offset                            # boy: male + young
embeddings[7] = base[0] + gender_offset + youth_offset            # girl: female + young

# Add small noise
embeddings += np.random.randn(8, dim) * 0.2

# PCA to 2D
pca = PCA(n_components=2, random_state=42)
coords = pca.fit_transform(embeddings)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot all words
colors = [MLPURPLE, MLPURPLE, MLBLUE, MLBLUE, MLORANGE, MLORANGE, MLGREEN, MLGREEN]
for i, (word, color) in enumerate(zip(words, colors)):
    ax.scatter(coords[i, 0], coords[i, 1], c=color, s=120, zorder=5, edgecolors='white', linewidth=0.5)
    offset_x = 0.15
    offset_y = 0.15
    ax.annotate(word, (coords[i, 0], coords[i, 1]),
                textcoords="offset points", xytext=(8, 8),
                fontsize=13, fontweight='bold', color=color)

# Draw analogy arrows: king - man + woman -> queen
# Arrow 1: king to man (subtract man)
ax.annotate('', xy=coords[2], xytext=coords[0],
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=2.5, linestyle='--'))
# Arrow 2: man to woman (add woman direction)
ax.annotate('', xy=coords[3], xytext=coords[2],
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=2.5, linestyle='--'))
# Arrow 3: woman offset applied to king -> queen
ax.annotate('', xy=coords[1], xytext=coords[0],
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=3))

# Add analogy equation
ax.text(0.02, 0.97, r'king $-$ man $+$ woman $\approx$ queen',
        transform=ax.transAxes, fontsize=14, fontweight='bold',
        color=MLRED, va='top',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=MLRED, alpha=0.8))

ax.set_title("Word Analogy: king - man + woman " + r"$\approx$" + " queen", fontsize=16, fontweight='bold')
ax.set_xlabel("First Principal Component")
ax.set_ylabel("Second Principal Component")

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_08_word_analogy/chart.pdf")
