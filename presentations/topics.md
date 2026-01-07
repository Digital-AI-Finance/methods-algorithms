# Student Presentation Topics

**Course**: Methods and Algorithms - MSc Data Science
**Format**: 15-minute individual presentations
**Schedule**: 2-3 presentations per session

---

## Topic Selection Process

1. Topics are assigned on a first-come, first-served basis
2. Sign up via Moodle before Session 1
3. Each student presents once during the course
4. Presentations are graded using the rubric in `rubrics/presentation_rubric.md`

---

## Session 1-2: Regression Topics

### Topic 1: Ridge vs Lasso Regression - When to Use Which?

**Description**: Compare L1 (Lasso) and L2 (Ridge) regularization techniques. Explain the mathematical differences, demonstrate when each is preferred, and show how Elastic Net combines both approaches.

**Key Points to Cover**:
- Mathematical formulation of both penalties
- Geometric interpretation (why Lasso produces sparse solutions)
- Cross-validation for lambda selection
- Real-world example with feature selection

**Suggested Resources**:
- Hastie et al., "Elements of Statistical Learning", Chapter 3
- scikit-learn documentation on linear models

---

### Topic 2: Logistic Regression in Healthcare - Disease Prediction

**Description**: Explore how logistic regression is applied in medical diagnosis. Discuss model calibration, threshold selection for clinical decisions, and interpretation of odds ratios for medical professionals.

**Key Points to Cover**:
- Binary classification for disease screening
- ROC curves and choosing optimal thresholds
- Calibration curves and Brier score
- Communicating risk to patients and doctors

**Suggested Resources**:
- Steyerberg, "Clinical Prediction Models"
- MIMIC-III database examples

---

### Topic 3: Feature Engineering for Linear Models

**Description**: Demonstrate techniques to enhance linear model performance through feature engineering. Cover polynomial features, interaction terms, binning, and handling categorical variables.

**Key Points to Cover**:
- Polynomial and interaction features
- One-hot vs target encoding for categories
- Feature scaling and normalization
- Avoiding data leakage during feature engineering

**Suggested Resources**:
- Kuhn & Johnson, "Feature Engineering and Selection"
- Kaggle feature engineering tutorials

---

## Session 3: Distance-Based Methods

### Topic 4: Distance Metrics Beyond Euclidean

**Description**: Explore alternative distance metrics for KNN and clustering. Compare Manhattan, Chebyshev, Mahalanobis, and cosine distance. Discuss when each is appropriate.

**Key Points to Cover**:
- Mathematical definitions of each metric
- Effect on KNN decision boundaries
- Mahalanobis for correlated features
- Cosine similarity for text/high-dimensional data

**Suggested Resources**:
- Aggarwal, "Data Mining: The Textbook", Chapter 3
- scipy.spatial.distance documentation

---

### Topic 5: K-Means++ and Initialization Strategies

**Description**: Deep dive into K-Means initialization methods. Compare random initialization, K-Means++, and K-Means||. Show how initialization affects convergence and final cluster quality.

**Key Points to Cover**:
- The problem with random initialization
- K-Means++ algorithm step-by-step
- Scalable K-Means|| for large datasets
- Multiple restarts and choosing best result

**Suggested Resources**:
- Arthur & Vassilvitskii (2007), "K-means++: The Advantages of Careful Seeding"
- scikit-learn KMeans implementation details

---

### Topic 6: DBSCAN vs K-Means - Density-Based Clustering

**Description**: Compare partitioning (K-Means) and density-based (DBSCAN) clustering. Discuss handling non-spherical clusters, outlier detection, and parameter selection for DBSCAN.

**Key Points to Cover**:
- DBSCAN algorithm: eps and min_samples
- Advantages for arbitrary-shaped clusters
- Automatic outlier detection
- HDBSCAN as a modern alternative

**Suggested Resources**:
- Ester et al. (1996), original DBSCAN paper
- HDBSCAN documentation and tutorials

---

## Session 4: Ensemble Methods

### Topic 7: XGBoost vs Random Forest - A Comparison

**Description**: Compare bagging (Random Forest) and boosting (XGBoost) ensemble methods. Discuss when to use each, computational considerations, and hyperparameter tuning strategies.

**Key Points to Cover**:
- Bagging vs boosting conceptual differences
- Bias-variance tradeoffs of each approach
- Key hyperparameters for XGBoost
- Performance benchmarks on common datasets

**Suggested Resources**:
- Chen & Guestrin (2016), "XGBoost: A Scalable Tree Boosting System"
- Kaggle competition winning solutions

---

### Topic 8: SHAP Values for Model Interpretability

**Description**: Explain how SHAP (SHapley Additive exPlanations) values enable interpretation of complex models. Demonstrate global and local explanations for tree-based models.

**Key Points to Cover**:
- Game theory foundation (Shapley values)
- TreeSHAP for efficient computation
- Feature importance vs dependence plots
- Explaining individual predictions

**Suggested Resources**:
- Lundberg & Lee (2017), "A Unified Approach to Interpreting Model Predictions"
- SHAP library documentation and examples

---

### Topic 9: Imbalanced Classification with Tree Ensembles

**Description**: Address class imbalance in fraud detection and rare event prediction using tree ensembles. Cover SMOTE, class weights, and threshold optimization.

**Key Points to Cover**:
- Impact of imbalance on model training
- Oversampling (SMOTE) vs undersampling
- Class weights in Random Forest/XGBoost
- Evaluation: precision-recall, F1, balanced accuracy

**Suggested Resources**:
- imbalanced-learn library documentation
- He & Garcia (2009), "Learning from Imbalanced Data"

---

## Session 5: Dimensionality Reduction

### Topic 10: UMAP - The Modern Alternative to t-SNE

**Description**: Introduce UMAP (Uniform Manifold Approximation and Projection) as a faster alternative to t-SNE. Compare mathematical foundations, speed, and preservation of global structure.

**Key Points to Cover**:
- Topological data analysis foundation
- UMAP parameters: n_neighbors, min_dist
- Speed comparison with t-SNE
- When to choose UMAP vs t-SNE vs PCA

**Suggested Resources**:
- McInnes et al. (2018), UMAP paper
- umap-learn library examples

---

### Topic 11: PCA in Finance - Portfolio Risk Decomposition

**Description**: Apply PCA to decompose portfolio risk into principal components. Explain how factor models in finance relate to PCA and discuss practical applications in risk management.

**Key Points to Cover**:
- Covariance matrix of asset returns
- Interpreting principal components as risk factors
- Connection to Fama-French factors
- Variance contribution and risk attribution

**Suggested Resources**:
- Connor & Korajczyk, "Performance Measurement with the Arbitrage Pricing Theory"
- QuantLib examples

---

### Topic 12: Autoencoders vs PCA for Dimensionality Reduction

**Description**: Compare linear (PCA) and non-linear (autoencoder) dimensionality reduction. Demonstrate when neural network approaches outperform classical methods.

**Key Points to Cover**:
- Autoencoder architecture (encoder-decoder)
- Relationship: linear autoencoder = PCA
- Variational autoencoders for generative modeling
- Computational tradeoffs

**Suggested Resources**:
- Goodfellow et al., "Deep Learning", Chapter 14
- Keras/PyTorch autoencoder tutorials

---

## Session 6: Advanced Topics

### Topic 13: BERT and Transformer Embeddings

**Description**: Introduce BERT and transformer-based embeddings as the state-of-the-art in text representation. Compare with Word2Vec and discuss fine-tuning for finance applications.

**Key Points to Cover**:
- Transformer architecture overview
- Pre-training objectives (MLM, NSP)
- Sentence-BERT for semantic similarity
- FinBERT for financial NLP

**Suggested Resources**:
- Devlin et al. (2019), BERT paper
- Hugging Face transformers library

---

### Topic 14: Deep Q-Networks - From Atari to Real World

**Description**: Explain how Deep Q-Networks (DQN) extend tabular Q-learning with neural networks. Discuss experience replay, target networks, and applications beyond games.

**Key Points to Cover**:
- From Q-table to Q-network
- Experience replay buffer
- Target network for stability
- Limitations and extensions (Double DQN, Dueling DQN)

**Suggested Resources**:
- Mnih et al. (2015), DQN Atari paper
- OpenAI Spinning Up in Deep RL

---

### Topic 15: Multi-Armed Bandits in A/B Testing

**Description**: Apply multi-armed bandit algorithms to online experimentation. Compare epsilon-greedy, UCB, and Thompson Sampling for efficient A/B testing with fewer samples.

**Key Points to Cover**:
- Exploration-exploitation in A/B testing
- Epsilon-greedy baseline
- Upper Confidence Bound (UCB)
- Thompson Sampling with Bayesian updates

**Suggested Resources**:
- Russo et al. (2018), "A Tutorial on Thompson Sampling"
- Google's Bandits for Recommendations

---

## Presentation Schedule

| Session | Topics | Presenter |
|---------|--------|-----------|
| 1 | Topics 1-2 | TBD |
| 2 | Topic 3 | TBD |
| 3 | Topics 4-6 | TBD |
| 4 | Topics 7-9 | TBD |
| 5 | Topics 10-12 | TBD |
| 6 | Topics 13-15 | TBD |

---

## Grading Criteria

See `rubrics/presentation_rubric.md` for detailed grading criteria:
- Content Accuracy (25 points)
- Clarity and Organization (25 points)
- Visual Aids and Slides (25 points)
- Timing and Delivery (25 points)

**Total: 100 points**
