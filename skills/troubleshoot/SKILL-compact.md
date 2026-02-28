# Troubleshoot Plugin Issues (compact)

Systematic debug guide for Claude Code plugin problems.

## When to Invoke

Use when a plugin is not loading, a skill is not triggering, a command is not appearing, an MCP server is not starting, or hooks are not firing.

## Quick Diagnosis

| Symptom | Fix |
|---------|-----|
| Not in `/plugin list` | Validate JSON (`jq . .claude-plugin/plugin.json`), check `.claude-plugin/` exists, restart |
| Skill ignored | Check YAML frontmatter (`---`, name, description starting "Use when..."), verify `skills/` at root not `.claude-plugin/skills/` |
| Command missing | Check `commands/name.md` has YAML frontmatter with description, restart |
| MCP tools missing | Check paths use `${CLAUDE_PLUGIN_ROOT}`, `chmod +x` scripts, test server independently |
| Hooks not firing | Validate `hooks/hooks.json` with `jq`, check matcher regex, `chmod +x` scripts |

## Common Pitfalls

- Skills in `.claude-plugin/skills/` -- move to `skills/` at plugin root
- Hardcoded absolute paths -- use `${CLAUDE_PLUGIN_ROOT}`
- Forgot to restart -- always restart after changes
- Script not executable -- `chmod +x`
- Testing without uninstall -- uninstall before reinstalling

## Full Debug Workflow

```bash
jq . .claude-plugin/plugin.json               # 1. Validate JSON
jq . hooks/hooks.json 2>/dev/null              # 2. Validate hooks
grep -r "Users/" . --include='*.json'          # 3. Check hardcoded paths
find . -name "*.sh" ! -perm -u+x              # 4. Check permissions
/plugin uninstall my-plugin@my-dev             # 5. Clean reinstall
/plugin marketplace add /path/to/plugin
/plugin install my-plugin@my-dev
# 6. Restart Claude Code
```

---
*For detailed per-symptom walkthroughs, read SKILL.md.*
