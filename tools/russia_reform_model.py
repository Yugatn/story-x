#!/usr/bin/env python3
"""Transparent scenario calculator for the AS Russia reform model.

Standard-library only. Illustrative defaults are NOT estimates for Russia.
Supply official, consistently defined annual inputs in a JSON file to obtain
scenario calculations. This is a budget/fund arithmetic model, not a macro
forecast: it does not estimate VAT pass-through, inflation, growth, or behavior.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

SCENARIOS = [
    # Values are policy deltas/parameters, not empirical estimates.
    {"name": "baseline", "vat_rate": None, "resource_share": 0.0,
     "export_share": 0.0, "discount_per_person": 0.0, "discount_coverage": 0.0},
    {"name": "fund_only", "vat_rate": None, "resource_share": 0.10,
     "export_share": 0.05, "discount_per_person": 0.0, "discount_coverage": 0.0},
    {"name": "vat_reduction", "vat_rate": 0.21, "resource_share": 0.0,
     "export_share": 0.0, "discount_per_person": 0.0, "discount_coverage": 0.0},
    {"name": "targeted_discounts", "vat_rate": None, "resource_share": 0.0,
     "export_share": 0.0, "discount_per_person": 12000.0, "discount_coverage": 1_000_000},
    {"name": "combined", "vat_rate": 0.21, "resource_share": 0.10,
     "export_share": 0.05, "discount_per_person": 12000.0, "discount_coverage": 1_000_000},
]

REQUIRED = {
    "year", "baseline_vat_rate", "effective_vat_base_rub",
    "state_resource_revenue_rub", "state_export_industry_revenue_rub",
    "opening_fund_assets_rub", "fund_realized_return_rate",
    "fund_payout_rub", "discount_admin_cost_rub", "public_budget_headroom_rub",
}


def load_config(path: str | None) -> dict[str, Any]:
    if path is None:
        # Clearly fictional scale inputs for a smoke test only.
        return {
            "year": 2026,
            "baseline_vat_rate": 0.22,
            "effective_vat_base_rub": 1_000_000_000_000.0,
            "state_resource_revenue_rub": 100_000_000_000.0,
            "state_export_industry_revenue_rub": 10_000_000_000.0,
            "opening_fund_assets_rub": 500_000_000_000.0,
            "fund_realized_return_rate": 0.03,
            "fund_payout_rub": 10_000_000_000.0,
            "discount_admin_cost_rub": 500_000_000.0,
            "public_budget_headroom_rub": 0.0,
            "metadata": {
                "status": "ILLUSTRATIVE_NOT_RUSSIA_DATA",
                "note": "Replace all numeric values with sourced official data before interpretation."
            }
        }
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    missing = sorted(REQUIRED - data.keys())
    if missing:
        raise ValueError("Missing required config keys: " + ", ".join(missing))
    return data


def validate_config(c: dict[str, Any]) -> None:
    for key in REQUIRED - {"year"}:
        if not isinstance(c[key], (int, float)) or isinstance(c[key], bool):
            raise ValueError(f"{key} must be numeric")
        if key != "fund_realized_return_rate" and c[key] < 0:
            raise ValueError(f"{key} must be non-negative")
    if not 0 <= c["baseline_vat_rate"] <= 1:
        raise ValueError("baseline_vat_rate must be between 0 and 1")
    if not -1 <= c["fund_realized_return_rate"] <= 1:
        raise ValueError("fund_realized_return_rate must be between -1 and 1")


def calculate(c: dict[str, Any], s: dict[str, Any]) -> dict[str, Any]:
    rate = c["baseline_vat_rate"] if s["vat_rate"] is None else s["vat_rate"]
    if not 0 <= rate <= 1:
        raise ValueError(f"Scenario {s['name']}: VAT rate must be between 0 and 1")

    # First-order arithmetic only. VAT base and effective rate must be
    # defined consistently with exemptions, deductions, refunds and imports.
    vat_delta = c["effective_vat_base_rub"] * (rate - c["baseline_vat_rate"])
    pension_transfer = (
        c["state_resource_revenue_rub"] * s["resource_share"]
        + c["state_export_industry_revenue_rub"] * s["export_share"]
    )
    discount_cost = s["discount_per_person"] * s["discount_coverage"]
    administration = c["discount_admin_cost_rub"] if discount_cost > 0 else 0.0
    fund_income = c["opening_fund_assets_rub"] * c["fund_realized_return_rate"]
    closing_assets = (
        c["opening_fund_assets_rub"] + pension_transfer + fund_income
        - c["fund_payout_rub"]
    )
    # Relative to the no-reform baseline. A transfer to the fund is a
    # current-budget outflow but remains a public-sector asset; avoid
    # double-counting it as a loss of consolidated public wealth.
    budget_delta = vat_delta - pension_transfer - discount_cost - administration
    return {
        "year": c["year"],
        "scenario": s["name"],
        "status": c.get("metadata", {}).get("status", "USER_SUPPLIED_INPUTS_NOT_INDEPENDENTLY_VERIFIED"),
        "vat_rate": rate,
        "vat_revenue_change_rub_approx": round(vat_delta, 2),
        "resource_fund_transfer_rub": round(pension_transfer, 2),
        "discount_cost_rub": round(discount_cost, 2),
        "discount_admin_cost_rub": round(administration, 2),
        "current_budget_delta_rub_approx": round(budget_delta, 2),
        "fund_return_rub": round(fund_income, 2),
        "fund_payout_rub": round(c["fund_payout_rub"], 2),
        "fund_closing_assets_rub_approx": round(closing_assets, 2),
        "budget_headroom_rub": round(c["public_budget_headroom_rub"], 2),
        "within_headroom_arithmetic_only": budget_delta + c["public_budget_headroom_rub"] >= 0,
        "household_discount_gross_rub": round(discount_cost, 2),
        "interpretation_warning": (
            "No macroeconomic, inflation, VAT pass-through, distributional or behavioral effects estimated. "
            "A positive arithmetic budget result is not proof of economic desirability."
        ),
    }


def run_smoke_tests() -> None:
    c = load_config(None)
    validate_config(c)
    baseline = calculate(c, SCENARIOS[0])
    assert baseline["vat_revenue_change_rub_approx"] == 0
    assert baseline["resource_fund_transfer_rub"] == 0
    assert baseline["discount_cost_rub"] == 0
    lower_vat = calculate(c, SCENARIOS[2])
    assert lower_vat["vat_revenue_change_rub_approx"] < 0
    fund = calculate(c, SCENARIOS[1])
    assert fund["resource_fund_transfer_rub"] > 0
    assert fund["fund_closing_assets_rub_approx"] > baseline["fund_closing_assets_rub_approx"]
    discounts = calculate(c, SCENARIOS[3])
    assert discounts["discount_cost_rub"] == 12_000_000_000
    print("Smoke tests passed: baseline, VAT delta sign, fund transfer, fund assets, discount arithmetic.", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", help="Path to JSON config containing official annual inputs")
    parser.add_argument("--output", default="russia_reform_scenarios.csv", help="Output CSV path")
    parser.add_argument("--test", action="store_true", help="Run smoke tests and exit")
    args = parser.parse_args()
    if args.test:
        run_smoke_tests()
        return 0
    try:
        config = load_config(args.input)
        validate_config(config)
        rows = [calculate(config, s) for s in SCENARIOS]
        out = Path(args.output)
        with out.open("w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
        print(f"Wrote {len(rows)} scenarios to {out}")
        if config.get("metadata", {}).get("status") == "ILLUSTRATIVE_NOT_RUSSIA_DATA":
            print("WARNING: default inputs are fictional smoke-test values, not Russian official data.", file=sys.stderr)
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
