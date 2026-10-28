import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "bookguard_backup.py"

class BackupTests(unittest.TestCase):
    def test_roundtrip_and_tamper(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "repo"
            root.mkdir()
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            (root / "sample.txt").write_text("Сохранение авторского текста", encoding="utf-8")
            subprocess.run(["git", "-C", str(root), "add", "sample.txt"], check=True)
            subprocess.run(["git", "-C", str(root), "-c", "user.email=test@example.org", "-c", "user.name=Test", "commit", "-qm", "fixture"], check=True)
            dest = Path(temp) / "external" / "before"
            def call(*args):
                return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)
            self.assertEqual(call("create", "--root", str(root), "--dest", str(dest)).returncode, 0)
            self.assertEqual(call("verify", "--dest", str(dest)).returncode, 0)
            (dest / "snapshot.tar.gz").write_bytes((dest / "snapshot.tar.gz").read_bytes() + b"tamper")
            self.assertNotEqual(call("verify", "--dest", str(dest)).returncode, 0)
            self.assertNotEqual(call("create", "--root", str(root), "--dest", str(root / "backups")).returncode, 0)

if __name__ == "__main__":
    unittest.main()
