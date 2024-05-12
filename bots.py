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
    def __init__(self, vehicle, dist_covered, in_fuel):
        self.vehicle = vehicle
        self.dist_covered = dist_covered
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

    def write_data(filename, data_log):
        """
        Write the travel data into a csv file
        """
        with open(filename, 'a') as file:
            file.write(data_log)

    def fuel_in_tank(self):
        """
        Calculates the fuel for the vehicle during a journey
        """
        if self.vehicle=='dio':
            initial_data = self.Honda_Dio()
        if self.vehicle=='activa':
            initial_data = self.Honda_Activa()

            
        fuel_capacity = initial_data['fuel_capacity']                   # Litres
        mileage = initial_data['mileage']                               # kmpl
        fuel_spent = self.dist_covered/initial_data['mileage']          # Calculate fuel spent
        max_distance = initial_data['mileage']*self.in_fuel             # Maximum distance possible
        fuel_left = self.in_fuel - fuel_spent                           # Fuel left in tank
        dist_left = max_distance - self.dist_covered
        data_log = np.array(datetime.date(), self.vehicle, self.in_fuel, self.dist_covered, fuel_left, dist_left)

        write_data('data_log.csv', data_log)

        return {'fuel_spent': fuel_spent, 'fuel_left': fuel_left, 'dist_left': dist_left, 'max_distance': max_distance}


    def run(self):
        """
        Run the Vehicles class
        """
        # Assign the total minutes left for recording
        data = self.fuel_in_tank()

        fuel_left = round(data['fuel_left'], 2)
        dist_left = round(data['dist_left'], 2)
        max_distance = round(data['max_distance'], 2)
        fuel_spent = round(data['fuel_spent'], 2)

        try:
            if self.dist_covered < max_distance:
                if fuel_left > 1.2:
                    log.info(f"Fuel capacity : {fuel_left} Litres | Fuel enough for {dist_left} km")
                elif 1.2 < fuel_left < 0.6:
                    log.warning(f"Fuel capacity : {fuel_left} Litres | Low fuel enough for {dist_left} km")
                else:
                    log.warning(f"Fuel capacity : {fuel_left} Litres | Very Low fuel enough for {dist_left} km | Refuel now!")

        except Exception as e:
            log.error(f"Error : {e}")

class Camera():
    """
    Camera details
    """
    def __init__(self, memory, FORMAT):
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