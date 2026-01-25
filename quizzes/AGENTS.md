# quizzes/

<!-- Parent: ../AGENTS.md -->

**Generated**: 2026-01-25
**Purpose**: Moodle XML quiz files for online assessments covering course topics L01-L06

---

## Overview

This directory contains **Moodle-compatible XML quiz files** for formative and summative assessments. Each quiz covers 2 consecutive topics and includes:
- Multiple-choice questions (MCQs) with detailed feedback
- Conceptual understanding checks
- Application-based questions
- Randomized answer order to prevent memorization

Quizzes are uploaded to Moodle LMS and can be auto-graded.

---

## Key Files

| File | Topics Covered | Questions | Status |
|------|----------------|-----------|--------|
| `quiz1_topics_1_2.xml` | L01 (Linear Regression), L02 (Logistic Regression) | 20 | Complete |
| `quiz2_topics_3_4.xml` | L03 (KNN & K-Means), L04 (Random Forests) | 20 | Complete |
| `quiz3_topics_5_6.xml` | L05 (PCA & t-SNE), L06 (Embeddings & RL) | 20 | Pending |

**Template source**: `../templates/quiz_template.xml`

---

## For AI Agents

### Quiz Structure

Each quiz XML file contains:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
  <!-- Category definition -->
  <question type="category">
    <category>
      <text>$course$/Methods and Algorithms/Quiz N - Topic Names</text>
    </category>
  </question>

  <!-- Question 1 -->
  <question type="multichoice">
    <name><text>Question Name</text></name>
    <questiontext format="html">
      <text><![CDATA[<p>Question text here</p>]]></text>
    </questiontext>
    <defaultgrade>1</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <single>true</single>
    <shuffleanswers>true</shuffleanswers>
    <answernumbering>abc</answernumbering>

    <!-- Correct answer: fraction="100" -->
    <answer fraction="100" format="html">
      <text><![CDATA[Correct answer text]]></text>
      <feedback format="html">
        <text><![CDATA[Explanation why correct]]></text>
      </feedback>
    </answer>

    <!-- Incorrect answers: fraction="0" -->
    <answer fraction="0" format="html">
      <text><![CDATA[Incorrect answer 1]]></text>
      <feedback format="html">
        <text><![CDATA[Explanation why incorrect]]></text>
      </feedback>
    </answer>
    <!-- More incorrect answers... -->

    <generalfeedback format="html">
      <text><![CDATA[General explanation]]></text>
    </generalfeedback>
  </question>

  <!-- More questions... -->
</quiz>
```

### XML Schema Details

#### Question Type (multichoice)

| Element | Required | Description |
|---------|----------|-------------|
| `<name>` | Yes | Question identifier (shows in Moodle question bank) |
| `<questiontext>` | Yes | The actual question (HTML formatted) |
| `<defaultgrade>` | Yes | Points for correct answer (typically 1) |
| `<penalty>` | Yes | Penalty for wrong answer (0.3333333 = 33% penalty) |
| `<single>` | Yes | `true` for single-choice, `false` for multiple-choice |
| `<shuffleanswers>` | Yes | `true` to randomize answer order |
| `<answernumbering>` | Yes | `abc` (a,b,c) or `123` (1,2,3) or `ABCD` |

#### Answer Options

| Attribute/Element | Value | Description |
|-------------------|-------|-------------|
| `fraction="100"` | Correct | 100% credit (correct answer) |
| `fraction="0"` | Incorrect | 0% credit (wrong answer) |
| `fraction="50"` | Partial | 50% credit (partially correct - for multiple-select) |
| `<feedback>` | Optional | Feedback shown after submission |
| `<generalfeedback>` | Optional | General explanation shown after quiz completion |

---

### How to Create/Edit Quizzes

#### Method 1: Edit XML Directly

```bash
# 1. Copy template
cp templates/quiz_template.xml quizzes/quiz3_topics_5_6.xml

# 2. Edit XML in text editor
# - Update category name
# - Add questions following template structure

# 3. Validate XML syntax
xmllint --noout quizzes/quiz3_topics_5_6.xml

# 4. Test import in Moodle sandbox
```

#### Method 2: Use Moodle UI (Recommended for Non-Technical Users)

```
1. Log into Moodle → Question Bank → Import
2. Choose "Moodle XML format"
3. Upload quiz XML file
4. Review imported questions
5. Edit in Moodle UI as needed
6. Export back to XML to keep file updated
```

---

### Question Writing Guidelines

**CRITICAL**: Follow these guidelines to ensure high-quality assessments.

#### 1. Question Stems

**Good**:
- Clear, concise, and unambiguous
- Tests understanding, not memorization
- Avoids "All of the above" or "None of the above"

```xml
<questiontext format="html">
  <text><![CDATA[<p>What does the sigmoid function map its input to?</p>]]></text>
</questiontext>
```

**Bad**:
```xml
<!-- Vague, ambiguous -->
<text><![CDATA[<p>Which of the following is true about logistic regression?</p>]]></text>
```

#### 2. Answer Options

**Requirements**:
- Exactly **4 answer options** per question (1 correct, 3 incorrect)
- Incorrect options should be **plausible** (avoid obviously wrong answers)
- Similar length across all options (avoid length bias)

**Distractor design** (incorrect answers):
- Common misconceptions
- Partially correct statements
- Related but distinct concepts

**Example**:
```xml
<!-- Question: What does R² measure? -->
<answer fraction="100"><text>Proportion of variance explained</text></answer>  <!-- Correct -->
<answer fraction="0"><text>Correlation coefficient</text></answer>  <!-- Common confusion -->
<answer fraction="0"><text>Mean squared error</text></answer>  <!-- Related metric -->
<answer fraction="0"><text>Number of significant variables</text></answer>  <!-- Misconception -->
```

#### 3. Feedback

**Provide feedback for**:
- **Each answer option** (explains why correct/incorrect)
- **General feedback** (broader context or learning point)

```xml
<answer fraction="100">
  <text><![CDATA[Sum of squared residuals (SSR)]]></text>
  <feedback format="html">
    <text><![CDATA[<p>Correct! OLS minimizes the sum of squared differences between observed and predicted values.</p>]]></text>
  </feedback>
</answer>

<generalfeedback format="html">
  <text><![CDATA[
    <p>OLS is a regression method that finds coefficients by minimizing SSR.
    Under normality assumptions, this is equivalent to maximum likelihood estimation.</p>
  ]]></text>
</generalfeedback>
```

#### 4. Difficulty Levels

**Distribute questions across difficulty levels**:

| Level | % of Quiz | Description | Example |
|-------|-----------|-------------|---------|
| Easy | 30% | Recall, definitions | "What does OLS stand for?" |
| Medium | 50% | Application, interpretation | "Given R²=0.85, what does this mean?" |
| Hard | 20% | Analysis, evaluation | "When would Ridge be preferred over OLS?" |

---

### Question Topics Coverage

#### Quiz 1: L01 (Linear Regression) + L02 (Logistic Regression)

**L01 topics** (10 questions):
- OLS objective function
- Normal equation
- Gradient descent (learning rate, convergence)
- R² interpretation
- Residual analysis
- Regularization (Ridge, Lasso)
- Bias-variance tradeoff
- Assumptions (linearity, homoscedasticity)

**L02 topics** (10 questions):
- Sigmoid function
- Log loss (cross-entropy)
- Decision boundary
- ROC curve, AUC
- Precision vs Recall
- Confusion matrix interpretation
- Class imbalance handling
- Logistic vs Linear regression

#### Quiz 2: L03 (KNN & K-Means) + L04 (Random Forests)

**L03 topics** (10 questions):
- KNN distance metrics
- K selection (odd vs even)
- Curse of dimensionality
- K-Means algorithm steps
- Elbow method
- Silhouette score
- Voronoi diagrams
- KNN vs K-Means differences

**L04 topics** (10 questions):
- Decision tree splitting criteria (Gini, entropy)
- Bootstrap sampling
- Feature importance
- OOB error
- Random vs Deterministic forests
- Overfitting prevention
- Ensemble voting
- Hyperparameters (n_estimators, max_depth)

#### Quiz 3: L05 (PCA & t-SNE) + L06 (Embeddings & RL) - Pending

**L05 topics** (10 questions):
- PCA objective (variance maximization)
- Scree plot interpretation
- Principal components
- Reconstruction error
- t-SNE perplexity
- PCA vs t-SNE use cases
- Dimensionality reduction benefits

**L06 topics** (10 questions):
- Word embeddings (Word2Vec, GloVe)
- Embedding similarity
- Q-learning
- Exploration vs Exploitation
- Reward shaping
- RL vs Supervised learning

---

### Validation Requirements

Before committing quiz changes:

#### 1. XML Syntax Validation

```bash
# Install xmllint (part of libxml2)
sudo apt-get install libxml2-utils  # Linux
brew install libxml2  # macOS

# Validate syntax
xmllint --noout quizzes/quiz1_topics_1_2.xml

# Expected output: (no errors)
```

#### 2. Content Validation Checklist

- [ ] Exactly 20 questions (10 per topic)
- [ ] Each question has 4 answer options (1 correct, 3 incorrect)
- [ ] All correct answers have `fraction="100"`
- [ ] All incorrect answers have `fraction="0"`
- [ ] `<shuffleanswers>true</shuffleanswers>` is set
- [ ] Feedback provided for each answer
- [ ] General feedback provided for complex questions
- [ ] No typos or grammatical errors
- [ ] Questions test understanding, not just memorization

#### 3. Moodle Import Test

```
1. Set up Moodle sandbox (or use test course)
2. Question Bank → Import → Moodle XML format
3. Upload quiz file
4. Review imported questions:
   - All questions imported successfully
   - Correct answers marked correctly
   - Feedback displays properly
   - HTML formatting works
5. Create test quiz and take it to verify functionality
```

---

### Common XML Issues

| Issue | Symptom | Fix |
|-------|---------|-----|
| Invalid XML | Import fails with parsing error | Run `xmllint` to find syntax error (missing closing tag, unescaped `<`, etc.) |
| CDATA not used | HTML tags rendered as text | Wrap HTML in `<![CDATA[...]]>` |
| Wrong fraction | Incorrect answer marked correct | Verify `fraction="100"` only on correct answer |
| Missing feedback | No feedback after answer | Add `<feedback>` element to each answer |
| Category not set | Questions import to wrong category | Check `<category><text>` matches course structure |

**HTML in questions**: Always use CDATA for HTML content to avoid XML parsing errors.

```xml
<!-- Correct: HTML in CDATA -->
<text><![CDATA[<p>Question with <b>bold</b> text</p>]]></text>

<!-- Incorrect: HTML without CDATA (will break) -->
<text><p>Question with <b>bold</b> text</p></text>
```

---

### Adding Mathematical Formulas

Moodle supports **MathJax** for LaTeX math rendering:

```xml
<questiontext format="html">
  <text><![CDATA[
    <p>What is the derivative of the loss function \( L(\beta) = \frac{1}{2n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 \)?</p>
  ]]></text>
</questiontext>
```

**Inline math**: Use `\( ... \)` or `$ ... $`

**Display math**: Use `\[ ... \]` or `$$ ... $$`

**Example**:
```xml
<text><![CDATA[
  <p>The sigmoid function is defined as:</p>
  <p>\[ \sigma(z) = \frac{1}{1 + e^{-z}} \]</p>
]]></text>
```

---

### Updating Existing Quizzes

**Workflow**:

```bash
# 1. Export current version from Moodle
# Question Bank → Export → Moodle XML format → Download

# 2. Edit XML file
# - Add/remove questions
# - Fix errors
# - Update feedback

# 3. Validate
xmllint --noout quizzes/quiz1_topics_1_2.xml

# 4. Re-import to Moodle
# Question Bank → Import → Moodle XML format → Replace existing questions

# 5. Test quiz functionality

# 6. Commit updated XML to repository
git add quizzes/quiz1_topics_1_2.xml
git commit -m "Update Quiz 1: Add 2 questions on regularization"
```

---

## Quiz Administration

### Moodle Quiz Settings (Recommended)

| Setting | Recommended Value | Rationale |
|---------|-------------------|-----------|
| Time limit | 30 minutes | 1.5 min per question |
| Attempts allowed | 2 | Allow learning from mistakes |
| Grading method | Highest grade | Encourage retakes |
| Question order | Shuffle | Prevent cheating |
| Show feedback | After quiz close | Prevent sharing answers |
| Review options | Show correct answers after close | Educational value |
| Passing grade | 70% | Standard for MSc courses |

---

## Related Files

- **Parent hierarchy**: `../AGENTS.md` (project root)
- **Template source**: `../templates/quiz_template.xml`
- **Slides**: `../slides/L0X_Topic/` (quiz questions derived from lecture content)
- **Notebooks**: `../notebooks/L0X_*.ipynb` (practice exercises complement quizzes)
- **Manifest**: `../manifest.json` (tracks quiz status)
- **CLI**: `python infrastructure/course_cli.py inventory list` (shows quiz coverage)
