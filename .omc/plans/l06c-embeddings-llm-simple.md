# Plan: Embeddings in the LLM World — Visual Guide

## Task
Create `L06c_embeddings_llm_simple.tex` — a formula-free visual lecture tracing the evolution from static word embeddings (Word2Vec) to contextual embeddings (BERT/GPT) to modern LLMs. Following the `formula-free-visual-lecture` skill pattern with the contrast arc.

## Relationship to L06a (Embeddings Visual Guide)

L06a teaches "what are embeddings" as a standalone primer. L06c teaches "how embeddings evolved into LLMs" — a different story that shares the same starting point but diverges at slide 9.

**Overlap**: 3 charts are reused from L06a (`01_word_embedding_space`, `top10_08_word_analogy`, `02_similarity_heatmap`) because the static-embeddings recap is essential setup before the LLM story. These 3 charts appear in a compressed 4-slide recap (slides 5-8), NOT the 7-slide deep exploration L06a gives them.

**Differentiation**: L06c uses 4 charts NOT in L06a (`top10_10_embedding_dimensions`, `top10_12_context_window`, `top10_11_word_frequency_rank`, `top10_18_embedding_pca_variance`). All 4 TikZ comics are NEW (not reused from L06a). The entire second half (slides 13-25) covers content that does NOT exist in any other lecture: polysemy, self-attention, contextual embeddings, LLM scaling, and modern API usage.

**For instructors**: Use L06a if your audience needs only classic embeddings. Use L06c if you want the "Word2Vec → ChatGPT" evolution story. They are complements, not replacements.

## Skill Applied
`skills/formula-free-visual-lecture.md` — uses the skill's contrast arc: "Method A works → Method A has limits → Method B saves the day."

### Skill Arc Adaptation

The skill template has 4 acts: Problem, Method A, Method B, Comparison. This plan uses:
- **Act 1** = Problem + Static Embeddings Work (compressed intro — recap, not deep dive)
- **Act 2** = Going Deeper + The Limit (charts that BRIDGE to LLMs, ending with polysemy failure)
- **Act 3** = Contextual Embeddings → LLMs (the Method B section)
- **Act 4** = LLM Revolution + Applications (comparison + forward-looking)

The "limit" moment (polysemy) occurs at the END of Act 2 rather than at the Act 2/3 boundary. This positions it as the cliff-hanger that propels into Act 3, which is narratively stronger for a "before/after" evolution story.

## Requirements
1. **Zero formulas**: No `$$`, no loss functions, no attention equations, no softmax
2. **Comics**: 4 TikZ stick-figure comics at structural points. Max 25 lines TikZ each
3. **Chart subset**: 7 charts curated from existing L06 pool (no new chart.py files)
4. **Course standards**: Madrid theme, 8pt, 16:9, `\bottomnote{}` on every content slide, XKCD bookends
5. **Standalone file**: Does not replace any existing file
6. **Preamble**: Copy from L06_embeddings_rl_simple.tex (identical to all L06 variants)
7. **New topic coverage**: Must go beyond Word2Vec to cover BERT, GPT, attention (conceptually), and the scaling story

## Acceptance Criteria
- [ ] AC1: .tex compiles with 0 errors, 0 Overfull
- [ ] AC2: 22-28 slides
- [ ] AC3: At least 4 TikZ comics (total tikzpictures >= 7 including diagrams)
- [ ] AC4: Exactly 7 reused charts (no new chart.py files)
- [ ] AC5: Zero `$$` display math
- [ ] AC6: `\bottomnote{}` on every content slide
- [ ] AC7: XKCD bookends (opening + closing)
- [ ] AC8: Covers the full arc: Word2Vec → polysemy limit → BERT/GPT → LLM revolution

## Chart Curation (7 from existing pool)

| # | Story Beat | Chart Path | Also in L06a? | Why |
|---|-----------|------------|---------------|-----|
| 1 | "Words become points" | `01_word_embedding_space` | Yes (recap) | GloVe 2D plot — essential starting point |
| 2 | "Words have math!" | `top10_08_word_analogy` | Yes (recap) | King-Queen — wow moment for static |
| 3 | "Who's similar?" | `02_similarity_heatmap` | Yes (recap) | Cosine similarity — proof static works |
| 4 | "Word frequency patterns" | `top10_11_word_frequency_rank` | No | Zipf's law — shows how embeddings learn from frequency, bridges to "LLMs read everything" |
| 5 | "How many dimensions?" | `top10_10_embedding_dimensions` | No | Quality vs dims — bridges to LLM scale |
| 6 | "Context matters" | `top10_12_context_window` | No | Context window — bridges to attention |
| 7 | "Embedding structure" | `top10_18_embedding_pca_variance` | No | PCA of embeddings — shows they have structure |

**Why these 7**: Charts 1-3 recap static embeddings (compressed). Charts 4-7 are ALL unique to L06c and all serve as bridges to LLM concepts: frequency → data scale, dimensions → model scale, context window → attention window, PCA structure → representation quality.

### Chart Bridging Notes (IMPORTANT for implementer)

- **Chart 5 (embedding_dimensions)**: The chart shows quality vs 2-50 dimensions. The accompanying text MUST bridge to LLM scale: "This chart shows up to 50 dimensions. BERT uses 768. GPT-4 uses over 12,000. More dimensions = richer meaning."
- **Chart 6 (context_window)**: The chart shows Word2Vec windows of 1-12 words. The accompanying text MUST bridge: "Word2Vec looks at a few neighbors. BERT sees the whole sentence. GPT-4 can see 128,000 words at once."

## TikZ Comics (4 structural comics + 3 diagrams = 7 total)

### Comics (ALL new — none reused from L06a)

| # | Title | Description | Position |
|---|-------|-------------|----------|
| C1 | "Lost in Translation 2.0" | Stick figure with smartphone showing chat bubble. Computer behind: "01101". Speech bubble: "I can text you, but can the computer really UNDERSTAND me?" Different from L06a's C1 (word cards). | Slide 4 (opening problem) |
| C2 | "The Dictionary Analogy" | Stick figure next to bookshelf (3 rectangles). Each book = one word with ONE definition. Arrow pointing to "bank" book: only says "money place". Caption: "Static embeddings = one meaning per word, forever." | Slide 8 (static embedding analogy) |
| C3 | "The Conversation" | Two stick figures talking. Left says "bank" with context bubbles: "river", "fish", "water". Right says "bank" with: "money", "loan", "ATM". Same word, different meaning! Caption: "Context changes everything." | Slide 15 (contextual embedding — Method B pivot) |
| C4 | "From Dictionary to Conversation Partner" | Left: stick figure with book (small). Arrow. Right: stick figure with large robot. Robot speech bubble: "I understand context now!" | Slide 23 (resolution) |

### TikZ Diagrams (non-comic)

| # | Description | Position |
|---|-------------|----------|
| D1 | Self-attention: 3 word boxes in a row ("The", "bank", "collapsed"). Arrows from "bank" to other words with varying thickness. Caption: "Each word asks: which other words help me understand my meaning?" | Slide 16 |
| D2 | 3-step flowchart: "1. Read Context → 2. Compute Attention → 3. Update Meaning" | Slide 17 |
| D3 | Scaling timeline: 4 boxes left-to-right getting progressively larger: Word2Vec (2013, small) → GloVe (2014) → BERT (2018, medium) → GPT-4 (2023, large). Arrow underneath: "Same idea, bigger models" | Slide 20 |

**Total TikZ elements: 7** (4 comics + 3 diagrams). All under 25-line budget.

## Slide Plan (25 slides)

### Front Matter (3 slides)
1. **Title page** — "From Words to Worlds: Embeddings in the Age of LLMs" / "How Computers Went from Reading Words to Understanding Language"
2. **XKCD Opening** — `images/1838_machine_learning.png` with framing: "How did we go from computers that can't read to ChatGPT?"
3. **Learning Objectives** — (1) Explain what word embeddings do and why they matter, (2) Identify the limit of static embeddings (polysemy), (3) Describe how LLMs use contextual embeddings to understand language

### Act 1: The Problem + Static Embeddings Work (5 slides)
4. **TikZ Comic C1: "Lost in Translation 2.0"** — Computers see characters, not meaning
5. **CHART: Word Embedding Space** (`01_word_embedding_space`) — "Word2Vec solved this: words become points, similar words are close!"
6. **CHART: Word Analogy** (`top10_08_word_analogy`) — "King - Man + Woman = Queen — embeddings capture meaning as math!"
7. **CHART: Similarity Heatmap** (`02_similarity_heatmap`) — "Dark = similar. The computer learned this from reading text alone."
8. **TikZ Comic C2: "The Dictionary Analogy"** — Static embeddings = dictionary: one definition per word, fixed forever

### Act 2: Going Deeper + The Limit (5 slides)
9. **CHART: Word Frequency** (`top10_11_word_frequency_rank`) — "Words follow Zipf's law. Embeddings learn from which words appear together. LLMs read EVERYTHING."
10. **CHART: Embedding Dimensions** (`top10_10_embedding_dimensions`) — "More dimensions = richer meaning. This shows 50. BERT uses 768. GPT-4 uses 12,000+."
11. **CHART: Context Window** (`top10_12_context_window`) — "Word2Vec sees a few neighbors. BERT sees the sentence. GPT-4 sees 128K words."
12. **CHART: Embedding PCA** (`top10_18_embedding_pca_variance`) — "Embeddings have structure: a few principal components capture most of the meaning."
13. **The Big Problem: One Word, Many Meanings** — "I deposited money at the bank" vs "I sat on the river bank". Word2Vec gives BOTH the same vector for "bank". That's wrong!

### Act 3: Contextual Embeddings → LLMs (5 slides)
14. **Transition** — "What if embeddings could CHANGE based on context? What if 'bank' near 'river' meant something different than 'bank' near 'money'?"
15. **TikZ Comic C3: "The Conversation"** — Same word in different contexts = different meaning. Contextual embeddings compute a NEW vector every time.
16. **TikZ Diagram D1: Self-Attention** — "Each word asks the other words: help me understand my meaning." Arrows show attention weights.
17. **TikZ Diagram D2: How Contextual Embeddings Work (3 Steps)** — "1. Read the surrounding words. 2. Compute attention (who's important?). 3. Update each word's meaning based on context."
18. **What Changed?** — Comparison table (5 rows): Static (one vector, small, 2013, same "bank" always, Word2Vec) vs Contextual (new vector each time, huge, 2018+, different "bank" per context, BERT/GPT).

**Note for implementer on slide 17**: The flowchart says "Read the surrounding words" rather than "Read ALL words at once" because GPT-style models read left-to-right (autoregressive), not all at once like BERT. Add a bottomnote: "BERT reads all words at once. GPT reads left-to-right. Both use attention to weigh which words matter most."

### Act 4: The LLM Revolution + Applications (4 slides)
19. **TikZ Diagram D3: The Scaling Timeline** — Word2Vec (2013) → GloVe (2014) → BERT (2018) → GPT-4 (2023), boxes getting larger. "Same idea, bigger models"
20. **What Can LLMs Do?** — 4 capabilities: generate text, answer questions, translate, reason. "All built on the same foundation: embeddings + attention."
21. **Finance in the LLM Era** — ChatGPT for report analysis, BERT for sentiment classification, GPT for document Q&A, embedding search for similar contracts. Block: "Every LLM application starts with embeddings."
22. **The Python Recipe** — Two columns:
    - Left (Classic): `from gensim.models import Word2Vec` / `model.wv.most_similar("bank")`
    - Right (Modern): `from openai import OpenAI` / `client.embeddings.create(input="bank loan", model="text-embedding-3-small")`

### Closing (3 slides)
23. **TikZ Comic C4: "From Dictionary to Conversation Partner"** — Resolution: static (book) → contextual (chatting robot)
24. **Key Takeaways** — 5 bullets: (1) Embeddings turn words into meaningful numbers, (2) Static embeddings give one vector per word — fast but miss context, (3) Contextual embeddings (BERT/GPT) compute new vectors based on surrounding words, (4) LLMs are contextual embeddings scaled to billions of parameters, (5) Every AI language tool — from search to ChatGPT — is built on embeddings
25. **XKCD Closing** — `images/2173_trained_a_neural_net.png`

**Total: 25 slides, 7 charts, 4 TikZ comics, 3 TikZ diagrams = 7 TikZ total, 0 formulas**

## Implementation Steps

| Step | Description | Files |
|------|-------------|-------|
| 1 | Create `L06c_embeddings_llm_simple.tex` with preamble from L06_embeddings_rl_simple.tex | `slides/L06_Embeddings_RL/L06c_embeddings_llm_simple.tex` |
| 2 | Write all 25 slides per plan above | same file |
| 3 | Compile and verify 0 errors, 0 Overfull | `L06c_embeddings_llm_simple.pdf` |
| 4 | Copy PDF to `docs/slides/pdf/`. In `docs/index.html`, add `<a class="ccard" href="slides/pdf/L06c_embeddings_llm_simple.pdf" download>` entry with title "LLM Visual Guide" and label "25-slide embeddings-to-LLMs" in the L06 `<div class="cgrid">` block | `docs/slides/pdf/`, `docs/index.html` |
| 5 | Update manifest.json (add `embeddings_llm_simple_slides` entry) | `manifest.json` |

## Verification
```bash
# L06c (25 slides: 24 content + 1 title → 24 bottomnotes)
grep -c "begin{frame" L06c_embeddings_llm_simple.tex           # 25 (22-28 range)
grep -c "chart.pdf" L06c_embeddings_llm_simple.tex             # 7
grep -c "bottomnote" L06c_embeddings_llm_simple.tex            # >= 24
grep -c '\$\$' L06c_embeddings_llm_simple.tex                  # 0
grep -c "begin{tikzpicture}" L06c_embeddings_llm_simple.tex    # >= 7
pdflatex -interaction=nonstopmode L06c_embeddings_llm_simple.tex
grep -c "Overfull" L06c_embeddings_llm_simple.log              # 0
```

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| LLM content has no existing charts | Covered by TikZ diagrams D1-D3 (within skill's TikZ budget) |
| Self-attention TikZ too complex | Keep to 3 word boxes + 3 arrows. Under 20 lines |
| "How LLMs Work" oversimplified | Acknowledge in bottomnote: "This is a 10,000-foot view. The math lives in L06_deepdive." |
| Encoder vs decoder confusion | Slide 17 bottomnote clarifies: BERT reads all at once, GPT reads left-to-right |
| 3 charts overlap with L06a | Intentional recap; 4 charts are unique to L06c; all comics are new |
| Bridging chart scale gap | Charts 5-6 include explicit framing text bridging Word2Vec scale to LLM scale |
| Both XKCD images already used in L06a/L06b | Different framing text; L06c asks "how did we get to ChatGPT?" |

---
PLAN_READY: .omc/plans/l06c-embeddings-llm-simple.md
