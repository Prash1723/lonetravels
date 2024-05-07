from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
from rich.layout import Layout
from rich.columns import Columns

import numpy as np
import time
from datetime import datetime
import datetime
import logging

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

            
            fuel_capacity = initial_data['fuel_capacity']           # Litres
            mileage = initial_data['mileage']                       # kmpl
            fuel_spent = 0
            distance_covered = 0

            signal_dict = {1.2: "Low fuel", 0.6: "Very low fuel"}
            while distance_covered < distance:
                for k, v in signal_dict.items():
                    if fuel_spent == k:
                        log.info("Fuel capacity : {:.2f} | {:.2f}".format(k,v))
        
        except Exception as e:
            log.error(f"Error : {e}")

    # def run(self):
    #     bot_on == "True"
    #     while bot_on:


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
 
    def run(self):
        """
        Camera runtime
        """
        # Add all the tables to a panel
        pan = Panel.fit(
            Columns(self.ML_cam()['battery']),
            title="Camera Battery",         # Title of the panel
            width=80,                       # Width of the panel
            border_style="red",             # Adding border panel
            padding=(1,2)                   # Space between tables
        )

        # Assign the total minutes left for recording
        battery_left = battery

        bot_on = True

        # Clear console
        rc.clear()
        # Print the tables
        with Live(pan, refresh_per_second=60) as live:
            while bot_on:
                next_step = str(input("Do you wish to recheck the camera battery? (Y/n) :")).lower()

                if next_step == "y" and battery_left > 0:
                    # Countdown timer
                    timer = datetime.timedelta(minutes = battery_left)
                    #log.info(timer)
                    time.sleep(5)
                    battery_left -= 1
                    live.update(pan)
                    time.sleep(5)
                else:
                    log.warning("Alert: Low Battery!")
                    bot_on=False


class location():
    """
    Location details
    """

    #def place(self)