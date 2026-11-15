"""Dependency-free checks for README, licensing and tracked secret filenames."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess


def tracked_paths(root: Path) -> list[str]:
    """Read only Git-tracked names; never inspect personal untracked data."""
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z"],
            capture_output=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return []
    return [p.decode("utf-8", errors="replace") for p in result.stdout.split(b"\0") if p]


def inspect(root: Path) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    readme, license_file = root / "README.md", root / "LICENSE"
    if not readme.is_file():
        errors.append("README.md is missing")
    else:
        content = readme.read_text(encoding="utf-8")
        if not re.search(r"(?m)^#\s+\S+", content):
            errors.append("README.md has no project title")
        if len(content.strip()) < 120:
            errors.append("README.md needs a meaningful project description")
        if "[LICENSE](LICENSE)" not in content:
            errors.append("README.md must link to LICENSE")
    if not license_file.is_file():
        errors.append("LICENSE is missing")
    else:
        terms = license_file.read_text(encoding="utf-8")
        if not any(x in terms for x in ("MIT License", "All rights reserved")):
            warnings.append("Review non-standard license terms manually")
        if "Copyright" not in terms:
            warnings.append("LICENSE lacks an explicit copyright notice")
    for path in tracked_paths(root):
        base = Path(path).name.lower()
        if base in {".env", ".env.local", ".env.production", "id_rsa", "id_ed25519"}:
            errors.append(f"Potential secret file is tracked: {path}")
    return {"repository": root.name, "ok": not errors, "errors": errors, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = inspect(args.root.resolve())
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Repository quality gate: {'PASS' if result['ok'] else 'FAIL'} ({result['repository']})")
        for item in result["errors"]:
            print(f"ERROR: {item}")
        for item in result["warnings"]:
            print(f"WARNING: {item}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
