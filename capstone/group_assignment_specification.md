# ML Pipeline Challenge: Group Assignment Specification

**Course:** Methods and Algorithms — MSc Data Science
**Weight:** 60% of final grade
**Group Size:** 2-3 students
**Deliverables:** GitHub repository, written report (10-15 pages), PowerPoint presentation (15 min + 5 min Q&A)

---

## Overview

Each group will select a real-world finance or business problem, source an appropriate dataset, and build a complete machine learning pipeline that applies **five of the six course topics**. Your choice of which topics to include will determine a score multiplier applied to the technical analysis portion of your grade.

This assignment simulates the end-to-end workflow of a data science project in industry: problem formulation, data acquisition, exploratory analysis, model development, evaluation, and presentation of actionable insights to stakeholders.

---

## Course Topics and Difficulty Points

| Topic | Difficulty Points |
|-------|-------------------|
| L01: Linear Regression | 1 |
| L02: Logistic Regression | 1 |
| L03: KNN & K-Means | 2 |
| L04: Random Forests & Boosting | 2 |
| L05: PCA & t-SNE | 3 |
| L06: Embeddings & Reinforcement Learning | 4 |

**Total Possible:** 13 points

### How the Difficulty Multiplier Works

The topic you omit determines your difficulty multiplier, which is applied to the Technical Analysis score (50 points maximum):

- **Omit L01 or L02 (1 pt):** Remaining = 12, multiplier = 1.00, max technical score = 50/50
- **Omit L03 or L04 (2 pts):** Remaining = 11, multiplier = 0.96, max technical score = 48/50
- **Omit L05 (3 pts):** Remaining = 10, multiplier = 0.92, max technical score = 46/50
- **Omit L06 (4 pts):** Remaining = 9, multiplier = 0.88, max technical score = 44/50

**Important:** Every combination can still earn an A-range grade. The multiplier rewards ambitious topic selection but does not prevent excellent work on easier topics from achieving top marks.

---

## Timeline

| Milestone | When |
|-----------|------|
| Assignment introduced, GitHub tutorial | Session 1 |
| Groups formed, dataset proposal submitted | Session 2 |
| Lightning Talk 1 (dataset, EDA, topic selection) | Session 3 |
| Lightning Talk 2 (preliminary results from 3+ methods) | Session 5 |
| Final presentation day | Session 6 + 2 weeks |
| GitHub repo, report, slides due | Session 6 + 7 days (23:59) |
| Peer reviews due | Presentation day + 7 days |

---

## Group Formation

- **Size:** 2-3 students
- **Selection:** Self-selected with instructor approval by Session 2
- **Diversity Encouraged:** Mix of backgrounds (finance, computer science, statistics) is beneficial
- **Two-Person Bonus:** Groups of 2 receive 3 bonus points on final score to offset the smaller team size
- **Individual Accountability:** During Q&A, any member can be asked about any part of the project

If you are unable to form a group by Session 2, notify the instructor for assistance.

---

## Deliverables

### 1. GitHub Repository

Your repository must follow this structure:

```
group-project/
├── README.md
├── requirements.txt
├── data/
│   └── README.md       (data dictionary, source, license)
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_modeling.ipynb
│   └── 04_evaluation.ipynb
├── presentation/
│   └── slides.pptx
└── report/
    └── report.pdf
```

**Repository Requirements:**
- Minimum 10 meaningful commits distributed across all members
- All members must have at least 2 commits
- Reproducible: set random seeds, include `requirements.txt`
- No credentials or API keys committed
- Add instructor as collaborator (for private repos) or make public

**README.md Contents:**
- Project title and group members
- Problem statement (2-3 sentences)
- Instructions to reproduce results
- Link to presentation slides and report

**data/README.md Contents:**
- Data source (URL or citation)
- License information
- Data dictionary (all columns explained)
- Any preprocessing applied before upload

---

### 2. Written Report (10-15 pages)

| Section | Length (pages) | Content |
|---------|----------------|---------|
| Executive Summary | 0.5 | Problem, approach, key findings, recommendation (1 paragraph) |
| Problem Definition & Data | 1.5 | Business context, research question, dataset description, exploratory analysis |
| Methodology | 4-5 | One subsection per method (5 total): theory, implementation, hyperparameters, rationale |
| Results & Comparison | 3-4 | Quantitative results (tables/plots), model comparison, best performer, interpretation |
| Business Insights | 1 | Actionable recommendations for stakeholders based on findings |
| Limitations & Reflection | 1 | What didn't work, assumptions, data limitations, lessons learned |

**Formatting:**
- 11pt font, 1.15 line spacing
- Figures and tables must have captions
- References in APA or IEEE format
- Page count excludes references and appendices

---

### 3. PowerPoint Presentation (15 min + 5 min Q&A)

- **Length:** 15 slides maximum (excluding title and references)
- **Time:** 15 minutes for presentation, 5 minutes for Q&A
- **Participation:** All members must present roughly equal amounts
- **Structure:**
  - Slide 1: Title, group members
  - Slides 2-3: Problem and data
  - Slide 4: ML pipeline diagram (flowchart of your 5 methods)
  - Slides 5-12: Key results (one slide per method, plus comparison)
  - Slide 13: Deep dive on one interesting result
  - Slide 14: Business insights and recommendations
  - Slide 15: Limitations and next steps

**Q&A Participation:**
- Instructor AND peer groups will ask questions
- Questions may be directed to specific individuals
- Demonstrates understanding and contribution

---

### 4. Cross-Group Peer Review

After presentations, each group will review **two other groups' repositories** using the provided peer review form (available in `rubrics/peer_review_form.md`).

**Requirements:**
- Assigned by instructor (no reciprocal reviews)
- Rate 5 criteria on 1-5 scale with written justification
- Constructive feedback (what worked, what could improve)
- Due 7 days after presentation day

**Graded on Quality of Your Reviews (10 points):**
- Thoroughness: Did you examine code, notebooks, documentation?
- Constructiveness: Specific, actionable feedback?
- Professionalism: Respectful tone?

---

## Dataset Requirements

Your dataset must be:
- **Real-world data** (not synthetic or toy datasets)
- **Minimum size:** 1,000 observations and 10 features
- **Appropriate target variable(s)** for the problem
- **Documented:** Source and license clearly stated in `data/README.md`

**Suggested Sources:**
- Kaggle (finance, fraud detection, customer churn)
- UCI Machine Learning Repository
- Yahoo Finance / Google Finance
- FRED (Federal Reserve Economic Data)
- European Central Bank Statistical Data Warehouse
- World Bank Open Data
- SimFin (financial statement data)
- Financial PhraseBank (for NLP tasks with L06)

**Approval Process:**
- Submit 1-paragraph dataset description + link by Session 2
- Instructor approves or suggests alternatives
- Resubmit if needed before Session 3

---

## Combined Topic Requirements

Some topics cover two distinct techniques. Here's what's expected for full credit:

| Topic | For Full Credit (5/5) | Acceptable Partial (3-4/5) |
|-------|-------------------|--------------------|
| **L03: KNN + K-Means** | Both applied (KNN for classification/regression, K-Means for clustering) | One with strong analysis |
| **L04: RF + Boosting** | At least one ensemble (RF/Bagging) + one boosting method (XGBoost/LightGBM) compared | Only RF or only boosting |
| **L05: PCA + t-SNE** | PCA for dimensionality reduction + t-SNE for visualization | Only PCA applied |

**Exception:** If your dataset genuinely doesn't support one technique (e.g., no clear clustering structure for K-Means), explain why in your report. This demonstrates analytical thinking and will not be penalized.

---

## L06: Embeddings & Reinforcement Learning — Special Rules

For L06, you may apply **EITHER embeddings OR reinforcement learning** (not required to do both).

### Option A: Embeddings
- Pre-trained embeddings (Word2Vec, GloVe, FinBERT) are acceptable
- Apply to text data (news sentiment, financial disclosures)
- Show how embeddings improve performance vs. baseline

### Option B: Reinforcement Learning
- Simplified trading environment sufficient (3-5 states, 2-3 actions)
- Use Q-learning or policy gradient
- **Negative results are acceptable** — RL often underperforms on real data
- Full credit awarded if analysis and reflection are rigorous

**L06 is the highest-difficulty topic (4 points).** Even if results are underwhelming, thoughtful implementation and honest reflection earn full marks.

---

## Grading Overview (100 points)

| Category | Points |
|----------|--------|
| **Technical Analysis** | 50 (after difficulty multiplier) |
| **Communication** | 30 |
| **Problem Framing & Insight** | 10 |
| **Peer Review Quality** | 10 |
| **Total** | **100** |

**Bonus:**
- 2-person groups: +3 points

**Detailed Rubric:** See `rubrics/group_assignment_rubric.md` for scoring criteria in each category.

---

## Lightning Talks (10% of course grade, separate from this rubric)

Lightning Talks are formative and graded separately (10% of overall course grade).

### Lightning Talk 1 (Session 3, 5 minutes)
- Dataset overview and problem definition
- Initial exploratory analysis (2-3 visualizations)
- Topic selection (which 5 methods and why)
- One challenge or open question

### Lightning Talk 2 (Session 5, 5 minutes)
- Preliminary results from at least 3 methods
- What's working, what's not
- Revised plan for final stretch

**Feedback:** Instructor provides written feedback within 48 hours to guide final work.

---

## Academic Integrity

- **Code:** Must be original. If you adapt code from online sources, cite it in comments.
- **AI Tools:** ChatGPT, GitHub Copilot, and similar tools are permitted for coding assistance but must be disclosed in your report (Appendix).
- **Written Analysis:** Must be in your own words. Paraphrasing without citation is plagiarism.
- **Detection:** All reports are subject to plagiarism detection software.

**Violations result in zero credit and referral to the Academic Integrity Committee.**

---

## Late Policy

- **24-hour grace period:** -5 points (no questions asked)
- **Beyond 24 hours:** -10 points per additional day (max -30 points)
- **No extensions** granted without documented emergency (medical, family)

All deliverables (GitHub repo, report, slides) must be submitted by the deadline to avoid penalty.

---

## Group Dissolution Policy

If your group encounters irreconcilable issues:

### Before Session 4
- Members may join other groups (instructor facilitates)
- No grade penalty

### After Session 4
- Reduced scope: 4 topics instead of 5 (no multiplier penalty)
- Notify instructor within 48 hours of dissolution
- Individual contribution assessment still applies

**Proactive communication is key.** If issues arise, contact the instructor immediately.

---

## Individual Contribution Assessment

All members complete a confidential survey rating each teammate on:
- Technical contribution (coding, modeling)
- Communication (writing, presenting)
- Project management (organization, deadlines)

**Scale:** 1 (did not contribute) to 5 (exceptional contribution)

**Grade Adjustment:**
- If a member's rating is >1.5 standard deviations below the group mean, they will be asked to complete a 5-minute oral defense.
- Based on survey and defense, individual grades may be adjusted +/- 10%.

**Example:** Group earns 88/100. Member with low ratings and weak defense: 79/100 (88 - 10%). Member with exceptional ratings: 97/100 (88 + 10%).

---

## Grade Conversion

| Score | Letter Grade |
|-------|--------------|
| 93-100 | A |
| 85-92 | A- |
| 78-84 | B+ |
| 70-77 | B |
| 62-69 | C+ |
| 55-61 | C |
| <55 | F |

---

## Overall Course Grade Breakdown

This group assignment is the largest component of your final grade:

| Component | Weight |
|-----------|--------|
| **Group Assignment** | **60%** |
| Session Quizzes (3 quizzes: L01-L02, L03-L04, L05-L06) | 20% |
| Class Participation | 10% |
| Lightning Talks | 10% |

---

## Resources and Support

- **Example Projects:** See `capstone/example_projects.md` for annotated examples of past work at A, B, and C levels.
- **Rubrics:** Detailed scoring criteria in `rubrics/group_assignment_rubric.md` and `rubrics/peer_review_form.md`.
- **GitHub Tutorial:** Provided in Session 1 (recorded for reference).
- **Office Hours:** Instructor available for dataset approval, technical questions, group issues.
- **Course Forum:** Post questions (excluding code sharing) for peer and instructor responses.

---

## Frequently Asked Questions

**Q: Can we use a dataset from a previous course?**
A: Only if you significantly extend the analysis (new methods, deeper investigation). Discuss with instructor first.

**Q: What if our RL agent fails to learn anything useful?**
A: That's a common outcome with RL on real data. Full credit if you diagnose why, compare to baselines, and reflect on limitations.

**Q: Can we include L06 embeddings AND RL?**
A: Yes, if your problem supports it (e.g., RL trading agent using embedded news sentiment). This earns extra recognition but does not increase the difficulty multiplier beyond 4 points.

**Q: Do we need to tune hyperparameters for all 5 methods?**
A: Yes, at minimum use grid search or random search for key hyperparameters. Document your search space in the report.

**Q: Can we split into two 2-person groups after Session 3?**
A: No. Group composition is locked after Session 2. If issues arise, see the Group Dissolution Policy.

---

## Contact

For questions or issues:
- **Office Hours:** See course syllabus for schedule
- **Course Forum:** Post non-sensitive questions for community support
- **Email:** For private matters (group conflicts, extensions) only

---

**Good luck! This is your opportunity to showcase the breadth of skills you've developed across all six course topics. Choose a problem you're passionate about, build something meaningful, and tell a compelling story with your data.**

---

*Last updated: Session 1*
