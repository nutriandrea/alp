---
type: alp-glossary
---

- **RAG** — Retrieval-Augmented Generation. Giving an LLM relevant context
  at query time instead of relying on training data.
- **Chunk** — A passage of text (typically 300-500 tokens) that is embedded
  and retrieved as a unit.
- **Embedding** — A dense vector representing the meaning of a text.
  Similar meanings → nearby vectors.
- **Vector store** — An index of embeddings enabling fast similarity search.
- **BM25** — A classic keyword ranking algorithm (the modern TF-IDF).
- **Hybrid retrieval** — Combining vector + keyword signals with a weight `alpha`.
- **Cross-encoder** — A model that jointly encodes query + chunk for precise
  relevance scoring. Slower but more accurate than dot product.
- **Recall@k** — Fraction of questions where the right answer is in the
  top-k retrieved chunks.
- **Faithfulness** — Whether the generated answer stays within the retrieved
  context (doesn't hallucinate).
- **LLM-as-judge** — Using an LLM to score answer quality, e.g. faithfulness.
