---
type: alp-concept
id: indexing
title: Building the Search Index
prerequisites: [encoding]
tags: [indexing, performance, python]
---
A search index is a matrix of embeddings: one row per document, one
column per dimension.

```python
import numpy as np

documents = [
    "New York's top-rated pizzerias",
    "Best coffee shops in Brooklyn",
    "Chicago deep dish pizza guide",
    "Los Angeles vegan restaurants",
]

# Encode all documents at once
doc_embeddings = model.encode(documents)
# Shape: (4, 384)  —  4 documents, 384 dimensions each
```

**For small corpora** (< 100K docs), you can brute-force search:
compute similarity against every document.

**For large corpora**, you need an **ANN (Approximate Nearest Neighbors)**
index like FAISS or Annoy.

```python
import faiss

dimension = 384
index = faiss.IndexFlatIP(dimension)  # Inner product = cosine similarity
index.add(doc_embeddings.astype("float32"))
```

Previous: [[encoding]] | Next: [[query-and-rank]]
