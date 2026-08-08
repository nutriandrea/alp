---
type: alp-lab
id: build-a-server
title: Build a Production-Ready MCP Server
concepts-covered: [tools-and-resources, designing-tools, lifecycle, production]
verification:
  - Connects via stdio AND is verified in the MCP Inspector
  - Exposes at least 5 tools across 2 domains, each with zod validation
  - State-changing tools are idempotent (safe to retry)
  - Logs to stderr only, with per-call timing and redacted args
  - Fails gracefully: bad input → structured error, not a crash
prerequisites: [scaffold-server]
---
## Objective

Build a small but production-hardened MCP server. Pick a domain you know
well (e.g., a note organizer, a task tracker, a code search helper) — the
domain matters less than the engineering rigor.

## Requirements

- Node 18+ with `@modelcontextprotocol/sdk`
- zod for validation
- Persist state to a JSON file (survives restarts)

## Task

1. **Define 5+ tools across 2 domains** (e.g. `notes_*` and `search_*`).
   - Use single-responsibility naming from [[designing-tools]]
2. **Validate everything** with zod; add descriptions to every field.
3. **Persist state** — write-through JSON file on every mutation.
4. **Idempotency** — mutating tools accept an `idempotencyKey` and return
   the same result on retry.
5. **Instrument** — wrap every handler to log timing + redacted args to
   **stderr only** ([[lifecycle]]).
6. **Structured errors** — bad input returns `isError: true`.
7. **Config** — support `--config path` and env overrides.
8. **Verify in the Inspector** — run every tool, including failure cases.

## Verify

- [ ] Inspector lists all tools with correct schemas
- [ ] Calling with invalid input returns a clean error
- [ ] Retrying a mutation with the same key doesn't duplicate state
- [ ] `node index.mjs` produces no stdout noise (only protocol)
- [ ] Server survives a config-file error (falls back to defaults)

## Hints

- [[tools-and-resources]] for primitive choice
- [[designing-tools]] for tool ergonomics
- [[lifecycle]] for config + logging
- [[production]] for hardening + the checklist
