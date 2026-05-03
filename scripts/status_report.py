from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

from common import ROOT, markdown_files, page_record, rel, today, write_text


def count_unique_ids(path: Path, pattern: str) -> int:
    if not path.exists():
        return 0
    text = path.read_text(encoding="utf-8", errors="replace")
    return len(set(re.findall(pattern, text)))


def count_pages() -> dict[str, int]:
    return {
        "paper_cards": len(markdown_files(ROOT / "wiki" / "papers")),
        "concepts": len(markdown_files(ROOT / "wiki" / "concepts")),
        "confirmed_gaps": count_unique_ids(ROOT / "wiki" / "gaps" / "confirmed-gaps.md", r"\bGAP-\d{4}\b"),
        "open_questions": count_unique_ids(ROOT / "wiki" / "gaps" / "open-questions.md", r"\bOQ-\d{4}\b"),
        "idea_batches": len(markdown_files(ROOT / "wiki" / "idea-candidates")),
        "hypotheses": len([p for p in markdown_files(ROOT / "wiki" / "hypotheses") if p.name != "index.md"]),
        "proof_sketches": len(markdown_files(ROOT / "wiki" / "proof-sketches")),
        "experiment_briefs": len(markdown_files(ROOT / "wiki" / "experiment-briefs")),
        "experiment_reports": len(markdown_files(ROOT / "wiki" / "experiment-reports")),
        "decisions": len(markdown_files(ROOT / "wiki" / "decisions")),
        "synthesis": len(markdown_files(ROOT / "wiki" / "synthesis")),
    }


def status_distribution(root: Path) -> dict[str, int]:
    values = Counter()
    for path in markdown_files(root):
        if path.name == "index.md":
            continue
        fm = page_record(path).get("frontmatter", {})
        status = str(fm.get("status") or fm.get("result") or fm.get("decision") or "unknown")
        values[status] += 1
    return dict(sorted(values.items()))


def recent_log_lines(limit: int = 12) -> list[str]:
    path = ROOT / "log.md"
    if not path.exists():
        return []
    lines = [line for line in path.read_text(encoding="utf-8", errors="replace").splitlines() if line.strip()]
    return lines[-limit:]


def render_log_line(line: str) -> str:
    if line.startswith("#"):
        return line
    return f"- {line.removeprefix('- ').strip()}"


def lint_summary() -> dict[str, int]:
    path = ROOT / "workspace" / "manifests" / "lint_report.json"
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return data.get("summary", {})


def render() -> str:
    counts = count_pages()
    lines = [
        f"# Research Wiki Status: {today()}",
        "",
        "## Object Counts",
        "",
    ]
    for key, value in counts.items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## HYP Status Distribution", ""])
    hyp_status = status_distribution(ROOT / "wiki" / "hypotheses")
    if hyp_status:
        for key, value in hyp_status.items():
            lines.append(f"- {key}: {value}")
    else:
        lines.append("- None")
    lines.extend(["", "## Experiment Report Results", ""])
    exp_status = status_distribution(ROOT / "wiki" / "experiment-reports")
    if exp_status:
        for key, value in exp_status.items():
            lines.append(f"- {key}: {value}")
    else:
        lines.append("- None")
    lines.extend(["", "## Lint Summary", ""])
    summary = lint_summary()
    if summary:
        for key, value in summary.items():
            lines.append(f"- {key}: {value}")
    else:
        lines.append("- No lint report found.")
    lines.extend(["", "## Recent Log", ""])
    for line in recent_log_lines():
        lines.append(render_log_line(line))
    return "\n".join(lines) + "\n"


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / "scan_sources.py")], cwd=ROOT, check=True)
    report_path = ROOT / "workspace" / "reports" / "status" / f"status-{today()}.md"
    write_text(report_path, render())
    print(f"Wrote {rel(report_path)}")


if __name__ == "__main__":
    main()
