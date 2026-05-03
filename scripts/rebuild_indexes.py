from __future__ import annotations

import subprocess
import sys
from collections import Counter, defaultdict

from common import ROOT, markdown_files, page_record, rel, write_json


def build_indexes() -> dict:
    pages = [page_record(path) for path in markdown_files(ROOT / "wiki")]
    by_type: dict[str, list[dict]] = defaultdict(list)
    for page in pages:
        by_type[str(page.get("type") or "page")].append(page)
    summary = {
        "total_pages": len(pages),
        "by_type": dict(sorted(Counter(page.get("type") for page in pages).items())),
        "paths_by_type": {
            key: [record["path"] for record in records]
            for key, records in sorted(by_type.items())
        },
    }
    return {"pages": pages, "summary": summary}


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / "scan_sources.py")], cwd=ROOT, check=True)
    data = build_indexes()
    out = ROOT / "workspace" / "manifests"
    write_json(out / "wiki_index.json", data)
    print(f"Indexed {data['summary']['total_pages']} wiki pages.")
    print(f"Wrote {rel(out / 'wiki_index.json')}")


if __name__ == "__main__":
    main()

