# MCP CLI (compact)

Interact with MCP servers on-demand via the `mcp` CLI tool — discover tools, resources, and prompts without pre-loaded integrations.

## When to Invoke

Need to explore, test, or make one-off calls to an MCP server without permanent configuration.

## Prerequisites

Binary at `~/.local/bin/mcp`. Install: `cd /tmp && git clone --depth 1 https://github.com/f/mcptools.git && cd mcptools && CGO_ENABLED=0 go build -o ~/.local/bin/mcp ./cmd/mcptools`

## Core Workflow

1. **Discover tools**: `mcp tools <server-command>`
2. **Discover resources**: `mcp resources <server-command>`
3. **Discover prompts**: `mcp prompts <server-command>`
4. **Get JSON schema**: `mcp tools --format json <server-command>`
5. **Call a tool**: `mcp call <tool_name> --params '<json>' <server-command>`
6. **Read a resource**: `mcp read-resource <uri> <server-command>`

## Quick Reference

| Action | Command |
|--------|---------|
| List tools | `mcp tools <server>` |
| Call tool | `mcp call <tool> --params '<json>' <server>` |
| JSON output | Add `-f json` or `-f pretty` |
| Add alias | `mcp alias add <name> <server-command>` |
| Remove alias | `mcp alias remove <name>` |
| Guard access | `mcp guard --allow 'tools:read_*' --deny 'tools:write_*' <server>` |

## Common Servers

```bash
# Filesystem
mcp tools npx -y @modelcontextprotocol/server-filesystem /path
# Memory
mcp tools npx -y @modelcontextprotocol/server-memory
# GitHub (needs GITHUB_PERSONAL_ACCESS_TOKEN)
mcp tools docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN ghcr.io/github/github-mcp-server
```

## Key Rules

- **Always discover first** — run `mcp tools` before calling anything
- **Use aliases** for multi-step operations: `mcp alias add fs <server>` then `mcp call ... fs`
- **Single quotes** around JSON params to avoid shell expansion
- **Parameter types**: `param:str`, `param:num`, `param:bool`, `[param:str]` = optional
- For complex JSON, write to temp file: `--params "$(cat params.json)"`

## Transports

- **stdio** (default for npx/node), **HTTP** (auto-detected for URLs), **SSE** (`--transport sse`)

---
*For authentication, debugging, and full examples, read SKILL.md.*
