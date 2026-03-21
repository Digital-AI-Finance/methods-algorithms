# Work Plan: Discovery-Based Learning Handouts

## Context

### Original Request
Create simple discovery-based learning handouts (pre-class) with solutions and visuals for all 6 lectures of the MSc Data Science course "Methods and Algorithms."

### Research Findings
- **Existing quiz template** at `docs/quiz/quiz_template.html` provides reusable CSS/JS patterns: purple/blue gradient nav, card layout, KaTeX math, responsive grid
- **67 chart PNGs** already deployed at `docs/slides/images/LXX_Topic/*.png` -- these can be embedded directly in handouts (no PDF conversion needed)
- **docs/index.html** dashboard has a sidebar nav and lesson sections where handout links can be added
- Each lecture follows PMSP (Problem-Method-Solution-Practice) structure; handout activities should scaffold toward the Problem and Method phases
- Finance/banking case studies per lecture: L01=house prices, L02=credit scoring, L03=customer segmentation, L04=fraud detection, L05=portfolio risk, L06=sentiment/trading

### What Makes This Different From Quizzes
Quizzes test knowledge AFTER lecture. Handouts activate curiosity BEFORE lecture via:
- Data-first: show a chart or dataset, then ask what students observe
- Prediction: "What do you think happens if...?"
- Hands-on: "Draw a line", "Group these customers", "Calculate this distance"
- Guided discovery: questions scaffold toward the formal concept
- Solutions reveal the method name and connect to lecture content

## Work Objectives

### Core Objective
Produce 6 standalone HTML handout files and one reusable template, integrated into the course dashboard.

### Deliverables
1. `docs/handouts/handout_template.html` -- reusable HTML template
2. `docs/handouts/L01_handout.html` -- Linear Regression discovery (6 activities)
3. `docs/handouts/L02_handout.html` -- Logistic Regression discovery (6 activities)
4. `docs/handouts/L03_handout.html` -- KNN & K-Means discovery (7 activities)
5. `docs/handouts/L04_handout.html` -- Random Forests discovery (6 activities)
6. `docs/handouts/L05_handout.html` -- PCA & t-SNE discovery (6 activities)
7. `docs/handouts/L06_handout.html` -- Embeddings & RL discovery (6 activities)
8. Updated `docs/index.html` -- add "Pre-Class Handouts" section with links

### Definition of Done
- All 6 handout HTML files render correctly in a browser
- Each handout has 5-8 discovery activities with embedded chart images
- Solutions are hidden by default and expand on click
- KaTeX renders math correctly
- Mobile-responsive layout (single column on small screens)
- Dashboard links work
- Consistent visual branding with quizzes (same nav, colors, card style)

## Guardrails

### Must Have
- Standalone HTML files (no build step, no external dependencies except KaTeX CDN)
- Same CSS variables and nav bar as quiz template (--mlpurple, --mlblue, gradient nav)
- Each activity includes: (a) a visual or data table, (b) 2-3 guided questions, (c) expandable solution
- Chart images referenced via relative path `../slides/images/LXX_Topic/XX_name.png`
- Finance context in at least 2 activities per handout
- KaTeX for any math expressions
- `renderMath()` called directly at end of body (not in DOMContentLoaded) per CLAUDE.md

### Must NOT Have
- No server-side dependencies (no Node, no Python)
- No quiz-style scoring or grading -- these are open-ended discovery, not right/wrong
- No subplots or new chart generation -- use only existing PNG files
- No changes to existing quiz files
- No complex JavaScript frameworks

## Task Flow

```
T01 (Template) --> T02-T07 (6 handouts, sequential) --> T08 (Dashboard integration)
```

All handout files share the template structure, so T01 must complete first. T02-T07 can technically run in parallel but share no dependencies beyond the template. T08 depends on T02-T07 being done.

## Detailed TODOs

### T01: Create Handout HTML Template
**File:** `docs/handouts/handout_template.html`
**Acceptance criteria:**
- Reuses quiz CSS variables (--mlpurple, --mlblue, --bg, --card-bg, --text, --border)
- Nav bar: purple/blue gradient, title "Pre-Class Discovery: [Topic]", links to Dashboard and GitHub
- Activity card layout: white card with subtle shadow, numbered badge (Activity 1, 2...)
- Each activity card contains:
  - Title (question-based, e.g., "Can You Spot the Pattern?")
  - Visual area: `<img>` tag for chart PNG, or HTML `<table>` for inline data
  - Guided questions: numbered list of 2-3 questions
  - Expandable solution: `<details><summary>Reveal Solution</summary>` with answer text
- Progress indicator: "Activity X of Y" at top
- Navigation between activities: prev/next buttons or scroll-based
- Footer with links to related quiz and lecture slides
- Responsive: 1-column max-width 800px centered layout (handouts are linear, not grid)
- KaTeX CDN links (same versions as quizzes: katex@0.16.9)
- renderMath() at end of body

### T02: L01 Linear Regression Handout (6 activities)
**File:** `docs/handouts/L01_handout.html`
**Charts to embed:** 01_simple_regression.png, 03_residual_plots.png, 04_gradient_descent.png, 06_regularization_comparison.png, 07_bias_variance.png
**Activities:**

1. **"Draw Your Best Line"** -- Show a scatter plot (table of 6 house data points: sqft, price). Ask students to (a) plot them on graph paper, (b) draw a line, (c) measure vertical distances. Solution: This is what linear regression does -- minimizes squared distances.

2. **"What Does This Chart Tell You?"** -- Embed 01_simple_regression.png. Ask: (a) What relationship do you see? (b) Predict price for 2000 sqft. (c) How confident are you? Solution: The line is the OLS fit; introduces $y = \beta_0 + \beta_1 x$.

3. **"Good Fit or Bad Fit?"** -- Embed 03_residual_plots.png. Ask: (a) What patterns do you see in the residuals? (b) Which plot suggests a good model? (c) What would a "perfect" residual plot look like? Solution: Random scatter = good; patterns = model misspecification.

4. **"The Downhill Walk"** -- Embed 04_gradient_descent.png. Ask: (a) Imagine you are blindfolded on a hilly landscape. How would you find the lowest point? (b) What happens if you take very large steps? Very small? Solution: Gradient descent; learning rate tradeoff.

5. **"Too Simple vs. Too Complex"** -- Embed 07_bias_variance.png. Ask: (a) Which model would you trust for a new data point? (b) What goes wrong with the wiggly line? (c) What goes wrong with the flat line? Solution: Bias-variance tradeoff.

6. **"Predicting House Prices"** -- Data table with 5 houses (sqft, bedrooms, age, price). Ask: (a) Which feature matters most for price? (b) Can you estimate a formula? (c) What happens if sqft and bedrooms are highly correlated? Solution: Multiple regression, multicollinearity.

### T03: L02 Logistic Regression Handout (6 activities)
**File:** `docs/handouts/L02_handout.html`
**Charts to embed:** 01_sigmoid_function.png, 02_decision_boundary.png, 04_roc_curve.png, 06_confusion_matrix.png
**Activities:**

1. **"Approve or Deny?"** -- Table of 8 loan applicants (income, debt ratio, credit score, outcome: approved/denied). Ask: (a) Sort by income -- does higher income always mean approval? (b) Which feature matters most? (c) Can you draw a rule? Solution: Need a model that outputs probability, not just yes/no.

2. **"The S-Shaped Curve"** -- Embed 01_sigmoid_function.png. Ask: (a) What happens at the extremes (very large/small input)? (b) What is the output at input=0? (c) Why is this shape useful for probabilities? Solution: Sigmoid function maps any number to [0,1].

3. **"Where Do You Draw the Line?"** -- Embed 02_decision_boundary.png. Ask: (a) Where would you place a boundary to separate the two groups? (b) Can a straight line do it? (c) What about the points near the boundary? Solution: Decision boundary; threshold at 0.5.

4. **"The Confusion Table"** -- Embed 06_confusion_matrix.png. Ask: (a) Which is worse in banking: approving a bad loan or rejecting a good customer? (b) Count the errors in each category. (c) If you move the threshold, what changes? Solution: Confusion matrix; precision vs recall tradeoff.

5. **"Which Model Wins?"** -- Embed 04_roc_curve.png. Ask: (a) What does the diagonal line represent? (b) Which curve is better and why? (c) Can a model be perfect? Solution: ROC curve; AUC; random baseline.

6. **"Your Turn: Credit Scoring"** -- Table of 6 new applicants with features. Ask: (a) Predict approve/deny for each. (b) How confident are you (0-100%)? (c) Two applicants have the same income but different outcomes -- why? Solution: Logistic regression combines features via weighted sum into probability.

### T04: L03 KNN & K-Means Handout (7 activities)
**File:** `docs/handouts/L03_handout.html`
**Charts to embed:** 01_knn_boundaries.png, 02_distance_metrics.png, 03_kmeans_iteration.png, 04_elbow_method.png, 12_kmeans_worked_example.png
**Activities:**

1. **"Who Are Your Neighbors?"** -- Grid of 12 customers (age, annual spending) labeled as High/Low value. One unlabeled new customer. Ask: (a) Find the 3 nearest customers to the new one. (b) What label would you give? (c) What if you used 7 neighbors instead? Solution: KNN classification; k matters.

2. **"How Far Apart?"** -- Embed 02_distance_metrics.png. Two customer profiles with 3 features. Ask: (a) Calculate distance using |a-b| for each feature. (b) Does the distance change if you multiply income by 1000? (c) Why is scaling important? Solution: Manhattan vs Euclidean distance; feature scaling.

3. **"Draw the Boundaries"** -- Embed 01_knn_boundaries.png. Ask: (a) Where do the decision boundaries fall? (b) Are they smooth or jagged? (c) What happens as k increases? Solution: KNN decision boundaries smooth with larger k.

4. **"Group These Customers"** -- Table of 10 customers (age, spending). Ask: (a) Divide them into 3 groups that make sense to you. (b) Compare your grouping with the image below. (c) How did you decide which group each customer belongs to? Solution: K-means clustering; centroid-based assignment.

5. **"Watch the Algorithm"** -- Embed 03_kmeans_iteration.png. Ask: (a) What changed between iterations? (b) When would the algorithm stop? (c) What if the starting points were different? Solution: K-means convergence; initialization sensitivity.

6. **"How Many Groups?"** -- Embed 04_elbow_method.png. Ask: (a) What happens to the error as you add more clusters? (b) Where is the "elbow"? (c) Why not just use k=10? Solution: Elbow method for choosing k; diminishing returns.

7. **"K-Means By Hand"** -- Embed 12_kmeans_worked_example.png. Small 2D dataset (6 points). Ask: (a) Pick 2 starting centroids. (b) Assign each point to nearest centroid. (c) Recalculate centroids. (d) Repeat once. Solution: One full K-means iteration worked out.

### T05: L04 Random Forests Handout (6 activities)
**File:** `docs/handouts/L04_handout.html`
**Charts to embed:** 01_decision_tree.png, 02_feature_importance.png, 08_gini_split.png, 05_ensemble_voting.png, 06_bias_variance.png
**Activities:**

1. **"20 Questions for Fraud"** -- Table of 8 transactions (amount, merchant type, time of day, foreign, outcome: fraud/legit). Ask: (a) What is the single best yes/no question to separate fraud from legit? (b) Ask a second question. (c) Draw your question tree. Solution: Decision tree; splitting on features.

2. **"Which Split Is Better?"** -- Embed 08_gini_split.png. Two possible splits shown with class distributions. Ask: (a) Which split creates purer groups? (b) Count: what fraction of each group is fraud? (c) Why is a 90/10 split better than 60/40? Solution: Gini impurity; information gain.

3. **"One Tree vs. Many Trees"** -- Embed 01_decision_tree.png. Ask: (a) What happens if you train this tree on slightly different data? (b) Would the splits change? (c) How could you make predictions more stable? Solution: Variance problem; wisdom of crowds.

4. **"Voting Committee"** -- Embed 05_ensemble_voting.png. Ask: (a) If 7 out of 10 classifiers say "fraud", what do you conclude? (b) Why is a committee better than one expert? (c) What if all 10 experts were trained on the same data? Solution: Ensemble voting; need diversity (bootstrap).

5. **"Which Feature Matters?"** -- Embed 02_feature_importance.png. Ask: (a) Which feature is most important for prediction? (b) Does "important" mean the same as "causal"? (c) If you removed the top feature, what would happen? Solution: Feature importance; correlation vs causation caveat.

6. **"Overfitting the Fraud Detector"** -- Embed 06_bias_variance.png. Ask: (a) What happens when the tree is very deep? (b) What happens when it is very shallow? (c) How does a forest fix this? Solution: Bias-variance tradeoff; random forest reduces variance.

### T06: L05 PCA & t-SNE Handout (6 activities)
**File:** `docs/handouts/L05_handout.html`
**Charts to embed:** 02_principal_components.png, 01_scree_plot.png, 03_reconstruction.png, 04_tsne_perplexity.png, 05_pca_vs_tsne.png
**Activities:**

1. **"Too Many Numbers"** -- Table of 6 stocks with 5 features (return, volatility, volume, P/E, beta). Ask: (a) Can you visualize 5 dimensions on paper? (b) Which features seem redundant? (c) If you could keep only 2 features, which 2 capture the most information? Solution: Dimensionality reduction motivation; PCA finds the best combinations.

2. **"Find the Direction of Maximum Spread"** -- Embed 02_principal_components.png. Ask: (a) If you had to summarize this 2D cloud with one line, where would you draw it? (b) Why along the widest spread? (c) What does the second arrow capture? Solution: Principal components; variance maximization.

3. **"How Many Components?"** -- Embed 01_scree_plot.png. Ask: (a) How much variance does the first component capture? (b) At which component does adding more stop helping much? (c) If you keep 3 components, what percentage of information do you lose? Solution: Scree plot; explained variance ratio; elbow criterion.

4. **"Compress and Reconstruct"** -- Embed 03_reconstruction.png. Ask: (a) What information was lost when reducing to 2 components? (b) Is the reconstruction close to the original? (c) When is a lossy approximation good enough? Solution: PCA reconstruction; acceptable information loss.

5. **"The Map of Similarities"** -- Embed 04_tsne_perplexity.png. Ask: (a) Which points are clustered together? (b) Does the distance between clusters matter? (c) The same data is shown 3 times with different settings -- what changed? Solution: t-SNE; perplexity parameter; local vs global structure.

6. **"PCA vs. t-SNE: Which to Use?"** -- Embed 05_pca_vs_tsne.png. Ask: (a) Which visualization preserves global distances better? (b) Which shows clusters more clearly? (c) Can you run t-SNE on new data without recomputing? Solution: PCA is linear/fast/invertible; t-SNE is nonlinear/visual-only.

### T07: L06 Embeddings & RL Handout (6 activities)
**File:** `docs/handouts/L06_handout.html`
**Charts to embed:** 01_word_embedding_space.png, 02_similarity_heatmap.png, 03_rl_loop.png, 04_q_learning_grid.png, 05_reward_curves.png
**Activities:**

1. **"Words as Numbers"** -- List of 8 financial terms (stock, bond, interest, dividend, inflation, risk, return, portfolio). Ask: (a) Which pairs are most similar in meaning? (b) Rank the top 3 most similar pairs. (c) How would you assign each word a score from 0-10 for "riskiness" and "return"? Solution: Word embeddings; similar words have similar vectors.

2. **"The Meaning Map"** -- Embed 01_word_embedding_space.png. Ask: (a) Which words are close together? (b) Does their proximity match your intuition? (c) What would "king - man + woman = ?" look like as an arrow? Solution: Embedding space; vector arithmetic on meaning.

3. **"How Similar?"** -- Embed 02_similarity_heatmap.png. Ask: (a) Which pair has the highest similarity? (b) Are any words surprisingly similar or different? (c) How might a bank use these similarities? Solution: Cosine similarity; applications in search, recommendation.

4. **"The Learning Loop"** -- Embed 03_rl_loop.png. Ask: (a) A robot trader can buy, sell, or hold. It gets +1 for profit, -1 for loss. What should it learn? (b) How is this different from supervised learning (where someone tells you the answer)? (c) What is the role of "state"? Solution: RL loop; agent, environment, state, action, reward.

5. **"Navigate the Grid"** -- Embed 04_q_learning_grid.png. Ask: (a) The agent starts at top-left and wants to reach the goal. What path would you take? (b) Some cells have penalties. How do you avoid them? (c) If you could store a "goodness score" for each cell+action, how would you update it? Solution: Q-learning; state-action values; Bellman update.

6. **"Learning to Trade"** -- Embed 05_reward_curves.png. Ask: (a) The agent starts badly -- why? (b) When does it start improving? (c) Why does the curve plateau? (d) What might cause the occasional dips? Solution: Reward curves; exploration vs exploitation; epsilon decay.

### T08: Dashboard Integration
**File:** `docs/index.html`
**Acceptance criteria:**
- Add sidebar nav entry under "Quizzes" for "Pre-Class Handouts" with links to L01-L06
- Add a new section before the Quizzes section titled "Pre-Class Discovery Handouts" with 6 cards
- Each card: handout icon, lecture title, activity count, link to handout HTML
- Use same card styling as existing content cards
- Update hero stats to include handout count

## Commit Strategy

**Single commit** after all files are created and verified:
```
Add discovery-based pre-class handouts for L01-L06

6 interactive HTML handouts with guided discovery activities,
embedded chart visuals, and expandable solutions. Includes
reusable template and dashboard integration.
```

## Success Criteria
1. All 7 HTML files (1 template + 6 handouts) exist in `docs/handouts/`
2. Each handout has 5-8 activities with embedded chart PNGs that load correctly
3. Solutions are hidden by default, expand on click
4. KaTeX math renders in all handouts
5. Mobile responsive (usable on phone screens)
6. Dashboard links navigate to each handout
7. Visual branding matches existing quizzes (nav bar, colors, card style)
8. No JavaScript errors in browser console

---

## Lecture-to-Folder Mapping (for image paths)

| ID | Folder Name |
|----|-------------|
| L01 | `L01_Introduction_Linear_Regression` |
| L02 | `L02_Logistic_Regression` |
| L03 | `L03_KNN_KMeans` |
| L04 | `L04_Random_Forests` |
| L05 | `L05_PCA_tSNE` |
| L06 | `L06_Embeddings_RL` |

Image path pattern: `../slides/images/{Folder Name}/{chart_name}.png`

## Template Design Decisions (from Critic review)

- **Navigation**: Scroll-based (not prev/next buttons). Activities are cards in a vertical stack — students scroll down. Simpler to build, works well on mobile.
- **`<details><summary>` styling**: Solution box gets `background: #f0f7ff` (light blue), `border-left: 4px solid var(--mlblue)`, `padding: 16px`, `margin-top: 12px`, `border-radius: 8px`. Summary text styled as `color: var(--mlblue)`, `font-weight: 600`, `cursor: pointer`.
- **Image `alt` text**: Every `<img>` tag gets descriptive alt text (e.g., "Scatter plot showing house price vs size with fitted regression line").
- **`loading="lazy"`**: All chart `<img>` tags include `loading="lazy"` for mobile performance.
- **Progress**: Static text banner at top: "6 Activities | Linear Regression" — not a progress bar.

## Critic Issue Resolution Log

**Iteration 1: OKAY with 5 advisory improvements incorporated:**

| Advisory | Resolution |
|----------|-----------|
| Missing folder name mapping | Added explicit mapping table above |
| `<details>` styling unspecified | Added CSS specs: light blue background, blue left border, bold summary |
| Prev/next vs scroll ambiguous | Decided: scroll-based (simpler, better mobile UX) |
| Missing `alt` text for images | Added: all `<img>` tags require descriptive alt text |
| Missing `loading="lazy"` for performance | Added: all chart images use lazy loading |
