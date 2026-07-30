# Changelog

## v0.2.1 — Polish & Publish (Current)

- `pip install alp-tools` — package published on PyPI
- README rewritten with badges, visual layout, GitHub topics
- Tools refactored into proper `alp_tools` Python package
- `alp-validate` added (vault structure validator)

## v0.2 — ALP

**Rebranded to ALP (Agent Learning Protocol).** Simplified to a directory
convention + OKF compatibility. Three letters, like MCP.

### Changes from TRAIL
- Stripped tree notation, complex linking → flat `[[wiki-links]]`
- Removed custom file format → pure markdown + YAML frontmatter
- Added OKF compatibility profile (ALP vault IS an OKF bundle)
- Added progressive loading strategy (context-window aware)
- Tools: `alp-extract` (text → vault), `alp-learn` (vault navigation)
- Example: semantic-search-tutorial vault

## v0.1 — TRAIL

Tree-structured Agent Learning Pathways. First concrete spec attempt.
Used tree nodes with prerequisite DAGs — too complex.

### Key insight that survived
- Agents need structured learning paths, not just docs
- Prerequisites matter for agent comprehension
- Progressive disclosure is essential for context windows

## v0.0 — VKIF

Agent file format for knowledge transfer. Exploration phase.
Tested: frontmatter-only concepts, skill files, OKF compatibility.
Informed the design but too abstract to be useful directly.

## Pre-history — Gap Analysis

The realization that MCP (tools), OKF (knowledge), and Skills (behaviour)
cover three of four pillars. The fourth — learning pathways — has no standard.

This gap was validated through adversarial review:
- Security review: identified vault provenance as risk (CRITICAL)
- Architecture review: flagged complexity risk (needs to be like MCP: simple)
- Feasibility review: 5-15% end-to-end adoption risk
- Adoption review: format fatigue is the primary threat
