import unittest
import pandas as pd
from src.mortgage import fixed_mortgage_schedule, monthly_mortgage_payment, monthly_interest_payment


class TestMortgage(unittest.TestCase):
    def test_monthly_mortgage_payment(self) -> None:
        years = 30
        annual_interest_rate_percentage = 2
        principal = 55000
        expected_result = 203.29
        result = monthly_mortgage_payment(principal=principal,
                                          years=years,
                                          annual_interest_rate_percentage=annual_interest_rate_percentage,
                                          )
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_monthly_interest_payment(self) -> None:
        annual_interest_rate_percentage = 2
        principal = 55000
        expected_result = 91.67
        result = monthly_interest_payment(principal=principal,
                                          annual_interest_rate_percentage=annual_interest_rate_percentage
                                          )
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_fixed_mortgage_schedule_one_year(self) -> None:
        principal = 55000
        years = 1
        annual_interest_rate_percentage = 2

        expected_data = [
            [12, 0, 0, 0, 55000],
            [11, 4633, 4541, 92, 50459],
            [10, 4633, 4549, 84, 45909],
            [9, 4633, 4557, 77, 41353],
            [8, 4633, 4564, 69, 36789],
            [7, 4633, 4572, 61, 32217],
            [6, 4633, 4579, 54, 27637],
            [5, 4633, 4587, 46, 23050],
            [4, 4633, 4595, 38, 18456],
            [3, 4633, 4602, 31, 13853],
            [2, 4633, 4610, 23, 9243],
            [1, 4633, 4618, 15, 4625],
            [0, 4633, 4625, 8, 0],
        ]
        expected_df = pd.DataFrame(expected_data, columns=
            ['pending_periods', 'monthly_payment', 'principal_payment', 'interest_payment', 'remaining_principal']
        )

        result_df = fixed_mortgage_schedule(principal=principal,
                                            years=years,
                                            annual_interest_rate_percentage=annual_interest_rate_percentage)

        pd.testing.assert_frame_equal(result_df, expected_df)
