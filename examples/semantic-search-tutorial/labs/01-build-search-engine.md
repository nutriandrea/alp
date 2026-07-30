---
type: alp-lab
id: build-semantic-search
title: Build a Semantic Search Engine
concepts-covered: [encoding, indexing, query-and-rank]
verification:
  - Can search 50+ documents in under 1 second
  - Results ranked by semantic similarity (not keyword match)
  - Works with out-of-vocabulary queries (words not in any document)
prerequisites: [setup-environment]
---
## Objective

Build a semantic search engine over a collection of news headlines.

## Requirements

- Python 3.10+
- sentence-transformers
- numpy
- (optional) faiss-cpu for ANN index

## Task

1. **Load data**: Create a list of 50+ news headlines (any topic).
2. **Encode**: Embed all headlines using `all-MiniLM-L6-v2`.
3. **Search**: Implement `search(query, top_k=5)` using cosine similarity.
4. **Verify**:
   - Search for a concept not explicitly in any headline (e.g., "technology"
     should find headlines about AI, software, gadgets).
   - The most relevant results should appear at the top, not exact keyword matches.

## Hints

- [[encode-and-search]] for the basic pattern
- [[query-and-rank]] for the FAISS integration
- Use `[[glossary]]` if you forget a term
