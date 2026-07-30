# ALP — Agent Learning Protocol

**Learn what. Learn how. Learn progressively.**

ALP is an open standard for structured learning pathways that AI agents can
follow. Think of it as **MCP for learning**: just as MCP standardizes how
agents access **tools**, ALP standardizes how they learn **skills**.

```
┌──────────────────────────────────────────────────────────────┐
│   The Four Pillars of Agent-Native Content                   │
│                                                              │
│   Tools     MCP    │  How agents DO things                   │
│   Knowledge OKF    │  How agents KNOW things                 │
│   Behavior  Skills │  How agents ACT                         │
│   Learning  ALP    │  HOW AGENTS LEARN  ← YOU ARE HERE       │
└──────────────────────────────────────────────────────────────┘
```

## Why ALP?

Current standards cover tools (MCP), knowledge bases (OKF/Vaults), and
agent behaviours (Skills). But **none** cover learning pathways:

- How does an agent progress from beginner → expert in a domain?
- How does it know prerequisites before attempting a concept?
- How does it practice, verify, and consolidate what it learned?
- How does a YouTube tutorial become something an agent can study?

ALP fills this gap: a **progressive learning protocol** that any agent,
any LLM, any source format can use.

## Quick Start

```bash
# 1. Create an ALP vault from any text
cat transcript.txt | python tools/alp-extract --name my-tutorial

# 2. Navigate the syllabus
python tools/alp-learn --vault my-tutorial/

# 3. Study concept by concept
python tools/alp-learn --vault my-tutorial/ --concept 0
```

## How It Works

A **single directory of markdown files** with YAML frontmatter:

```
my-vault/
├── alp.md              # Syllabus: metadata + curriculum + prerequisites
├── concepts/           # Atomic knowledge chunks (load on demand)
├── practices/          # Executable exercises with verification
├── labs/               # Extended hands-on projects
├── cheatsheet.md       # Quick reference
└── glossary.md         # Terminology
```

An agent consuming ALP:

1. **Loads `alp.md`** — reads the syllabus (~200 tokens)
2. **Checks prerequisites** — navigates to pre-req vaults if needed
3. **Loads concepts in order** — one file at a time (~500–2K tokens each)
4. **Takes notes** — writes structured notes in its personal vault
5. **Practices** — runs exercises after relevant concepts
6. **Consolidates** — generates cheat sheets, summaries
7. **Verifies** — executes labs with verification criteria

## Key Design Principles

| Principle | Why |
|-----------|-----|
| **Simple** | Markdown + YAML. No SDK, no runtime, no dependencies |
| **Composable** | Vaults link via `[[wiki-links]]`; prerequisites chain across vaults |
| **Progressive** | Load syllabus first, concepts on demand. Context-efficient |
| **Universal** | Works with any agent, any LLM, any source (YouTube, blog, doc, lecture) |
| **Compatible** | Every ALP file is a valid [OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) file |

## The Origin Story

ALP was born from a gap analysis of the agent content ecosystem.
After mapping MCP (tools), OKF (knowledge), and Skills (behaviour),
we found **no standard for learning pathways** — the "fourth pillar".

The protocol evolved through three iterations:

| Version | Name | Insight |
|---------|------|---------|
| v0.0 | VKIF | Agent file format for knowledge transfer |
| v0.1 | TRAIL | Tree-structured agent learning pathways |
| **v0.2** | **ALP** | **Simple directory convention + OKF compatible** |

The full story is in [docs/origin.md](docs/origin.md).

## Tools

| Tool | Description |
|------|-------------|
| [`alp-extract`](tools/alp-extract) | Convert raw text/transcript → ALP vault |
| [`alp-learn`](tools/alp-learn) | Navigate an ALP vault (syllabus → concepts) |
| `alp-validate` | Validate ALP vault structure |

## Spec Status

**v0.1 — Experimental.** The spec is stable but expects iteration as
the ecosystem learns what works. See [spec/v0.1.md](spec/v0.1.md).

## Compatibility

ALP v0.1 is compatible with OKF v0.1. An ALP vault IS an OKF bundle.
See [docs/okf-profile.md](docs/okf-profile.md).

## Example

The [`examples/semantic-search-tutorial/`](examples/semantic-search-tutorial/)
directory is a complete ALP vault for building semantic search.

```bash
python tools/alp-learn --vault examples/semantic-search-tutorial/
```

## License

Apache 2.0. Free to use, implement, and extend.
