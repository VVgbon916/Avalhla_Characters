#!/usr/bin/env python3
"""Deterministic CrossWorld repository contract checker. Stdlib only."""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {"record_type", "concept_id", "canonical_name", "scope", "status", "description"}
RECORD_TYPES = {
    "ENTITY", "PRESENCE", "ASPECT", "BOND", "WORLD",
    "DOOR", "CROSSING", "SKILL", "CRAFT", "OBJECT", "COLOR",
}
STATUSES = {"CANONICAL", "TARGET", "LEGACY", "DERIVED"}

DIR_TYPES = {
    "PRESENCES": "PRESENCE",
    "ASPECTS": "ASPECT",
    "BONDS": "BOND",
    "WORLDS": "WORLD",
    "DOORS": "DOOR",
    "CROSSINGS": "CROSSING",
    "SKILLS": "SKILL",
    "CRAFTS": "CRAFT",
    "OBJECTS": "OBJECT",
    "COLORS": "COLOR",
    "ENTITIES": "ENTITY",
}

LEGACY_PATHS = {
    Path("CANON/ARTIFACTS"),
    Path("CANON/EQUIPMENT"),
    Path("CANON/RELATIONSHIPS"),
    Path("CROSSINGS"),
    Path("docs/AVVA_VISUAL_GRAMMAR.md"),
}

def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    
def main() -> int:
    errors: list[str] = []
    records: list[tuple[Path, dict]] = []
    ids: dict[str, Path] = {}
    names: dict[tuple[str, str], Path] = {}

    json_files = sorted(p for p in ROOT.rglob("*.json") if ".git" not in p.parts)
    for path in json_files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path}: invalid JSON: {exc}")
            continue

        if path.parent.name == "schema":
            continue

        if "record_type" not in data:
            continue

        missing = REQUIRED - set(data)
        if missing:
            errors.append(f"{path}: missing required fields: {sorted(missing)}")
            continue

        record_type = data["record_type"]
        status = data["status"]

        if record_type not in RECORD_TYPES:
            errors.append(f"{path}: unknown record_type={record_type!r}")
        if status not in STATUSES:
            errors.append(f"{path}: unknown status={status!r}")

        concept_id = data["concept_id"]
        scope = data["scope"]
        canonical_name = data["canonical_name"]

        if concept_id in ids:
            errors.append(f"{path}: duplicate concept_id {concept_id!r}; first={ids[concept_id]}")
        else:
            ids[concept_id] = path

        key = (scope, canonical_name)
        if key in names:
            errors.append(
                f"{path}: duplicate canonical_name {canonical_name!r} in scope {scope!r}; first={names[key]}"
            )
        else:
            names[key] = path

        expected = DIR_TYPES.get(path.parent.name)
        if expected and record_type != expected:
            errors.append(f"{path}: directory {path.parent.name} expects {expected}, found {record_type}")

        aliases = data.get("aliases", [])
        if len(aliases) != len(set(aliases)):
            errors.append(f"{path}: duplicate aliases")

        records.append((path, data))

    for path in LEGACY_PATHS:
        if (ROOT / path).exists():
            errors.append(f"forbidden legacy path remains: {path}")

    cobuild_like = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        name = path.name.upper()
        if any(token in name for token in ("COBUILD", "COBUILDER", "AI_CONTEXT", "OPERATING_LAW")):
            cobuild_like.append(path)
    for path in cobuild_like:
        errors.append(f"competing CoBuilder/operating-law artifact in domain repo: {path.relative_to(ROOT)}")

    for path, data in records:
        for rel in data.get("relations", []):
            target = rel.get("target_concept_id")
            if not target:
                errors.append(f"{path}: relation missing target_concept_id")
            elif target not in ids:
                errors.append(f"{path}: orphan relation target {target!r}")

    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if " " in path.name:
            errors.append(f"filename contains spaces: {rel}")
        if "\\" in path.name:
            errors.append(f"filename contains a literal backslash: {rel}")

    for schema in (ROOT / "schema").glob("*.json"):
        try:
            json.loads(schema.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{schema}: invalid schema JSON: {exc}")

    visual = ROOT / "docs/AvvA_VISUAL_GRAMMAR.md"
    if not visual.exists():
        errors.append("missing canonical AvvA visual grammar")
    else:
        text = visual.read_text(encoding="utf-8")
        for marker in ("THE RELATION SURVIVES THE SKIN.", "second l", "vv", "Dawa <"):
            if marker not in text:
                errors.append(f"{visual}: missing visual grammar marker {marker!r}")

    if errors:
        for error in errors:
            fail(error)
        print(f"\nRESULT: FAIL ({len(errors)} finding(s))")
        return 1

    print(f"RECORDS={len(records)}")
    print(f"CONCEPT_IDS={len(ids)}")
    print(f"SCOPED_NAMES={len(names)}")
    print("RESULT: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
