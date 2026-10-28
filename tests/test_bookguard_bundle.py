import pathlib
import subprocess
import sys
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "bookguard_bundle.py"

class BundleTests(unittest.TestCase):
    def test_bundle_restore_and_tamper(self):
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d) / "repo"
            root.mkdir()
            subprocess.run(["git", "init", "-q", "-b", "main", str(root)], check=True)
            (root / "book.txt").write_text("Авторский оригинал", encoding="utf-8")
            subprocess.run(["git", "-C", str(root), "add", "."], check=True)
            subprocess.run(["git", "-C", str(root), "-c", "user.email=test@example.org",
                            "-c", "user.name=Test", "commit", "-qm", "original"], check=True)
            dest = pathlib.Path(d) / "independent"
            def call(mode):
                return subprocess.run([sys.executable, str(SCRIPT), mode, "--root", str(root),
                                       "--dest", str(dest)], capture_output=True, text=True)
            self.assertEqual(call("create").returncode, 0)
            self.assertEqual(call("verify").returncode, 0)
            with (dest / "repository.bundle").open("ab") as f:
                f.write(b"tamper")
            self.assertNotEqual(call("verify").returncode, 0)

if __name__ == "__main__":
    unittest.main()
