# Light Orchestration V1

Use this reference when query, research lookup, or synthesis-lite work risks
making the main agent read too many wiki pages. The goal is context relief, not
a heavy autonomous multi-agent system.

## Purpose

The main agent should keep the high-leverage work: understanding the user goal,
building the source set, enforcing evidence and lifecycle boundaries, and
writing the final answer. Helper subagents are optional read-only assistants
that help shrink or compress context before the main agent answers.

V1 is for:

- query
- research lookup
- synthesis-lite

V1 is not for rewriting ingest, promoting candidates, creating HYP records,
proof sketches, EXP briefs, EXP reports, DEC records, or running experiments.

## Role Split

Main agent:

- Decide the task kind and whether helper work is useful.
- Read the startup files and use `index.md` plus `workspace/manifests/` to
  construct the smallest plausible source set.
- Decide whether `raw/` access is justified.
- Review helper output for evidence labels, uncertainty, and lifecycle safety.
- Produce the final user-facing answer and only suggest durable write-back
  targets unless the user requested a write workflow.

`scout`:

- Perform read-only source narrowing.
- Prefer `index.md`, `research-agenda.md`, and these manifests:
  `workspace/manifests/wiki_index.json`,
  `workspace/manifests/wiki_pages.json`, and
  `workspace/manifests/paper_cards.json`.
- Avoid full wiki page reads unless needed to disambiguate the shortlist.
- Return included, skipped, and uncertain sources with brief reasons.

`reader-synthesizer`:

- Read only the 3-8 wiki pages or paper cards assigned by the main agent.
- Return an evidence-aware summary packet, comparison table, conflict note, or
  synthesis draft as requested.
- Keep `EXTRACTED`, `INFERRED`, `AMBIGUOUS`, and `UNVERIFIED` claims separate.
- Do not decide final research conclusions or durable write-back.

Do not create a separate `integrator` role in V1. The main agent should do the
final integration so the answer keeps one evidence boundary and one lifecycle
boundary.

## When To Use

Do not use helper subagents when:

- The user asks about one known paper card, concept page, gap page, or
  comparison page.
- `index.md` and the manifests already reduce the source set to a few obvious
  pages.
- The question is a single-page lookup.

Use only `scout` when:

- The user asks which pages, paper cards, or open questions are relevant to a
  method axis or topic.
- The candidate sources cross page types and the main agent cannot safely pick
  the minimal set from the startup files alone.
- The first need is source-set narrowing, not synthesis.

Use `scout` followed by `reader-synthesizer` when:

- The user asks to compare several method families.
- The answer requires a small field synthesis across multiple wiki objects.
- The user asks for gap or idea directions from existing compiled memory, but
  the workflow must not create or promote lifecycle objects.
- The relevant evidence is distributed enough that the main agent would
  otherwise carry many pages in context.

## Default Startup Context

Give helper subagents only what they need for their step. Do not clone the
main agent's whole context into every helper.

- Shared rule excerpts should cover `AGENTS.md` boundaries, the user goal, and
  the relevant task workflow.
- `scout` should receive the user question, the relevant startup excerpts, and
  manifest/index access. It should not default to reading `wiki/` bodies.
- `reader-synthesizer` should receive the selected source set and the evidence
  labeling rules. It should not search broadly after dispatch.
- `raw/` is not exposed unless the main agent explicitly opens it for a listed
  trigger.

The main agent should keep the final context focused on the source shortlist
and the helper's compressed packet, not copied source text.

## Soft Dispatch Contract

When assigning helper work, include these fields in plain language:

```text
task_kind:
user_goal:
startup_context:
source_set:
allowed_paths:
raw_access:
evidence_policy:
output_format:
write_policy:
```

Recommended defaults:

- `raw_access: false`
- `write_policy: read-only draft only`
- `output_format: Evidence-Aware Summary Packet`
- `allowed_paths: index.md, research-agenda.md, workspace/manifests/, and the
  explicitly selected wiki pages`

## Raw Access Triggers

Keep `raw/` closed by default. The main agent may explicitly allow a helper to
inspect `raw/` only when at least one trigger applies:

- A paper card is insufficient for the user's question.
- Existing compiled claims conflict and need evidence audit.
- The user asks for citation audit.
- A key method or experiment detail is missing from compiled memory.

When `raw/` is opened, state the trigger and keep the allowed raw paths narrow.
Do not let raw evidence silently replace compiled wiki memory in the final
answer.

## V1 Boundaries

- Helper subagents do not edit `wiki/`, `index.md`, or `log.md`.
- Helper subagents do not create, promote, or update candidate, HYP, proof,
  EXP, report, or DEC objects.
- Helper subagents do not raise evidence strength.
- `workspace/` manifests support routing and source narrowing, but they are
  not durable research evidence.
- V1 does not add an automatic dispatcher, dispatch validator, schema, lint
  rule, or script.
- The main agent may suggest possible write-back targets, but durable writes
  require a user-requested write workflow or explicit confirmation.
