---
type: alp-concept
id: designing-tools
title: "Designing Great Tools"
prerequisites: [tools-and-resources]
tags: [mcp, tool-design, ux]
---
The difference between a good MCP server and a great one is tool design.
Models can't "click around" — they rely entirely on what you declare.

## Principle 1: One Tool, One Job

```typescript
// BAD — overloaded
server.tool("text_ops", {}, async (args) => { /* do 5 things */ });

// GOOD — single responsibility
server.tool("text_setContent", ...)
server.tool("text_getContent", ...)
server.tool("text_search", ...)
```

Models pick tools by name + description. Granular tools are easier to
discover and compose. (This is exactly why InDesign MCP exposes 183 tools.)

## Principle 2: Descriptions Are Documentation

A model never reads your code. It reads:

- The tool name
- The `description`
- The `inputSchema` field descriptions

Write descriptions that state **what** it does, **when** to use it, and
**side effects**:

```typescript
description: "Deletes a file. Permanently. Use only when the user
explicitly asks to delete something. Irreversible."
```

## Principle 3: Validate Everything

Models hallucinate arguments. Validate on the server side:

```typescript
import { z } from "zod";

server.tool(
  "place_order",
  {
    symbol: z.string().min(1).max(10),
    quantity: z.number().int().positive().max(10000),
  },
  async ({ symbol, quantity }) => { ... }
);
```

Reject bad input with a clear error message, not a crash.

## Principle 4: Structured Results

Return machine-readable results, not prose:

```typescript
{ content: [{ type: "text", text: JSON.stringify({ ok: true, id, duration }) }] }
```

The model reads the JSON and knows exactly what happened. For images/files
use `mcp__image__` or file references.

## Principle 5: Fail Explicitly

```typescript
try {
  await riskyOp();
} catch (e) {
  return { content: [{ type: "text", text: `Error: ${e.message}` }], isError: true };
}
```

Return `isError: true` so the model knows the call failed and can recover.
Silent failures are the #1 cause of confused agents.

## Checklist

- [ ] Name describes the action (`create_`, `get_`, `set_`, `delete_`)
- [ ] Description covers side effects
- [ ] Every schema field has a description
- [ ] Input validated server-side
- [ ] Results are structured JSON
- [ ] Errors return `isError: true`
