import unittest
from src.itp_rates import ITP


class TestITP(unittest.TestCase):
    def setUp(self):
        self.itp = ITP()

    def test_get_itp_valid(self):
        self.assertEqual(self.itp.get_itp("Cataluña"), 10.0)
        self.assertEqual(self.itp.get_itp("Madrid"), 6.0)

    def test_get_itp_invalid(self):
        with self.assertRaises(ValueError):
            self.itp.get_itp("Barcelona")

    def test_itp_costs_valid(self):
        self.assertAlmostEqual(self.itp.itp_costs("Cataluña", 100000), 10000.0)
        self.assertAlmostEqual(self.itp.itp_costs("Madrid", 200000), 12000.0)

    def test_itp_costs_invalid_community(self):
        with self.assertRaises(ValueError):
            self.itp.itp_costs("Barcelona", 100000)

    def test_itp_costs_invalid_price(self):
        with self.assertRaises(ValueError):
            self.itp.itp_costs("Madrid", -1)

    def test_itp_cost_zero_price(self):
        self.assertEqual(self.itp.itp_costs("Cataluña", 0), 0.0)

    def test_itp_cost_float_price(self):
        self.assertAlmostEqual(self.itp.itp_costs("Canarias", 123456.78), 8024.6907, places=4)