"""Tests for the input provenance audit."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import russia_reform_data_audit as audit
import russia_reform_model as model


class DataAuditTests(unittest.TestCase):
    def complete_config(self):
        config = model.load_config(None)
        config["metadata"] = {
            "status": "OFFICIAL_DATA_REVIEWED",
            "data_cutoff": "2026-09-30",
            "definitions": "All monetary values are RUB for calendar year 2026; periods and definitions reconciled.",
            "sources": [],
        }
        for field in sorted(model.REQUIRED - {"year"}):
            config["metadata"]["sources"].append({
                "field": field,
                "url": "https://example.invalid/source",
                "publisher": "Test publisher",
                "publication_date": "2026-09-30",
                "accessed_date": "2026-10-13",
                "unit": "RUB or rate as specified by field",
                "definition": "Test-only fixture to verify metadata validation logic.",
            })
        return config

    def test_complete_provenance_record_passes_metadata_checks(self):
        self.assertEqual(audit.audit_config(self.complete_config()), [])

    def test_illustrative_default_is_rejected_as_official_evidence(self):
        errors = audit.audit_config(model.load_config(None))
        self.assertTrue(any("OFFICIAL_DATA_REVIEWED" in error for error in errors))
        self.assertTrue(any("metadata.sources" in error for error in errors))

    def test_missing_numeric_field_source_is_rejected(self):
        config = self.complete_config()
        config["metadata"]["sources"] = [
            source for source in config["metadata"]["sources"]
            if source["field"] != "effective_vat_base_rub"
        ]
        self.assertTrue(any("effective_vat_base_rub" in error for error in audit.audit_config(config)))

    def test_invalid_cutoff_date_is_rejected(self):
        config = self.complete_config()
        config["metadata"]["data_cutoff"] = "2026-99-99"
        self.assertTrue(any("data_cutoff" in error for error in audit.audit_config(config)))

    def test_duplicate_source_record_is_rejected(self):
        config = self.complete_config()
        config["metadata"]["sources"].append(dict(config["metadata"]["sources"][0]))
        self.assertTrue(any("duplicate provenance" in error for error in audit.audit_config(config)))

    def test_non_https_source_url_is_rejected(self):
        config = self.complete_config()
        config["metadata"]["sources"][0]["url"] = "http://example.invalid/source"
        self.assertTrue(any("absolute HTTPS" in error for error in audit.audit_config(config)))


if __name__ == "__main__":
    unittest.main()
