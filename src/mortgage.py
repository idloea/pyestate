import numpy_financial as npf
import pandas as pd


def monthly_mortgage_payment(principal: float, years: int, annual_interest_rate_percentage: float) -> float:
    """
    Calculates the fixed monthly mortgage payment using the loan principal, term, and annual interest rate.

    Parameters:
    - principal: The total loan amount.
    - years: The loan term in years.
    - annual_interest_rate_percentage: The annual interest rate as a percentage (e.g., 5 for 5%).

    Returns:
    - The monthly payment amount as a float.
    """

    annual_interest_rate = annual_interest_rate_percentage / 100
    monthly_interest_rate = annual_interest_rate / 12
    number_of_payments = years * 12
    return npf.pmt(monthly_interest_rate, number_of_payments, -principal)

def monthly_interest_payment(principal: float, annual_interest_rate_percentage: float) -> float:
    """
    Calculates the interest portion of a monthly mortgage payment.

    Parameters:
    - principal: The remaining principal amount.
    - annual_interest_rate_percentage: The annual interest rate as a percentage.

    Returns:
    - The monthly interest payment as a float.
    """

    annual_interest_rate = annual_interest_rate_percentage / 100
    monthly_interest_rate = annual_interest_rate / 12
    return principal * monthly_interest_rate

def fixed_mortgage_schedule(principal: float, years: int, annual_interest_rate_percentage: float) -> pd.DataFrame:
    """
    Generates a fixed-rate mortgage amortization schedule.

    Parameters:
    - principal: The total loan amount.
    - years: The loan term in years.
    - annual_interest_rate_percentage: The annual interest rate as a percentage.

    Returns:
    - A pandas DataFrame with columns:
      ['pending_periods', 'monthly_payment', 'principal_payment', 'interest_payment', 'remaining_principal']
      Each row represents a monthly payment period.
    """

    columns = ['pending_periods', 'monthly_payment', 'principal_payment', 'interest_payment', 'remaining_principal']
    df = pd.DataFrame(columns=columns)
    pending_periods = years * 12
    df.loc[0] = [pending_periods, 0, 0, 0, principal]

    monthly_payment = monthly_mortgage_payment(principal=principal,
                                               years=years,
                                               annual_interest_rate_percentage=annual_interest_rate_percentage)
    index = 1
    while pending_periods != 0:
        pending_periods = pending_periods - 1
        principal = df.iloc[-1]['remaining_principal']

        interest_payment = monthly_interest_payment(principal=principal,
                                                    annual_interest_rate_percentage=annual_interest_rate_percentage)
        principal_payment = monthly_payment - interest_payment
        remaining_principal = principal - principal_payment

        new_row = pd.DataFrame(data=[[pending_periods, monthly_payment, principal_payment, interest_payment,
                                      remaining_principal]],
                               columns=df.columns)

        df = pd.concat([df.iloc[:index], new_row, df.iloc[index:]]).reset_index(drop=True)
        index = index + 1

    df = df.round(0).astype(int)  # Round to nearest integer as mortgage payments are typically whole numbers
    return df
