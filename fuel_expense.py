from rich.logging import Console
import numpy as np

rc = Console()

distance_traveled, total_fuel_price = int(input("Distance to be covered :")), int(input("Fuel price today :"))

def calculate_fuel_expense(distance: "Distance covered", price: "Fuel price per litre"):
    """
    Returns the total fuel spent for the distance travelled
    """
    mileage = 44  # km per litre
    economy = np.arange(35,46) # Economy of the bike
    
    try:
        fuel_expense = (distance / mileage) * price  # Update fuel_price_per_litre with the current fuel price
    except Exception:
        rc.log("[red]Error[/red] : There has been an error while running the expense function")

    rc.log("[yellow]Total fuel expense: {:.2f} INR".format(fuel_expense))

calculate_fuel_expense(distance_traveled, total_fuel_price)
