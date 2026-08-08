---
type: alp-concept
id: generation
title: Generating Answers from Retrieved Context
prerequisites: [retrieval]
tags: [generation, prompting, llm]
---
Retrieval gives you context. Generation turns it into an answer. The
prompt structure is the difference between a chatbot and a RAG system.

## The Base Template

```python
def build_prompt(query, retrieved, instructions=""):
    context = "\n\n".join(
        f"[Source: {meta['source']}]\n{chunk}" for chunk, meta in retrieved
    )
    return f"""You are a precise assistant. Answer using ONLY the context below.
If the answer is not in the context, say "I don't know" — do not guess.

CONTEXT:
{context}

QUESTION: {query}

ANSWER:"""
```

## Rules That Matter

1. **Force grounded answers** — "If not in context, say you don't know."
   This single line kills most hallucinations.
2. **Cap context** — 4-8 chunks ≈ 2-4K tokens. More is not better; it
   dilutes attention and adds latency.
3. **Order matters** — Put the most relevant chunk first (models attend
   more to the beginning and end).
4. **Include source pointers** — `[Source: docs/api.md]` enables
   citations and trust.

## Advanced: Streaming with Sources

```python
def stream_answer(query, retrieved):
    prompt = build_prompt(query, retrieved)
    stream = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    for event in stream:
        yield event.choices[0].delta.content or ""
```

## When the Context Is Insufficient

| Situation | Strategy |
|-----------|----------|
| Top-5 chunks don't answer | Retrieve more, rerank, then regenerate |
| Query has multiple intents | Sub-query, retrieve per intent, merge |
| No chunk is relevant | Explicitly refuse instead of forcing an answer |

## The Feedback Loop

Store every (query, retrieved, answer, user_feedback) tuple. That data is
your evaluation set for [[evaluation]] — and it's the only way to know
whether retrieval changes actually help.
