---
name: audit
description: Audit an existing skill against best practices — checks structure, frontmatter, invocation control, description quality, and anti-patterns. Use when verifying a skill before deployment.
---

# Skill Audit

Verify a skill follows best practices and the official specification.

## Instructions

Given a skill path (SKILL.md or skill directory), check each item below. Report findings as PASS/WARN/FAIL.

## Audit Checklist

### Structure
- [ ] Valid YAML frontmatter with `---` delimiters
- [ ] `name` field present (lowercase, hyphens, max 64 chars)
- [ ] `description` field present and specific (includes trigger keywords)
- [ ] SKILL.md under 500 lines
- [ ] References one level deep from SKILL.md (no nested chains)
- [ ] SKILL-compact.md exists if SKILL.md > 200 lines (run `gen-skill-compact.sh --check <dir>` to verify freshness)

### Invocation Control
- [ ] `disable-model-invocation: true` set if skill has side effects (deploy, commit, send)
- [ ] `user-invocable: false` set if skill is background knowledge only
- [ ] `allowed-tools` declared if specific tools needed
- [ ] `context: fork` used for isolation where appropriate

### Content Quality
- [ ] Uses standard markdown headings (NOT XML tags)
- [ ] Description includes both "what" and "when" triggers
- [ ] Examples are concrete, not abstract
- [ ] Has Quick Start or Instructions section
- [ ] No vague guidance ("use best judgment") — specific steps

### Anti-Patterns
- [ ] No XML tags in body
- [ ] No deep reference nesting
- [ ] No "punting" patterns (scripts handle errors, not "ask Claude to fix")
- [ ] No overly broad descriptions ("helps with things")

### Optional Intermesh Manifest

- [ ] If `intermesh.yaml` exists and `command -v intermesh >/dev/null 2>&1` succeeds, run `intermesh manifest validate <path>/intermesh.yaml`; report its diagnostics as normal audit findings.
- [ ] If Intermesh is unavailable, mark manifest validation `SKIP` rather than WARN/FAIL and continue the existing audit unchanged.
- [ ] The absence of `intermesh.yaml` is not an audit finding unless the user explicitly requires Intermesh routing metadata.

## Output Format

```
Skill Audit: {skill-name}
──────────────────────────────
Structure:          {N}/6 pass
Invocation Control: {N}/4 pass
Content Quality:    {N}/5 pass
Anti-Patterns:      {N}/4 pass
──────────────────────────────
Overall: {PASS | WARN (N issues) | FAIL (N issues)}

Issues:
- [WARN] Description could be more specific
- [FAIL] Missing disable-model-invocation for deploy workflow
```
