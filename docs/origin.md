# Origin Story: How ALP Was Born

## The Gap

In mid-2026, we mapped the agent content ecosystem. Three pillars existed:

| Pillar | Standard | What it does |
|--------|----------|-------------|
| Tools | MCP | How agents access tools, APIs, data sources |
| Knowledge | OKF / Vaults | How agents store and retrieve knowledge |
| Behaviour | Skills | How agents act (prompts, workflows) |

But a fourth pillar was missing: **how agents learn**.

MCP gave agents hands (tools). OKF gave them a library (knowledge). Skills
gave them instincts (behaviour). But nothing gave them a **curriculum**.

## The Insight

Agents currently learn by:
1. **Reading raw docs** — no structure, no prerequisites, no progression
2. **Random skill loading** — skills are installed, not studied
3. **Trial and error** — expensive, unreliable, no knowledge consolidation

What if an agent could "attend a lecture" the way a student does?

- See the syllabus first
- Check prerequisites
- Study concept by concept
- Take notes
- Practice with exercises
- Verify understanding with labs
- Get a cheat sheet for recall

This is the **live lecture** vision: an agent as a student, a vault as a
course, learning as a structured process.

## The Iterations

### VKIF (v0.0) — "What if agents had a file format?"

Started as a general "agent knowledge interchange format." Too abstract.
The only survivor: frontmatter + markdown is the right container.

### TRAIL (v0.1) — "Tree-structured Agent Learning"

Made it concrete: a tree of learning nodes with prerequisite DAGs.
Too complex. Agents have limited context — a tree with cross-links
requires too much navigation logic. Killed it.

### ALP (v0.2) — "Agent Learning Protocol"

The breakthrough: **make it as simple as MCP**.

MCP succeeded because it's just a protocol — no SDK, no runtime, no
complex schema. ALP should be the same: a **directory convention** +
**frontmatter rules**. Any agent can consume it, any tool can produce it.

## The Fourth Pillar

```
         MCP          OKF         Skills         ALP
    ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
    │  Tools   │ │Knowledge │ │Behaviour │ │Learning  │
    │          │ │          │ │          │ │          │
    │   DO     │ │  KNOW    │ │   ACT    │ │  LEARN   │
    └──────────┘ └──────────┘ └──────────┘ └──────────┘
```

ALP completes the stack. An agent equipped with all four can:
- **Do** things (MCP) — access tools and data
- **Know** things (OKF) — retrieve knowledge
- **Act** appropriately (Skills) — follow best practices
- **Learn** new things (ALP) — acquire skills it doesn't have

## Design Decisions

| Decision | Why |
|----------|-----|
| **Markdown + YAML** | Universal, human-readable, no compilation step |
| **Directory convention** | No special files, works with any markdown renderer |
| **[[wiki-links]]** | Familiar from Obsidian, Roam, Logseq |
| **Progressive loading** | Context windows are finite — load what you need |
| **OKF compatible** | Don't fragment the ecosystem — be a superset |
| **v0.1 experimental** | Don't pretend it's stable before real-world use |

## What's Next

ALP is at the same stage MCP was at its launch: a spec with examples
and a vision. The next steps are:
1. Real-world usage (convert tutorials, study them with agents)
2. Feedback-driven iteration
3. Community contributions
4. Reference implementations in multiple languages

The protocol will evolve. What won't change: the goal of making agent
learning as structured and reliable as tool access (MCP).
