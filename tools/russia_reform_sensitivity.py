#!/usr/bin/env python3
"""Deterministic sensitivity grid for the AS Russia reform arithmetic model.

This is not a macroeconomic forecast. It varies resource/export receipts, fund
returns, VAT policy and discount coverage, then reports direct arithmetic only.
Use sourced annual inputs via --input; defaults are explicitly fictional.
"""
from __future__ import annotations

import argparse
import csv
import itertools
import json
import sys
from pathlib import Path
from typing import Any

import russia_reform_model as base


def build_grid(config: dict[str, Any]) -> list[dict[str, Any]]:
    """Build a transparent 3x3x3x3x3 grid around supplied inputs."""
    base.validate_config(config)
    rows: list[dict[str, Any]] = []
    resource_shocks = (0.0, -0.25, -0.50)
    export_shocks = (0.0, -0.25, -0.50)
    returns = (-0.05, 0.0, float(config["fund_realized_return_rate"]))
    vat_rates = (
        float(config["baseline_vat_rate"]),
        max(0.0, float(config["baseline_vat_rate"]) - 0.01),
        max(0.0, float(config["baseline_vat_rate"]) - 0.02),
    )
    discount_multipliers = (0.5, 1.0, 1.5)

    for r_shock, e_shock, fund_return, vat_rate, d_mult in itertools.product(
        resource_shocks, export_shocks, returns, vat_rates, discount_multipliers
    ):
        c = dict(config)
        c["state_resource_revenue_rub"] = config["state_resource_revenue_rub"] * (1 + r_shock)
        c["state_export_industry_revenue_rub"] = config["state_export_industry_revenue_rub"] * (1 + e_shock)
        c["fund_realized_return_rate"] = fund_return
        scenario = {
            "name": "combined_sensitivity",
            "vat_rate": vat_rate,
            "resource_share": 0.10,
            "export_share": 0.05,
            "discount_per_person": 12000.0,
            "discount_coverage": 1_000_000 * d_mult,
        }
        result = base.calculate(c, scenario)
        rows.append({
            "year": c["year"],
            "input_status": c.get("metadata", {}).get("status", "USER_SUPPLIED_INPUTS_NOT_INDEPENDENTLY_VERIFIED"),
            "resource_revenue_shock_pct": round(r_shock * 100, 2),
            "export_revenue_shock_pct": round(e_shock * 100, 2),
            "fund_return_pct": round(fund_return * 100, 2),
            "vat_rate": round(vat_rate, 5),
            "discount_coverage_multiplier": d_mult,
            "resource_fund_transfer_rub": result["resource_fund_transfer_rub"],
            "vat_revenue_change_rub_approx": result["vat_revenue_change_rub_approx"],
            "discount_cost_rub": result["discount_cost_rub"],
            "discount_admin_cost_rub": result["discount_admin_cost_rub"],
            "current_budget_delta_rub_approx": result["current_budget_delta_rub_approx"],
            "fund_closing_assets_rub_approx": result["fund_closing_assets_rub_approx"],
            "within_headroom_arithmetic_only": result["within_headroom_arithmetic_only"],
            "warning": "Arithmetic sensitivity only; no inflation, prices, behavior, distributional or macro effects modeled.",
        })
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", help="JSON config with sourced official annual inputs")
    parser.add_argument("--output", default="russia_reform_sensitivity.csv")
    parser.add_argument("--test", action="store_true", help="Run a lightweight grid smoke test")
    args = parser.parse_args()
    try:
        config = base.load_config(args.input)
        if args.input:
            from russia_reform_data_audit import audit_config
            errors = audit_config(config)
            if errors:
                raise ValueError("Input provenance audit failed: " + "; ".join(errors))
        rows = build_grid(config)
        if args.test:
            if len(rows) != 243:
                raise AssertionError(f"Expected 243 cases, got {len(rows)}")
            if not any(row["fund_return_pct"] == -5.0 for row in rows):
                raise AssertionError("Missing negative-return stress cases")
            print("Sensitivity smoke test passed: 243 cases, including negative-return stress.")
            return 0
        with Path(args.output).open("w", newline="", encoding="utf-8-sig") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
        print(f"Wrote {len(rows)} sensitivity cases to {args.output}")
        if config.get("metadata", {}).get("status") == "ILLUSTRATIVE_NOT_RUSSIA_DATA":
            print("WARNING: default inputs are fictional, not official Russian data.", file=sys.stderr)
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
