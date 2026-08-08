---
type: alp-practice
id: hybrid-retrieval
title: Combine Vector and Keyword Retrieval
concepts-covered: [retrieval]
---
## Steps

1. Install the BM25 ranker:
   ```bash
   pip install rank-bm25
   ```

2. Extend your `rag_demo.py` from the previous practice:

   ```python
   from rank_bm25 import BM25Okapi

   # Build BM25 index over the same chunks
   bm25 = BM25Okapi([c.split() for c in chunks])

   def hybrid_search(query, query_vec, alpha=0.5, top_k=3):
       # vector scores
       vec_results = store.search(query_vec, top_k * 2)
       vec_scores = {c: s for c, s in vec_results}
       # keyword scores
       kw_scores = dict(zip(chunks, bm25.get_scores(query.split())))

       combined = []
       for c in chunks:
           vs = vec_scores.get(c, 0)
           ks = kw_scores.get(c, 0)
           combined.append((c, alpha * vs + (1 - alpha) * ks))

       combined.sort(key=lambda x: x[1], reverse=True)
       return combined[:top_k]

   query = "passages retrieval vector"
   query_vec = rng.normal(size=384)
   for c, s in hybrid_search(query, query_vec):
       print(f"{s:8.3f}  {c[:60]}")
   ```

3. Run it and compare against pure-vector retrieval (concept 4).

## Expected Output
A ranked list of chunks where keyword hits surface alongside
semantic matches — try queries with and without a term that appears
literally in the corpus to see the difference.

## Hint
- [[retrieval]] for the hybrid rationale and alpha tuning
