from typing import Union

ITP_RATES = {
            "Andalucia": 8.0,
            "Aragon": 8.0,
            "Asturias": 8.0,
            "Baleares": 8.0,
            "Canarias": 6.5,
            "Cantabria": 10.0,
            "Castilla - La Mancha": 9.0,
            "Castilla Leon": 8.0,
            "Cataluña": 10.0,
            "Ceuta": 6.0,
            "Madrid": 6.0,
            "Valencia": 10.0,
            "Extremadura": 8.0,
            "Galicia": 10.0,
            "La Rioja": 7.0,
            "Melilla": 6.0,
            "Murcia": 8.0,
            "Navarra": 6.0,
            "Pais Vasco": 4.0
        }


def get_itp_cost(autonomous_community: str, price: Union[int, float]) -> float:
    """
    Calculate the ITP costs based on the autonomous community and property price.

    Args:
        autonomous_community (str): The autonomous community where the property is located.
        price (Union[int, float]): The price of the property.

    Returns:
        float: The calculated ITP costs.
    """
    if autonomous_community not in ITP_RATES:
        raise ValueError(f"{autonomous_community} is not a valid community.")
    itp_costs = price * ITP_RATES[autonomous_community] / 100
    return itp_costs
