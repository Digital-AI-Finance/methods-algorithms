"""Create the complete directory structure for Methods and Algorithms course."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Directory structure
DIRECTORIES = [
    # Infrastructure
    "infrastructure",
    "infrastructure/validators",
    "infrastructure/builders",
    "infrastructure/reporters",
    "infrastructure/deployers",
    "infrastructure/generators",

    # Documentation
    "docs",
    "docs/css",
    "docs/js",
    "docs/assets",

    # Slides for each topic
    "slides/L01_Introduction_Linear_Regression",
    "slides/L01_Introduction_Linear_Regression/01_simple_regression",
    "slides/L01_Introduction_Linear_Regression/02_multiple_regression",
    "slides/L01_Introduction_Linear_Regression/03_residual_plots",
    "slides/L01_Introduction_Linear_Regression/04_gradient_descent",
    "slides/L01_Introduction_Linear_Regression/05_learning_curves",
    "slides/L01_Introduction_Linear_Regression/06_regularization",
    "slides/L01_Introduction_Linear_Regression/07_bias_variance",
    "slides/L01_Introduction_Linear_Regression/08_decision_flowchart",
    "slides/L01_Introduction_Linear_Regression/temp",

    "slides/L02_Logistic_Regression",
    "slides/L02_Logistic_Regression/01_sigmoid_function",
    "slides/L02_Logistic_Regression/02_decision_boundary",
    "slides/L02_Logistic_Regression/03_log_loss",
    "slides/L02_Logistic_Regression/04_roc_curve",
    "slides/L02_Logistic_Regression/05_precision_recall",
    "slides/L02_Logistic_Regression/06_confusion_matrix",
    "slides/L02_Logistic_Regression/07_decision_flowchart",
    "slides/L02_Logistic_Regression/temp",

    "slides/L03_KNN_KMeans",
    "slides/L03_KNN_KMeans/01_knn_decision_boundary",
    "slides/L03_KNN_KMeans/02_distance_metrics",
    "slides/L03_KNN_KMeans/03_kmeans_iterations",
    "slides/L03_KNN_KMeans/04_elbow_method",
    "slides/L03_KNN_KMeans/05_silhouette_analysis",
    "slides/L03_KNN_KMeans/06_voronoi_diagram",
    "slides/L03_KNN_KMeans/07_decision_flowchart",
    "slides/L03_KNN_KMeans/temp",

    "slides/L04_Random_Forests",
    "slides/L04_Random_Forests/01_decision_tree",
    "slides/L04_Random_Forests/02_feature_importance",
    "slides/L04_Random_Forests/03_bootstrap_sampling",
    "slides/L04_Random_Forests/04_oob_error",
    "slides/L04_Random_Forests/05_ensemble_voting",
    "slides/L04_Random_Forests/06_bias_variance",
    "slides/L04_Random_Forests/07_decision_flowchart",
    "slides/L04_Random_Forests/temp",

    "slides/L05_PCA_tSNE",
    "slides/L05_PCA_tSNE/01_scree_plot",
    "slides/L05_PCA_tSNE/02_principal_components",
    "slides/L05_PCA_tSNE/03_reconstruction_error",
    "slides/L05_PCA_tSNE/04_tsne_perplexity",
    "slides/L05_PCA_tSNE/05_projection_comparison",
    "slides/L05_PCA_tSNE/06_cluster_preservation",
    "slides/L05_PCA_tSNE/07_decision_flowchart",
    "slides/L05_PCA_tSNE/temp",

    "slides/L06_Embeddings_RL",
    "slides/L06_Embeddings_RL/01_word_embeddings",
    "slides/L06_Embeddings_RL/02_similarity_heatmap",
    "slides/L06_Embeddings_RL/03_rl_agent_environment",
    "slides/L06_Embeddings_RL/04_qlearning_gridworld",
    "slides/L06_Embeddings_RL/05_reward_curves",
    "slides/L06_Embeddings_RL/06_exploration_exploitation",
    "slides/L06_Embeddings_RL/07_decision_flowchart",
    "slides/L06_Embeddings_RL/temp",

    # Quizzes
    "quizzes",

    # Notebooks
    "notebooks",

    # Datasets
    "datasets",

    # Presentations
    "presentations",

    # Capstone
    "capstone",
    "capstone/examples",

    # Rubrics
    "rubrics",

    # Syllabus
    "syllabus",

    # Templates
    "templates",
]

def create_structure():
    """Create all directories."""
    created = []
    for dir_path in DIRECTORIES:
        full_path = BASE_DIR / dir_path
        if not full_path.exists():
            full_path.mkdir(parents=True, exist_ok=True)
            created.append(dir_path)
    return created

if __name__ == "__main__":
    created = create_structure()
    print(f"Created {len(created)} directories:")
    for d in created:
        print(f"  {d}")
    print("\nDirectory structure setup complete.")
