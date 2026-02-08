# datasets/

<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 | Updated: 2026-02-07 -->

**Generated**: 2026-01-25 | **Updated**: 2026-02-07
**Purpose**: Synthetic finance/business datasets for course notebooks and exercises

---

## Overview

This directory contains **synthetic datasets** designed for educational purposes in the Methods and Algorithms course. All datasets simulate realistic finance and business scenarios while ensuring:
- **Privacy**: No real customer or financial data
- **Reproducibility**: Generated with fixed random seeds
- **Educational value**: Clear patterns for learning ML concepts
- **Realism**: Mimics real-world finance data structures and distributions

All datasets are used in Jupyter notebooks (`../notebooks/`) and can be loaded locally or via GitHub raw URLs for Colab compatibility.

---

## Key Files

| File | Purpose | Rows | Features | Used In |
|------|---------|------|----------|---------|
| `housing_synthetic.csv` | Housing price prediction (regression) | 200 | 5 | L01 (Linear Regression) |
| `credit_synthetic.csv` | Credit default prediction (classification) | 1000 | 10 | L02 (Logistic Regression), L04 (Random Forests) |
| `customers_synthetic.csv` | Customer segmentation (clustering) | 500 | 8 | L03 (KNN & K-Means) |
| `transactions_synthetic.csv` | Financial transactions (fraud detection) | 10000 | 12 | L02 (Logistic Regression) |
| `portfolio_synthetic.csv` | Portfolio returns (dimensionality reduction) | 252 | 50 | L05 (PCA & t-SNE) |

**Generation scripts**: Stored in `infrastructure/generators/dataset_generator.py` (if applicable)

---

## For AI Agents

### Dataset Details

#### housing_synthetic.csv

**Use case**: Predict housing prices based on property features

| Column | Type | Range/Values | Description |
|--------|------|--------------|-------------|
| `size_sqm` | float | 50-250 | Property size in square meters |
| `bedrooms` | int | 1-5 | Number of bedrooms |
| `age_years` | float | 0-50 | Age of the property in years |
| `distance_km` | float | 1-20 | Distance to city center in km |
| `price` | float | 50000-600000 | Target: property price in currency units |

**Generation parameters**:
```python
true_intercept = 50000
true_coefs = [2000, 15000, -800, -3000]  # size, bedrooms, age, distance
noise_std = 30000
```

**Key relationships**:
- Positive: size (+2000/sqm), bedrooms (+15000/bedroom)
- Negative: age (-800/year), distance (-3000/km)
- Noise: N(0, 30000) added to simulate real-world variability

---

#### credit_synthetic.csv

**Use case**: Predict credit default (binary classification)

| Column | Type | Range/Values | Description |
|--------|------|--------------|-------------|
| `age` | int | 21-70 | Customer age |
| `income` | float | 20000-150000 | Annual income |
| `debt_ratio` | float | 0-1 | Debt-to-income ratio |
| `credit_score` | int | 300-850 | Credit score |
| `num_accounts` | int | 0-10 | Number of credit accounts |
| `num_defaults` | int | 0-5 | Past defaults in last 5 years |
| `employment_length` | int | 0-30 | Years with current employer |
| `has_mortgage` | int | 0/1 | Has active mortgage (binary) |
| `has_cosigner` | int | 0/1 | Has loan cosigner (binary) |
| `default` | int | 0/1 | **Target**: Credit default (1=default, 0=no default) |

**Class distribution**: ~20% default (class imbalance)

**Key relationships**:
- High debt_ratio → higher default risk
- Low credit_score → higher default risk
- Higher income → lower default risk

---

#### customers_synthetic.csv

**Use case**: Customer segmentation for marketing (clustering)

| Column | Type | Range/Values | Description |
|--------|------|--------------|-------------|
| `customer_id` | int | 1-500 | Unique customer identifier |
| `age` | int | 18-80 | Customer age |
| `income` | float | 15000-200000 | Annual income |
| `spending_score` | float | 1-100 | Spending behavior score |
| `account_balance` | float | 0-100000 | Current account balance |
| `num_products` | int | 1-5 | Number of products held |
| `years_customer` | int | 0-20 | Years as customer |
| `online_activity` | float | 0-1 | Online banking activity (normalized) |

**Cluster structure**: 3-4 natural clusters (e.g., young spenders, wealthy savers, inactive)

---

#### transactions_synthetic.csv

**Use case**: Fraud detection (binary classification with extreme imbalance)

| Column | Type | Range/Values | Description |
|--------|------|--------------|-------------|
| `transaction_id` | int | 1-10000 | Unique transaction ID |
| `amount` | float | 1-10000 | Transaction amount |
| `timestamp` | datetime | 2025-01-01 to 2025-12-31 | Transaction timestamp |
| `merchant_category` | str | 10 categories | Merchant category code |
| `location_distance` | float | 0-1000 | Distance from customer home (km) |
| `time_since_last` | float | 0-168 | Hours since last transaction |
| `num_transactions_day` | int | 1-20 | Transactions in past 24h |
| `avg_transaction_amount` | float | 10-500 | Customer's avg transaction |
| `is_international` | int | 0/1 | International transaction |
| `device_type` | str | mobile/desktop/pos | Device used |
| `fraud` | int | 0/1 | **Target**: Fraud label (1=fraud, 0=legitimate) |

**Class distribution**: ~1-2% fraud (extreme imbalance - requires SMOTE or class weighting)

---

#### portfolio_synthetic.csv

**Use case**: Portfolio risk analysis and dimensionality reduction

| Column | Type | Range/Values | Description |
|--------|------|--------------|-------------|
| `date` | date | 252 trading days | Trading date (1 year) |
| `asset_1` to `asset_50` | float | -0.1 to 0.1 | Daily returns for 50 assets |

**Structure**:
- 252 rows (trading days in a year)
- 50 columns (asset returns)
- Returns are correlated (simulate sector effects)
- High-dimensional → ideal for PCA to find principal components

**Covariance structure**: Designed with ~5 underlying factors (sectors)

---

### How to Load Datasets

#### Local Environment

```python
import pandas as pd

# Load dataset
df = pd.read_csv('../datasets/housing_synthetic.csv')
print(f'Dataset shape: {df.shape}')
df.head()
```

#### Google Colab (Fallback Pattern)

**ALWAYS use this pattern** in notebooks for Colab compatibility:

```python
import os
import pandas as pd

try:
    # Try local path first
    if os.path.exists('../datasets/housing_synthetic.csv'):
        df = pd.read_csv('../datasets/housing_synthetic.csv')
        print('Loaded dataset from local file')
    else:
        # GitHub raw URL for Colab
        url = 'https://raw.githubusercontent.com/Digital-AI-Finance/methods-algorithms/master/datasets/housing_synthetic.csv'
        df = pd.read_csv(url)
        print('Loaded dataset from GitHub')
except Exception as e:
    print(f'Could not load dataset: {e}')
    print('Generating synthetic data as fallback...')
    # Include synthetic generation code here
```

**GitHub raw URL format**:
```
https://raw.githubusercontent.com/OWNER/REPO/BRANCH/datasets/FILENAME.csv
```

Replace `OWNER/REPO/BRANCH` with actual repository details.

---

### Regenerating Datasets

If datasets need to be regenerated (e.g., to fix issues or update):

```python
# Example: Regenerate housing_synthetic.csv
import numpy as np
import pandas as pd

np.random.seed(42)  # CRITICAL: Use same seed for reproducibility

n_samples = 200
size = np.random.uniform(50, 250, n_samples)
bedrooms = np.random.randint(1, 6, n_samples)
age = np.random.uniform(0, 50, n_samples)
distance_center = np.random.uniform(1, 20, n_samples)

# True coefficients
true_intercept = 50000
true_coefs = [2000, 15000, -800, -3000]
noise = np.random.normal(0, 30000, n_samples)

price = (true_intercept +
         true_coefs[0] * size +
         true_coefs[1] * bedrooms +
         true_coefs[2] * age +
         true_coefs[3] * distance_center +
         noise)

df = pd.DataFrame({
    'size_sqm': size,
    'bedrooms': bedrooms,
    'age_years': age,
    'distance_km': distance_center,
    'price': price
})

df.to_csv('datasets/housing_synthetic.csv', index=False)
print('Dataset regenerated successfully')
```

**CRITICAL**: Always use `np.random.seed(42)` to ensure reproducibility across course materials.

---

### Validation Requirements

Before committing new/modified datasets:

1. **Check shape**: Verify row/column counts match documentation
2. **Check types**: Ensure dtypes are correct (int, float, str, datetime)
3. **Check ranges**: Validate values are within expected ranges
4. **Check missing values**: `df.isnull().sum()` should be zero (unless intentional)
5. **Test loading**: Verify both local and GitHub URL loading work
6. **Document**: Update this AGENTS.md file with dataset details

```python
# Validation script
import pandas as pd

df = pd.read_csv('datasets/housing_synthetic.csv')

# Shape check
assert df.shape == (200, 5), f'Expected (200, 5), got {df.shape}'

# Column check
expected_cols = ['size_sqm', 'bedrooms', 'age_years', 'distance_km', 'price']
assert list(df.columns) == expected_cols, f'Column mismatch: {df.columns}'

# No missing values
assert df.isnull().sum().sum() == 0, 'Dataset has missing values'

# Range checks
assert df['size_sqm'].between(50, 250).all(), 'size_sqm out of range'
assert df['bedrooms'].between(1, 5).all(), 'bedrooms out of range'

print('Validation passed!')
```

---

### Adding New Dataset

**Step-by-step**:

1. **Create generation script** (or manually create CSV)
   ```python
   # datasets/generate_new_dataset.py
   import numpy as np
   import pandas as pd

   np.random.seed(42)
   # ... generation logic ...
   df.to_csv('datasets/new_dataset.csv', index=False)
   ```

2. **Run script** to generate CSV
   ```bash
   python datasets/generate_new_dataset.py
   ```

3. **Validate** using validation script above

4. **Document** in this file:
   - Add row to Key Files table
   - Add detailed column description
   - Document generation parameters

5. **Update manifest.json**:
   ```json
   {
     "L0X": {
       "dataset": "datasets/new_dataset.csv"
     }
   }
   ```

6. **Test in notebook**:
   - Update notebook to load new dataset
   - Verify fallback pattern works
   - Test in Colab

---

## Data Privacy and Ethics

**IMPORTANT**: All datasets in this directory are **100% synthetic** and contain no real personal or financial data.

- **Synthetic generation**: Created using random number generators with fixed seeds
- **No PII**: No real names, addresses, SSNs, or identifiable information
- **Educational use**: Designed solely for teaching ML algorithms
- **Distribution**: Safe to share publicly via GitHub

**If adding real data**: DO NOT commit to this repository. Use synthetic generation instead.

---

## Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| `FileNotFoundError` in Colab | Incorrect GitHub URL | Use raw.githubusercontent.com URL format |
| Different results each notebook run | Random operations without seed | Set `np.random.seed(42)` before data generation |
| Encoding errors | Non-UTF8 characters | Save CSV with `encoding='utf-8'` |
| Large file size | Too many rows/columns | Reduce sample size or use compression |
| Class imbalance warnings | Highly imbalanced classes | Document imbalance ratio, use SMOTE in notebooks |

---

## Related Files

- **Parent hierarchy**: `../AGENTS.md` (project root)
- **Notebooks**: `../notebooks/L0X_*.ipynb` (use these datasets)
- **Generators**: `../infrastructure/generators/dataset_generator.py` (if applicable)
- **Manifest**: `../manifest.json` (tracks dataset assignments)
- **CLI**: `python infrastructure/course_cli.py inventory list` (shows dataset usage)
