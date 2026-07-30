---
type: alp-concept
id: query-and-rank
title: Query & Rank Results
prerequisites: [indexing]
tags: [query, ranking, python]
---
Search = encode the query + find the nearest embeddings + return results.

```python
def search(query, model, index, documents, top_k=3):
    # 1. Encode the query
    query_vec = model.encode([query])

    # 2. Search the index
    scores, indices = index.search(query_vec.astype("float32"), top_k)

    # 3. Return results
    results = []
    for score, idx in zip(scores[0], indices[0]):
        results.append({
            "text": documents[idx],
            "score": float(score),
        })
    return results

# Try it
results = search("pizza places", model, index, documents)
for r in results:
    print(f"{r['score']:.3f}  {r['text']}")
# 0.892  New York's top-rated pizzerias
# 0.756  Chicago deep dish pizza guide
# 0.423  Best coffee shops in Brooklyn
```

The results are ordered by similarity score. This is the core of
semantic search — everything else (filters, caching, hybrid search)
builds on this foundation.

Previous: [[indexing]]
