"""Tests for the deterministic sensitivity grid."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import russia_reform_model as model
import russia_reform_sensitivity as sensitivity


class SensitivityTests(unittest.TestCase):
    def setUp(self):
        self.config = model.load_config(None)

    def test_grid_has_243_cases(self):
        self.assertEqual(len(sensitivity.build_grid(self.config)), 243)

    def test_grid_contains_stress_dimensions(self):
        rows = sensitivity.build_grid(self.config)
        self.assertEqual({r["resource_revenue_shock_pct"] for r in rows}, {0, -25, -50})
        self.assertEqual({r["export_revenue_shock_pct"] for r in rows}, {0, -25, -50})
        self.assertEqual({r["discount_coverage_multiplier"] for r in rows}, {0.5, 1.0, 1.5})
        self.assertEqual({r["fund_return_pct"] for r in rows}, {-5.0, 0.0, 3.0})

    def test_resource_shock_reduces_fund_transfer(self):
        rows = sensitivity.build_grid(self.config)
        cases = [r for r in rows if r["export_revenue_shock_pct"] == 0
                 and r["fund_return_pct"] == 0 and r["vat_rate"] == 0.22
                 and r["discount_coverage_multiplier"] == 1.0]
        by_shock = {r["resource_revenue_shock_pct"]: r for r in cases}
        self.assertGreater(by_shock[0]["resource_fund_transfer_rub"],
                           by_shock[-25]["resource_fund_transfer_rub"])
        self.assertGreater(by_shock[-25]["resource_fund_transfer_rub"],
                           by_shock[-50]["resource_fund_transfer_rub"])

    def test_negative_return_is_included_as_stress_case(self):
        rows = sensitivity.build_grid(self.config)
        stressed = [r for r in rows if r["fund_return_pct"] == -5.0]
        self.assertEqual(len(stressed), 81)
        self.assertTrue(all("Arithmetic sensitivity only" in r["warning"] for r in rows))


if __name__ == "__main__":
    unittest.main()
