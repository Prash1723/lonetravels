from rich.console import Console

rc = Console()

def refuel(distance: "Distance to be covered", initial_fuel: "Initial fuel in the tank"):
    """
    Calculates the refueling time for the vehicle during a journey
    """

    tank_capacity = 5.3 # Litres
    mileage = 44 # kmpl
    fuel_spent = 0
    distance_covered = 0
    
    signal_dict = {1.2: "Low fuel", 0.6: "Very low fuel"}

    while distance_covered < distance:
        for k, v in signal_dict.items():
            if fuel_spent == k:
                rc.log("Fuel capacity : {:.2f} | {:.2f}".format(k,v))
