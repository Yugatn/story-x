"""Unit tests for the illustrative AS Russia reform scenario calculator."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import russia_reform_model as model


class ReformModelTests(unittest.TestCase):
    def setUp(self):
        self.config = {
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
            "metadata": {"status": "TEST_FIXTURE_NOT_OFFICIAL_DATA"},
        }

    def test_baseline_has_no_policy_delta(self):
        row = model.calculate(self.config, model.SCENARIOS[0])
        self.assertEqual(row["vat_revenue_change_rub_approx"], 0)
        self.assertEqual(row["resource_fund_transfer_rub"], 0)
        self.assertEqual(row["discount_cost_rub"], 0)

    def test_vat_reduction_reduces_first_order_revenue_estimate(self):
        row = model.calculate(self.config, model.SCENARIOS[2])
        self.assertLess(row["vat_revenue_change_rub_approx"], 0)

    def test_fund_transfer_and_closing_assets(self):
        row = model.calculate(self.config, model.SCENARIOS[1])
        self.assertEqual(row["resource_fund_transfer_rub"], 10_500_000_000)
        expected = 500_000_000_000 + 10_500_000_000 + 15_000_000_000 - 10_000_000_000
        self.assertEqual(row["fund_closing_assets_rub_approx"], expected)

    def test_discount_program_cost(self):
        row = model.calculate(self.config, model.SCENARIOS[3])
        self.assertEqual(row["discount_cost_rub"], 12_000_000_000)
        self.assertEqual(row["discount_admin_cost_rub"], 500_000_000)

    def test_invalid_vat_rate_is_rejected(self):
        bad = dict(self.config)
        bad["baseline_vat_rate"] = 1.2
        with self.assertRaises(ValueError):
            model.validate_config(bad)

    def test_negative_revenue_is_rejected(self):
        bad = dict(self.config)
        bad["state_resource_revenue_rub"] = -1
        with self.assertRaises(ValueError):
            model.validate_config(bad)

    def test_non_finite_revenue_is_rejected(self):
        bad = dict(self.config)
        bad["state_resource_revenue_rub"] = float("nan")
        with self.assertRaises(ValueError):
            model.validate_config(bad)

    def test_invalid_year_is_rejected(self):
        bad = dict(self.config)
        bad["year"] = 2026.5
        with self.assertRaises(ValueError):
            model.validate_config(bad)


if __name__ == "__main__":
    unittest.main()
