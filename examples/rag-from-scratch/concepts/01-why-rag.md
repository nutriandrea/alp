---
type: alp-concept
id: why-rag
title: Why RAG? The Problem with Pure LLMs
prerequisites: []
tags: [rag, llm, fundamentals]
---
A pure LLM answers from its training data. It does not know:

- Your private documents
- Facts that changed after training
- The latest version of your API
- Your company's internal conventions

RAG (retrieval-augmented generation) fixes this by giving the model
**relevant context** at query time. Instead of asking the model to
"know" everything, you *retrieve* the right passages from your own
corpus and insert them into the prompt.

## The Core Loop

```
Query ──► Retrieve relevant passages ──► Insert into prompt ──► Generate
              │                                      │
              ▼                                      ▼
         Your corpus                          LLM with context
```

## Why This Matters

| Problem | Pure LLM | RAG |
|---------|----------|-----|
| Private docs | Hallucinates or says "I don't know" | Grounds answers in real passages |
| Stale knowledge | Trained months ago | Retrieves fresh content |
| Citations | None | Can point to source passages |
| Cost | Retrain for every update | Just update the index |

**Key insight**: RAG is not a library — it's a pattern. You can build a
working version with NumPy and the OpenAI API. That's what this vault teaches.
