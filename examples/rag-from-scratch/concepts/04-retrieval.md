---
type: alp-concept
id: retrieval
title: Retrieval Strategies That Actually Work
prerequisites: [vector-stores]
tags: [retrieval, ranking, hybrid-search]
---
Embedding similarity alone is rarely enough. The best RAG systems use
**hybrid retrieval** — combining semantic and keyword signals.

## Strategy 1: Pure Vector (baseline)

```python
def retrieve(query_vec, store, top_k=5):
    results = store.search(query_vec, top_k)
    return results
```
Fast, works for synonyms and paraphrases. Fails on exact identifiers
(e.g., `API_KEY`, `v2.3.1`) where exact match matters.

## Strategy 2: Hybrid (vector + BM25)

```python
from rank_bm25 import BM25Okapi

# Build once
bm25 = BM25Okapi([chunk.split() for chunk in store.chunks])

def hybrid_search(query, query_vec, store, alpha=0.5, top_k=5):
    vec_scores = dict(store.search(query_vec, top_k * 3))
    bm_scores = dict(zip(store.chunks, bm25.get_scores(query.split())))

    combined = []
    for chunk in vec_scores:
        combined.append((chunk, alpha * vec_scores[chunk] + (1 - alpha) * bm_scores.get(chunk, 0)))

    combined.sort(key=lambda x: x[1], reverse=True)
    return combined[:top_k]
```

`alpha` balances the two signals. Tune it on your evaluation set.

## Strategy 3: Reranking

Retrieve 20-50 candidates, then rerank with a cross-encoder:

```python
from sentence_transformers import CrossEncoder

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
pairs = [(query, chunk) for chunk, _ in candidates]
scores = reranker.predict(pairs)  # far more accurate than dot product
```

Cross-encoders jointly attend to query+chunk — slow but much more precise.
This is the single highest-leverage improvement for retrieval quality.

## Strategy 4: Query expansion

Expand the query before searching:

- Generate 2-3 paraphrases with an LLM, search each, merge results
- Add synonyms ("car" → "automobile, vehicle, sedan")

## Common Failure Modes

| Symptom | Fix |
|---------|-----|
| Retrieves topically similar but useless chunks | Rerank with cross-encoder |
| Misses exact code/version strings | Add BM25 keyword path |
| Everything scores ~equal | Increase `top_k`, then rerank |
| Stale results | Rebuild index on document change |

**Key insight**: Retrieval quality is 80% of RAG quality. Nail this before
touching prompts.
