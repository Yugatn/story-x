import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "bookguard_notion_export.py"
spec = importlib.util.spec_from_file_location("bookguard_notion_export", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

ROOT = "a" * 32
CHILD = "b" * 32

def fake_request(path, token):
    if path == "pages/" + ROOT:
        return {"id": ROOT, "object": "page"}
    if path == "pages/" + CHILD:
        raise module.urllib.error.HTTPError("mock", 404, "block, not page", {}, None)
    if path == "blocks/" + CHILD:
        return {"id": CHILD, "object": "block"}
    if path.startswith("blocks/" + ROOT + "/children"):
        return {"results": [{"id": CHILD, "has_children": True}], "has_more": False}
    if path.startswith("blocks/" + CHILD + "/children"):
        return {"results": [{"id": "c" * 32, "has_children": False}], "has_more": False}
    raise AssertionError(path)

class ExportTests(unittest.TestCase):
    def test_nested_blocks_and_manifest(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "backup"
            with patch.object(module, "request", side_effect=fake_request), patch.dict(module.os.environ, {"NOTION_TOKEN": "fixture"}), patch.object(sys, "argv", ["tool", "--pages", ROOT, "--dest", str(out)]):
                module.main()
            meta = json.loads((out / "manifest.json").read_text())
            self.assertEqual(meta["items"], 2)
            for name, checksum in meta["sha256"].items():
                self.assertEqual(module.hashlib.sha256((out / name).read_bytes()).hexdigest(), checksum)
            self.assertTrue((out / (CHILD + ".block.json")).exists())

if __name__ == "__main__":
    unittest.main()
