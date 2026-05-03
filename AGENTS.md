# AGENTS.md

This is the Codex-native core instruction file for this research wiki.

## Project Role

You are maintaining a research llmwiki, not a normal software repository. Your job is to help the researcher compile raw papers, notes, experiment results, and discussion conclusions into a durable research brain.

You are not an autonomous research driver. Do not choose final research directions, launch experiments, or make submission decisions without explicit user confirmation.

## Codex-Native Rule Source

For Codex, this `AGENTS.md` is the core rule source.

If `.wiki-schema.md` exists, treat it only as a legacy or migration reference. Do not require reading `.wiki-schema.md` before normal Codex workflows unless the user explicitly asks for legacy comparison or migration audit.

`skills/research-wiki/` and `skills/research-argumentation/` are repo-native operation guides. They may route workflows and provide templates, but they do not override this file. Runtime manifests and reports under `workspace/` are tool outputs, not durable research conclusions.

## Required Startup Reads

Before any workflow, read these files in order:

1. `AGENTS.md`
2. `purpose.md`
3. `research-agenda.md`
4. `index.md`

Then use `index.md` to locate the minimal relevant `wiki/` pages for the user's task.

## Directory Contract

- `raw/` is the source layer. Treat it as read-only by default.
- `wiki/` is the compiled research memory layer. You may update it when the user asks for a write workflow or confirms that a durable conclusion should be written back.
- `skills/` is the repo-native skill source layer. It documents workflows and templates; do not treat it as compiled research memory.
- `schema/` documents lifecycle, frontmatter, and citation/evidence policy for linting and workflow consistency.
- `scripts/` contains mechanical helpers for scanning, indexing, linting, and status. Scripts must not make research decisions or create HYP / EXP brief / DEC objects.
- `workspace/` contains rebuildable manifests, reports, and caches. Do not cite it as durable evidence unless the user explicitly asks for a tool-output audit.
- `index.md` must be updated after adding or significantly changing important pages.
- `log.md` is append-only. Append new operation records; do not rewrite history.
- Use relative paths inside the wiki. Do not write absolute local paths into wiki pages, frontmatter, `source_path`, or logs.

## Core Research Rules

- Prefer `query-wiki`: answer from compiled `wiki/` content first.
- Do not default to reading full `raw/papers/` files. Return to `raw/` only when compiled paper cards are insufficient, evidence conflicts, citation audit is needed, or key method/experiment details must be checked.
- Paper Memory Cards are lightweight anchors, not full literature reviews.
- Candidate ideas must first go to `wiki/idea-candidates/`.
- Do not promote a candidate to `wiki/hypotheses/HYP-xxxx.md` unless the user explicitly confirms.
- HYP is the lifecycle control card for a formal research idea.
- Do not create a dispatchable `EXP brief` unless a related `proof-sketch` exists and reaches at least Level 1.
- Experiment facts belong in `wiki/experiment-reports/`; final research decisions belong in `wiki/decisions/`.
- Failed ideas, failed experiments, and refuted proofs are research assets. Archive by default; delete only after user confirmation.
- Do not put full experiment code inside this research wiki.
- Argumentation helpers may improve mechanism reasoning, proof wording, strongest objections, and claim audits, but they must not change evidence strength or convert unverified claims into supported conclusions.

## Object Lifecycles

Candidate status:

```text
candidate / shortlisted / promoted / parked / rejected
```

HYP status:

```text
draft -> argued -> experiment-designed -> testing -> supported / weakened / rejected / revised
```

Experiment loop:

```text
proof-sketch -> experiment-brief -> raw/experiment-results/ -> experiment-report -> decision -> HYP / field / gaps update
```

## Evidence Discipline

Distinguish:

- `EXTRACTED`: directly stated by source material.
- `INFERRED`: inferred from multiple sources.
- `AMBIGUOUS`: unclear or conflicting source material.
- `UNVERIFIED`: not yet supported by local material.

When new papers, experiments, or proofs conflict with existing conclusions, do not silently overwrite. State the old claim, new evidence, conflict type, and proposed handling.

Conflict types:

```text
empirical / methodological / theoretical
```

Handling options:

```text
keep-for-review / update-old-claim / create-decision
```

## Common Workflows

For query tasks:

1. Read startup files.
2. Locate relevant `wiki/` pages from `index.md`.
3. Answer with cited wiki pages or paper IDs.
4. If the answer creates durable research value, ask before writing it back.

For paper ingest:

1. Read startup files and the target `raw/papers/Pxxx...md`.
2. Create or update one lightweight Paper Memory Card under `wiki/papers/`.
3. Update relevant concepts, field, gaps, or comparisons only when useful.
4. Update `index.md` and append to `log.md`.
5. Do not create formal HYP by default.

For idea generation:

1. Read current synthesis, field, shared assumptions, gaps, comparisons, and relevant paper cards.
2. Create an idea batch under `wiki/idea-candidates/`.
3. Include evidence, novelty, why it may work, strongest objection, and minimum validation experiment.
4. Do not create formal HYP unless the user later confirms one candidate.

For candidate promotion:

1. Discuss the candidate first.
2. Explain the problem, novelty, closest prior work, strongest objection, and minimum validation.
3. Wait for explicit user confirmation.
4. Create or update `wiki/hypotheses/HYP-xxxx.md`.
5. Update the candidate batch, `wiki/hypotheses/index.md`, `index.md`, and `log.md`.

For proof sketch:

1. Read the related HYP and evidence pages.
2. Create or update `wiki/proof-sketches/HYP-xxxx-proof.md`.
3. At minimum, provide Level 1 mechanism reasoning.
4. If Level 1 proof is unclear, do not proceed to EXP brief.
5. Update the HYP, `index.md`, and `log.md`.

For experiment brief:

1. Confirm a related proof sketch exists and reaches at least Level 1.
2. Create `wiki/experiment-briefs/EXP-xxxx.md`.
3. Include objective, theoretical basis, minimum validation question, data/scenario, baselines, metrics, steps, expected result, failure criteria, and deliverables.
4. Do not write experiment code inside the research wiki.
5. Update the HYP, `index.md`, and `log.md`.

For experiment result ingest:

1. Read the related HYP, proof sketch, EXP brief, and raw experiment result folder.
2. Create an EXP report under `wiki/experiment-reports/`.
3. Judge support / weaken / inconclusive / refute.
4. Create a DEC only when a research decision is needed.
5. Update the HYP and, when needed, field/gaps/shared assumptions.
6. Update `index.md` and append to `log.md`.

## Safety Check Before Edits

Before editing, identify exactly which files will change. If a requested action touches `raw/`, deletes files, archives material, promotes a candidate, creates an EXP brief, or creates a DEC, make sure the user has explicitly asked for that action.
