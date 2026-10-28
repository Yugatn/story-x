#!/usr/bin/env python3
"""Create and verify a full Git history backup outside the repository."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

def git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args], check=True, text=True, capture_output=True).stdout.strip()

def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def verify(dest):
    meta = json.loads((dest / "bundle-manifest.json").read_text(encoding="utf-8"))
    bundle = dest / "repository.bundle"
    if sha256(bundle) != meta["sha256"]:
        raise ValueError("Bundle checksum mismatch")
    with tempfile.TemporaryDirectory() as verify_dir:
        subprocess.run(["git", "init", "-q", verify_dir], check=True, capture_output=True)
        subprocess.run(["git", "-C", verify_dir, "bundle", "verify", str(bundle)], check=True, capture_output=True)
    with tempfile.TemporaryDirectory() as temp:
        subprocess.run(["git", "clone", "--quiet", str(bundle), temp], check=True, capture_output=True)
        actual = git(Path(temp), "rev-parse", "HEAD")
        if actual != meta["head"]:
            raise ValueError("Restored HEAD differs")
    print(json.dumps({"status": "RESTORE_VERIFIED", "sha256": meta["sha256"], "head": meta["head"]}))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("mode", choices=["create", "verify"])
    p.add_argument("--root", type=Path, default=Path.cwd())
    p.add_argument("--dest", type=Path, required=True)
    args = p.parse_args()
    root, dest = args.root.resolve(), args.dest.resolve()
    if args.mode == "verify":
        verify(dest)
        return
    if dest == root or root in dest.parents:
        raise ValueError("Backup must be outside repository")
    if dest.exists() and any(dest.iterdir()):
        raise ValueError("Destination not empty")
    if git(root, "status", "--porcelain"):
        raise ValueError("Working tree is dirty; snapshot and bundle must be coordinated")
    dest.mkdir(parents=True, exist_ok=True)
    bundle = dest / "repository.bundle"
    subprocess.run(["git", "-C", str(root), "bundle", "create", str(bundle), "--all"], check=True)
    meta = {"schema": 1, "head": git(root, "rev-parse", "HEAD"), "sha256": sha256(bundle)}
    (dest / "bundle-manifest.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    verify(dest)

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("BOOKGUARD_BLOCKED:", exc, file=sys.stderr)
        sys.exit(1)
