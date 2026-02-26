# interplug

Plugin development toolkit for Claude Code.

## What this does

interplug covers the full plugin lifecycle: scaffolding a new plugin, validating its structure, and troubleshooting when things don't work. Three focused skills instead of one monolithic guide.

The `create` skill walks through planning, directory creation, component wiring (skills, hooks, agents, commands, MCP servers), and release preparation. The `validate` skill checks everything a plugin needs to load correctly: `plugin.json` schema, path references, hook permissions, skill structure. The `troubleshoot` skill is a diagnostic guide for the three most common failure modes: plugin not loading, skill not triggering, hooks not firing.

## Installation

First, add the [interagency marketplace](https://github.com/mistakeknot/interagency-marketplace) (one-time setup):

```bash
/plugin marketplace add mistakeknot/interagency-marketplace
```

Then install the plugin:

```bash
/plugin install interplug
```

## Usage

Create a new plugin:

```
/interplug:create
```

Validate plugin structure:

```
/interplug:validate
```

Debug a broken plugin:

```
/interplug:troubleshoot
```

Or ask naturally:

```
"create a plugin for code formatting"
"why isn't my plugin loading?"
"check if my plugin.json is correct"
```

## Architecture

```
skills/
  create/
    SKILL.md                Full lifecycle creation workflow
    references/
      plugin-structure.md   Plugin manifest and directory conventions
      common-patterns.md    Hooks, MCP servers, skill patterns
      polyglot-hooks.md     Writing hooks in Python, Node, Go, etc.
      troubleshooting.md    Common failure modes and fixes
  validate/
    SKILL.md                Structural validation checks
  troubleshoot/
    SKILL.md                Diagnostic guide for common failures
```

## Companion plugins

- **[interskill](https://github.com/mistakeknot/interskill)** — skill authoring toolkit (for creating skills within plugins)
- **[interdev](https://github.com/mistakeknot/interdev)** — Claude Code reference docs and MCP CLI interaction

## Ecosystem

interplug was extracted from [interdev](https://github.com/mistakeknot/interdev)'s `developing-claude-code-plugins` skill. The original monolithic skill covered plugins, skills, and Claude Code reference — now each concern has its own plugin.
