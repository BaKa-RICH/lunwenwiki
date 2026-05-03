# Maintenance Workflow

Use this workflow for non-destructive health checks.

## Status

Run `python scripts/status_report.py` to summarize:

- paper cards
- concepts
- gaps and open questions
- idea batches
- hypotheses and status distribution
- experiment briefs/reports
- decisions
- recent log entries
- lint summary when available

## Lint

Run `python scripts/lint_wiki.py` to check:

- paper cards with missing `source_path`
- raw papers without paper cards
- obvious broken wiki links
- HYP records with missing proof/EXP/DEC links
- EXP briefs without proof sketches
- EXP reports not reflected in HYP
- DEC records without HYP or EXP evidence
- likely `index.md` omissions

## Rebuild Indexes

Run `python scripts/rebuild_indexes.py` to rebuild machine-readable manifests
under `workspace/manifests/`. This must not edit `index.md` automatically.

