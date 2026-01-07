# Capstone Project Specification

**Course**: Methods and Algorithms - MSc Data Science
**Weight**: 40% of final grade
**Deliverable**: Written report (PDF, 10-15 pages)

---

## Overview

The capstone project is an open-ended, individual project where you apply machine learning methods from this course to solve a real-world problem in finance or business. The project demonstrates your ability to:

1. Define a clear problem that requires ML methods
2. Select and justify appropriate algorithms
3. Implement a working solution
4. Interpret and communicate results

---

## Timeline

| Milestone | Date |
|-----------|------|
| Project introduced | Session 4 |
| Topic proposal due | End of Session 5 |
| Final report due | 2 weeks after Session 6 |

---

## Requirements

### 1. Problem Selection

Choose a problem from the finance or business domain. The problem must:

- Require a machine learning solution (not just descriptive statistics)
- Have available data (public dataset or synthetic data you generate)
- Be achievable within the course timeframe
- Align with methods covered in this course

**Example Problem Areas**:
- Credit risk assessment and default prediction
- Customer segmentation and churn prediction
- Fraud detection in financial transactions
- Stock price prediction or trading signals
- Portfolio risk analysis and optimization
- Sentiment analysis of financial news
- Anomaly detection in banking data

### 2. Method Application

Your project must:

- Apply **at least 2 methods** from the course
- Compare the methods and justify your final selection
- Use the decision framework reasoning from lectures
- Demonstrate understanding of assumptions and limitations

**Methods from the Course**:
- Linear Regression (L01)
- Logistic Regression (L02)
- K-Nearest Neighbors (L03)
- K-Means Clustering (L03)
- Random Forests (L04)
- PCA / t-SNE (L05)
- Word Embeddings (L06)
- Q-Learning (L06)

### 3. Implementation

- Code must be functional and documented
- Include key code snippets in the appendix
- Use Python with standard libraries (scikit-learn, pandas, numpy)
- Reproducibility: random seeds should be set

### 4. Report Quality

- Professional academic writing
- Clear structure following the template
- Proper citations for any external sources
- Figures and tables must be readable and labeled

---

## Report Structure

Use the following structure for your report (10-15 pages total):

### 1. Executive Summary (1 page)

- Problem statement in 2-3 sentences
- Methods used
- Key findings and business implications
- Main recommendation

### 2. Problem Definition (2 pages)

- Business context and motivation
- Why this problem matters
- What question are you answering?
- Success criteria: how will you measure success?

### 3. Data Description (1 page)

- Data source (public dataset or synthetic)
- Number of observations and features
- Target variable description
- Data quality issues and how you addressed them
- Train/test split strategy

### 4. Methodology (3 pages)

- Why you chose the methods you did
- Decision framework reasoning (when to use each method)
- Feature engineering and preprocessing
- Hyperparameter tuning approach
- Evaluation metrics and why they're appropriate

### 5. Results and Interpretation (3 pages)

- Model performance comparison
- Feature importance analysis (if applicable)
- Visualization of key results
- Business interpretation: what do the results mean?
- Actionable insights

### 6. Limitations and Future Work (1 page)

- Assumptions made and potential violations
- What could improve the analysis?
- Next steps if this were a real project
- Generalization considerations

### 7. References

- Cite all external sources
- Include course materials where relevant

### 8. Appendix

- Key code snippets (not full notebooks)
- Additional figures or tables
- Data dictionary if applicable

---

## Evaluation Criteria

Your project is graded using the rubric in `rubrics/capstone_rubric.md`:

| Criterion | Points |
|-----------|--------|
| Problem Definition | 20 |
| Method Selection | 20 |
| Implementation | 20 |
| Results Interpretation | 20 |
| Report Quality | 20 |
| **Total** | **100** |

---

## Example Capstone Topics

Here are example topics to inspire your project:

### Credit Default Prediction
Compare logistic regression and random forest for predicting loan defaults. Analyze feature importance to understand key risk factors.

### Customer Churn Analysis
Use K-Means to segment customers, then build a churn prediction model. Compare classification performance across segments.

### Portfolio Risk Decomposition
Apply PCA to decompose portfolio risk into principal components. Identify which factors drive most of the portfolio variance.

### Fraud Detection System
Build a fraud detection model handling extreme class imbalance. Compare multiple methods and optimize for recall.

### Financial Sentiment Analysis
Use word embeddings to represent financial news articles. Build a classifier to predict market sentiment.

### Trading Signal Generation
Apply Q-learning to learn a simple trading policy. Analyze the learned strategy and its performance.

---

## Submission Guidelines

1. **Format**: PDF document
2. **Length**: 10-15 pages (excluding appendix)
3. **File naming**: `LastName_FirstName_Capstone.pdf`
4. **Submit via**: Moodle assignment dropbox
5. **Code**: Include key snippets in appendix; full notebook optional

---

## Academic Integrity

- This is an individual project
- All work must be your own
- Cite all external sources
- AI tools (ChatGPT, etc.) may be used for coding assistance but not for writing the report text
- Plagiarism detection will be applied

---

## Questions?

Contact the instructor during office hours or via the course forum on Moodle.
