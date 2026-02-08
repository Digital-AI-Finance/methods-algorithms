# Example Projects: ML Pipeline Challenge

**These examples illustrate the expected scope, depth, and quality. Your project should demonstrate similar analytical rigor.**

**All quantitative results below are illustrative — your actual results will differ based on your dataset and implementation.**

---

## Example 1: Credit Risk Modeling

**Difficulty**: Moderate (Omits L06 — remaining 9 difficulty points, multiplier 0.88)
**Dataset**: Kaggle "Home Credit Default Risk" (300K+ loans, 120+ features)

**Why this combination works**: Credit risk is a classic finance problem. The binary default/no-default target naturally supports logistic regression and tree ensembles. The large feature set benefits from PCA dimensionality reduction. K-Means segments borrowers into risk profiles.

### Topic Pipeline

#### 1. L01: Linear Regression — Predict log(annuity amount) from applicant features as a precursor analysis

**Key results**:
- Adjusted R-squared = 0.48, indicating moderate explanatory power
- VIF analysis identifies 3 highly collinear features (VIF > 10) — these are dropped or combined
- Breusch-Pagan test detects heteroscedasticity (p = 0.003) — use robust standard errors
- F-test confirms joint significance of predictors (F = 245, p < 0.001)
- Residual diagnostics show slight non-normality (QQ-plot deviates in tails)

**Implementation notes**: Use `statsmodels` for detailed regression diagnostics. Apply log transformation to the target (annuity amount) to stabilize variance. Report both coefficient estimates and 95% confidence intervals.

---

#### 2. L02: Logistic Regression — Classify default vs. no-default

**Key results**:
- AUC = 0.76 on hold-out test set (10-fold CV mean = 0.75, SD = 0.02)
- Likelihood ratio test comparing nested models: chi-squared = 45.3, p < 0.001 (adding employment features significantly improves fit)
- Hosmer-Lemeshow test indicates adequate calibration (p = 0.15, fail to reject null of good fit)
- Odds ratios reveal top risk factors:
  - External source score 2: OR = 0.42 (p < 0.001) — higher score = lower default risk
  - Days employed (per 1000 days): OR = 0.87 (p = 0.002)
  - Number of previous loans: OR = 1.12 (p = 0.01)

**Implementation notes**: Use `sklearn.linear_model.LogisticRegressionCV` for regularization path. Check class balance (defaults are ~8% of sample) — consider SMOTE or class weights. Report precision-recall curve in addition to ROC.

---

#### 3. L03: K-Means — Segment borrowers into risk clusters

**Key results**:
- Silhouette analysis finds k=4 optimal (mean silhouette = 0.38)
- Gap statistic confirms k=4 as the "elbow"
- Cluster profiles:
  - **Cluster 1** (32% of borrowers): "Low-risk salaried" — high income, stable employment, 3% default rate
  - **Cluster 2** (28%): "High-risk self-employed" — variable income, 18% default rate
  - **Cluster 3** (25%): "Mid-risk retirees" — lower income, 9% default rate
  - **Cluster 4** (15%): "Young first-time borrowers" — short credit history, 14% default rate
- Davies-Bouldin index = 1.12 (lower is better, confirms reasonable separation)

**Implementation notes**: Standardize features before clustering. Use PCA-reduced features (first 15 components) to avoid curse of dimensionality. Visualize clusters with t-SNE colored by cluster label.

---

#### 4. L04: Random Forest + XGBoost — Main prediction model with boosting comparison

**Key results**:
- Random Forest: AUC = 0.80, F1 = 0.63, optimal threshold = 0.18 (maximizes F1)
- XGBoost: AUC = 0.82, F1 = 0.66, optimal threshold = 0.15
- Paired t-test on 5-fold CV AUC scores confirms XGBoost significantly better (mean difference = 0.02, p = 0.04)
- SHAP analysis reveals top features:
  1. EXT_SOURCE_2 (credit bureau score)
  2. EXT_SOURCE_3 (alternative credit bureau score)
  3. DAYS_BIRTH (age in days — older applicants less risky)
  4. AMT_CREDIT (loan amount)
  5. DAYS_EMPLOYED
- Permutation importance confirms SHAP ranking (95% CI computed via bootstrap)
- Feature interaction: SHAP interaction plot shows EXT_SOURCE_2 x DAYS_EMPLOYED interaction (young + low score = highest risk)

**Implementation notes**: Use `xgboost.XGBClassifier` with early stopping and 20% validation split. Hyperparameter tuning via `RandomizedSearchCV` (50 iterations). Report feature importance with error bars.

---

#### 5. L05: PCA + t-SNE — Reduce 120 features, visualize risk structure

**Key results**:
- First 15 principal components explain 78% of cumulative variance
- Parallel analysis (via permutation test) retains 10 components at 95% confidence
- Scree plot shows clear "elbow" at PC 6
- PC1 (24% variance): "financial capacity" factor (high loadings on income, credit amount)
- PC2 (12% variance): "credit history" factor (high loadings on previous loans, bureau scores)
- PC3 (8% variance): "age/stability" factor (high loadings on age, employment duration)
- t-SNE visualization (perplexity=30, 1000 iterations):
  - Default cases (red) overlap significantly with non-defaults (blue)
  - This confirms prediction difficulty — no clean separability in feature space
  - Some default clusters emerge in high-risk regions, but substantial overlap persists

**Implementation notes**: Use `sklearn.decomposition.PCA` with `whiten=True`. For t-SNE, try perplexities in [10, 30, 50] and report best visual separation. Color points by both cluster label (K-Means) and default status.

---

### Business Insight

"The XGBoost model identifies 72% of defaults in the top 20% riskiest applicants (high precision for top-decile). Deploying this as a pre-screening tool could reduce default losses by an estimated 30% while rejecting only 15% of good borrowers (false positive rate at optimized threshold).

SHAP analysis reveals credit bureau scores (EXT_SOURCE_2, EXT_SOURCE_3) dominate predictions — the bank should invest in enriching this data and negotiating access to additional bureau information.

K-Means segmentation shows the 'high-risk self-employed' cluster has 18% default rate vs. 3% for 'low-risk salaried' — consider differential pricing or higher down-payment requirements for this segment."

---

### What Makes This Project Strong

- **Clear business problem**: Credit risk with quantifiable financial impact
- **Statistical tests at every step**: VIF, Breusch-Pagan, likelihood ratio test, silhouette, paired t-test
- **Honest reporting of model limitations**: t-SNE shows overlap (prediction is hard), acknowledged
- **Actionable business recommendation**: Specific operational changes (pre-screening, data acquisition, segment-based pricing)
- **Appropriate method choices**: Each method serves a purpose (L01 for inference, L02 for baseline classification, L03 for segmentation, L04 for best prediction, L05 for dimensionality reduction and visualization)

---

## Example 2: Customer Churn Prediction

**Difficulty**: High (Omits L01 — remaining 12 difficulty points, multiplier 1.00)
**Dataset**: Kaggle "Telco Customer Churn" (7K customers, 21 features) + Financial PhraseBank for sentiment analysis

**Why this combination works**: Churn prediction combines classification with customer segmentation. Adding L06 (embeddings) through sentiment analysis of public financial complaint text demonstrates the full NLP pipeline. Omitting L01 is natural since churn is a binary classification problem (not regression).

### Topic Pipeline

#### 1. L02: Logistic Regression — Baseline churn prediction

**Key results**:
- AUC = 0.83 on test set (stratified 70/30 train/test split)
- Odds ratios reveal key churn drivers:
  - Month-to-month contract: OR = 4.2 (p < 0.001) vs. two-year contract
  - Fiber optic internet: OR = 2.1 (p = 0.003) — counterintuitive, suggests service quality issues
  - Tech support = No: OR = 1.8 (p = 0.02)
  - Tenure (per year): OR = 0.92 (p < 0.001) — longer tenure reduces churn
- AIC model selection: reduced model (12 features) preferred over full model (21 features), delta-AIC = -8.3
- Brier score = 0.18 (calibration is good)

**Implementation notes**: Handle missing values in TotalCharges (0.2% of rows). One-hot encode categorical features. Use `LogisticRegressionCV` with L2 penalty.

---

#### 2. L03: KNN + K-Means — KNN churn classifier + customer segmentation

**Key results**:

**KNN Classifier**:
- k=7 selected via 5-fold CV (best accuracy = 0.79)
- Distance metric: Euclidean on standardized features
- AUC = 0.79 (lower than logistic regression 0.83 — simpler decision boundary works better)
- Confusion matrix at default threshold: precision = 0.65, recall = 0.71

**K-Means Segmentation** (k=3):
- Silhouette score = 0.35 (moderate separation)
- Gap statistic confirms k=3 as optimal
- Cluster profiles:
  - **Cluster 1** (38%): "High-value loyal" — tenure > 40 months, two-year contracts, 8% churn rate
  - **Cluster 2** (34%): "At-risk new" — tenure < 12 months, month-to-month contracts, 47% churn rate
  - **Cluster 3** (28%): "Price-sensitive mid-tenure" — tenure 12-40 months, lower monthly charges, 23% churn rate
- ANOVA confirms clusters differ significantly on tenure (F = 245, p < 0.001) and monthly charges (F = 89, p < 0.001)

**Implementation notes**: Use `sklearn.neighbors.KNeighborsClassifier` with `n_jobs=-1` for speed. For K-Means, try k in [2, 3, 4, 5, 6] and compare silhouette + Gap statistic.

---

#### 3. L04: Random Forest + XGBoost — Best-performing churn model

**Key results**:
- Random Forest: AUC = 0.84, F1 = 0.64
- XGBoost: AUC = 0.86, F1 = 0.68
- Paired t-test on 5-fold CV: XGBoost vs. logistic regression AUC difference = 0.03, p = 0.02 (significant improvement)
- SHAP analysis:
  - Top feature: contract type (month-to-month adds +0.4 to log-odds)
  - Interaction: tenure x contract type (short tenure + month-to-month = extreme risk)
  - Internet service type has non-linear effect (fiber optic high risk, DSL moderate, no service low risk)
- Feature importance stability: bootstrap 95% CI for top 5 features all exclude zero

**Implementation notes**: Use `xgboost.XGBClassifier` with scale_pos_weight to handle class imbalance (churn = 27% of sample). Early stopping on validation set.

---

#### 4. L05: PCA + t-SNE — Customer feature visualization

**Key results**:
- First 5 principal components explain 72% of variance
- PC1 (28% variance): "Engagement" factor (high loadings on tenure, contract type, number of services)
- PC2 (18% variance): "Spending" factor (high loadings on monthly charges, total charges)
- PC3 (12% variance): "Service complexity" factor (high loadings on internet service, tech support)
- Parallel analysis retains 4 components
- t-SNE (perplexity=30, 1000 iterations):
  - Visual separation between churners (red) and non-churners (blue)
  - Churners concentrate in "low engagement" region (low PC1)
  - "At-risk new" cluster (from K-Means) clearly separates in t-SNE space

**Implementation notes**: Standardize before PCA. For t-SNE, set `random_state` for reproducibility and try multiple perplexities.

---

#### 5. L06: Word Embeddings — Sentiment from complaint text

**Key results**:
- Dataset: Financial PhraseBank (4,840 sentences labeled positive/neutral/negative)
- Pre-trained embeddings: Word2Vec Google News 300d (via `gensim`)
- Document embedding: Average word vectors per sentence, weighted by TF-IDF
- Cosine similarity clustering (hierarchical clustering with Ward linkage) reveals 4 complaint themes:
  1. **Billing issues** (32% of complaints): "charge", "bill", "fee", "overcharge"
  2. **Service quality** (28%): "slow", "outage", "connection", "dropped"
  3. **Pricing concerns** (24%): "expensive", "increase", "price", "cost"
  4. **Support problems** (16%): "wait", "representative", "help", "hold"
- Sentiment feature: Mean sentiment score per customer (inferred from complaint topic prevalence in telco complaint forum, scraped and mapped to Financial PhraseBank labels)
- **Impact**: Adding sentiment feature to XGBoost improves AUC from 0.86 to 0.87 (delta = 0.01, p = 0.08 via paired t-test — modest and not statistically significant at alpha=0.05, but demonstrates the NLP pipeline)

**Implementation notes**: Download `gensim-data` Word2Vec model. For small datasets, embeddings may not improve much — **this is OK to report honestly**. The value is in demonstrating the method, not inflating its impact.

---

### Business Insight

"Combining XGBoost predictions with K-Means segmentation allows targeted intervention:

**Recommendation 1**: Target the 'at-risk new' cluster (tenure < 12 months, month-to-month contracts) with 12-month contract discounts. Model predicts this reduces churn from 47% to 34% (estimated 23% churn reduction), recovering $480K in annual revenue (assuming $60 monthly ARPU and 800 at-risk customers).

**Recommendation 2**: Sentiment analysis shows billing complaints dominate (32% of complaint themes). Deploy proactive billing communication (itemized monthly summaries, alerts before price changes) to reduce billing-related churn.

**Recommendation 3**: Fiber optic customers churn at 2.1x the rate of DSL customers (OR = 2.1) — investigate fiber service quality issues (outages, speed consistency). SHAP shows this is the second-most important feature after contract type."

---

### What Makes This Project Strong

- **Uses an external NLP corpus**: Financial PhraseBank demonstrates embeddings on a separate dataset, then applies to telco domain
- **Honest about modest NLP improvement**: AUC lift of 0.01 is small and not significant — this honesty is valued
- **Segmentation directly drives business recommendations**: K-Means isn't just exploratory, it informs operational strategy
- **Full statistical rigor**: Likelihood ratio tests, paired t-tests, silhouette analysis, parallel analysis, bootstrap CIs
- **Includes L06 (high difficulty)**: Demonstrates the full course pipeline including advanced NLP

---

## Example 3: Equity Factor Investing with RL

**Difficulty**: Maximum (Omits L03 — remaining 11 difficulty points, multiplier 0.96)
**Dataset**: Yahoo Finance daily prices for 50 S&P 500 stocks (2015-2025), financial ratios from SimFin

**Why this combination works**: Finance students can leverage factor models (L01), return prediction (L02, L04), risk factor decomposition (L05), and trading strategy (L06). This is the most ambitious combination — and the example honestly shows that some methods (RL) may not outperform simple baselines. **Negative results are valuable when analyzed rigorously.**

### Topic Pipeline

#### 1. L01: Linear Regression — Fama-French three-factor model

**Key results**:
- Model: R_i - R_f = alpha + beta1 * MKT + beta2 * SMB + beta3 * HML + error
- Applied to 50 stocks individually (daily returns, 2015-2020 training period)
- Median adjusted R-squared = 0.31 (typical for individual stocks — systematic factors explain ~30% of variance)
- Alpha (excess return) significant for 5 of 50 stocks at p < 0.05 (expected by chance: 2.5 stocks, so slightly elevated)
- Diagnostics:
  - Durbin-Watson statistic: median = 1.92 (no autocorrelation)
  - Breusch-Pagan test detects heteroscedasticity for 18 stocks (p < 0.05) — use HAC (Newey-West) standard errors
  - Jarque-Bera test: 42 stocks have non-normal residuals (heavy tails) — expected for daily returns
- Beta interpretation: High-beta stocks (beta > 1.5) include tech growth names, low-beta (beta < 0.7) include utilities

**Implementation notes**: Download Fama-French factors from Kenneth French's data library. Use `statsmodels.regression.linear_model.OLS` with HAC standard errors (`cov_type='HAC', cov_kwds={'maxlags':5}`).

---

#### 2. L02: Logistic Regression — Predict next-month outperformance

**Key results**:
- Target: y = 1 if stock return > market return next month, else 0
- Features: momentum (1M, 3M, 6M returns), value (P/E, P/B ratios), size (market cap), volatility (30-day realized vol)
- AUC = 0.56 on test set (2021-2023) — **barely above random (0.50)**
- Brier score = 0.25 (calibration is poor)
- **Honest conclusion**: Logistic regression has limited predictive power for equity returns. This is expected — markets are highly efficient for large-cap stocks. AUC of 0.56 is consistent with academic literature on return predictability.
- Coefficient significance: momentum (6M) has p = 0.04, but effect size is tiny (OR = 1.08 per 10% return)
- Class balance: 48% outperformers, 52% underperformers (well balanced)

**Implementation notes**: Use walk-forward validation (retrain monthly). Report both in-sample and out-of-sample AUC. **Do not overfit** — this is a negative result, which is scientifically valuable.

---

#### 3. L04: Random Forest + XGBoost — Feature-rich return prediction

**Key results**:
- Random Forest: classification accuracy = 53% (vs. 50% baseline)
- XGBoost: classification accuracy = 55%, AUC = 0.58
- Binomial test: 55% accuracy over 600 stock-month predictions, p = 0.04 (significantly better than random)
- SHAP analysis:
  - Top feature: 6-month momentum (SHAP value range: -0.05 to +0.08)
  - Second: P/E ratio (low P/E slightly predictive of outperformance)
  - Third: 30-day realized volatility (high vol → unpredictable, neutral SHAP)
- Walk-forward validation (retrain every 6 months): feature importance unstable across time windows (correlation of importance ranks = 0.43 between 2018-2020 and 2021-2023 windows)
- **This instability is evidence of non-stationarity** — feature relationships change over time

**Implementation notes**: Use `xgboost.XGBClassifier` with `objective='binary:logistic'`. Report SHAP summary plot and feature importance over multiple time windows.

---

#### 4. L05: PCA — Factor structure of stock returns

**Key results**:
- PCA on correlation matrix of 50 stock returns (daily, 2015-2023)
- PC1: "Market factor" — explains 42% of variance, positive loadings on all stocks (captures systematic risk)
- PC2: "Sector rotation" — explains 9% of variance, high loadings on tech (positive) vs. utilities (negative)
- PC3: "Size factor" — explains 5% of variance, high loadings on large-cap vs. small-cap
- PC4-PC6 explain 3-4% each
- Parallel analysis (via permutation test on randomized data) retains 6 components at 95% confidence
- Cumulative variance explained by 6 PCs: 73%
- **Interpretation**: The 6 PCs correspond to interpretable risk factors (market, sector, size, value, momentum, volatility regime) — consistent with multifactor asset pricing theory

**Implementation notes**: Use correlation matrix (not covariance) to avoid scale dominance by high-volatility stocks. Visualize loadings as a heatmap to identify sector patterns.

---

#### 5. L06: Reinforcement Learning (Q-Learning) — Simple trading agent

**State space**:
- Momentum quintile: [1, 2, 3, 4, 5] based on 6-month return rank
- Volatility regime: [low, medium, high] based on 30-day realized vol tercile
- Current position: [long, neutral, short]
- Total states: 5 x 3 x 3 = 45

**Action space**:
- Buy (if not already long), Hold, Sell (if long), Short (if neutral or sold)

**Reward function**:
- Daily return of position - 10 basis points transaction cost (0.1%) per trade

**Algorithm**:
- Q-learning with epsilon-greedy exploration (epsilon decay from 0.3 to 0.01 over 500 episodes)
- Learning rate alpha = 0.1, discount gamma = 0.95
- Training period: 2015-2020 (1,260 trading days)
- Test period: 2021-2023 (756 trading days)

**Key results**:
- **Backtested Sharpe ratio** (test period):
  - RL agent: 0.45
  - Buy-and-hold benchmark: 0.55
  - **The agent UNDERPERFORMS** after transaction costs
- Turnover: RL agent trades 18 times per month on average (180 bps monthly cost = 21.6 bps per trade)
- Average holding period: 1.2 days (extremely short, incurs high costs)
- Q-table convergence: Max Q-value change < 0.01 after 800 episodes (appears to converge)

**Why it failed (rigorous analysis)**:
1. **Small state space loses information**: Discretizing momentum into 5 bins discards continuous information. High-frequency price movements not captured.
2. **Transaction costs dominate**: 10 bps per trade x 18 trades/month = 180 bps/month = 21.6% annualized cost. Even a 2% monthly alpha is wiped out.
3. **Market non-stationarity violates MDP assumptions**: The transition probabilities P(s' | s, a) change over time (regime shifts, Fed policy changes). The agent trained on 2015-2020 doesn't generalize to 2021-2023 (COVID recovery, inflation regime).
4. **Exploration-exploitation tradeoff**: Epsilon-greedy is simplistic. More sophisticated methods (Thompson sampling, UCB) might improve, but unlikely to overcome costs.
5. **Benchmark is strong**: S&P 500 buy-and-hold has Sharpe 0.55 (good period). Beating this requires substantial alpha, which is rare.

**This negative result is graded positively** because:
- The analysis is rigorous and honest
- The failure is explained with evidence (transaction costs, non-stationarity)
- Alternative explanations are considered (state space, algorithm choice)
- The student demonstrates deep understanding of WHY RL is challenging for equity trading

**Implementation notes**: Use `numpy` arrays for Q-table. Implement epsilon decay schedule. Log all trades for post-hoc analysis. Compare to simple baselines (buy-and-hold, momentum strategy).

---

### Business Insight

"PCA reveals 6 principal components explain 73% of return variation, corresponding to market, sector, size, value, momentum, and volatility factors. This confirms multifactor models are empirically valid.

The RL trading agent fails to beat buy-and-hold — **an honest and important finding**. After 10 bps transaction costs, the agent's Sharpe ratio (0.45) is lower than passive buy-and-hold (0.55). This underscores equity market efficiency at daily frequencies for large-cap stocks.

XGBoost achieves 55% directional accuracy (p = 0.04) and estimated 1.2% annual alpha before costs, which disappears after realistic 20 bps round-trip transaction costs. This suggests:
1. Predictive signals exist but are weak
2. High-frequency trading without cost advantages is unprofitable
3. Focus on lower-frequency (monthly rebalancing) factor strategies to reduce turnover

**Recommendation**: Deploy a PCA-based risk parity portfolio (weight by inverse PC variance) rebalanced quarterly. Avoid RL-based trading until transaction costs drop below 2 bps (requires market-maker status or internal crossing)."

---

### What Makes This Project Strong

- **Most ambitious topic combination**: Includes L06 RL, the highest-difficulty method
- **Honest reporting of negative results**: RL underperforms, and this is reported transparently
- **Negative results analyzed rigorously**: Five specific reasons WHY the RL agent failed, with evidence
- **Multiple statistical tests throughout**: Breusch-Pagan, Jarque-Bera, binomial test, parallel analysis
- **Finance domain expertise demonstrated**: Fama-French model, Sharpe ratios, transaction cost analysis
- **Appropriate baselines**: Buy-and-hold and simple momentum strategies, not just "best model wins"
- **Reproducible**: All hyperparameters, state/action spaces, and reward functions documented

---

## Tips for Your Project

### 1. Start Early
Dataset approval at Session 2 means you need to explore options NOW. Download 2-3 candidate datasets, check for:
- Sufficient observations (at least 1,000 rows for most methods, more for RL)
- Suitable target variable (continuous for L01, binary/multiclass for L02/L04)
- Enough features (at least 10+ for PCA to be meaningful)
- No excessive missing data (>20% missing is problematic)

### 2. Choose a Dataset That Works for 5 Methods
Not every dataset supports all methods. Ask:
- **Supervised target available?** (Required for L01, L02, L04)
- **Enough features for PCA?** (Need 10+ features, ideally 20+)
- **Enough observations for train/test split?** (1,000+ rows recommended)
- **Clusterable structure?** (For K-Means, need natural groupings — check with preliminary visualization)
- **Text or sequential data for L06?** (Embeddings/RL require specific data types)

### 3. Negative Results Are OK
If a method doesn't work well, **explain WHY** — this demonstrates understanding. Examples:
- "Logistic regression AUC = 0.52 (barely above random) because the classes are highly overlapping in feature space, as confirmed by t-SNE visualization."
- "K-Means silhouette score = 0.18 (poor) because the data has no natural clusters — density-based clustering (DBSCAN) might be more appropriate."
- "RL agent underperforms buy-and-hold due to transaction costs and non-stationarity, as evidenced by Q-table divergence in test period."

### 4. Statistical Rigor Matters
Don't just report accuracy. Use:
- **Hypothesis tests**: t-test, chi-squared, F-test, likelihood ratio test
- **Confidence intervals**: Bootstrap 95% CIs for feature importance, AUC, Sharpe ratio
- **Diagnostic tests**: VIF, Breusch-Pagan, Durbin-Watson, Hosmer-Lemeshow, Jarque-Bera
- **Validation strategies**: k-fold CV, walk-forward validation, stratified splits
- **Multiple metrics**: Don't rely on accuracy alone — report AUC, F1, precision, recall, Brier score

### 5. Business Framing Elevates Your Work
Go beyond "Model X is best" — what would you actually recommend to a decision-maker?
- **Quantify impact**: "Deploying this model reduces churn by 23%, recovering $480K annual revenue."
- **Specify actions**: "Target segment 2 with discount offers, not segment 1."
- **Acknowledge limitations**: "Model assumes stable market conditions — retrain quarterly."
- **Compare costs/benefits**: "Alpha of 1.2% is wiped out by 20 bps transaction costs."

### 6. Git Workflow Matters
Commit early and often. Don't dump everything in one commit at the deadline.
- **Bad**: 1 commit with 5,000 lines changed on deadline day
- **Good**: 20+ commits throughout the project (exploratory analysis, L01 regression, L02 classification, hyperparameter tuning, final report, etc.)

We will review your commit history. Sparse commits suggest lack of incremental progress.

### 7. Reproducibility Is Testable
We will clone your repo and try to run your code. If it doesn't work, you lose points.
- **Include `requirements.txt`** with exact package versions
- **Set random seeds** for reproducibility (`np.random.seed(42)`, `random_state=42`)
- **Document data download**: Provide links or scripts to fetch data
- **Test on a clean environment**: Before submission, clone your own repo in a fresh directory and run it

---

## Suggested Datasets

| Dataset | Source | Size | Good For |
|---------|--------|------|----------|
| Home Credit Default Risk | Kaggle | 300K+ rows, 120+ features | Credit risk, classification, PCA |
| Telco Customer Churn | Kaggle | 7K rows, 21 features | Churn, segmentation, moderate size |
| Give Me Some Credit | Kaggle | 150K rows, 11 features | Credit scoring, imbalanced classes |
| S&P 500 Stock Data | Yahoo Finance | 2,500+ days x 50 stocks | Factor models, time series, RL |
| Credit Card Fraud Detection | Kaggle | 280K rows, 30 features (PCA-transformed) | Fraud, extreme imbalance (0.17% fraud) |
| Financial PhraseBank | Research repository | 4,840 sentences | Sentiment, embeddings (small, use for L06) |
| UCI Bank Marketing | UCI ML Repository | 45K rows, 17 features | Marketing, classification |
| European Central Bank Data | ECB Statistical Data Warehouse | Macro time series | Macro finance, regression |
| SimFin Financial Data | SimFin | 2,000+ companies, 100+ ratios | Company fundamentals, factor models |
| FRED Economic Data | Federal Reserve Economic Data | Thousands of time series | Macro indicators, time series |
| Lending Club Loan Data | Kaggle | 2M+ loans, 150 features | Credit risk, large dataset, PCA |
| Online Retail Dataset | UCI | 500K transactions | Customer segmentation, RFM analysis |
| Bitcoin Historical Data | Kaggle / CryptoCompare | Daily prices, 2010-2025 | Crypto factor models, volatility prediction |
| Employee Attrition | Kaggle (IBM HR Analytics) | 1,470 rows, 35 features | HR churn, classification |
| Wine Quality | UCI | 6,497 rows, 12 features | Regression/classification, moderate size |

**Pro tip**: Combine datasets for L06. Example: Use Telco Churn (main dataset) + Financial PhraseBank (for embeddings demonstration).

---

## Questions?

Contact the instructor during office hours or via the course forum. Dataset approval is **mandatory at Session 2** — don't wait until Session 4.

**Good luck! We look forward to seeing rigorous, honest, and insightful analyses.**
