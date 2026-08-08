---
type: alp-vault
alp-version: 0.1
name: rag-from-scratch
version: 1.0.0
description: Build a retrieval-augmented generation (RAG) pipeline from first principles — chunking, embeddings, retrieval, and generation.
author: alp-spec
source: https://github.com/nutriandrea/alp
source-type: doc
prerequisites:
  - alp:python-basics
  - alp:semantic-search-tutorial
curriculum:
  - id: why-rag
    title: Why RAG? The Problem with Pure LLMs
    path: concepts/01-why-rag.md
  - id: chunking
    title: "Chunking: Splitting Documents Effectively"
    path: concepts/02-chunking.md
  - id: vector-stores
    title: Vector Stores and Indexing
    path: concepts/03-vector-stores.md
  - id: retrieval
    title: Retrieval Strategies That Actually Work
    path: concepts/04-retrieval.md
  - id: generation
    title: Generating Answers from Retrieved Context
    path: concepts/05-generation.md
  - id: evaluation
    title: Evaluating Your RAG Pipeline
    path: concepts/06-evaluation.md
tags: [rag, llm, retrieval, embeddings, ai, python]
---

# RAG from Scratch

A complete, first-principles guide to retrieval-augmented generation.

Start with `alp-learn --vault examples/rag-from-scratch/` and work
concept by concept. Each concept is self-contained and load-on-demand.

Full curriculum (6 concepts):
1. Why RAG? The Problem with Pure LLMs
2. Chunking: Splitting Documents Effectively
3. Vector Stores and Indexing
4. Retrieval Strategies That Actually Work
5. Generating Answers from Retrieved Context
6. Evaluating Your RAG Pipeline

Recommended labs: `labs/01-build-full-pipeline.md`
