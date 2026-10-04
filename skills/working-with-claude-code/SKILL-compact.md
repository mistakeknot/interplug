# Working with Claude Code (compact)

Reference library for Claude Code official documentation — plugins, hooks, MCP servers, skills, configuration, and integrations.

Resolve the installed skill symlink and set `SKILL_DIR` to its actual directory.
Read this skill's `references/` there, independently of the target project's
working directory. Bundled docs are a snapshot; verify changing details against
current official documentation. Refresh the snapshot only within authorized scope.

## When to Invoke

Creating/configuring plugins, MCP servers, hooks, or skills. Troubleshooting Claude Code. Setting up integrations (VS Code, JetBrains, CI/CD).

## Quick Lookup Table

| Task | Read |
|------|------|
| Create a plugin | `plugins.md` then `plugins-reference.md` |
| Set up MCP server | `mcp.md` |
| Configure hooks | `hooks.md` then `hooks-guide.md` |
| Write a skill | `skills.md` |
| CLI commands | `cli-reference.md` |
| Troubleshoot | `troubleshooting.md` |
| Configuration | `settings.md` |
| General setup | `setup.md` or `quickstart.md` |

## Workflow

1. Identify the relevant doc file from the table above
2. Read it from `references/` directory
3. Find the answer in official documentation
4. Apply the solution

For broad topics, start with the overview doc then drill into specifics. For uncertain topics, use Grep to search across `references/`.

## Key Docs (37 files in `references/`)

- **Core**: overview, quickstart, setup, settings, cli-reference, common-workflows
- **Extending**: plugins, plugins-reference, plugin-marketplaces, skills, mcp, hooks, hooks-guide, slash-commands, sub-agents
- **Integrations**: vs-code, jetbrains, devcontainer, github-actions, gitlab-ci-cd
- **Operations**: memory, checkpointing, costs, monitoring-usage, analytics
- **Infrastructure**: security, iam, network-config, model-config, llm-gateway, amazon-bedrock, google-vertex-ai

## Updating Docs

```bash
node "$SKILL_DIR/scripts/update_docs.js"
```

Fetches latest from docs.claude.com. Run when docs seem outdated or new features are released.

## Key Rule

**Always consult official documentation before guessing** about config paths, API structures, hook names, or feature capabilities.

---
*For the complete doc index and workflow details, read SKILL.md.*
