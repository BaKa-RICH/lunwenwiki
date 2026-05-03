# Research Wiki Lifecycle Schema

This document defines the minimal lifecycle vocabulary for the research wiki.
`AGENTS.md` remains the highest-priority rule source.

## Candidate Status

```text
candidate / shortlisted / promoted / parked / rejected
```

- `candidate`: proposed but not yet selected.
- `shortlisted`: worth discussion before promotion.
- `promoted`: explicitly promoted to a formal HYP.
- `parked`: preserved for possible later use.
- `rejected`: rejected but retained as a research asset.

## HYP Status

```text
draft -> argued -> experiment-designed -> testing -> supported / weakened / rejected / revised
```

- `draft`: formal HYP exists, but argument is incomplete.
- `argued`: problem, mechanism, evidence, and objections have been discussed.
- `experiment-designed`: at least one EXP brief exists.
- `testing`: experiment is running or awaiting result ingest.
- `supported`: current evidence supports the HYP.
- `weakened`: current evidence partially weakens the HYP.
- `rejected`: evidence refutes the HYP.
- `revised`: HYP has been materially reframed after feedback.

## Experiment Report Result

```text
supports / weakens / inconclusive / refutes
```

Use `supports` only when the result directly supports the HYP mechanism. Use
`weakens` when it partially supports the mechanism but exposes important limits,
tradeoffs, or failures.

## Decision Values

```text
continue / revise / park / reject
```

DEC records are research decisions, not submission decisions.

## Closed Loop

```text
candidate -> HYP -> proof-sketch -> experiment-brief -> raw/experiment-results/
-> experiment-report -> decision -> HYP / field / gaps update
```

Do not create an EXP brief unless the related proof sketch reaches at least
Level 1.

