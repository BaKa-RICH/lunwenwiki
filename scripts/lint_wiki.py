from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Any

from common import ROOT, markdown_files, page_record, rel, resolve_wiki_link, today, wiki_links, write_json, write_text


def load_pages() -> list[dict[str, Any]]:
    return [page_record(path) for path in markdown_files(ROOT / "wiki")]


def paper_source_issues(paper_cards: list[dict[str, Any]]) -> list[dict[str, str]]:
    issues = []
    for card in paper_cards:
        fm = card.get("frontmatter", {})
        source_path = str(fm.get("source_path") or "").strip()
        if not source_path:
            issues.append({"path": card["path"], "reason": "missing_source_path"})
            continue
        if not (ROOT / source_path).exists():
            issues.append({"path": card["path"], "source_path": source_path, "reason": "source_missing"})
    return issues


def raw_without_cards(raw_papers: list[Path], paper_cards: list[dict[str, Any]]) -> list[str]:
    sources = {
        str(card.get("frontmatter", {}).get("source_path") or "").replace("\\", "/")
        for card in paper_cards
    }
    missing = []
    for path in raw_papers:
        relative = rel(path)
        if relative not in sources:
            missing.append(relative)
    return sorted(missing)


def broken_links(pages: list[dict[str, Any]]) -> list[dict[str, str]]:
    issues = []
    for page in pages:
        path = ROOT / page["path"]
        for link in wiki_links(path.read_text(encoding="utf-8", errors="replace")):
            if resolve_wiki_link(link) is None:
                issues.append({"path": page["path"], "link": link})
    return issues


def lifecycle_issues(pages: list[dict[str, Any]]) -> list[dict[str, str]]:
    issues: list[dict[str, str]] = []
    by_path = {page["path"]: page for page in pages}
    hypotheses = [page for page in pages if page["path"].startswith("wiki/hypotheses/") and page["path"] != "wiki/hypotheses/index.md"]
    proof_paths = {page["path"] for page in pages if page["path"].startswith("wiki/proof-sketches/")}
    exp_briefs = [page for page in pages if page["path"].startswith("wiki/experiment-briefs/")]
    exp_reports = [page for page in pages if page["path"].startswith("wiki/experiment-reports/")]
    decisions = [page for page in pages if page["path"].startswith("wiki/decisions/")]

    for hyp in hypotheses:
        fm = hyp.get("frontmatter", {})
        if str(fm.get("status") or "").strip() in {"experiment-designed", "testing", "supported", "weakened", "rejected", "revised"}:
            related = fm.get("related_proof_sketches") or []
            if not related and not proof_paths:
                issues.append({"path": hyp["path"], "reason": "advanced_hyp_missing_proof_reference"})

    for brief in exp_briefs:
        fm = brief.get("frontmatter", {})
        proof = str(fm.get("related_proof_sketch") or "").strip()
        if not proof:
            issues.append({"path": brief["path"], "reason": "experiment_brief_missing_related_proof_sketch"})

    for report in exp_reports:
        fm = report.get("frontmatter", {})
        hyp = str(fm.get("related_hypothesis") or "").strip()
        if not hyp:
            issues.append({"path": report["path"], "reason": "experiment_report_missing_related_hypothesis"})

    for dec in decisions:
        fm = dec.get("frontmatter", {})
        if not str(fm.get("related_hypothesis") or "").strip():
            issues.append({"path": dec["path"], "reason": "decision_missing_related_hypothesis"})
        if not str(fm.get("decision") or "").strip():
            issues.append({"path": dec["path"], "reason": "decision_missing_decision_value"})
    return issues


def index_omissions(pages: list[dict[str, Any]]) -> list[str]:
    index_text = (ROOT / "index.md").read_text(encoding="utf-8", errors="replace")
    important_roots = (
        "wiki/papers/",
        "wiki/concepts/",
        "wiki/comparisons/",
        "wiki/field/",
        "wiki/gaps/",
        "wiki/synthesis/",
        "wiki/hypotheses/",
        "wiki/proof-sketches/",
        "wiki/experiment-briefs/",
        "wiki/experiment-reports/",
        "wiki/decisions/",
    )
    missing = []
    for page in pages:
        path = page["path"]
        if path == "wiki/hypotheses/index.md":
            continue
        if path.startswith(important_roots):
            stem_link = path[:-3] if path.endswith(".md") else path
            if stem_link not in index_text and Path(path).stem not in index_text:
                missing.append(path)
    return sorted(missing)


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        f"# Research Wiki Lint Report: {payload['date']}",
        "",
        "## Summary",
        "",
    ]
    for key, value in payload["summary"].items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    for title, items in payload["findings"].items():
        lines.extend([f"## {title}", ""])
        if not items:
            lines.extend(["- None", ""])
            continue
        for item in items[:50]:
            lines.append(f"- {item}")
        if len(items) > 50:
            lines.append(f"- ... {len(items) - 50} more")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / "scan_sources.py")], cwd=ROOT, check=True)
    pages = load_pages()
    paper_cards = [page for page in pages if page["path"].startswith("wiki/papers/")]
    raw_papers = markdown_files(ROOT / "raw" / "papers")
    findings = {
        "paper_source_issues": paper_source_issues(paper_cards),
        "raw_papers_without_cards": raw_without_cards(raw_papers, paper_cards),
        "broken_wiki_links": broken_links(pages),
        "lifecycle_issues": lifecycle_issues(pages),
        "possible_index_omissions": index_omissions(pages),
    }
    summary = {key: len(value) for key, value in findings.items()}
    payload = {"date": today(), "summary": summary, "findings": findings}
    manifest_path = ROOT / "workspace" / "manifests" / "lint_report.json"
    report_path = ROOT / "workspace" / "reports" / "lint" / f"lint-{today()}.md"
    write_json(manifest_path, payload)
    write_text(report_path, render_markdown(payload))
    print(f"Wrote {rel(manifest_path)}")
    print(f"Wrote {rel(report_path)}")
    for key, count in summary.items():
        print(f"{key}: {count}")


if __name__ == "__main__":
    main()

