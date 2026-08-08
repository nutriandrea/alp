---
type: alp-practice
id: connect-from-opencode
title: Connect Your Server to a Real Host
concepts-covered: [lifecycle, transports]
---
## Steps

1. Keep your server from the previous practice running.

2. Add it to your host's MCP config. For OpenCode, edit `opencode.json`:

   ```json
   {
     "mcpServers": {
       "my-server": {
         "command": "node",
         "args": ["/absolute/path/to/my-mcp-server/index.mjs"]
       }
     }
   }
   ```

   For Claude Desktop: `claude mcp add my-server -- node index.mjs`

3. Restart the host and ask it:
   > "Use the hello tool to greet me."

4. Check the host connected successfully (your server logs to stderr).

## Expected Output
The host discovers `hello`, the agent calls it with your name, and the
response appears in chat.

## Hint
- [[lifecycle]] for the config file anatomy
- [[transports]] for the exact `mcpServers` shape
