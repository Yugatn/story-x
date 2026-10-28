#!/usr/bin/env python3
"""BookGuard: create and verify portable repository snapshots. Standard library only."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile

def run(*args):
    return subprocess.check_output(args, text=True).strip()

def digest(data):
    return hashlib.sha256(data).hexdigest()

def archive_bytes(root):
    paths = run("git", "-C", str(root), "ls-files", "-z").split("\0")
    with io.BytesIO() as buffer:
        with tarfile.open(fileobj=buffer, mode="w:gz", format=tarfile.PAX_FORMAT) as tar:
            for name in sorted(x for x in paths if x):
                path = root / name
                if not path.is_file() or path.is_symlink():
                    raise RuntimeError("Tracked path missing or symlink: " + name)
                data = path.read_bytes()
                info = tarfile.TarInfo(name)
                info.size = len(data)
                info.mtime = 0
                info.mode = 0o644
                tar.addfile(info, io.BytesIO(data))
        return buffer.getvalue()

def verify(archive, manifest):
    meta = json.loads(manifest.read_text(encoding="utf-8"))
    blob = archive.read_bytes()
    if digest(blob) != meta["archive_sha256"]:
        raise RuntimeError("Archive SHA-256 mismatch")
    found = {}
    with tarfile.open(fileobj=io.BytesIO(blob), mode="r:gz") as tar:
        for item in tar:
            if not item.isfile() or item.name.startswith("/") or ".." in Path(item.name).parts or item.name in found:
                raise RuntimeError("Unsafe archive entry")
            found[item.name] = digest(tar.extractfile(item).read())
    if found != meta["files"]:
        raise RuntimeError("File manifest mismatch")
    with tempfile.TemporaryDirectory() as tmp:
        for name in sorted(found):
            target = Path(tmp) / name
            target.parent.mkdir(parents=True, exist_ok=True)
            with tarfile.open(fileobj=io.BytesIO(blob), mode="r:gz") as tar:
                target.write_bytes(tar.extractfile(name).read())
            if digest(target.read_bytes()) != found[name]:
                raise RuntimeError("Restore verification failed: " + name)
    return meta

def create(root, dest, label):
    if not dest.is_absolute():
        raise RuntimeError("Backup destination must be absolute")
    if dest == root or root in dest.parents:
        raise RuntimeError("Backup destination must be outside repository")
    if dest.exists() and any(dest.iterdir()):
        raise RuntimeError("Destination must be empty to prevent overwrites")
    dest.mkdir(parents=True, exist_ok=True)
    blob = archive_bytes(root)
    files = {}
    with tarfile.open(fileobj=io.BytesIO(blob), mode="r:gz") as tar:
        for item in tar:
            files[item.name] = digest(tar.extractfile(item).read())
    manifest = {"schema": 1, "label": label, "repository": root.name,
                "commit": run("git", "-C", str(root), "rev-parse", "HEAD"),
                "archive_sha256": digest(blob), "files": files}
    archive = dest / "snapshot.tar.gz"
    record = dest / "manifest.json"
    archive.write_bytes(blob)
    record.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    verify(archive, record)
    print(json.dumps({"status": "RESTORE_TEST_PASSED", "path": str(dest),
                      "sha256": manifest["archive_sha256"], "files": len(files)}, ensure_ascii=False))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["create", "verify"])
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--dest", type=Path, required=True)
    parser.add_argument("--label", choices=["before", "after"], default="before")
    args = parser.parse_args()
    root = args.root.resolve()
    dest = args.dest.resolve()
    if args.mode == "create":
        create(root, dest, args.label)
    else:
        meta = verify(dest / "snapshot.tar.gz", dest / "manifest.json")
        print(json.dumps({"status": "RESTORE_TEST_PASSED", "files": len(meta["files"])}))

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("BACKUP_BLOCKED:", error, file=sys.stderr)
        sys.exit(1)
