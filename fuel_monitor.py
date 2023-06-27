from rich.logging import Console

console = Console()

def calculate_fuel(distance: "Total distance of the journey", initial_fuel: "Current fuel in the tank"):
    """
    Calculates the fuel to be consumed over the total distance
    """

    tank_capacity = 5.3  # litres
    mileage = 44  # km per litre
    fuel_spent = 0
    distance_covered = 0

    # Calculate the distance
    while distance_covered < distance:
        if fuel_spent >= current_fuel:
            console.log("[red]Out of fuel!")
            break

        fuel_required = (distance - distance_covered) / mileage
        
        # Fuel spent overall
        if fuel_spent + fuel_required > initial_fuel:
            fuel_required = initial_fuel - fuel_spent

        fuel_spent += fuel_required
        distance_covered += fuel_required * mileage

        console.log("[yellow]Distance Covered : {:.2f} km | Fuel Spent : {:.2f} litres".format(distance_covered, fuel_spent))
    
    # Conclusion
    if distance_covered >= distance:
        console.log("[yellow]Reached the destination!")
    else:
        console.log("[red]Unable to complete the journey.")
        console.log("[green]Total fuel required for the journey : {:.2f} litres | Distance left : {:.2f} km".format((distance / mileage) - fuel_spent,
            (distance - distance_covered)))
    

# Run the function
distance_to_travel = int(input("Distance to cover : "))
current_fuel = int(input("Current fuel in tank : "))
calculate_fuel(distance_to_travel, current_fuel)
