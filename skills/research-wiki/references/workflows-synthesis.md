# Synthesis Workflow

Use this workflow for mini-synthesis, batch synthesis, field synthesis, concept
cleanup, gap consolidation, and source-quality audits.

## Evidence Rules

- Prefer compiled `wiki/` material.
- Use a source set or coverage note for multi-paper synthesis.
- Do not silently overwrite older claims. Record the old claim, new evidence,
  conflict type, and proposed handling.
- Do not inflate certainty. Mark claims as `EXTRACTED`, `INFERRED`,
  `AMBIGUOUS`, or `UNVERIFIED`.

## Steps

1. Define the source set.
2. Separate included, skipped, out-of-scope, and uncertain materials.
3. For broad or uncertain source sets, use
   `references/light-orchestration.md` as a context-saving route:
   - use `scout` to narrow candidate pages from `index.md` and
     `workspace/manifests/`;
   - use `reader-synthesizer` to compress the selected pages into an
     evidence-aware draft.
4. Summarize what changed in field understanding, shared assumptions, gaps,
   comparisons, or candidate idea signals.
5. Update only durable target pages when the user requested a write workflow.
6. Update `index.md` and append `log.md` for durable wiki changes.

For query or synthesis-lite work, helper subagents return drafts only. The main
agent decides whether any durable target page should be updated; helper output
does not itself become a research conclusion.

## Template

Use `assets/templates/field-synthesis.md` for field-level outputs.
