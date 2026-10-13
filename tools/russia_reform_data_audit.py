#!/usr/bin/env python3
"""Audit provenance metadata before policy-model inputs are treated as evidence.

This validator does not verify that a source is truthful or that its numbers
match the publication. It enforces a minimum provenance record and flags
unreviewed/illustrative input files before numerical analysis.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import russia_reform_model as model

NUMERIC_FIELDS = sorted(model.REQUIRED - {"year"})
SOURCE_FIELDS = {"field", "url", "publisher", "publication_date", "accessed_date", "unit", "definition"}


def audit_config(config: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    try:
        model.validate_config(config)
    except (KeyError, TypeError, ValueError) as exc:
        errors.append(f"Numeric input validation failed: {exc}")

    metadata = config.get("metadata")
    if not isinstance(metadata, dict):
        return errors + ["metadata must be an object"]
    if metadata.get("status") != "OFFICIAL_DATA_REVIEWED":
        errors.append("metadata.status must be OFFICIAL_DATA_REVIEWED; illustrative or unreviewed data cannot pass")
    cutoff = metadata.get("data_cutoff")
    try:
        date.fromisoformat(cutoff)
    except (TypeError, ValueError):
        errors.append("metadata.data_cutoff must be a valid ISO date (YYYY-MM-DD)")

    definitions = metadata.get("definitions")
    if not isinstance(definitions, str) or len(definitions.strip()) < 30:
        errors.append("metadata.definitions must describe units, period alignment and reconciliation (at least 30 characters)")

    sources = metadata.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("metadata.sources must contain a source record for every numeric input field")
        sources = []

    indexed: dict[str, dict[str, Any]] = {}
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            errors.append(f"metadata.sources[{index}] must be an object")
            continue
        missing = sorted(SOURCE_FIELDS - source.keys())
        if missing:
            errors.append(f"metadata.sources[{index}] missing fields: {', '.join(missing)}")
            continue
        field = source.get("field")
        if field not in NUMERIC_FIELDS:
            errors.append(f"metadata.sources[{index}].field must name a model numeric field")
            continue
        if field in indexed:
            errors.append(f"duplicate provenance records for numeric field: {field}")
        indexed[field] = source
        parsed_url = urlparse(str(source.get("url", "")))
        if parsed_url.scheme != "https" or not parsed_url.netloc:
            errors.append(f"metadata.sources[{index}].url must be an absolute HTTPS URL")
        for date_field in ("publication_date", "accessed_date"):
            try:
                date.fromisoformat(source[date_field])
            except (TypeError, ValueError):
                errors.append(f"metadata.sources[{index}].{date_field} must be YYYY-MM-DD")
        for text_field in ("url", "publisher", "unit", "definition"):
            if not isinstance(source.get(text_field), str) or not source[text_field].strip():
                errors.append(f"metadata.sources[{index}].{text_field} must be non-empty")

    for field in NUMERIC_FIELDS:
        if field not in indexed:
            errors.append(f"missing source provenance for numeric field: {field}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Input JSON to audit; no fictional defaults accepted")
    args = parser.parse_args()
    try:
        config = json.loads(Path(args.input).read_text(encoding="utf-8"))
        errors = audit_config(config)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"AUDIT ERROR: {exc}", file=sys.stderr)
        return 2
    if errors:
        print("DATA PROVENANCE AUDIT FAILED:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("DATA PROVENANCE AUDIT PASSED. This validates metadata completeness only, not source truth or economic validity.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
