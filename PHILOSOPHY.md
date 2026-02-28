# interplug Philosophy

## Purpose
Plugin development toolkit — lifecycle management, structure validation, and troubleshooting for Claude Code plugins. Extracted from interdev.

## North Star
Zero friction from idea to published plugin.

## Working Priorities
- Structure validation accuracy
- Lifecycle completeness (create → test → publish)
- Troubleshooting clarity

## Brainstorming Doctrine
1. Start from outcomes and failure modes, not implementation details.
2. Generate at least three options: conservative, balanced, and aggressive.
3. Explicitly call out assumptions, unknowns, and dependency risk across modules.
4. Prefer ideas that improve clarity, reversibility, and operational visibility.

## Planning Doctrine
1. Convert selected direction into small, testable, reversible slices.
2. Define acceptance criteria, verification steps, and rollback path for each slice.
3. Sequence dependencies explicitly and keep integration contracts narrow.
4. Reserve optimization work until correctness and reliability are proven.

## Decision Filters
- Does this reduce time from idea to working plugin?
- Does this catch structural errors before publish?
- Is the error message actionable?
- Does this work for both new and experienced plugin authors?
