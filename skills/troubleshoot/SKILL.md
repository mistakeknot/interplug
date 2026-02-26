---
name: troubleshoot
description: Use when a Claude Code plugin is not working — plugin not loading, skill not triggering, command not appearing, MCP server not starting, or hooks not firing. Provides systematic debug steps.
---

# Troubleshoot Plugin Issues

Systematic debug guide for Claude Code plugin problems.

## Quick Diagnosis

Identify your symptom and jump to the relevant section:

| Symptom | Section |
|---------|---------|
| Plugin doesn't appear in `/plugin list` | Plugin Not Loading |
| Skill exists but Claude ignores it | Skill Not Triggering |
| `/command` not available | Command Not Appearing |
| MCP tools not available | MCP Server Not Starting |
| Hook scripts don't execute | Hooks Not Firing |
| Changes don't take effect | Development Workflow |

## Plugin Not Loading

1. **Validate JSON**: `jq . .claude-plugin/plugin.json`
2. **Check structure**: `.claude-plugin/` must exist at plugin root with `plugin.json`
3. **Check paths**: `grep -r "/Users/" .claude-plugin/` should return nothing
4. **Restart Claude Code** — changes only take effect after restart
5. **Check installation**: `/plugin list`

## Skill Not Triggering

1. **Check YAML frontmatter** — must have `---` delimiters, `name`, `description`
2. **Verify description** — must start with "Use when..." and describe triggers
3. **Check location** — must be `skills/skill-name/SKILL.md` (not inside `.claude-plugin/`)
4. **Test explicitly** — ask for a task that exactly matches the description

## Command Not Appearing

1. **Check location** — `commands/command-name.md` at plugin root
2. **Check format** — must have YAML frontmatter with `description`
3. **Restart Claude Code** — commands load at startup

## MCP Server Not Starting

1. **Check paths** — must use `${CLAUDE_PLUGIN_ROOT}` in all config
2. **Check permissions** — `chmod +x` on scripts and binaries
3. **Test independently** — run server outside Claude Code to check for errors
4. **Check logs** — `claude --debug` for startup errors
5. **Verify command** — `which node` or equivalent

## Hooks Not Firing

1. **Check location** — `hooks/hooks.json` at plugin root
2. **Validate JSON** — `jq . hooks/hooks.json`
3. **Check matcher** — regex pattern in `"matcher"` field
4. **Check script paths** — use `${CLAUDE_PLUGIN_ROOT}`
5. **Check permissions** — `chmod +x` on all hook scripts
6. **Test directly** — run the script manually

## Development Workflow Issues

**Changes not taking effect:**
```bash
/plugin uninstall my-plugin@my-dev
# Make changes
/plugin install my-plugin@my-dev
# Restart Claude Code
```

**Can't install locally:**
1. Check `.claude-plugin/marketplace.json` exists and is valid
2. Verify marketplace is added: `/plugin marketplace list`

## Common Pitfalls

| Mistake | Fix |
|---------|-----|
| Skills in `.claude-plugin/skills/` | Move to `skills/` at root |
| Hardcoded absolute paths | Use `${CLAUDE_PLUGIN_ROOT}` |
| Forgot to restart | Always restart after changes |
| Script not executable | `chmod +x script.sh` |
| Invalid JSON | Validate with `jq` |
| Vague skill description | Be specific about triggers |
| Testing without uninstall | Uninstall before reinstalling |

## Full Debug Workflow

```bash
# 1. Validate all JSON
jq . .claude-plugin/plugin.json
jq . hooks/hooks.json 2>/dev/null

# 2. Check paths
grep -r "Users/" . --include='*.json'

# 3. Check permissions
find . -name "*.sh" ! -perm -u+x

# 4. Clean reinstall
/plugin uninstall my-plugin@my-dev
/plugin marketplace remove /path/to/plugin
/plugin marketplace add /path/to/plugin
/plugin install my-plugin@my-dev
# Restart Claude Code
```

## Reference

For detailed component formats, see `/interplug:create` references:
- `references/plugin-structure.md` — directory layout and syntax
- `references/polyglot-hooks.md` — cross-platform hooks
