from rich.console import Console
from rich.logging import RichHandler
import numpy as np
import time
from datetime import datetime
import datetime
import logging

now = datetime.now()

rc = Console()

# Format for logging
FORMAT='%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Configuration for logging
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

# Assign logger
log = logging.getLogger("rich")

# File output settings
FileOut = logging.FileHandler('app.log')

log.addHandler(FileOut)

class Vehicles():
    """
    All vehicle details
    """

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
        """
        Calculates the fuel for the vehicle during a journey
        """
        try:
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
                        log.info("Fuel capacity : {:.2f} | {:.2f}".format(k,v))
        
        except Exception as e:
            log.error(f"Error : {e}")

    def run(self):
        bot_on == "True"
        while bot_on:


class Camera():
    """
    Camera details
    """
    def __init__(self, memory, FORMAT):
        #self.on_time = on_time
        self.memory = memory
        self.battery = 180
        self.format = FORMAT

    def ML_cam(self):
        x = {}
        if self.memory=='8gb':
            if self.format=='FHD':
                x = {
                'battery': 180,                 # minutes
                'memory': 2138,                 # minutes
                }
            if self.format=='HD':
                x = {
                'battery': 180,                 # minutes
                'memory': 7156,                 # minutes
                }
            if self.format=='VGA':
                x = {
                'battery': 180,                 # minutes
                'memory': 599940                # minutes
                }

        if self.memory=='16gb':
            if self.format=='FHD':
                x = {
                'battery': 180,                 # minutes
                'memory': 2138*2,               # minutes
                }
            if self.format=='HD':
                x = {
                'battery': 180,                 # minutes
                'memory': 7156*2,               # minutes
                }
            if self.format=='VGA':
                x = {
                'battery': 180,                 # minutes
                'memory': 599940*2              # minutes
                }

        return x

    def camera_runtime(self, battery):
 
        # Assign the total minutes left for recording
        battery_left = battery
 
        # Loop to battery minutes
        while battery_left > 0:
 
            # Countdown timer
            timer = datetime.timedelta(minutes = battery_left)
            log.info(timer, end="\r")
            time.sleep(60)
            battery_left -= 1
 
        log.warning("Alert: Low Battery!")

    def run(self):
        """
        Camera runtime
        """  
        bot_on = True
        while bot_on:
            #cam_data = {"FHD": self.FHD, "HD": self.HD, "VGA": self.VGA, "battery": self.battery}

            next_step = str(input("Do you wish to recheck the camera battery? (Y/n) :")).lower()

            if next_step == "y":
                self.camera_runtime(self.ML_cam()['battery'])

            else:
                bot_on=False


class location():
    """
    Location details
    """

    #def place(self)