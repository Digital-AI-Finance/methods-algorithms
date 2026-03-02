# Plan: Simplify Group Assignment and Publish as GitHub Pages HTML

## Context

### Original Request
Substantially simplify the group assignment specification and publish it as a standalone HTML page on GitHub Pages (`docs/assignment.html`), linked from the main course site.

### Current State
- `capstone/group_assignment_specification.md` (390 lines) -- Full spec with 17+ sections
- `docs/index.html` (339 lines) -- Course website; Assignment section at lines 279-309 links to GitHub markdown files
- The assignment section currently shows 5 cards linking to GitHub-hosted .md files (Specification, Rubric, Peer Review, Contribution, Examples)

### What Changes
The simplified assignment keeps ONLY 5 sections (from the original 17+). Everything else is removed. The HTML page becomes the single canonical location students read, replacing the links to GitHub markdown files.

---

## Work Objectives

### Core Objective
Create a clean, readable HTML assignment page with only the essential information students need, and link it from the main site.

### Deliverables
1. **`docs/assignment.html`** -- Standalone HTML page with 5 sections
2. **`docs/index.html` update** -- Assignment section rewritten to link to `assignment.html`

### Definition of Done
- `docs/assignment.html` exists, is valid HTML, and renders correctly in a browser
- It contains EXACTLY the 5 required sections (no more, no less)
- Styling matches `docs/index.html` (same fonts, colors, spacing conventions)
- `docs/index.html` Assignment section links to `assignment.html` instead of GitHub markdown URLs
- No broken links on either page

---

## Must Have / Must NOT Have

### MUST Have
- Section 1: Overview (what the assignment is)
- Section 2: Group Formation (size, selection, bonus)
- Section 3: Deliverables (GitHub repo, report, presentation, ONE peer review -- simplified)
- Section 4: Dataset Requirements (minimum size, sources, approval)
- Section 5: Combined Topic Requirements (what L03/L04/L05 expect for full credit)
- Topic difficulty table (L01=1, L02=1, L03=2, L04=2, L05=3, L06=4)
- Difficulty multiplier explanation (omit 1pt=1.00, 2pts=0.96, 3pts=0.92, 4pts=0.88)
- Consistent styling with `docs/index.html`

### MUST NOT Have
- Timeline section
- L06 Special Rules section
- Grading Overview section
- Lightning Talks section
- Academic Integrity section
- Late Policy section
- Group Dissolution Policy section
- Individual Contribution Assessment section
- Grade Conversion table
- Course Grade Breakdown section
- Resources section
- FAQ section
- Contact section
- Links to GitHub-hosted markdown files for assignment (remove from index.html)

---

## Task Flow

```
Task 1: Create docs/assignment.html
    |
    v
Task 2: Update docs/index.html Assignment section
    |
    v
Task 3: Verify both pages render correctly
```

No parallelism needed -- Task 2 depends on Task 1 existing, Task 3 depends on both.

---

## Detailed Tasks

### Task 1: Create `docs/assignment.html`

**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\docs\assignment.html`

**Action:** Create new file.

**HTML Structure:**
- Standalone HTML5 page
- Same `<head>` setup as `index.html`: charset UTF-8, viewport meta, system fonts
- Navigation bar matching `index.html` style (`.nav` class): "Methods & Algorithms" title, link back to `index.html`
- Main content area with white background cards, matching the lesson-section styling

**Content -- Section by Section:**

**Section 1: Overview**
Source: Lines 10-15 of `group_assignment_specification.md`
Content to include:
- "ML Pipeline Challenge" title
- Each group selects a real-world finance/business problem, sources a dataset, builds a complete ML pipeline applying 5 of 6 course topics
- Choice of topics determines a difficulty multiplier on the technical analysis score
- Weight: 60% of final grade, groups of 2-3 students
- Include the topic difficulty table (L01-L06 with points) and the multiplier explanation (omit 1pt=1.00 through omit 4pts=0.88)
- Note that every combination can still earn an A-range grade

**Section 2: Group Formation**
Source: Lines 58-66 of `group_assignment_specification.md`
Content to include:
- Size: 2-3 students
- Self-selected with instructor approval by Session 2
- Diversity encouraged
- Two-person bonus: +3 points on final score
- Individual accountability: any member can be asked about any part during Q&A
- If unable to form a group by Session 2, notify instructor

**Section 3: Deliverables**
Source: Lines 70-168 of `group_assignment_specification.md`
Content to include (SIMPLIFIED):

3a. GitHub Repository:
- Required folder structure (the code block from lines 76-91)
- Minimum 10 meaningful commits distributed across members; all members at least 2 commits
- Reproducible: random seeds, requirements.txt
- README.md contents (project title, members, problem statement, reproduce instructions)

3b. Written Report (10-15 pages):
- The section table (Executive Summary, Problem Definition, Methodology, Results, Business Insights, Limitations)
- Formatting: 11pt font, 1.15 spacing, captioned figures, APA/IEEE references

3c. PowerPoint Presentation (15 min + 5 min Q&A):
- 15 slides max
- All members present roughly equal amounts
- Slide structure guide

3d. Peer Review (SIMPLIFIED from "Cross-Group Peer Review"):
- Each group reviews ONE other group's repository (NOT two as in the current spec)
- Use the provided peer review form
- Rate criteria on 1-5 scale with written justification
- Constructive, specific, actionable feedback
- Due 7 days after presentation day
- Remove the "Graded on Quality" point breakdown (that's grading info, which is removed)

**Section 4: Dataset Requirements**
Source: Lines 171-193 of `group_assignment_specification.md`
Content to include:
- Real-world data (not synthetic or toy)
- Minimum: 1,000 observations and 10 features
- Appropriate target variable(s)
- Documented source and license in data/README.md
- Suggested sources list (Kaggle, UCI, Yahoo Finance, FRED, ECB, World Bank, SimFin, Financial PhraseBank)
- Approval process: submit 1-paragraph description + link by Session 2, instructor approves or suggests alternatives

**Section 5: Combined Topic Requirements**
Source: Lines 196-207 of `group_assignment_specification.md`
Content to include:
- The table: L03 (KNN+K-Means), L04 (RF+Boosting), L05 (PCA+t-SNE) with "Full Credit" and "Acceptable Partial" columns
- The exception note: if dataset doesn't support one technique, explain why in report -- demonstrates analytical thinking, no penalty

**Styling Specifications:**
- Copy the CSS variables/approach from `index.html`:
  - Font: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif`
  - Background: `#f6f8fa`
  - Text color: `#24292e`
  - Link color: `#0066CC`
  - Nav bar: `background: #1a1a4e`, sticky top
  - Content cards: white background, `1px solid #e1e4e8` border, `6px` border-radius, `12px` padding
  - Section headers: use the blue accent (`#0066CC`) consistent with the assignment section in index.html
  - Tables: `font-size: 11px`, `border-collapse: collapse`, light gray header rows
  - Code blocks: `background: #f6f8fa`, `border: 1px solid #e1e4e8`, `border-radius: 4px`, monospace font
- Page should be responsive (readable on mobile)
- Max content width ~900px, centered
- No sidebar needed (single-page document)

**Acceptance Criteria:**
- [ ] File exists at `docs/assignment.html`
- [ ] Contains exactly 5 sections: Overview, Group Formation, Deliverables, Dataset Requirements, Combined Topic Requirements
- [ ] Contains the topic difficulty table with all 6 topics and points
- [ ] Contains the multiplier explanation (4 tiers)
- [ ] Peer review says ONE group (not two)
- [ ] No content from removed sections (Timeline, L06 Special Rules, Grading Overview, Lightning Talks, Academic Integrity, Late Policy, Group Dissolution, Individual Contribution, Grade Conversion, Course Grade Breakdown, Resources, FAQ, Contact)
- [ ] Visual style matches `index.html` (fonts, colors, nav bar, card styling)
- [ ] Valid HTML5
- [ ] Responsive layout

---

### Task 2: Update `docs/index.html` Assignment Section

**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\docs\index.html`

**Action:** Edit lines 279-309 (the `<!-- Group Assignment Section -->` block).

**What to change:**

Replace the current section content. The current section has:
- A description paragraph
- 3 stat boxes (5 Topics, 60%, 100 Points)
- 5 cards linking to GitHub markdown files (Specification, Rubric, Peer Review, Contribution, Examples)
- A separate difficulty points table

Replace with:
- Keep the section header: `GA` badge + "Group Assignment (60% of Grade)"
- Keep the description paragraph (ML Pipeline Challenge summary)
- Keep the 3 stat boxes (5 Topics Required, 60% of Course Grade, 100 Points Total)
- Replace the 5 GitHub-linking cards with a SINGLE prominent link/button to `assignment.html`
  - Style it as a prominent card or button: "View Full Assignment Specification" linking to `assignment.html`
  - Optionally keep 1-2 supplementary cards for the rubric and peer review form (these are separate documents that remain on GitHub), but the primary "Specification" link must go to assignment.html
- Keep the difficulty points table (it's useful as a quick reference on the main page)

**Specific HTML changes:**

1. In the `.cgrid` with 5 cards (lines 289-295), replace:
   - The "Specification" card href from `https://github.com/.../group_assignment_specification.md` to `assignment.html`
   - Keep Rubric card (still links to GitHub rubric .md)
   - Keep Peer Review card (still links to GitHub peer review form .md)
   - REMOVE the "Contribution" card (contribution survey is part of the removed "Individual Contribution Assessment" section)
   - REMOVE the "Examples" card (examples are part of the removed "Resources" section)
   - Change grid from 5-column to 3-column: `grid-template-columns:repeat(3,1fr)`

2. In the sidebar navigation (lines 106-112), update the "Group Assignment" details section:
   - Keep "Overview" link pointing to `#assignment`
   - Change "Specification" to link to `assignment.html`
   - Keep "Rubric" and "Peer Review"
   - Remove "Examples"

**Acceptance Criteria:**
- [ ] Assignment "Specification" card links to `assignment.html` (not GitHub)
- [ ] "Contribution" and "Examples" cards removed
- [ ] Grid changed to 3 columns
- [ ] Sidebar updated (remove "Examples")
- [ ] Difficulty points table still present on main page
- [ ] No broken links

---

### Task 3: Visual Verification

**Action:** Open both files in a browser to verify rendering.

Since this is a static HTML project, the executor should:
1. Confirm `docs/assignment.html` is valid HTML (no unclosed tags, no syntax errors)
2. Confirm the file is properly structured with all 5 sections
3. Confirm `docs/index.html` changes don't break the rest of the page
4. Confirm the link from index.html to assignment.html is a relative link (`assignment.html`, not absolute)

**Acceptance Criteria:**
- [ ] Both files parse as valid HTML
- [ ] No obvious structural issues (unclosed tags, missing quotes)
- [ ] Links are relative (both files in `docs/` directory)

---

## Commit Strategy

Single commit with both files:
```
Simplify group assignment and publish as GH Pages HTML

- Create docs/assignment.html with 5 essential sections only
  (Overview, Group Formation, Deliverables, Dataset Requirements,
  Combined Topic Requirements)
- Update docs/index.html to link to assignment.html
- Peer review simplified to one group (was two)
- Removed 12+ sections: Timeline, L06 Special Rules, Grading,
  Lightning Talks, Academic Integrity, Late Policy, etc.
```

Files to commit:
- `docs/assignment.html` (new)
- `docs/index.html` (modified)

---

## Success Criteria

1. A student visiting the course website clicks "Specification" and sees a clean, well-formatted HTML page with exactly 5 sections
2. The page loads instantly (no external dependencies, no JavaScript needed)
3. The styling feels like it belongs to the same site as index.html
4. The content is substantially shorter than the original 390-line markdown (targeting roughly 5 sections vs. 17+)
5. No information from the removed sections leaks into the HTML page
6. The peer review is simplified to reviewing ONE other group (not two)
