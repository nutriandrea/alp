---
type: alp-concept
id: what-is-mcp
title: "What is MCP? The Protocol in 5 Minutes"
prerequisites: []
tags: [mcp, fundamentals, protocol]
---
The Model Context Protocol (MCP) is an open standard that connects AI
assistants to data and tools. Think of it as **USB-C for AI applications**:
one standard connector instead of a vendor-specific cable per device.

## The Three Actors

```
┌──────────────┐   MCP protocol   ┌──────────────┐
│   HOST       │ ◄──────────────► │    SERVER    │
│ (Claude,     │                  │  exposes     │
│  OpenCode,   │                  │  tools/data  │
│  agents)     │                  │              │
└──────┬───────┘                  └──────▲───────┘
       │                                  │
       └────────────► CLIENT ◄────────────┘
             (manages the connection)
```

- **Host** — the application the user interacts with (Claude Desktop, OpenCode)
- **Client** — lives in the host, manages one server connection
- **Server** — exposes tools, resources, and prompts over MCP

## The Core Primitives

| Primitive | What it does | Analogy |
|-----------|-------------|---------|
| **Tools** | Actions the model can invoke | Functions |
| **Resources** | Data the model can read | GET endpoints |
| **Prompts** | Reusable instruction templates | Macros |

## Why MCP Won

Before MCP, every AI tool was a one-off integration: a plugin for each
platform, each with its own API. MCP gives us a single JSON-RPC protocol
over standard transports, so one server works with every host.

## Why ALP ships MCP servers

ALP vaults teach agents to *use* tools; MCP is the standard those tools
speak. Learning both unlocks the full agent workflow: an agent that can
learn a protocol (ALP) and execute it (MCP).
