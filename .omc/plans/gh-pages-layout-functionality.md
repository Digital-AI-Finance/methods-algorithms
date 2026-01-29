# GH Pages Layout & Functionality Review Plan

## Context

**Original Request:** Review visual design quality, CSS layout correctness, responsive behavior, and JavaScript functionality of the GitHub Pages site (docs/).

**Scope:** Layout/functionality only. NOT a link/content audit.

**Key Files:**
- `docs/index.html` - Landing page (3-column wiki layout)
- `docs/css/style.css` - 566 lines, CSS Grid + responsive
- `docs/js/main.js` - 109 lines, scroll spy + mobile menu + smooth scroll
- `docs/slides/L01_overview.html` - Representative Reveal.js slide (12 presentations total)
- `docs/slides/css/ml-theme.css` - 278 lines, custom Reveal.js theme

---

## Work Objectives

**Core Objective:** Identify all CSS layout bugs, JS functionality issues, responsive breakage, and Reveal.js integration problems. Produce a prioritized fix list.

**Deliverables:**
1. Detailed findings report with severity ratings (CRITICAL / MAJOR / MINOR / COSMETIC)
2. Specific CSS/JS fixes for each issue found

**Definition of Done:** Every issue in the 10-point review checklist has been analyzed with a verdict (BUG / OK / IMPROVEMENT).

---

## Must Have
- Analyze every issue in the checklist below
- Provide file:line references for all bugs found
- Severity rating for each finding
- Concrete fix (code snippet) for each bug

## Must NOT Have
- Link validation (already done separately)
- Content review (text, images, accuracy)
- New features or redesign proposals
- Changes to Reveal.js library code

---

## Task Flow

All tasks are independent code-analysis tasks. They can run in parallel.

### Task 1: CSS Grid Double-Offset Bug Analysis
**Files:** `docs/css/style.css` lines 47-51, 140-144
**Issue:** `.main-content` has `grid-column: 2` (already placed in 2nd column by grid) AND `margin-left: var(--sidebar-width)` (220px). The sidebar is `position: fixed` so it is removed from flow, meaning the grid's first column collapses to 0. The margin-left then compensates. Analyze whether this actually produces a double offset or works correctly given the fixed sidebar.
**Acceptance Criteria:**
- Verdict: Does the layout render correctly or is there a 220px gap?
- If bug: provide the fix (likely remove margin-left or adjust grid-template-columns)
- Test at desktop (>1200px), tablet (768-1200px), mobile (<768px)

### Task 2: Main Content Padding Analysis
**Files:** `docs/css/style.css` line 143
**Issue:** `padding: 40px 10px 40px 10px` gives only 10px horizontal padding. With content between sidebar (220px) and TOC (200px), effective content width = viewport - 420px - 20px padding. On a 1440px screen that is ~1000px of content with only 10px breathing room from the TOC edge.
**Acceptance Criteria:**
- Verdict: Is 10px too tight? Does text butt against the TOC sidebar?
- Recommendation with specific padding values
- Check if TOC sidebar padding (20px) provides visual separation

### Task 3: Mobile Responsive Behavior (index.html)
**Files:** `docs/css/style.css` lines 462-519, `docs/js/main.js` lines 57-86
**Analysis points:**
- At 768px breakpoint: grid changes to `1fr 160px`. Sidebar hides (translateX). Main content gets `margin-left: 0`. TOC stays at 160px fixed right. Does main content overlap with TOC?
- Mobile menu toggle: button appears, toggles `.open` class on sidebar, overlay shows. Does clicking nav items close sidebar? (Yes, line 78-85 handles this.)
- At 1200px breakpoint: TOC narrows to 180px. Does the CSS variable override (line 468-469) actually work? `:root` re-declaration inside media query should work.
- Is there a breakpoint gap? Between 768-1200 no grid change but TOC shrinks. Main content still has `margin-left: var(--sidebar-width)` = 220px. Grid is still 3-column. This should work.
**Acceptance Criteria:**
- Verdict per breakpoint (>1200, 768-1200, <768, <480)
- Any overlap/overflow issues identified
- Mobile menu open/close verified correct

### Task 4: Scroll Spy (IntersectionObserver) Correctness
**Files:** `docs/js/main.js` lines 12-52
**Analysis points:**
- `rootMargin: '-20% 0px -60% 0px'` means the intersection zone is the middle 20% of the viewport (top 20% excluded, bottom 60% excluded). This is a narrow active zone.
- Multiple sections can fire `isIntersecting: true` simultaneously if they overlap this zone. The observer processes entries in order but doesn't guarantee only one is active. Last one wins per callback batch.
- Sections are queried as `.section` and matched by `id` attribute to `href` on `.toc-link` and `.nav-item`. All IDs match (home, l01-l06, quizzes, capstone).
- Edge case: If a section is shorter than the active zone, it may never trigger or trigger very briefly.
**Acceptance Criteria:**
- Verdict: Does scroll spy reliably highlight the correct section?
- Identify any race conditions or flickering issues
- Check if the rootMargin values are appropriate

### Task 5: Reveal.js Home Button Positioning
**Files:** `docs/slides/L01_overview.html` lines 86-107
**Analysis:**
- Home button: `position: fixed; top: 15px; left: 15px; z-index: 100; width: 40px; height: 40px; border-radius: 50%`
- Reveal.js menu plugin button is typically at top-left. Menu config has `openButton: true` which adds a hamburger at top-left.
- Both at z-index 100, both top-left corner. Potential overlap.
- Chalkboard toggleNotesButton: `left: 70px, bottom: 30px`. Chalkboard toggleChalkboardButton: `left: 30px, bottom: 30px`. These are bottom-left, no conflict with home button.
**Acceptance Criteria:**
- Verdict: Does home button overlap with Reveal.js menu button?
- If overlap: provide repositioning fix
- Check all four corners for element collisions

### Task 6: PDF Download Button vs Reveal.js Controls
**Files:** `docs/slides/L01_overview.html` lines 54-83
**Analysis:**
- PDF button: `position: fixed; bottom: 20px; right: 20px; z-index: 100`
- Reveal.js controls: `controlsLayout: 'bottom-right'` - navigation arrows at bottom-right
- Reveal.js slide-number: `.slide-number` styled in ml-theme.css with purple background, positioned by Reveal.js default (bottom-right)
- Potential triple collision at bottom-right: PDF button + nav controls + slide number
**Acceptance Criteria:**
- Verdict: Do PDF button, nav arrows, and slide number overlap?
- If overlap: provide repositioning fix with specific pixel values

### Task 7: Slide Footer & Dynamic Counter
**Files:** `docs/slides/L01_overview.html` lines 177-182, 335-352; `docs/slides/css/ml-theme.css` lines 186-213
**Analysis:**
- Footer: `.slide-footer` is `position: absolute; bottom: 0; height: 40px` inside `.reveal` div
- Footer-right is updated on `slidechanged` and `ready` events with `current / total`
- `event.indexh + 1` counts horizontal slides only. With nested sections (vertical slides), this shows the section number, not the absolute slide number. `Reveal.getTotalSlides()` returns all slides.
- Mismatch: if there are 10 total slides across 4 sections, footer shows "1/10", "2/10", "3/10", "4/10" - skipping vertical slides in the numerator.
- Footer is INSIDE `.reveal` but positioned absolute. It will be part of the slide scaling, so it renders inside the presentation frame. This is correct.
**Acceptance Criteria:**
- Verdict: Does slide counter display correctly for both horizontal and vertical navigation?
- Identify the horizontal-only counting bug
- Provide fix using `Reveal.getSlidePastCount() + 1` or similar

### Task 8: TOC Sidebar Scroll Behavior
**Files:** `docs/css/style.css` lines 147-156
**Analysis:**
- TOC: `position: fixed; top: 40px; right: 0; height: calc(100vh - 80px); overflow-y: auto`
- With 9 items in the TOC list, each ~30px tall, total ~270px. On any viewport taller than 350px this won't scroll. OK.
- But TOC is fixed at right: 0, overlapping the grid's third column. Since grid column 3 exists (200px), and TOC is fixed/removed from flow, the grid third column is empty space that prevents main content from extending under the TOC. This is correct.
**Acceptance Criteria:**
- Verdict: Does TOC stay correctly positioned during scroll?
- Any z-index or overlap issues?

### Task 9: Reveal.js Custom Theme Integration
**Files:** `docs/slides/css/ml-theme.css`, `docs/slides/L01_overview.html`
**Analysis:**
- Theme loaded AFTER `white.css` base theme, so overrides apply correctly
- Slides use image-based content (`<img>` per slide), so most text styling in ml-theme.css (lists, tables, code) is unused but harmless
- `.reveal .slides section` in ml-theme.css sets `padding: 20px 50px`, but inline HTML overrides with `display: flex !important; height: 100%`. The inline style takes precedence for display/height, but padding from ml-theme.css still applies (adding 50px horizontal padding to image slides that only need centering). This wastes space around images.
- `.slide-footer` height 40px at bottom + `margin: 0` in Reveal config means slides go edge-to-edge but footer overlaps last 40px of slide content.
**Acceptance Criteria:**
- Verdict: Does the theme render correctly with image-based slides?
- Does the 50px padding waste space around slide images?
- Does footer overlap slide content?

### Task 10: Cross-Browser & Accessibility Quick Scan
**Files:** All HTML/CSS/JS in docs/
**Analysis:**
- CSS Grid: supported in all modern browsers. OK.
- `scroll-behavior: smooth`: not supported in Safari <15.4. Graceful degradation (instant scroll). OK.
- IntersectionObserver: supported everywhere modern. OK.
- `position: fixed` inside CSS Grid: works correctly in all browsers.
- Accessibility: mobile menu toggle has `aria-label`. Home button has `title` but no `aria-label`. Slide images have generic `alt="Slide N"` - poor for screen readers but acceptable for image-based slides.
- Color contrast: sidebar white-on-dark-blue is fine. TOC gray text (#64748b) on white may fail WCAG AA for small text (13px).
**Acceptance Criteria:**
- List any browser compatibility issues
- List accessibility gaps with severity

---

## Commit Strategy

Single commit after all fixes applied:
```
Fix GH Pages layout and functionality issues

- [list of specific fixes applied]
```

## Success Criteria

1. All 10 tasks have a verdict (BUG / OK / IMPROVEMENT)
2. Every BUG has a concrete fix with file:line reference
3. No CRITICAL issues remain unaddressed
4. Findings organized by severity for easy triage
