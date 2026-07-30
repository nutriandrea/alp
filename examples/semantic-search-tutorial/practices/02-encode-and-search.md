---
type: alp-practice
id: encode-and-search
title: Encode Documents and Search
concepts-covered: [encoding, indexing, query-and-rank]
---
## Steps

1. Create a file `search_demo.py`:

   ```python
   from sentence_transformers import SentenceTransformer
   import numpy as np

   model = SentenceTransformer("all-MiniLM-L6-v2")

   corpus = [
       "Python is a programming language",
       "JavaScript runs in the browser",
       "Rust is a systems programming language",
       "TypeScript adds types to JavaScript",
       "Go is designed at Google",
   ]

   docs_emb = model.encode(corpus)
   query_emb = model.encode(["typed language"])

   scores = np.dot(docs_emb, query_emb.T).flatten()
   top_k = np.argsort(scores)[::-1][:3]

   for idx in top_k:
       print(f"{scores[idx]:.3f}  {corpus[idx]}")
   ```

2. Run it:
   ```bash
   python search_demo.py
   ```

## Expected Output
Expected "TypeScript adds types to JavaScript" as the top result.
