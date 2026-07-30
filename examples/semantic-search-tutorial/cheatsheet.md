---
type: alp-cheatsheet
---

## Commands

| Action | Command |
|--------|---------|
| Install | `pip install sentence-transformers numpy faiss-cpu` |
| Load model | `SentenceTransformer("all-MiniLM-L6-v2")` |
| Encode one | `model.encode("text")` |
| Encode many | `model.encode(["a", "b", "c"])` |
| Similarity | `np.dot(query_emb, doc_embs.T)` |
| FAISS index | `faiss.IndexFlatIP(dim)` then `index.add(emb)`, `index.search(q, k)` |
| Top-k indices | `np.argsort(scores)[::-1][:k]` |

## Models

| Model | Dims | Speed | Accuracy |
|-------|------|-------|----------|
| all-MiniLM-L6-v2 | 384 | fastest | good |
| all-mpnet-base-v2 | 768 | medium | best |
| text-embedding-3-small | 1536 | API | best (OpenAI) |
