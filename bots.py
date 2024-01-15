from rich.console import Console
import numpy as np
import time
from datetime import datetime

now = datetime.now()

rc = Console()

class Vehicles(self):
    """All vehicle details"""
    self.speed = speed
    self.start_time = datetime.now()
    self.mv_time = mv_time
    self.fuel_capactiy = fuel_capacity
    self.mileage = mileage
    self.optimum_speed = optimum_speed
    self.distance = distance
    self.in_fuel = in_fuel

    def Honda_Dio(self):
        fuel_capacity = 5.3                         # Litres
        mileage = 44                                # KMPL
    	optimum_speed = np.range(35,46,1)
        speed = 0                                   # KMPH
        return {'fuel_capacity': fuel_capacity, 'mileage': mileage, 'optimum_speed': optimum_speed, 'speed': speed}

    def Honda_Activa(self):
        fuel_capacity = 5.3                         # Litres
	mileage = 40                                # KMPL
    	optimum_speed = np.range(35,46,1)
        speed = 0                                   # KMPH

    def moving_vehicle(self):
        in_cap = self.Honda_Dio
        if in_cap['speed'] = 

    def fuel_in_tank(self, distance: "Distance to be covered", in_fuel: "Initial fuel in the tank"):
        """ Calculates the fuel for the vehicle during a journey"""
        fuel_capacity = 5.3         # Litres
        mileage = 44                # kmpl
        fuel_spent = 0
        distance_covered = 0

        signal_dict = {1.2: "Low fuel", 0.6: "Very low fuel"}

        while distance_covered < distance:
            for k, v in signal_dict.items():
                if fuel_spent == k:
                    rc.log("Fuel capacity : {:.2f} | {:.2f}".format(k,v))

class Camera(self):
    """Camera details"""
    self.on_time = on_time
    self.battery = battery
    self.FHD = FHD
    self.HD = HD
    self.VGA = VGA

    def Mirrorless_cam(self):
        FHD = 35.64             # minutes
        HD = 119.27             # minutes
        VGA = 9999              # minutes
        battery = 3             # hours

    def start_camera(self):
        
        rc.log(battery, style="green")

class location(self):
    """Location details"""

    def place(self):
