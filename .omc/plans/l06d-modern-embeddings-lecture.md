# Plan: Modern Embeddings in Practice -- Visual Guide

## Task
Create `L06d_modern_embeddings_simple.tex` -- a short (~10 slides) formula-free visual lecture about **embeddings as used TODAY** (Hugging Face, sentence-transformers, RAG, vector databases). This is a practical "how to use modern embeddings" guide, NOT an evolution story (that is L06c) and NOT a Word2Vec primer (that is L06a).

## Relationship to Other L06 Lectures

| Lecture | Focus | Overlap with L06d |
|---------|-------|--------------------|
| L06a (16 slides) | Word2Vec/GloVe basics, word-level embeddings, gensim | NONE -- L06d assumes L06a knowledge, does not repeat it |
| L06c (25 slides) | Word2Vec-to-BERT-to-GPT evolution story | NONE -- L06d is practical TODAY, not historical |
| L06d (10 slides) | Modern embedding tools: sentence-transformers, RAG, vector DBs | THIS plan |

**Key differentiator**: L06a/L06c explain WHAT embeddings are. L06d shows HOW practitioners use them TODAY.

## Requirements
1. ~10 slides (short, focused)
2. Zero formulas: no `$$` display math
3. 2 TikZ comics minimum (opening problem + closing), max 25 lines each
4. Course standards: Madrid theme, 8pt, 16:9, `\bottomnote{}` on every content slide, XKCD bookends
5. Preamble: copy lines 1-107 from L06a_embeddings_simple.tex (identical across all L06 variants)
6. File: `slides/L06_Embeddings_RL/L06d_modern_embeddings_simple.tex`
7. 1-2 new charts acceptable if needed; reuse existing where possible

## Acceptance Criteria
- [ ] AC1: .tex compiles with 0 errors, 0 Overfull warnings
- [ ] AC2: 10-12 slides total (frame count)
- [ ] AC3: At least 2 TikZ comics (stick figures, max 25 lines each)
- [ ] AC4: Zero `$$` display math anywhere in file
- [ ] AC5: `\bottomnote{}` on every content slide (all frames except title)
- [ ] AC6: XKCD bookends (opening slide 2 + closing slide 11)
- [ ] AC7: Covers: sentence embeddings, sentence-transformers library, cosine similarity for search, RAG pipeline, vector databases, model selection
- [ ] AC8: Real Python code with `from sentence_transformers import SentenceTransformer`
- [ ] AC9: No overlap with L06a (Word2Vec/GloVe) or L06c (evolution story)

## Chart Allocation

### Existing Charts to Reuse: 1

| # | Chart Path | Why |
|---|-----------|-----|
| 1 | `02_similarity_heatmap/chart.pdf` | Cosine similarity is THE core operation in modern embedding search. Reused with new framing text about semantic search, not word similarity. |

Note: `01_word_embedding_space` and `top10_13_embedding_neighbors` are already in L06a and are word-level -- they do not fit L06d's sentence-level focus.

### New Charts to Create: 1

| # | Folder Name | Description | Why New |
|---|-------------|-------------|---------|
| 1 | `14_rag_pipeline_flow` | Horizontal flowchart showing the RAG pipeline: Documents -> Chunk -> Embed -> Store in Vector DB -> Query arrives -> Embed query -> Retrieve top-K -> Feed to LLM -> Answer. Use ML color palette, box-and-arrow style, 5 steps. | No existing chart covers RAG. This is the central concept of the lecture. |

**Chart 14 specification:**
- figsize=(10, 6), dpi=150, ML color palette
- Style: rounded boxes connected by arrows, left-to-right flow
- 5 labeled boxes: "Documents" -> "Chunk + Embed" -> "Vector DB" -> "Retrieve" -> "LLM Answer"
- Each box has a 1-line subtitle (e.g., "Split text into paragraphs", "sentence-transformers", "FAISS / ChromaDB", "Top-K nearest", "GPT generates answer")
- Clean, no clutter, large readable fonts

## TikZ Comics (2 comics + 1 diagram = 3 TikZ total)

| # | Slide | Title | Description |
|---|-------|-------|-------------|
| C1 | 3 | "So Many Documents!" | Stick figure at desk, overwhelmed by stack of document rectangles (3-4 stacked). Speech bubble: "How do I find the RIGHT one?" Sets up the search/retrieval problem that modern embeddings solve. |
| C2 | 9 | "The Smart Librarian" | Stick figure (librarian) with a small robot assistant. User asks question. Robot points to correct document on shelf. Speech bubble: "Found it! This paragraph answers your question." Resolution: embeddings + RAG = smart retrieval. |

| # | Slide | Title | Description |
|---|-------|-------|-------------|
| D1 | 6 | "Sentence vs Word Embedding" | Left side: 3 individual word boxes ("New", "York", "City") each with own arrow to different points. Right side: one long box "New York City" with single arrow to one point. Caption: "Word embeddings: 3 separate vectors. Sentence embeddings: 1 vector for the whole meaning." |

## Slide-by-Slide Plan (10 slides)

### Slide 1: Title Page
```
\title[L06d: Modern Embeddings]{Modern Embeddings: A Practical Guide}
\subtitle{How to Use Embeddings in 2025 with Hugging Face, RAG, and Vector Databases}
```

### Slide 2: XKCD Opening
- Image: `images/1838_machine_learning.png`
- Framing: "You already know what embeddings are (L06a). Now: how do practitioners actually USE them today?"
- `\bottomnote{XKCD #1838 by Randall Munroe (CC BY-NC 2.5)}`

### Slide 3: TikZ Comic C1 -- "So Many Documents!"
- Stick figure overwhelmed by documents
- Sets up the practical problem: given thousands of documents, how do you find the answer to a question?
- Text below: "Modern embeddings solve this: they let you SEARCH by meaning, not keywords."
- `\bottomnote{Keyword search fails when the user says "revenue" but the document says "income".}`

### Slide 4: From Words to Sentences
- Two columns:
  - Left: **Word Embeddings (L06a)**: one vector per word, "bank" always the same, Word2Vec/GloVe
  - Right: **Sentence Embeddings (Today)**: one vector per sentence/paragraph, captures full meaning, sentence-transformers
- Block: "Modern applications embed SENTENCES, not individual words."
- `\bottomnote{sentence-transformers is the most popular library: 100M+ downloads on Hugging Face.}`

### Slide 5: The Key Players
- Compact list of today's embedding ecosystem:
  - **Open source**: sentence-transformers (all-MiniLM-L6-v2, all-mpnet-base-v2)
  - **API-based**: OpenAI (text-embedding-3-small), Cohere (embed-v3), Voyage AI
  - **Leaderboard**: MTEB on Hugging Face ranks hundreds of models
- `\bottomnote{Tip: start with all-MiniLM-L6-v2 (free, fast, good). Upgrade to API models if you need top accuracy.}`

### Slide 6: TikZ Diagram D1 -- Sentence vs Word Embedding
- Visual comparison: 3 separate word vectors vs 1 sentence vector
- Text: "Sentence embeddings understand that 'New York City' is one concept, not three unrelated words."
- `\bottomnote{Technical detail: sentence-transformers use mean pooling over token embeddings from a transformer model.}`

### Slide 7: CHART -- Similarity Heatmap (reused)
- Chart: `02_similarity_heatmap/chart.pdf`
- New framing for L06d: "This is the core operation behind semantic search. Compute cosine similarity between your query embedding and every document embedding. The darkest match wins."
- `\bottomnote{Cosine similarity ranges from -1 (opposite) to +1 (identical). In practice, scores above 0.7 are strong matches.}`

### Slide 8: NEW CHART -- RAG Pipeline
- Chart: `14_rag_pipeline_flow/chart.pdf`
- Text above: "RAG = Retrieval-Augmented Generation: the #1 pattern for using embeddings with LLMs."
- Brief description of each step (2-3 bullet points)
- `\bottomnote{RAG lets an LLM answer questions about YOUR documents without retraining. Used at JPMorgan, Bloomberg, every major bank.}`

### Slide 9: TikZ Comic C2 -- "The Smart Librarian"
- Resolution comic: embeddings + RAG = smart document retrieval
- 3 key takeaways as numbered list:
  1. Embed your documents once, store vectors in a database (FAISS, ChromaDB, Pinecone)
  2. When a question arrives, embed it and find the nearest documents
  3. Feed those documents to an LLM for a precise answer
- `\bottomnote{Vector databases: FAISS (Meta, free), ChromaDB (open source), Pinecone (cloud). All work with sentence-transformers.}`

### Slide 10: Try It Yourself -- Python Code
- Verbatim code block (6-8 lines):
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")

docs = ["Annual revenue rose 12%", "Q3 losses exceeded forecast"]
query = "How did the company perform financially?"

doc_embeddings = model.encode(docs)
query_embedding = model.encode(query)
# Use cosine similarity to find the best match!
```
- `\bottomnote{pip install sentence-transformers. Free, runs locally, no API key needed. Hugging Face Hub has 5000+ embedding models.}`

### Slide 11: XKCD Closing
- Image: `images/2173_trained_a_neural_net.png`
- `\bottomnote{XKCD #2173 by Randall Munroe (CC BY-NC 2.5). Next: try the RAG notebook with real financial filings!}`

**Total: 11 slides, 1 reused chart, 1 new chart, 2 TikZ comics, 1 TikZ diagram = 3 TikZ total, 0 formulas**

## Implementation Steps

| Step | Description | Files | Depends On |
|------|-------------|-------|------------|
| 1 | Create new chart `14_rag_pipeline_flow/chart.py` | `slides/L06_Embeddings_RL/14_rag_pipeline_flow/chart.py` | -- |
| 2 | Run chart.py to generate chart.pdf | `14_rag_pipeline_flow/chart.pdf` | Step 1 |
| 3 | Create `L06d_modern_embeddings_simple.tex` with full preamble (lines 1-107 from L06a) and all 11 slides per plan | `slides/L06_Embeddings_RL/L06d_modern_embeddings_simple.tex` | Step 2 |
| 4 | Compile with pdflatex, verify 0 errors + 0 Overfull | `L06d_modern_embeddings_simple.pdf` | Step 3 |
| 5 | Update manifest.json: add `modern_embeddings_simple_slides` entry under L06 | `manifest.json` | Step 4 |

## Verification Commands

```bash
cd slides/L06_Embeddings_RL

# Chart builds
python 14_rag_pipeline_flow/chart.py

# Slide counts
grep -c "begin{frame" L06d_modern_embeddings_simple.tex          # expect: 11 (10-12 range)
grep -c "chart.pdf" L06d_modern_embeddings_simple.tex            # expect: 2
grep -c "bottomnote" L06d_modern_embeddings_simple.tex           # expect: >= 10
grep -c "begin{tikzpicture}" L06d_modern_embeddings_simple.tex   # expect: >= 3

# Zero formulas
grep -c '\$\$' L06d_modern_embeddings_simple.tex                 # expect: 0

# Compilation
pdflatex -interaction=nonstopmode L06d_modern_embeddings_simple.tex
grep -c "Overfull" L06d_modern_embeddings_simple.log             # expect: 0
grep -c "Error" L06d_modern_embeddings_simple.log                # expect: 0
```

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| RAG pipeline chart too complex for single figure | Keep to 5 boxes max, horizontal flow, large font. No sub-diagrams. |
| Verbatim code block causes Overfull | Use `\footnotesize` or `\scriptsize` for code. Keep lines under 60 characters. |
| Overlap with L06a on cosine similarity | Different framing: L06a shows word similarity, L06d frames it as semantic search engine. Different surrounding text. |
| Overlap with L06c on BERT/GPT | L06d mentions them only as "the models behind sentence-transformers", never explains how they work. L06c owns the explanation. |
| TikZ comics exceed 25-line budget | Both comics are simple: stick figure + rectangles + speech bubble. Pre-constrained to 15-20 lines each. |
| "sentence-transformers" library name may change | Use current name (stable since 2019). Bottomnote mentions Hugging Face Hub as alternative. |
| Students confused about word vs sentence embeddings | Slide 4 + TikZ D1 (slide 6) both address this explicitly with visual comparison. |

---
PLAN_READY: .omc/plans/l06d-modern-embeddings-lecture.md
