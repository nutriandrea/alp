---
type: alp-practice
id: chunk-and-embed
title: Chunk a Document and Build an Index
concepts-covered: [chunking, vector-stores]
---
## Steps

1. Create `rag_demo.py`:

   ```python
   import numpy as np

   def chunk_text(text, size=400, overlap=50):
       tokens = text.split()
       chunks = []
       for i in range(0, len(tokens), size - overlap):
           chunks.append(" ".join(tokens[i : i + size]))
       return chunks

   class VectorStore:
       def __init__(self, dim=384):
           self.vectors = np.zeros((0, dim))
           self.chunks = []

       def add(self, chunk, vector):
           self.vectors = np.vstack([self.vectors, vector])
           self.chunks.append(chunk)

       def search(self, query_vec, top_k=3):
           scores = self.vectors @ query_vec
           idx = np.argsort(scores)[::-1][:top_k]
           return [(self.chunks[i], float(scores[i])) for i in idx]

   # Build a tiny corpus
   corpus = (
       "RAG retrieves relevant passages before generating an answer. "
       "Chunking splits documents into embeddable passages. "
       "Embeddings represent meaning as vectors in high-dimensional space. "
       "Vector stores index embeddings for fast retrieval. "
       "Hybrid search combines semantic and keyword signals. "
       "Cross-encoders rerank candidates for higher precision. "
   ) * 5  # repeat to create a searchable corpus

   chunks = chunk_text(corpus, size=30, overlap=5)
   print(f"Created {len(chunks)} chunks")

   # Simulate embeddings with a hashing trick (real systems use a real model)
   rng = np.random.default_rng(42)
   vectors = rng.normal(size=(len(chunks), 384))
   store = VectorStore()
   for c, v in zip(chunks, vectors):
       store.add(c, v)

   print(f"Indexed {len(store.chunks)} chunks in vector store")
   ```

2. Run it:
   ```bash
   python rag_demo.py
   ```

## Expected Output
```
Created N chunks
Indexed N chunks in vector store
```

## Hint
- [[chunking]] for the split strategy
- [[vector-stores]] for the index design
- The real embedding step (concept 3 of the semantic-search vault)
  replaces the `rng.normal` placeholder.
