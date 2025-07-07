from typing import Union


class ITP:
    """
    Impuesto de Transmisiones Patrimoniales (ITP) rates for different Spanish communities. Tax to be paid on the
    transfer of property, typically in real estate transactions.
    """

    def __init__(self):
        self.itp_rates = {
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

    def get_itp(self, community: str) -> float:
        if community not in self.itp_rates:
            raise ValueError(f"{community} is not a valid community.")
        return self.itp_rates[community]

    def itp_costs(self, community: str, price: Union[int, float]) -> float:
        if price < 0:
            raise ValueError("Price cannot be negative.")
        itp_rate = self.get_itp(community)
        return (itp_rate / 100) * price