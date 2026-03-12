"""
Chart: Word Analogy - Vector Arithmetic in Embedding Space
king - man + woman ≈ queen visualized via PCA projection from 50D embeddings.
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
from sklearn.decomposition import PCA

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------
CHART_METADATA = {
    "title": "Word Analogy: Vector Arithmetic in Embedding Space",
    "description": (
        "Synthetic 50D word embeddings for 8 words projected to 2D via PCA. "
        "Demonstrates the parallelogram relationship king - man + woman ≈ queen."
    ),
    "url": "https://digital-ai-finance.github.io/methods-algorithms/slides/L06_Embeddings_RL/11_word_analogy_arithmetic",
}

# ---------------------------------------------------------------------------
# Style
# ---------------------------------------------------------------------------
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False
})

MLPURPLE = '#3333B2'
MLBLUE   = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN  = '#2CA02C'
MLRED    = '#D62728'

# ---------------------------------------------------------------------------
# Synthetic embeddings (50D with semantic structure)
# ---------------------------------------------------------------------------
rng = np.random.default_rng(42)

DIM = 50

# Basis vectors for semantic dimensions
gender_axis   = np.zeros(DIM); gender_axis[0]   = 1.0   # positive = female
royalty_axis  = np.zeros(DIM); royalty_axis[1]  = 1.0   # positive = royal
age_axis      = np.zeros(DIM); age_axis[2]      = 0.5   # positive = adult

# Build clean embeddings: (gender_score, royalty_score, age_score) + noise
def make_emb(gender, royalty, age, noise=0.15):
    e = gender * gender_axis + royalty * royalty_axis + age * age_axis
    e += rng.normal(0, noise, DIM)
    return e

# Primary words (large markers)
embeddings = {
    'man':     make_emb(gender=-1.0, royalty=0.0, age=1.0),
    'woman':   make_emb(gender= 1.0, royalty=0.0, age=1.0),
    'king':    make_emb(gender=-1.0, royalty=1.0, age=1.0),
    'queen':   make_emb(gender= 1.0, royalty=1.0, age=1.0),
    # Secondary words
    'prince':  make_emb(gender=-1.0, royalty=0.8, age=-0.3),
    'princess':make_emb(gender= 1.0, royalty=0.8, age=-0.3),
    'boy':     make_emb(gender=-1.0, royalty=0.0, age=-0.8),
    'girl':    make_emb(gender= 1.0, royalty=0.0, age=-0.8),
}

words   = list(embeddings.keys())
matrix  = np.array([embeddings[w] for w in words])

pca = PCA(n_components=2, random_state=42)
coords = pca.fit_transform(matrix)

word_to_coord = {w: coords[i] for i, w in enumerate(words)}

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, ax = plt.subplots()

primary   = ['man', 'woman', 'king', 'queen']
secondary = ['prince', 'princess', 'boy', 'girl']

male_words   = ['man', 'king', 'prince', 'boy']
female_words = ['woman', 'queen', 'princess', 'girl']

# Plot secondary words first (behind primary)
for w in secondary:
    x, y = word_to_coord[w]
    color = MLPURPLE if w in male_words else MLORANGE
    ax.scatter(x, y, s=80, color=color, alpha=0.4, zorder=2)
    ax.annotate(w, (x, y), textcoords='offset points', xytext=(6, 4),
                fontsize=11, color=color, alpha=0.6)

# Plot primary words
for w in primary:
    x, y = word_to_coord[w]
    color = MLPURPLE if w in male_words else MLORANGE
    ax.scatter(x, y, s=220, color=color, zorder=4, edgecolors='white', linewidths=1.0)
    offset = {'man': (-14, -18), 'woman': (6, -18), 'king': (-14, 8), 'queen': (6, 8)}
    ax.annotate(w, (x, y), textcoords='offset points', xytext=offset[w],
                fontsize=13, fontweight='bold', color=color)

# ---------------------------------------------------------------------------
# Parallelogram: man -> king  AND  woman -> queen  (royal dimension)
#                man -> woman AND  king  -> queen  (gender dimension)
# Draw dashed arrows for the gender shift: man->woman and king->queen
# ---------------------------------------------------------------------------
arrow_kw = dict(arrowstyle='->', color='#555555', lw=1.5,
                connectionstyle='arc3,rad=0.0',
                linestyle='dashed', mutation_scale=16)

for start, end in [('man', 'woman'), ('king', 'queen')]:
    ax.annotate('',
                xy=word_to_coord[end],
                xytext=word_to_coord[start],
                arrowprops=arrow_kw)

# Draw solid arrows for royalty shift: man->king and woman->queen
arrow_kw_solid = dict(arrowstyle='->', color='#888888', lw=1.2,
                      connectionstyle='arc3,rad=0.0',
                      linestyle='dotted', mutation_scale=14)

for start, end in [('man', 'king'), ('woman', 'queen')]:
    ax.annotate('',
                xy=word_to_coord[end],
                xytext=word_to_coord[start],
                arrowprops=arrow_kw_solid)

# ---------------------------------------------------------------------------
# Equation annotation
# ---------------------------------------------------------------------------
ax.text(0.03, 0.96,
        r'$\mathbf{king} - \mathbf{man} + \mathbf{woman} \approx \mathbf{queen}$',
        transform=ax.transAxes, fontsize=13,
        verticalalignment='top',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#F5F5F5', edgecolor='#CCCCCC', alpha=0.9))

# ---------------------------------------------------------------------------
# Legend
# ---------------------------------------------------------------------------
male_patch   = mpatches.Patch(color=MLPURPLE, label='Male words')
female_patch = mpatches.Patch(color=MLORANGE, label='Female words')
ax.legend(handles=[male_patch, female_patch], loc='lower right', framealpha=0.85)

# ---------------------------------------------------------------------------
# Labels, grid, URL
# ---------------------------------------------------------------------------
ax.set_xlabel('PCA Component 1')
ax.set_ylabel('PCA Component 2')
ax.set_title('Word Analogy: Vector Arithmetic in Embedding Space')
ax.grid(alpha=0.3)

ax.text(0.99, 0.01, CHART_METADATA["url"],
        transform=ax.transAxes, fontsize=7, color='#AAAAAA',
        ha='right', va='bottom')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
