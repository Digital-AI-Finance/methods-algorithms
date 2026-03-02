# L03 Recommended Additions

**Source:** Hostile Review Report 2026-02-05
**Current Score:** 34/100
**Target Score:** 70/100 (MSc-level pass)

---

## Priority Matrix

| Priority | Addition | Effort | Impact | Cumulative Score |
|----------|----------|--------|--------|------------------|
| **HIGH** |
| 1 | Gap Statistic section | 2h | +7 | 41 |
| 2 | Fix fraud detection (class imbalance) | 2h | +5 | 46 |
| 3 | EM Connection slide | 1h | +3 | 49 |
| 4 | Hopkins Statistic | 1h | +3 | 52 |
| 5 | K-Means++ O(log k) guarantee | 30m | +3 | 55 |
| **MEDIUM** |
| 6 | CV code example (GridSearchCV) | 1h | +3 | 58 |
| 7 | Cosine similarity section | 1h | +2 | 60 |
| 8 | VC dimension discussion | 1h | +2 | 62 |
| 9 | KNN consistency theorem | 1h | +2 | 64 |
| 10 | 3 unique deepdive charts | 3h | +3 | 67 |
| **LOW** |
| 11 | Fix formula edge cases | 30m | +4 | 71 |
| 12 | Add RFM to segmentation | 30m | +2 | 73 |
| 13 | Remove TBD placeholders | 5m | +2 | 75 |
| 14 | Differentiate exercises | 30m | +2 | 77 |
| 15 | Empty cluster handling | 15m | +2 | 79 |

**Total Effort:** ~15 hours
**Maximum Achievable Score:** 79/100 (Grade B)

---

## Implementation Details

### 1. Gap Statistic Section (HIGH - +7 points)

**Add to deepdive after silhouette (after line 398):**

```latex
\begin{frame}[t]{Gap Statistic for K Selection}
\textbf{The Problem with Elbow Method}
\begin{itemize}
\item Elbow is subjective - where exactly IS the elbow?
\item No formal statistical test
\end{itemize}
\vspace{0.5em}
\textbf{Gap Statistic (Tibshirani et al., 2001)}
$$Gap(k) = E^*[\log W_k] - \log W_k$$
\begin{itemize}
\item $W_k$ = within-cluster dispersion at K
\item $E^*$ = expected value under null (uniform reference)
\item Choose smallest K where $Gap(k) \geq Gap(k+1) - s_{k+1}$
\end{itemize}
\bottomnote{Gap statistic provides statistical justification for K selection}
\end{frame}
```

**Create new chart:** `08_gap_statistic/chart.py`

---

### 2. Fraud Detection Fix (HIGH - +5 points)

**Replace deepdive lines 508-525 with:**

```latex
\begin{frame}[t]{Finance Application: Fraud Detection}
\textbf{CRITICAL: Class Imbalance}
\begin{itemize}
\item Fraud is typically $<$1\% of transactions
\item Naive KNN majority vote: ALWAYS predicts non-fraud
\item Accuracy = 99\% but detects ZERO fraud!
\end{itemize}
\vspace{0.5em}
\textbf{Solutions}
\begin{itemize}
\item \textbf{SMOTE}: Synthetic Minority Oversampling
\item \textbf{Weighted voting}: Higher weight for fraud neighbors
\item \textbf{Cost-sensitive}: FN costs more than FP
\item Use \textbf{Precision-Recall}, NOT accuracy
\end{itemize}
\bottomnote{Always check class distribution before applying majority vote!}
\end{frame}
```

---

### 3. EM Connection Slide (HIGH - +3 points)

**Add to deepdive after convergence (after line 340):**

```latex
\begin{frame}[t]{K-Means as EM Special Case}
\textbf{Connection to Expectation-Maximization}
\begin{itemize}
\item K-Means = ``Hard EM'' for Gaussian Mixture Models
\item Assumes: spherical Gaussians, equal variance
\item E-step: assign points to nearest centroid (hard assignment)
\item M-step: update centroids as cluster means
\end{itemize}
\vspace{0.5em}
\textbf{Why This Matters}
\begin{itemize}
\item Explains WHY convergence is guaranteed
\item Explains WHY K-Means assumes spherical clusters
\item Opens door to soft clustering (GMM)
\end{itemize}
\bottomnote{Understanding EM connection deepens theoretical understanding}
\end{frame}
```

---

### 4. Hopkins Statistic (HIGH - +3 points)

**Add to deepdive before Gap statistic:**

```latex
\begin{frame}[t]{Should We Cluster? Hopkins Statistic}
\textbf{Before Clustering: Test for Cluster Tendency}
$$H = \frac{\sum u_i}{\sum u_i + \sum w_i}$$
\begin{itemize}
\item $u_i$ = distances from random points to nearest data point
\item $w_i$ = distances from data points to nearest neighbor
\item $H \approx 0.5$: uniform (no clusters)
\item $H > 0.75$: significant clustering tendency
\end{itemize}
\vspace{0.3em}
\textbf{Use Case}: Before running K-Means, verify data HAS cluster structure
\bottomnote{Don't cluster uniform data - Hopkins test catches this}
\end{frame}
```

---

### 5. K-Means++ Guarantee (HIGH - +3 points)

**Replace deepdive line 365:**

**Before:**
```
K-Means++ gives provably better initialization with theoretical guarantees
```

**After:**
```
K-Means++ achieves $O(\log k)$-competitive ratio: expected cost $\leq 8(\ln k + 2) \times$ optimal (Arthur \& Vassilvitskii, 2007)
```

---

### 6-15: See individual implementation notes in review report

---

## Quick Wins (< 1 hour total, +10 points)

1. **K-Means++ guarantee** (30m, +3 pts) - Single line edit
2. **TBD placeholders** (5m, +2 pts) - Remove or add actual links
3. **Empty cluster handling** (15m, +2 pts) - Add to pseudocode
4. **Formula edge cases** (30m, +4 pts) - Add bullet points

These quick wins alone raise score from 34 to 44 with minimal effort.

---

## Files to Create

| File | Purpose |
|------|---------|
| `08_gap_statistic/chart.py` | Gap statistic vs K visualization |
| `09_hopkins_test/chart.py` | Hopkins statistic illustration |
| `10_class_imbalance/chart.py` | Class imbalance impact visualization |

---

**Generated:** 2026-02-05
