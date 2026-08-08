---
type: alp-cheatsheet
---

## RAG Pipeline (5 steps)

```
Query → Chunk → Embed → Retrieve → Generate → Evaluate
```

## Chunking

| Strategy | When | Sizes |
|----------|------|-------|
| Fixed + overlap | Quick start | ~400 tok, overlap 50 |
| Recursive by structure | Default | `\n\n` → `\n` → `. ` |
| Semantic | Hard corpora | Model-based boundaries |

## Retrieval Formula

```python
combined = alpha * vector_score + (1 - alpha) * bm25_score
# then rerank top-20 with a cross-encoder
```

## Prompt Essentials

- "Answer using ONLY the context below"
- "If not in context, say I don't know"
- 4-8 chunks max, most relevant first
- `[Source: ...]` on every chunk

## Metrics to Track

| Metric | What it measures | Target |
|--------|------------------|--------|
| Recall@5 | Right chunk in top-5 | ≥ 0.8 |
| Precision@5 | Retrieved chunks relevant | ≥ 0.6 |
| Faithfulness | Answer grounded in context | ≥ 0.9 |

## Golden Rule

Change one thing → measure → keep it only if a metric improves.
