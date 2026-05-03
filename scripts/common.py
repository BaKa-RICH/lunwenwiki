from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_json(path: Path, data: Any) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    ensure_dir(path.parent)
    path.write_text(text, encoding="utf-8")


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def parse_frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---"):
        return {}
    match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.S)
    if not match:
        return {}
    fields: dict[str, Any] = {}
    lines = match.group(1).splitlines()
    current_key: str | None = None
    current_list: list[str] | None = None
    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.lstrip().startswith("- ") and current_key and current_list is not None:
            current_list.append(clean_scalar(line.lstrip()[2:]))
            fields[current_key] = current_list
            continue
        key_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not key_match:
            continue
        key, value = key_match.group(1), key_match.group(2).strip()
        current_key = key
        if value == "":
            current_list = []
            fields[key] = current_list
        else:
            current_list = None
            if value.startswith("[") and value.endswith("]"):
                body = value[1:-1].strip()
                if not body:
                    fields[key] = []
                else:
                    fields[key] = [clean_scalar(part.strip()) for part in body.split(",")]
            else:
                fields[key] = clean_scalar(value)
    return fields


def clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def title_from_markdown(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, re.M)
    return match.group(1).strip() if match else fallback


def wiki_links(text: str) -> list[str]:
    return sorted(set(match.group(1).split("|", 1)[0].strip() for match in re.finditer(r"\[\[([^\]]+)\]\]", text)))


def markdown_files(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def page_record(path: Path) -> dict[str, Any]:
    text = read_text(path)
    fm = parse_frontmatter(text)
    return {
        "path": rel(path),
        "type": str(fm.get("type") or infer_type_from_path(path)),
        "id": str(
            fm.get("paper_id")
            or fm.get("hypothesis_id")
            or fm.get("experiment_id")
            or fm.get("decision_id")
            or path.stem
        ),
        "title": str(fm.get("title") or title_from_markdown(text, path.stem)),
        "frontmatter": fm,
        "links": wiki_links(text),
    }


def infer_type_from_path(path: Path) -> str:
    parts = path.relative_to(ROOT).parts
    if len(parts) < 2:
        return "page"
    if parts[0] == "wiki":
        mapping = {
            "papers": "paper",
            "concepts": "concept",
            "gaps": "gap",
            "hypotheses": "hypothesis",
            "proof-sketches": "proof-sketch",
            "experiment-briefs": "experiment-brief",
            "experiment-reports": "experiment-report",
            "decisions": "decision",
            "synthesis": "synthesis",
        }
        return mapping.get(parts[1], parts[1])
    return "page"


def resolve_wiki_link(link: str) -> Path | None:
    target = link.strip()
    if not target:
        return None
    target = target.split("#", 1)[0].strip()
    if not target:
        return None
    candidates: list[Path] = []
    raw = target.replace("\\", "/")
    if raw.endswith(".md"):
        candidates.append(ROOT / raw)
    else:
        candidates.append(ROOT / f"{raw}.md")
        candidates.append(ROOT / raw)
        candidates.extend((ROOT / "wiki").rglob(f"{Path(raw).name}.md"))
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None

