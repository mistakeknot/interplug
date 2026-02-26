---
name: validate
description: Use when verifying a plugin is correctly structured before testing or publishing — checks plugin.json schema, directory layout, hooks declaration, skill structure, and file permissions.
---

# Validate Plugin Structure

Verify a Claude Code plugin follows structural requirements and conventions.

## Instructions

Given a plugin directory, check each item below. Report findings as PASS/WARN/FAIL.

## Validation Checklist

### Manifest (plugin.json)
- [ ] `.claude-plugin/plugin.json` exists and is valid JSON
- [ ] `name` field present (lowercase, hyphens only)
- [ ] `version` field present (semver format)
- [ ] `description` field present and descriptive
- [ ] No extra files in `.claude-plugin/` besides manifests

### Directory Layout
- [ ] Skills in `skills/` at plugin root (not inside `.claude-plugin/`)
- [ ] Commands in `commands/` at plugin root
- [ ] Each skill has `SKILL.md` with valid YAML frontmatter
- [ ] No orphaned directories (referenced in plugin.json but missing)
- [ ] No unreferenced skill directories (exist but not in plugin.json skills array)

### Paths and Variables
- [ ] All config paths use `${CLAUDE_PLUGIN_ROOT}` (not hardcoded)
- [ ] Relative paths in plugin.json start with `./`
- [ ] No absolute paths in any config file
- [ ] MCP server commands reference portable paths

### Hooks
- [ ] If `hooks/` directory exists, `hooks/hooks.json` is valid JSON
- [ ] Hooks declared in plugin.json if hooks directory exists
- [ ] Hook scripts are executable (`chmod +x`)
- [ ] Hook commands use `${CLAUDE_PLUGIN_ROOT}` for paths

### Permissions and Portability
- [ ] All `.sh` scripts have executable permission
- [ ] No Windows-specific paths without polyglot wrapper
- [ ] No `#!/usr/bin/env` shebangs with missing interpreters

## Quick Validation Commands

```bash
# Validate JSON
jq . .claude-plugin/plugin.json

# Check for hardcoded paths
grep -r '/Users/\|/home/\|C:\\' .claude-plugin/ hooks/ --include='*.json'

# Check permissions
find . -name '*.sh' ! -perm -u+x

# Check unreferenced skills
diff <(jq -r '.skills[]' .claude-plugin/plugin.json | sed 's|^\./skills/||' | sort) <(ls skills/ | sort)
```

## Output Format

```
Plugin Validation: {plugin-name} v{version}
──────────────────────────────────────
Manifest:     {N}/5 pass
Layout:       {N}/5 pass
Paths:        {N}/4 pass
Hooks:        {N}/4 pass
Permissions:  {N}/3 pass
──────────────────────────────────────
Overall: {PASS | WARN (N issues) | FAIL (N issues)}

Issues:
- [WARN] Unreferenced skill directory: old-skill/
- [FAIL] Hardcoded path in hooks.json: /Users/name/...
```
