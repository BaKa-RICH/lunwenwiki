# Proof, Experiment, And Decision Workflow

This workflow is the core research closed loop.

## Closed Loop

```text
candidate discussion
-> explicit promotion
-> HYP
-> proof-sketch
-> EXP brief
-> raw/experiment-results/
-> EXP report
-> DEC when needed
-> HYP / field / gaps update
-> health check
```

## Proof Sketch

1. Read the related HYP and evidence pages.
2. Create or update `wiki/proof-sketches/HYP-xxxx-proof.md`.
3. Provide at least Level 1 mechanism reasoning.
4. If Level 1 is unclear, do not proceed to an EXP brief.
5. Update the HYP, `index.md`, and `log.md`.

## EXP Brief

1. Confirm a related proof sketch exists and reaches Level 1.
2. Create `wiki/experiment-briefs/EXP-xxxx.md`.
3. Include objective, theoretical basis, minimum validation question, data or
   scenario, baselines, metrics, steps, expected result, failure criteria, and
   deliverables.
4. Do not write experiment code inside the research wiki.

## EXP Report

1. Read the related HYP, proof sketch, EXP brief, and raw experiment result
   folder.
2. Create an EXP report under `wiki/experiment-reports/`.
3. Judge `supports`, `weakens`, `inconclusive`, or `refutes`.
4. Update the HYP and, when needed, field/gaps/shared assumptions.

## DEC

Create a DEC only when the user asks for a decision or the report creates a
research decision need. A DEC records continue, revise, park, or reject. It is
not a submission decision.

## Templates

- `assets/templates/proof-sketch.md`
- `assets/templates/exp-brief.md`
- `assets/templates/exp-report.md`
- `assets/templates/decision.md`

