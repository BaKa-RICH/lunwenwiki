# Output Formats

## Query Answer

```text
Answer:
Evidence:
Uncertainty:
Possible write-back:
```

## Evidence-Aware Summary Packet

Use this as a compact helper-subagent return format for query, research
lookup, and synthesis-lite. It is not a durable wiki schema.

```text
Direct answer:
Sources used:
Key extracted claims:
Inferred points:
Uncertainties or conflicts:
Possible write-back targets:
```

## Candidate Review

```text
Problem:
Mechanism:
Evidence:
Novelty:
Strongest objection:
Minimum validation:
Recommendation:
```

## Health Check

```text
Summary:
Broken links:
Lifecycle gaps:
Index gaps:
Recommended next actions:
```

Keep final user-facing output concise. Put durable research details in wiki
pages, not chat prose, when the user asks for a write workflow.
