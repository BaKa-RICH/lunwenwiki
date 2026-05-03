from __future__ import annotations

from pathlib import Path

from common import ROOT, markdown_files, page_record, rel, write_json


def raw_paper_records() -> list[dict]:
    root = ROOT / "raw" / "papers"
    records = []
    for path in markdown_files(root):
        records.append(
            {
                "path": rel(path),
                "id_guess": path.stem.split("-", 1)[0],
                "name": path.name,
                "size_bytes": path.stat().st_size,
            }
        )
    return records


def wiki_page_records() -> list[dict]:
    return [page_record(path) for path in markdown_files(ROOT / "wiki")]


def paper_card_records(pages: list[dict]) -> list[dict]:
    return [page for page in pages if page.get("type") == "paper" or page.get("path", "").startswith("wiki/papers/")]


def lifecycle_records(pages: list[dict]) -> list[dict]:
    lifecycle_types = {
        "idea-batch",
        "hypothesis",
        "proof-sketch",
        "experiment-brief",
        "experiment-report",
        "decision",
    }
    return [
        page
        for page in pages
        if page.get("type") in lifecycle_types
        or any(f"/{part}/" in f"/{page.get('path', '')}" for part in ["idea-candidates", "hypotheses", "proof-sketches", "experiment-briefs", "experiment-reports", "decisions"])
    ]


def main() -> None:
    raw_papers = raw_paper_records()
    wiki_pages = wiki_page_records()
    paper_cards = paper_card_records(wiki_pages)
    lifecycle = lifecycle_records(wiki_pages)
    out = ROOT / "workspace" / "manifests"
    write_json(out / "raw_papers.json", raw_papers)
    write_json(out / "wiki_pages.json", wiki_pages)
    write_json(out / "paper_cards.json", paper_cards)
    write_json(out / "lifecycle_objects.json", lifecycle)
    print(f"Raw papers: {len(raw_papers)}")
    print(f"Wiki pages: {len(wiki_pages)}")
    print(f"Paper cards: {len(paper_cards)}")
    print(f"Lifecycle objects: {len(lifecycle)}")
    print(f"Wrote {rel(out)}")


if __name__ == "__main__":
    main()

