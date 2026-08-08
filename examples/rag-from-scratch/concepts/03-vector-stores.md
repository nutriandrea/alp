---
type: alp-concept
id: vector-stores
title: Vector Stores and Indexing
prerequisites: [chunking]
tags: [vector-store, indexing, embeddings]
---
Once text is chunked, each chunk becomes an **embedding vector**.
A vector store keeps those vectors indexed so retrieval is fast.

## You Don't Need a Vector Database

For learning and small corpora, an in-memory matrix + NumPy is enough:

```python
import numpy as np

class VectorStore:
    def __init__(self, dim=768):
        self.vectors = np.zeros((0, dim))
        self.chunks = []

    def add(self, chunk, vector):
        self.vectors = np.vstack([self.vectors, vector])
        self.chunks.append(chunk)

    def search(self, query_vec, top_k=5):
        scores = self.vectors @ query_vec
        idx = np.argsort(scores)[::-1][:top_k]
        return [(self.chunks[i], float(scores[i])) for i in idx]
```

## When to Upgrade to a Real Store

| Store | Best for | Why |
|-------|----------|-----|
| NumPy array | Learning, <100K chunks | Zero setup |
| FAISS | 1M+ vectors, CPU | Fast ANN search |
| Chroma / Qdrant | Persistence + metadata filters | Production-ish |
| pgvector | Already using Postgres | One system to rule them all |

## Index Types Matter

- **Exact (brute force)**: correct, O(n) per query. Fine for small data.
- **HNSW**: approximate, logarithmic. The default for most stores.
- **IVF**: cluster-based, fast but needs training on the data.

## Metadata: The Underrated Power

Store more than the vector:

```python
chunk_meta = {
    "text": "...",
    "source": "docs/api.md",
    "page": 42,
    "section": "Authentication",
    "updated_at": "2026-06-01",
}
```

Metadata enables filtered retrieval ("only from this repo", "only PDFs")
and makes citation output possible.
