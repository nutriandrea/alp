---
type: alp-practice
id: scaffold-server
title: Scaffold a Minimal stdio Server
concepts-covered: [what-is-mcp, transports]
---
## Steps

1. Create a new project:
   ```bash
   mkdir my-mcp-server && cd my-mcp-server
   npm init -y
   npm install @modelcontextprotocol/sdk zod
   ```

2. Create `index.mjs`:

   ```javascript
   import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
   import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
   import { z } from "zod";

   const server = new McpServer({ name: "my-server", version: "0.1.0" });

   server.tool("hello", { name: z.string().default("world") },
     ({ name }) => ({ content: [{ type: "text", text: `Hello, ${name}!` }] }));

   await server.connect(new StdioServerTransport());
   ```

3. Run it with the MCP Inspector:
   ```bash
   npx @modelcontextprotocol/inspector node index.mjs
   ```

4. Click through the inspector: you should see the `hello` tool, be able
   to call it, and see the JSON-RPC exchange.

## Expected Output
Inspector loads, lists `hello`, and calling it returns `Hello, <name>!`.

## Hint
- [[what-is-mcp]] for the actors
- [[transports]] for why stdio uses stdin/stdout
