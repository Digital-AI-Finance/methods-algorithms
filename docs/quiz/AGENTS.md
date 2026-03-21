<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-03-18 | Updated: 2026-03-18 -->

# quiz/

**Parent**: [../AGENTS.md](../AGENTS.md) (docs/)

## Purpose

Interactive JavaScript quizzes for self-assessment. Each quiz is a standalone HTML file using KaTeX for math rendering. No backend required -- all logic runs client-side.

## Key Files

| File | Topic | Questions |
|------|-------|-----------|
| `L01_linear_regression.html` | Linear regression basics | 20 |
| `L02_logistic_regression.html` | Logistic regression basics | 20 |
| `L03_knn.html` | K-Nearest Neighbors | 20 |
| `L03_kmeans.html` | K-Means clustering | 20 |
| `L03_knn_kmeans.html` | Combined KNN + K-Means | 20 |
| `L04_random_forests.html` | Random forests basics | 10 |
| `L04_random_forests_simple.html` | Random forests (simplified) | 10 |
| `L04_decision_trees.html` | Decision trees | 20 |
| `L04_ensemble_methods.html` | Ensemble methods | 20 |
| `L05_pca_simple.html` | PCA basics | 20 |
| `L05_tsne_simple.html` | t-SNE basics | 20 |
| `L05_pca_tsne.html` | Combined PCA + t-SNE | 20 |
| `L06_embeddings_simple.html` | Embeddings basics | 20 |
| `L06_rl_simple.html` | RL basics | 20 |
| `L06_embeddings_rl.html` | Combined Embeddings + RL | 20 |
| `quiz1_regression.html` | Cross-topic regression quiz | 20 |
| `quiz2_classification_ensemble.html` | Cross-topic classification quiz | 20 |
| `quiz3_advanced.html` | Advanced topics quiz | 20 |
| `quiz_template.html` | Template for new quizzes | - |

## For AI Agents

### Working In This Directory

- Quizzes are standalone HTML -- each file is self-contained with inline CSS/JS
- KaTeX is loaded from CDN for math rendering
- Call `render()` or `initQuiz()` directly at end of `<body>`, NOT inside DOMContentLoaded (may have already fired)
- Use `setTimeout(renderMath, 100)` after quiz initialization for KaTeX

### Creating New Quizzes

Copy `quiz_template.html` and follow the pattern. Each question needs:
- Question text (may include KaTeX `\( ... \)` for inline math)
- 4 answer options (radio buttons)
- Correct answer index
- Explanation text

### Testing

Open HTML files directly in a browser. No build step required.
