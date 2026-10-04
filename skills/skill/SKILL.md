---
name: skill
description: Expert guidance for creating Claude Code skills and slash commands — SKILL.md authoring, frontmatter, TDD pressure testing. For full plugin lifecycle (structure, release, marketplace), use /interplug:plugin.
---

# Creating Skills & Commands

This skill teaches how to create effective Claude Code skills following the official specification. It combines spec-driven creation with TDD-adapted pressure testing.

## Commands and Skills Are Now The Same Thing

Custom slash commands have been merged into skills. A file at `.claude/commands/review.md` and a skill at `.claude/skills/review/SKILL.md` both create `/review` and work the same way. Existing `.claude/commands/` files keep working. Skills add optional features: a directory for supporting files, frontmatter to control invocation, and automatic context loading.

**If a skill and a command share the same name, the skill takes precedence.**

## When To Create What

**Use a command file** (`commands/name.md`) when:
- Simple, single-file workflow
- No supporting files needed
- Task-oriented action (deploy, commit, triage)

**Use a skill directory** (`skills/name/SKILL.md`) when:
- Need supporting reference files, scripts, or templates
- Background knowledge Claude should auto-load
- Complex enough to benefit from progressive disclosure

Both use identical YAML frontmatter and markdown content format.

## Standard Markdown Format

Use YAML frontmatter + markdown body with **standard markdown headings**. Keep it clean and direct.

```markdown
---
name: my-skill-name
description: What it does and when to use it
---

# My Skill Name

## Quick Start
Immediate actionable guidance...

## Instructions
Step-by-step procedures...

## Examples
Concrete usage examples...
```

## Frontmatter Reference

All fields are optional. Only `description` is recommended.

| Field | Required | Description |
|-------|----------|-------------|
| `name` | No | Display name. Lowercase letters, numbers, hyphens (max 64 chars). Defaults to directory name. |
| `description` | Recommended | What it does AND when to use it. Claude uses this for auto-discovery. Max 1024 chars. |
| `argument-hint` | No | Hint shown during autocomplete. Example: `[issue-number]` |
| `disable-model-invocation` | No | Set `true` to prevent Claude auto-loading. Use for manual workflows like `/deploy`, `/commit`. Default: `false`. |
| `user-invocable` | No | Set `false` to hide from `/` menu. Use for background knowledge. Default: `true`. |
| `allowed-tools` | No | Tools Claude can use without permission prompts. Example: `Read, Bash(git *)` |
| `model` | No | Model to use. Options: `haiku`, `sonnet`, `opus`. |
| `context` | No | Set `fork` to run in isolated subagent context. |
| `agent` | No | Subagent type when `context: fork`. Options: `Explore`, `Plan`, `general-purpose`, or custom agent name. |

### Invocation Control

| Frontmatter | User can invoke | Claude can invoke | When loaded |
|-------------|----------------|-------------------|-------------|
| (default) | Yes | Yes | Description always in context, full content loads when invoked |
| `disable-model-invocation: true` | Yes | No | Description not in context, loads only when user invokes |
| `user-invocable: false` | No | Yes | Description always in context, loads when relevant |

**Use `disable-model-invocation: true`** for workflows with side effects: `/deploy`, `/commit`, `/triage-prs`, `/send-slack-message`. You don't want Claude deciding to deploy because your code looks ready.

**Use `user-invocable: false`** for background knowledge that isn't a meaningful user action: coding conventions, domain context, legacy system docs.

## Dynamic Features

### Arguments

Use `$ARGUMENTS` placeholder for user input. If not present in content, arguments are appended automatically.

Access individual args: `$ARGUMENTS[0]` or shorthand `$0`, `$1`, `$2`.

### Dynamic Context Injection

The `` !`command` `` syntax runs shell commands before content is sent to Claude.

### Running in a Subagent

Add `context: fork` to run in isolation. The skill content becomes the subagent's prompt.

## Progressive Disclosure

Keep SKILL.md under 500 lines. Split detailed content into reference files:

```
my-skill/
├── SKILL.md           # Entry point (required, overview + navigation)
├── reference.md       # Detailed docs (loaded when needed)
├── examples.md        # Usage examples (loaded when needed)
└── scripts/
    └── helper.py      # Utility script (executed, not loaded)
```

Keep references **one level deep** from SKILL.md.

## What Would You Like To Do?

1. **Create new skill** — Build from scratch (Phase 1: Spec → Phase 2: TDD Test)
2. **Create new command** — Build a slash command
3. **Audit existing skill** — Check against best practices (use `/interplug:audit`)
4. **Add component** — Add workflow/reference/example
5. **Get guidance** — Understand skill design

## Creating a New Skill

### Phase 1: Spec-Driven Creation

Follow [workflows/create-new-skill.md](workflows/create-new-skill.md) for the full step-by-step process.

Quick summary:
1. Choose type (command vs skill, manual vs background)
2. Write frontmatter (name, description, invocation control)
3. Write body with standard markdown headings
4. Add reference files if needed
5. Link references from SKILL.md

### Optional Intermesh Metadata

If the skill has explicit phrase, file-extension, environment, dependency, composition, conflict, or supersession relationships, offer to create an adjacent `intermesh.yaml`. Keep `SKILL.md` canonical; the manifest contains routing relationships only.

When `command -v intermesh >/dev/null 2>&1` succeeds, validate a created manifest with `intermesh manifest validate <skill-directory>/intermesh.yaml` and fix every reported error before completion. If Intermesh is unavailable, skip manifest generation and validation unless the user explicitly requested it; the existing skill-authoring workflow must continue unchanged.

### Phase 2: TDD Pressure Testing

After creating the skill, validate it using TDD-adapted testing. See [references/testing-skills-with-subagents.md](references/testing-skills-with-subagents.md) for the full methodology.

**Core principle:** If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing.

Quick summary:
1. **RED** — Run a pressure scenario with a subagent *without* the skill. Document exact rationalizations the agent uses to deviate.
2. **GREEN** — Load the skill and re-run. Verify the agent now complies.
3. **REFACTOR** — Find new rationalizations, plug loopholes, re-verify.

### Effective Descriptions

The description enables skill discovery. Include both **what** it does and **when** to use it.

**Good:** `"Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction."`

**Bad:** `"Helps with documents"`

## Anti-Patterns to Avoid

- **XML tags in body** — Use standard markdown headings
- **Vague descriptions** — Be specific with trigger keywords
- **Deep nesting** — Keep references one level from SKILL.md
- **Missing invocation control** — Side-effect workflows need `disable-model-invocation: true`
- **Too many options** — Provide a default with escape hatch
- **Punting to Claude** — Scripts should handle errors explicitly

## Reference Files

For detailed guidance, see:
- [official-spec.md](references/official-spec.md) — Official skill specification
- [best-practices.md](references/best-practices.md) — Skill authoring best practices
- [anthropic-best-practices.md](references/anthropic-best-practices.md) — Anthropic's official guidance
- [testing-skills-with-subagents.md](references/testing-skills-with-subagents.md) — TDD pressure testing
- [persuasion-principles.md](references/persuasion-principles.md) — Skill persuasion patterns
- [claude-search-optimization.md](references/claude-search-optimization.md) — CSO for skill discovery
