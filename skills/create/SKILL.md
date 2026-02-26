---
name: create
description: Use when creating a new Claude Code plugin from scratch, adding components to an existing plugin, setting up a development marketplace for testing, or releasing a plugin (versioning, tagging, marketplace distribution).
---

# Creating Claude Code Plugins

Full lifecycle workflow for plugin development — from planning through release and distribution.

## Plugin Development Workflow

### Phase 1: Plan

Before writing code:

1. **Define your plugin's purpose**
   - What problem does it solve?
   - Who will use it?
   - What components will it need?

2. **Choose your pattern** (read `references/common-patterns.md`)
   - Simple plugin with one skill?
   - MCP integration with guidance?
   - Command collection?
   - Hook-enhanced workflow?
   - Full-featured platform?

### Phase 2: Create Structure

1. **Create directories** (see `references/plugin-structure.md` for details):
   ```bash
   mkdir -p my-plugin/.claude-plugin
   mkdir -p my-plugin/skills
   # Add other component directories as needed
   ```

2. **Write plugin.json** (required):
   ```json
   {
     "name": "my-plugin",
     "version": "1.0.0",
     "description": "What your plugin does",
     "author": {"name": "Your Name"}
   }
   ```

3. **Create development marketplace** (for local testing):
   Create `.claude-plugin/marketplace.json`:
   ```json
   {
     "name": "my-dev",
     "plugins": [{
       "name": "my-plugin",
       "source": "./"
     }]
   }
   ```

### Phase 3: Add Components

For each component type, see `references/plugin-structure.md`:
- **Skills** — `skills/skill-name/SKILL.md` (use `/interskill:create` for authoring)
- **Commands** — `commands/command-name.md`
- **Hooks** — `hooks/hooks.json` (use `references/polyglot-hooks.md` for cross-platform)
- **MCP servers** — in plugin.json `mcpServers` section
- **Agents** — `agents/agent-name.md`

### Phase 4: Test Locally

1. **Install for testing**:
   ```bash
   /plugin marketplace add /path/to/my-plugin
   /plugin install my-plugin@my-dev
   ```
   Then restart Claude Code.

2. **Test each component** — run `/interplug:validate` to check structure.

3. **Iterate**: uninstall, modify, reinstall, restart.

### Phase 5: Debug

If something doesn't work, run `/interplug:troubleshoot` or read `references/troubleshooting.md`.

### Phase 6: Release and Distribute

1. **Version your release** — update `version` in plugin.json
2. **Commit and tag**:
   ```bash
   git add .
   git commit -m "Release v1.2.1: [brief description]"
   git tag v1.2.1
   git push origin main && git push origin v1.2.1
   ```

3. **Choose distribution method**:
   - **Direct GitHub** — users add your repo as marketplace
   - **Marketplace** — create separate marketplace repo with manifest
   - **Private/team** — configure in team's `.claude/settings.json`

See `references/plugin-structure.md` for complete distribution format.

## Critical Rules

1. **`.claude-plugin/` contains ONLY manifests** (plugin.json, marketplace.json)
2. **Use `${CLAUDE_PLUGIN_ROOT}` for all paths in config files**
3. **Use relative paths starting with `./` in plugin.json**
4. **Make scripts executable** (`chmod +x`)

## Reference Files

- [plugin-structure.md](references/plugin-structure.md) — directory layout, file formats, component syntax
- [common-patterns.md](references/common-patterns.md) — when to use each plugin pattern
- [polyglot-hooks.md](references/polyglot-hooks.md) — cross-platform hook wrapper
- [troubleshooting.md](references/troubleshooting.md) — debug guide for common issues

## Cross-References

- **interskill** — for skill authoring best practices within plugins
- **interdev:working-with-claude-code** — for official Claude Code documentation
