---
type: alp-vault
alp-version: 0.1
name: mcp-server-development
version: 1.0.0
description: Build a Model Context Protocol (MCP) server from scratch — protocol basics, tool design, transport, and production hardening.
author: alp-spec
source: https://modelcontextprotocol.io
source-type: doc
prerequisites:
  - alp:python-basics
  - alp:typescript-basics
curriculum:
  - id: what-is-mcp
    title: "What is MCP? The Protocol in 5 Minutes"
    path: concepts/01-what-is-mcp.md
  - id: tools-and-resources
    title: "Tools, Resources, and Prompts"
    path: concepts/02-tools-and-resources.md
  - id: transports
    title: "Transports: stdio and HTTP/SSE"
    path: concepts/03-transports.md
  - id: designing-tools
    title: "Designing Great Tools"
    path: concepts/04-designing-tools.md
  - id: lifecycle
    title: "Server Lifecycle and Configuration"
    path: concepts/05-lifecycle.md
  - id: production
    title: "Production Hardening"
    path: concepts/06-production.md
tags: [mcp, model-context-protocol, ai, agents, api, tools]
---

# MCP Server Development

Learn the Model Context Protocol by building a real server.

Start with `alp-learn --vault examples/mcp-server-development/`.

Full curriculum (6 concepts):
1. What is MCP? The Protocol in 5 Minutes
2. Tools, Resources, and Prompts
3. Transports: stdio and HTTP/SSE
4. Designing Great Tools
5. Server Lifecycle and Configuration
6. Production Hardening

Recommended lab: `labs/01-build-a-server.md`
