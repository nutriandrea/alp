---
type: alp-concept
id: transports
title: "Transports: stdio and HTTP/SSE"
prerequisites: [what-is-mcp]
tags: [mcp, transports, stdio, http, sse]
---
MCP works over two main transports. Pick based on where the server runs.

## stdio: The Local Default

The server runs as a child process, talking over stdin/stdout:

```
Host ──spawns──► Server (node/python process)
     stdin/stdout JSON-RPC
```

**Use when:** the server is local (CLI tool, local MCP for a code editor).

**Pros:** zero network config, secure by default (no ports), trivial auth.
**Cons:** one process per connection, local only.

Minimal stdio server in Node:

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new McpServer({ name: "demo", version: "1.0.0" });
server.tool("ping", {}, () => ({ content: [{ type: "text", text: "pong" }] }));

const transport = new StdioServerTransport();
await server.connect(transport);
```

## HTTP/SSE: The Remote Default

The server exposes an HTTP endpoint; hosts connect over Server-Sent Events.

**Use when:** the server is remote (SaaS, team tooling, cloud).

**Pros:** many clients, deploy anywhere, scale independently.
**Cons:** needs auth + rate limiting, TLS, and operational care.

## Rules of Thumb

1. **Start stdio** — simplest, most compatible, no security surface
2. **Move to HTTP** only when a remote deployment demands it
3. **Never** expose an MCP server without auth if it can mutate state
4. Test both against the official `npx @modelcontextprotocol/inspector`

## Client Configuration (the config file)

```json
{
  "mcpServers": {
    "demo": {
      "command": "npx",
      "args": ["-y", "my-mcp-server"]
    }
  }
}
```

This is the file your users paste into Claude Desktop / OpenCode. If this
config doesn't work out of the box, your server is "installed but broken."
