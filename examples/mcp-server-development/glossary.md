---
type: alp-glossary
---

- **MCP** — Model Context Protocol. Open standard connecting AI assistants
  to tools and data (USB-C for AI).
- **Host** — The app the user interacts with (Claude Desktop, OpenCode).
- **Client** — Component in the host managing one server connection.
- **Server** — Exposes tools/resources/prompts over MCP.
- **Tool** — An action the model can invoke, with an input schema.
- **Resource** — Read-only data (URI-addressable) the model can load.
- **Prompt** — A reusable instruction template the server defines.
- **Transport** — The wire protocol: stdio (local) or HTTP/SSE (remote).
- **JSON-RPC** — The message format MCP uses for requests/responses.
- **MCP Inspector** — Official dev tool for testing an MCP server.
- **Idempotency** — A call safe to repeat; retrying doesn't duplicate state.
- **isError** — Flag on a tool result telling the model the call failed.
