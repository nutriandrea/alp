---
type: alp-concept
id: chunking
title: "Chunking: Splitting Documents Effectively"
prerequisites: [why-rag]
tags: [chunking, preprocessing]
---
Before retrieval, you must split documents into **chunks** — passages
small enough to embed meaningfully and retrieve precisely.

## The Tradeoff

| Chunk size | Pros | Cons |
|-----------|------|------|
| Too small (50 tokens) | Precise retrieval | Loses context, more chunks to scan |
| Too large (2000 tokens) | Rich context | Dilutes meaning, exceeds model context |
| **Sweet spot (~300-500)** | Balances both | Requires tuning per corpus |

## Chunking Strategies

### 1. Fixed-size with overlap

```python
def chunk_text(text, size=400, overlap=50):
    tokens = text.split()
    chunks = []
    for i in range(0, len(tokens), size - overlap):
        chunks.append(" ".join(tokens[i : i + size]))
    return chunks
```

Overlap preserves sentence boundaries and context across splits.

### 2. Recursive by structure (preferred)

Split on markdown headings, then paragraphs, then sentences — only
descending when a chunk is still too big:

```python
import re

def recursive_chunk(text, sizes=[["\n\n", 2000], ["\n", 800], [". ", 400]]):
    for sep, max_len in sizes:
        parts = text.split(sep)
        if all(len(p.split()) <= max_len for p in parts):
            return [p for p in parts if p.strip()]
    return [text]
```

### 3. Semantic chunking

Use embeddings to find natural topic boundaries. More accurate, more
expensive — use only when the two strategies above underperform.

## Rules of Thumb

1. Never split mid-sentence if you can avoid it
2. Keep the source reference in every chunk's metadata
3. Store `chunk_index` to reassemble order later
4. For code, chunk by function/class boundaries, not lines
