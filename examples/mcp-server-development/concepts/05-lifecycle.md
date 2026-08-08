---
type: alp-concept
id: lifecycle
title: "Server Lifecycle and Configuration"
prerequisites: [transports]
tags: [mcp, lifecycle, config, cli]
---
A production MCP server is a CLI that is spawned by a host. That shapes
everything: CLI args, config files, logging, and shutdown.

## The Lifecycle

```
spawn (host starts process)
   │
   ▼
parse CLI args + load config
   │
   ▼
connect transport (stdio or HTTP)
   │
   ▼
serve until stdin closes / SIGTERM
   │
   ▼
cleanup (close DB, flush logs) → exit 0
```

## Config Loading (the boring 90%)

Most server friction is config. Support:

1. **Default config path** — `~/.config/<server>/config.json`
2. **CLI flag** — `--config path.json`
3. **Env overrides** — `SERVER_API_KEY=...`

Merge order: defaults < file < env < CLI.

```typescript
import { parseArgs } from "node:util";

const { values } = parseArgs({
  args: process.argv.slice(2),
  options: {
    config: { type: "string" },
    verbose: { type: "boolean", short: "v" },
  },
});
```

## Logging Discipline (critical)

MCP stdio uses **stdout for protocol messages**. Anything you `console.log`
goes into the protocol stream and corrupts it.

**Rule: log only to stderr or a file.**

```typescript
const log = (msg: string) => process.stderr.write(`[server] ${msg}\n`);
```

Provide `--verbose` for debugging and default to silent on stdout.

## Environment Requirements

In your README, tell users exactly what the server needs:

- `command`: `npx` / `python` / binary name
- `args`: full array, including the config path
- `env`: every variable (with example values)
- `cwd`: if the server needs to run from a directory

A user config should be copy-paste, not archaeology:

```json
{
  "mcpServers": {
    "my-server": {
      "command": "npx",
      "args": ["-y", "@scope/my-server", "--config", "/etc/my-server/config.json"],
      "env": { "MY_SERVER_API_KEY": "sk-..." }
    }
  }
}
```

## Graceful Shutdown

Handle `SIGTERM`/`SIGINT`: close the transport, flush buffers, then exit.
Hosts kill servers on reload — an abrupt exit loses state and annoys users.
