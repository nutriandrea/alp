<p align="center">
  <img src="https://img.shields.io/badge/status-experimental-orange" alt="Status">
  <img src="https://img.shields.io/badge/spec-v0.2-blueviolet" alt="Spec">
  <img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="License">
  <img src="https://img.shields.io/github/stars/nutriandrea/alp?style=social" alt="Stars">
</p>

<h1 align="center">⛰️ ALP — Agent Learning Protocol</h1>
<p align="center"><b>MCP for learning.</b> An open standard for structured learning pathways that AI agents can follow.</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> •
  <a href="#how-it-works">How It Works</a> •
  <a href="spec/v0.1.md">Spec</a> •
  <a href="docs/origin.md">Origin Story</a> •
  <a href="ROADMAP.md">Roadmap</a>
</p>

---

## Why ALP?

MCP gave agents **tools**. OKF gave them **knowledge**. Skills gave them
**behaviour**. But nothing gives them a **curriculum**.

```
╔══════════════════════════════════════════════════════════╗
║           The Four Pillars of Agent Content              ║
╠════════════╦══════════╦══════════╦═══════════════════════╣
║   MCP      ║   OKF    ║  Skills  ║   ALP                 ║
║  Tools     ║ Knowledge║ Behaviour║   LEARNING            ║
║   DO       ║   KNOW   ║   ACT    ║   LEARN               ║
╚════════════╩══════════╩══════════╩═══════════════════════╝
```

Current standards cover tools, knowledge bases, and agent behaviours.
**None** cover learning pathways — how an agent progresses from beginner
to expert, practices, verifies, and consolidates what it learned.

## Quick Start

```bash
# Install
pip install alp-tools

# Try it with the built-in example
alp-learn --vault examples/semantic-search-tutorial/

# Create a vault from any text
cat transcript.txt | alp-extract --name my-tutorial

# Study concept by concept
alp-learn --vault my-tutorial/ --concept 0
```

*Or run without install: `pip install pyyaml && python alp_tools/learn.py ...`*

---

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

### Agent Learning Loop

| Step | What the agent does | Context cost |
|------|-------------------|--------------|
| 1. Load syllabus | Read `alp.md` metadata + curriculum | ~200 tokens |
| 2. Check prerequisites | Navigate to pre-req vaults if unmet | ~100 tokens |
| 3. Load concept | Read one concept file | ~500–2K tokens |
| 4. Take notes | Write structured notes in personal vault | ~200 tokens |
| 5. Practice | Load and execute practice guide | ~300–1K tokens |
| 6. Consolidate | Generate cheat sheet, summary | ~200 tokens |
| 7. Verify | Execute lab, check verification criteria | ~500 tokens |

**Key insight**: An agent never loads more than 2–3 concepts at a time,
keeping the learning path under ~5K context tokens.

### Vault Composition

- **`concepts/`** — Atomic knowledge chunks. One idea per file.
  [`what-is-semantic-search.md`](examples/semantic-search-tutorial/concepts/01-what-is-semantic-search.md)
- **`practices/`** — Executable exercises. Install, configure, verify.
  [`setup.md`](examples/semantic-search-tutorial/practices/01-setup.md)
- **`labs/`** — Extended projects with verification criteria.
  [`build-search-engine.md`](examples/semantic-search-tutorial/labs/01-build-search-engine.md)
- **`cheatsheet.md`** — Quick reference for recall.
- **`glossary.md`** — Key terms and definitions.

### Linking

Vaults connect using `[[wiki-links]]`:

```
[[what-is-semantic-search]]          ← same vault
[[alp:python-basics/concepts/01]]    ← another vault
[[practices/01-setup]]               ← practice guide
```

---

## Design Principles

| Principle | Why |
|-----------|-----|
| **Simple** | Markdown + YAML. No SDK, no runtime. |
| **Composable** | Vaults link via `[[wiki-links]]`; prerequisites chain across vaults. |
| **Progressive** | Load syllabus first, concepts on demand. Context-efficient. |
| **Universal** | Works with any agent, any LLM, any source format. |
| **Compatible** | Every ALP file is a valid [OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) file. |

---

## Tools

| Tool | Description | Usage |
|------|-------------|-------|
| `alp-extract` | Convert raw text → ALP vault | `cat text \| alp-extract --name my-vault` |
| `alp-learn` | Navigate vault syllabus + concepts | `alp-learn --vault path/ --concept 0` |
| `alp-validate` | Validate vault structure & frontmatter | `alp-validate path/` |

*Install: `pip install alp-tools`*

---

## Spec Status

**v0.1 — Experimental.** The specification is published for early adopters
and ecosystem feedback. Expect iteration as real-world usage reveals what
works. See [`spec/v0.1.md`](spec/v0.1.md).

### Compatibility

ALP v0.1 is a superset of [OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) v0.1.
Every ALP file is a valid OKF file. See [`docs/okf-profile.md`](docs/okf-profile.md).

---

## Origin & Roadmap

ALP was born from a gap analysis of the agent content ecosystem.
The evolution: **VKIF (v0.0) → TRAIL (v0.1) → ALP (v0.2)**.

- [Full origin story](docs/origin.md) — How the fourth pillar was discovered
- [Changelog](CHANGELOG.md) — Every iteration documented
- [Roadmap](ROADMAP.md) — v0.3 → v1.0

---

## Contributing

ALP is an open standard. Contributions are welcome:

- **Create vaults** — Convert tutorials, docs, courses into ALP format
- **Build tools** — Extractors, viewers, integrations with agents
- **Improve the spec** — PRs with real-world rationale
- **Spread the word** — Star the repo, share with your network

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

<p align="center">
  <b>⛰️ ALP — Agent Learning Protocol</b><br>
  <a href="https://github.com/nutriandrea/alp">github.com/nutriandrea/alp</a><br>
  <sub>Apache 2.0 — Free to use, implement, and extend</sub>
</p>
