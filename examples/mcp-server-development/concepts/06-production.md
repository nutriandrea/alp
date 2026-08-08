---
type: alp-concept
id: production
title: "Production Hardening"
prerequisites: [lifecycle, designing-tools]
tags: [mcp, production, security, reliability]
---
Your MCP server will be called by AI agents — which means it will be
called with weird inputs, adversarial inputs, and in production loops.
Harden it like a public API.

## Security

### 1. Scope tools to least privilege

Don't expose `fs_write` globally. Scope to the intended directory,
require explicit paths, and reject `../` traversal:

```typescript
function safeResolve(base: string, input: string) {
  const p = path.resolve(base, input);
  if (!p.startsWith(base)) throw new Error("path escapes workspace");
  return p;
}
```

### 2. Validate everything, again

Treat every argument as untrusted user input — because for a remote
server, it is. Zod schemas are your first line.

### 3. Secrets never in tool output

If a tool can read files or run commands, make sure results are filtered
for API keys, tokens, and private keys before returning to the model.

### 4. Auth for remote servers

- **Bearer tokens** on HTTP transports as a baseline
- **OAuth 2.1** for multi-user remote servers
- Never rely on "it's on localhost"

## Reliability

| Risk | Mitigation |
|------|-----------|
| Long-running tool hangs | Timeouts per tool call (e.g. 30s) |
| Model retries forever | Idempotency keys for state-changing tools |
| Crash on bad input | Try/catch + `isError: true`, never crash |
| Losing connection | Reconnect with backoff (stdio: host re-spawns) |
| Rate-limited upstream API | Queue + retry with exponential backoff |

## Observability

```typescript
// Log every call: tool name, args (redacted), duration, error
function instrument(fn) {
  return async (args) => {
    const t0 = Date.now();
    try {
      const result = await fn(args);
      log(`tool=${fn.name} ok=${Date.now()-t0}ms`);
      return result;
    } catch (e) {
      log(`tool=${fn.name} err=${Date.now()-t0}ms ${e.message}`);
      throw e;
    }
  };
}
```

Metrics to track: calls per tool, error rate, p50/p95 latency, top
failing tools. This tells you what models actually use and what breaks.

## The Production Checklist

- [ ] Secrets load from env, never hardcoded
- [ ] Tools scoped to least privilege
- [ ] Remote transport has auth
- [ ] Every tool has a timeout
- [ ] State-changing tools support idempotency
- [ ] Errors are structured and recoverable
- [ ] Per-tool metrics logged
- [ ] Tested with the MCP Inspector
- [ ] `npm publish` / `pip publish` works from a clean machine
