# Query Workflow

Use this workflow when the user asks a question about the research state.

## Steps

1. Read the required startup files: `AGENTS.md`, `purpose.md`,
   `research-agenda.md`, and `index.md`.
2. Classify the request as `lookup`, `compare`, `gap scan`, or
   `synthesis-lite`.
3. Use `index.md` and `workspace/manifests/` when available to locate the
   smallest relevant set of `wiki/` pages.
4. If the source set is a single paper card or a few obvious pages, answer
   directly from compiled wiki memory.
5. If the candidate set is broad, crosses page types, or remains uncertain,
   use `references/light-orchestration.md`:
   - use `scout` when the next step is source-set narrowing;
   - use `reader-synthesizer` only after the source set is narrowed.
6. Return to `raw/` only when a paper card is insufficient, evidence conflicts,
   citation audit is requested, or method/experiment details must be checked.
7. Cite wiki pages or paper IDs in the answer.
8. If the answer creates durable research value, ask before writing it back.

## Output

Keep the answer short and evidence-aware:

- direct answer
- evidence pages or paper IDs
- uncertainty or conflict, if any
- possible durable write-back target, only if useful

If helper subagents were used, answer from their compressed summary packet and
the cited source set. Do not paste large source-page excerpts back into the
main context.
