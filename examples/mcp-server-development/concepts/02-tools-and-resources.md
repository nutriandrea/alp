---
type: alp-concept
id: tools-and-resources
title: "Tools, Resources, and Prompts"
prerequisites: [what-is-mcp]
tags: [mcp, tools, resources, prompts]
---
The three primitives are what a server exposes. Choosing the right
primitive is the core design skill.

## Tools: The Actions

Tools are functions the model can call. Each tool declares:

```typescript
{
  name: "get_weather",
  description: "Get current weather for a city",
  inputSchema: {
    type: "object",
    properties: {
      city: { type: "string", description: "City name" },
      unit: { type: "string", enum: ["celsius", "fahrenheit"] }
    },
    required: ["city"]
  }
}
```

**Rules:**
- Names: lowercase, snake_case, verb-first (`send_email`, not `email`)
- Descriptions are the model's only documentation — write them precisely
- Schemas use JSON Schema; every field needs a description

## Resources: The Data

Resources are read-only data the model can pull in:

```typescript
{
  uri: "file:///docs/architecture.md",
  name: "Architecture Doc",
  mimeType: "text/markdown"
}
```

Used for: configs, docs, logs, database schemas — anything the model
should read before deciding.

## Prompts: The Templates

Prompts are reusable instruction bundles:

```typescript
{
  name: "review-pr",
  description: "Review a pull request for a repo",
  arguments: [{ name: "prNumber", required: true }]
}
```

They let a server embed expert workflows ("review this PR", "triage this
bug") that any host can invoke.

## How to Choose

| The model should... | Use |
|--------------------|-----|
| Take an action that changes state | **Tool** |
| Read information to reason about | **Resource** |
| Follow a prepared workflow | **Prompt** |

Get this wrong and your server feels awkward to agents: tools that should
be resources, prompts that should be tools, etc.
