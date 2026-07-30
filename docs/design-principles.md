# Design Principles

## 1. Simple > Clever

MCP succeeded because it's just HTTP + JSON. ALP uses the same approach:
just markdown + YAML + directories.

- If you can write a README, you can create an ALP vault
- If you can read a file, your agent can learn from ALP
- No SDK, no runtime, no compilation step

## 2. Progressive Loading

Context windows are the fundamental constraint. ALP is designed for
finite context:

1. Syllabus only (~200 tokens) — discovery and routing
2. One concept at a time (~500–2K tokens) — deep study
3. Practice on demand (~300–1K tokens) — hands-on learning
4. Reference (~200 tokens) — recall and lookup

An agent never loads more than 2–3 concepts simultaneously.

## 3. Composable by Design

ALP vaults are not islands:

- `prerequisites` reference other vaults (`alp:python-basics`)
- `[[wiki-links]]` connect concepts within and across vaults
- Curriculum defines a canonical path, but agents can branch

A vault is a **node in a learning graph**, not a standalone document.

## 4. Source Agnostic

ALP doesn't care where content comes from:

- YouTube tutorial → extract transcript → ALP vault
- Blog post → parse headings → ALP vault
- Documentation → chunk by section → ALP vault
- Live lecture → real-time ASR → progressive vault

The extraction is a separate concern. ALP is the **storage and navigation**
standard.

## 5. Open Ecosystem, Not a Platform

ALP is a convention, not a product:

- Anyone can create vaults
- Any agent can consume vaults
- Any tool can generate vaults
- No central registry required (but one can exist)

Like MCP, the value is in the **network effect** of many vaults.

## 6. Compatible, Not Competitive

ALP doesn't replace OKF — it **extends** it:

- An ALP vault IS an OKF bundle
- An ALP concept IS an OKF concept
- OKF consumers can index ALP content without modification

This is the TCP/IP approach: coexist and interoperate, not fragment.
