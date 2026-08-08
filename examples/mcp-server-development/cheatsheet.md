---
type: alp-cheatsheet
---

## The Three Primitives

| Primitive | Model does | Use when |
|-----------|-----------|----------|
| Tool | Action / mutation | "do X" |
| Resource | Read data | "show me X" |
| Prompt | Follow workflow | "triage this X" |

## Tool Template

```typescript
server.tool(
  "verb_noun",
  { field: z.string().describe("what the field is") },
  async ({ field }) => ({
    content: [{ type: "text", text: JSON.stringify({ ok: true, field }) }],
  })
);
```

## Transports

| Transport | When | Notes |
|-----------|------|-------|
| stdio | local, most compatible | stdout = protocol, stderr = logs |
| HTTP/SSE | remote, multi-client | needs auth + TLS + rate limits |

## Rules

1. stdout is RESERVED for the protocol — log to stderr only
2. Describe every field; models read descriptions, not code
3. Validate with zod; return `isError: true` on failure
4. Scope tools to least privilege; reject path traversal
5. Make mutating tools idempotent (retry-safe)

## Config Shape

```json
{
  "mcpServers": {
    "name": {
      "command": "npx",
      "args": ["-y", "@scope/server"],
      "env": { "KEY": "value" }
    }
  }
}
```

## Test Loop

`npx @modelcontextprotocol/inspector node index.mjs` → try success + failure
cases → check stderr logs.
