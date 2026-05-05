---
name: research-wiki
description: "Use for maintaining this research wiki: querying compiled wiki memory, ingesting raw papers into paper memory cards, synthesizing field knowledge, managing idea candidates, hypotheses, proof sketches, experiment briefs, experiment reports, decisions, and wiki health checks. Do not use for manuscript polishing, submission advice, figure design, or running experiments."
---

# research-wiki

This skill is the workflow router for the local research wiki. `AGENTS.md`
remains the highest-priority rule source. This skill explains how to execute
the workflows without expanding `AGENTS.md` into a long operations manual.

## Route By Task

| User intent | Read |
| --- | --- |
| Ask questions from the compiled wiki | `references/workflows-query.md` |
| Reduce main-agent context load during query or synthesis | `references/light-orchestration.md` |
| Ingest or update a paper memory card | `references/workflows-ingest.md` |
| Create or update field/concept/gap synthesis | `references/workflows-synthesis.md` |
| Generate candidates or promote a candidate to HYP | `references/workflows-idea-hypothesis.md` |
| Create proof, EXP brief, EXP report, or DEC | `references/workflows-proof-exp-decision.md` |
| Run status, lint, or rebuild machine indexes | `references/workflows-maintenance.md` |
| Check object schema and lifecycle rules | `references/schema.md` |
| Format user-facing output | `references/output-formats.md` |

## Light Orchestration (V1)

Use `references/light-orchestration.md` when query, research lookup, or
synthesis-lite work would otherwise make the main agent read a broad set of
wiki pages. The main agent still owns routing, source-set construction,
evidence and lifecycle boundaries, and the final answer. Helper subagents are
read-only draft producers: they may scout candidate sources or compress a
small assigned source set, but they do not write durable wiki pages.

Prefer `index.md` and `workspace/manifests/` before deeper page reads.
`raw/` access stays closed by default and is opened only for the trigger cases
listed in the light orchestration reference. Keep the final context centered
on source shortlists and evidence-aware summary packets, not copied page text.

## Hard Boundaries

- Do not promote a candidate to `wiki/hypotheses/HYP-xxxx.md` without explicit
  user confirmation.
- Do not create an EXP brief unless a related proof sketch exists and reaches at
  least Level 1.
- Do not create a DEC unless the user requests a research decision or the EXP
  report explicitly raises a decision need.
- Do not edit `raw/` by default.
- Do not run experiments or write experiment code in this wiki.
- Do not use this skill for language polishing, submission targeting, figure
  design, Word/LaTeX production, or manuscript drafting.

## Template Map

Use templates from `assets/templates/` when writing durable wiki pages. Keep
paths inside pages relative to the repository root.
