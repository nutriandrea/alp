---
type: alp-lab
id: build-full-pipeline
title: Build a Complete RAG Pipeline with Real Data
concepts-covered: [chunking, vector-stores, retrieval, generation, evaluation]
verification:
  - Retrieves the correct passage for 8/10 golden questions (Recall@5 ≥ 0.8)
  - Answers stay within the retrieved context (Faithfulness ≥ 0.9)
  - Pipeline runs end-to-end on a 10+ page document in under 10 seconds
prerequisites: [chunk-and-embed]
---
## Objective

Build a working RAG system over a real document — the ALP specification
(`spec/v0.1.md`) or any 10+ page public document you choose.

## Requirements

- Python 3.10+
- `sentence-transformers` for real embeddings
- An LLM API key (OpenAI or compatible) for generation
- `rank-bm25` for the keyword path

## Task

1. **Ingest**: Read the document, split into chunks (recursive strategy).
2. **Embed**: Encode all chunks with `all-MiniLM-L6-v2` (or better).
3. **Index**: Build a vector store + BM25 index with metadata per chunk.
4. **Retrieve**: Implement hybrid search + optional cross-encoder rerank.
5. **Generate**: Build the grounded prompt from [[generation]], stream the answer.
6. **Evaluate**:
   - Write 10 golden questions with known-answer passages
   - Score Recall@5, Precision@5, Faithfulness
   - Log every (query, retrieved, answer) pair to `eval_log.jsonl`

## Verify

- [ ] Recall@5 ≥ 0.8 on your golden set
- [ ] Answers include a `[Source: ...]` pointer when grounded
- [ ] The system says "I don't know" on out-of-scope questions
- [ ] You can name the single change that most improved your metrics

## Hints

- [[chunking]] for split strategy
- [[vector-stores]] for index + metadata
- [[retrieval]] for hybrid + rerank
- [[generation]] for the prompt template
- [[evaluation]] for scoring and the A/B loop
