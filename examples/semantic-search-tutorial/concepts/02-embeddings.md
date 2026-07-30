---
type: alp-concept
id: embeddings
title: Understanding Embeddings
prerequisites: [what-is-semantic-search]
tags: [embeddings, vectors, fundamentals]
---
An **embedding** is a dense vector of floating-point numbers that
represents the *meaning* of a piece of text.

A good embedding places similar meanings close together in vector
space:

- "king" and "queen" have similar embeddings
- "king" and "potato" have very different embeddings

Semantic search uses this property: encode a query, encode documents,
find the closest vectors.

```
query: "best pizza NYC"
  → [0.23, 0.87, -0.12, ..., 0.45]   (1536 numbers)

doc: "New York's top-rated pizzerias"
  → [0.25, 0.85, -0.10, ..., 0.48]   (similar!)
```

The distance between two embeddings is measured with **cosine similarity**.
Values near 1.0 mean very similar; near -1.0 mean very different.

Next: [[encoding]]
