from rich.console import Console
import numpy as np
import time
from datetime import datetime

now = datetime.now()

rc = Console()

class Vehicles():
    """All vehicle details"""

    def __init__(self, vehicle, speed, start_time, mv_time, fuel_capacity, mileage, optimum_speed, distance, in_fuel):
        self.vehicle = vehicle
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
        optimum_speed = np.arange(35,46,1)
        speed = 0                                   # KMPH
        return {'fuel_capacity': fuel_capacity, 'mileage': mileage, 'optimum_speed': optimum_speed, 'speed': speed}

    def Honda_Activa(self):
        fuel_capacity = 5.3                         # Litres
        mileage = 40                                # KMPL
        optimum_speed = np.arange(35,46,1)
        speed = 0                                   # KMPH
        return {'fuel_capacity': fuel_capacity, 'mileage': mileage, 'optimum_speed': optimum_speed, 'speed': speed}

    def fuel_in_tank(self, distance: "Distance to be covered", in_fuel: "Initial fuel in the tank"):
        """ Calculates the fuel for the vehicle during a journey"""
        if self.vehicle=='dio':
            initial_data = self.Honda_Dio()
        if self.vehicle=='activa':
            initial_data = self.Honda_Activa()

        
        fuel_capacity = initial_data['fuel_capacity']         # Litres
        mileage = initial_data['mileage']                # kmpl
        fuel_spent = 0
        distance_covered = 0

        signal_dict = {1.2: "Low fuel", 0.6: "Very low fuel"}
        while distance_covered < distance:
            for k, v in signal_dict.items():
                if fuel_spent == k:
                    rc.log("Fuel capacity : {:.2f} | {:.2f}".format(k,v))

    def run(self):
        bot_on == "True"
        while bot_on:


class Camera():
    """Camera details"""
    def __init__(self, memory):
        #self.on_time = on_time
        self.memory = memory
        self.battery = 180
        self.FHD = 2138
        self.HD = 7156
        self.VGA = 599940

    def ML_cam(self):
        x = {}
        if self.memory == '8gb':
            x = {
            'battery': 180,                 # minutes
            'FHD': 2138,                    # minutes
            'HD': 7156,                     # minutes
            'VGA': 599940                   # hours
            }
        return x

    def camera_runtime(self, battery):
        
        battery_left = battery - time.time()
        rc.log("Camera battery time : {:.2f}".format(battery_left), style="green")
        battery = battery_left

    def run(self):
        """Camera runtime"""  
        bot_on = True
        while bot_on:
            #cam_data = {"FHD": self.FHD, "HD": self.HD, "VGA": self.VGA, "battery": self.battery}

            next_step = str(input("Do you wish to recheck the camera battery? (Y/n) :")).lower()

            if next_step == "y":
                self.camera_runtime(self.ML_cam()['battery'])

            else:
                break


class location():
    """Location details"""

    #def place(self):