# Creating Skills & Commands (compact)

Expert guidance for creating Claude Code skills and slash commands with spec-driven creation and TDD pressure testing.

## When to Invoke

Use when creating new skills or commands, auditing existing skills, or understanding skill structure and best practices.

## Commands vs Skills

- **Command** (`commands/name.md`): simple single-file workflow, no supporting files
- **Skill** (`skills/name/SKILL.md`): needs reference files, scripts, or templates; benefits from progressive disclosure
- Same YAML frontmatter + markdown format. Skills take precedence on name collision.

## Core Workflow

1. **Choose type** -- command vs skill, manual vs background
2. **Write frontmatter** -- name, description (starts with "Use when..."), invocation control
3. **Write body** -- standard markdown headings (no XML tags)
4. **Add references** -- keep one level deep from SKILL.md, stay under 500 lines
5. **TDD pressure test**:
   - RED: subagent runs without skill, document deviations
   - GREEN: load skill, verify compliance
   - REFACTOR: plug remaining loopholes

## Key Frontmatter

| Field | Purpose |
|-------|---------|
| `description` | What + when. Enables auto-discovery. Max 1024 chars. |
| `disable-model-invocation: true` | Side-effect workflows (deploy, commit). Claude cannot auto-invoke. |
| `user-invocable: false` | Background knowledge only. Hidden from `/` menu. |
| `allowed-tools` | Tools without permission prompts. E.g., `Read, Bash(git *)` |
| `context: fork` | Run in isolated subagent context |

## Anti-Patterns

- XML tags in body (use standard markdown)
- Vague descriptions ("helps with documents")
- Deep nesting of reference files
- Missing `disable-model-invocation` on side-effect workflows
- Skipping TDD phase -- if you didn't watch an agent fail without the skill, you don't know if it teaches the right thing

---
*For full spec, TDD methodology, and persuasion patterns, read SKILL.md.*
