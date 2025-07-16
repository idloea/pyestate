import unittest
from src.itp_rates import get_itp_cost, ITP_RATES

class TestGetITPCost(unittest.TestCase):
    def test_valid_community_and_price(self):
        for community, rate in ITP_RATES.items():
            price = 100000
            expected = price * rate / 100
            self.assertEqual(get_itp_cost(community, price), expected)

    def test_invalid_community_raises(self):
        with self.assertRaises(ValueError) as context:
            get_itp_cost("Unknown", 100000)
        self.assertIn("is not a valid community", str(context.exception))

    def test_float_price(self):
        community = "Madrid"
        price = 123456.78
        expected = price * ITP_RATES[community] / 100
        self.assertAlmostEqual(get_itp_cost(community, price), expected)
