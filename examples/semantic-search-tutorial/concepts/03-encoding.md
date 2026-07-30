---
type: alp-concept
id: encoding
title: Encoding Text with sentence-transformers
prerequisites: [embeddings]
tags: [encoding, sentence-transformers, python]
---
The `sentence-transformers` library turns text into embeddings with one
function call.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
embedding = model.encode("best pizza NYC")
# embedding is a numpy array of 384 floats
```

**Key properties:**
- `all-MiniLM-L6-v2` is a small, fast model (384 dimensions)
- One sentence takes ~5ms on CPU
- Larger models (like `all-mpnet-base-v2` with 768 dimensions) are more
  accurate but slower

The model outputs a normalized vector. You can measure similarity with
a dot product:

```python
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b)  # works because vectors are normalized
```

Previous: [[embeddings]] | Next: [[indexing]]
