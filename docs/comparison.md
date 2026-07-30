# ALP vs MCP vs OKF vs Skills

```
              MCP           OKF/Vaults      Skills          ALP
Scope         Tools         Knowledge       Behaviour       Learning
Unit          Server        Concept         Prompt          Vault
Discovery     mcp.json      Index           Registry        Curriculum
Navigation    Tools list    Search          Install         Prerequisites
State         Connection    Memory          Activated       Notes
Composability Tool chains   Wiki-links      Pipelines       Vault chains
Context cost  Per tool      Per concept     Per skill       Per concept
                          
```

## ALP is not a competitor to any of these.

| If you want... | Use... |
|----------------|--------|
| Your agent to read a file | OKF / Vaults |
| Your agent to run a tool | MCP |
| Your agent to behave consistently | Skills |
| Your agent to **learn something new** | ALP |

**ALP teaches skills that aren't installed yet.**
**OKF stores facts the agent knows.**
**MCP provides actions the agent can take.**
**Skills encode behaviours the agent should follow.**

## Integration Points

| Integration | How |
|-------------|-----|
| ALP → MCP | Vault can advertise MCP tools for practice/lab execution |
| ALP → OKF | Every ALP file IS an OKF file (superset frontmatter) |
| ALP → Skills | After studying a vault, agent consolidates into a skill |
| OKF → ALP | An OKF bundle + alp.md + curriculum = ALP vault |

## The Four Pillars Together

An agent equipped with all four:

1. **MCP** — "I can search the web, read files, run code"
2. **OKF** — "I know Python syntax, numpy API, ML concepts"
3. **Skills** — "I write tests first, use types, handle errors"
4. **ALP** — "I don't know semantic search yet, let me study it"
