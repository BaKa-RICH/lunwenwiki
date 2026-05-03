# Page Frontmatter Schema

This schema describes minimum frontmatter fields for durable wiki pages. Paths
must be relative to the repository root.

## Paper Memory Card

Required:

- `type: paper`
- `paper_id`
- `title`
- `source_path`
- `status`
- `confidence`
- `last_updated`

## Idea Batch

Required:

- `type: idea-batch`
- `topic`
- `status`
- `source_pages`
- `promoted_hypotheses`

## HYP

Required:

- `type: hypothesis`
- `hypothesis_id`
- `origin_candidate`
- `status`
- `related_proof_sketches`
- `related_experiments`
- `related_decisions`

## Proof Sketch

Required:

- `type: proof-sketch`
- `related_hypothesis`
- `level`
- `status`
- `source_pages`

## EXP Brief

Required:

- `type: experiment-brief`
- `experiment_id`
- `related_hypothesis`
- `related_proof_sketch`
- `status`

## EXP Report

Required:

- `type: experiment-report`
- `experiment_id`
- `related_hypothesis`
- `result`
- `source_path`

## DEC

Required:

- `type: decision`
- `decision_id`
- `related_hypothesis`
- `decision`
- `evidence`

