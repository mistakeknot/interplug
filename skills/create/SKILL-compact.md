# Creating Claude Code Plugins (compact)

Full lifecycle workflow for plugin development -- plan, create, test, release.

## When to Invoke

Use when creating a new plugin, adding components to an existing plugin, setting up a dev marketplace, or releasing a plugin.

## Core Workflow

1. **Plan** -- Define purpose, audience, and pattern (simple skill, MCP integration, command collection, hook-enhanced, full platform). Read `references/common-patterns.md`.

2. **Create structure**:
   ```bash
   mkdir -p my-plugin/.claude-plugin my-plugin/skills
   ```
   Write `.claude-plugin/plugin.json` (name, version, description, author).
   Create `.claude-plugin/marketplace.json` for local testing.

3. **Add components** -- See `references/plugin-structure.md`:
   - Skills: `skills/skill-name/SKILL.md`
   - Commands: `commands/command-name.md`
   - Hooks: `hooks/hooks.json`
   - MCP servers: in plugin.json `mcpServers`
   - Agents: `agents/agent-name.md`

4. **Test locally**:
   ```bash
   /plugin marketplace add /path/to/my-plugin
   /plugin install my-plugin@my-dev
   # Restart Claude Code
   ```

5. **Release** -- Update version in plugin.json, commit, tag, push tag. Distribute via GitHub, marketplace repo, or team settings.

## Critical Rules

- `.claude-plugin/` contains ONLY manifests (plugin.json, marketplace.json)
- Use `${CLAUDE_PLUGIN_ROOT}` for all paths in config files
- Use relative paths starting with `./` in plugin.json
- Make scripts executable (`chmod +x`)

---
*For component formats, patterns reference, and distribution details, read SKILL.md.*
