---
type: alp-concept
id: evaluation
title: Evaluating Your RAG Pipeline
prerequisites: [generation]
tags: [evaluation, metrics, testing]
---
"You can't improve what you can't measure." RAG evaluation has two halves:
retrieval quality and answer quality.

## Retrieval Metrics

- **Recall@k** — Is the right answer in the top-k retrieved chunks?
  The most important metric. If recall is low, nothing downstream works.
- **Precision@k** — Of the retrieved chunks, how many are relevant?
- **MRR (Mean Reciprocal Rank)** — Is the right chunk ranked first?

```python
def recall_at_k(retrieved_ids, relevant_id, k):
    return int(relevant_id in retrieved_ids[:k])
```

## Answer Metrics

- **Faithfulness** — Does the answer stay within the retrieved context?
  (Or does it hallucinate?)
- **Answer relevance** — Does it actually answer the question?
- **Citation accuracy** — Are the cited sources correct?

LLM-as-judge is the practical default:

```python
def judge_faithfulness(query, context, answer):
    prompt = f"""Does the answer stay strictly within the context?
CONTEXT: {context}
ANSWER: {answer}
Reply FAITHFUL or UNFAITHFUL with one-line reason."""
    ...
```

## Build a Golden Dataset (20-50 pairs)

1. Real queries from logs or domain experts
2. Ground-truth: which chunk(s) contain the answer
3. A reference answer written by a human

Then run your pipeline and score it:

```
Recall@5:   0.82
Precision@5: 0.60
Faithfulness: 0.91 / 1.0
```

## The A/B Loop

Every change (chunk size, alpha, reranker, prompt) must move a metric.
If it doesn't, revert it. This is how RAG becomes engineering instead
of vibes.

See `labs/01-build-full-pipeline.md` for the end-to-end build.
