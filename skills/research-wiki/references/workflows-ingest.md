# Paper Ingest Workflow

Use this workflow when the user asks to ingest or update a paper.

## Preconditions

- The target source must be under `raw/papers/`.
- Treat `raw/` as read-only unless the user explicitly requests a raw-layer
  change.

## Steps

1. Read startup files.
2. Read the target raw paper only after identifying the target.
3. Create or update one lightweight paper memory card under `wiki/papers/`.
4. Add or update concepts, comparisons, field notes, gaps, or open questions
   only when they carry durable cross-paper value.
5. Distinguish `EXTRACTED`, `INFERRED`, `AMBIGUOUS`, and `UNVERIFIED`.
6. Update `index.md` when an important page is added or materially changed.
7. Append a concise entry to `log.md`.
8. Do not create a formal HYP by default.

## Template

Use `assets/templates/paper-memory-card.md`.

