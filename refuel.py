from rich.console import Console

rc = Console()

def refuel(distance: "Distance to be covered", initial_fuel: "Initial fuel in the tank"):
    """
    Calculates the refueling time for the vehicle during a journey
    """

    tank_capacity = 5.3 # Litres
    mileage = 44 # kmpl
    fuel_spent = 0
