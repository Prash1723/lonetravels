from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
from rich.layout import Layout
from rich.columns import Columns

from db_connect import db_query

import numpy as np
import time
from datetime import datetime
import datetime
import logging

from PIL import Image
import os, pyperclip, re, send2trash
from pytesseract import image_to_string

# Assign Path
path = os.path.dirname(os.path.realpath(__file__))

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

#class db_connect:
    #def __init__(self, query)
        # Establish mysql connection
        #cnx = mysql.connector.connect(host="localhost", user="rider", password="Delhi2mumbai@", database="travel_diary")

        # Create cursor
        #mycursor = cnx.cursor()

        # Execute a query
        #mycursor.execute("SELECT * FROM travel_diary.vehicles;")

        # Fetch results
        #result = mycursor.fetchall()

        # Close the connection
        #cnx.close()

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
        mycursor.execute("SELECT name, fuel_capacity, mileage FROM travel_diary.vehicles WHERE name='Honda Dio'")
        result = mycursor.fetchall() 
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
        if self.memory=='32gb':
            if self.format=='FHD':
                x = {
                'battery': 180,                 # minutes
                'memory': 2138*4,               # minutes
                }
            if self.format=='HD':
                x = {
                'battery': 180,                 # minutes
                'memory': 7156*4,               # minutes
                }
            if self.format=='VGA':
                x = {
                'battery': 180,                 # minutes
                'memory': 599940*4              # minutes
                }

        return x

    def camera_runtime(self, battery):
 
        # Assign the total minutes left for recording
        battery_left = battery
 
        # Loop to battery minutes
        while battery_left > 0:
 
            # Countdown timer
            timer = datetime.timedelta(minutes = battery_left)
            log.info(timer)
            time.sleep(5)
            battery_left -= 1
 
        log.warning("Alert: Low Battery!")

    def run(self):
        """
        Camera runtime
        """

        # Add all the tables to a panel
        pan = Panel.fit(
            Columns(self.camera_runtime(self.ML_cam()['battery'])),
            title="Camera Battery",         # Title of the panel
            width=80,                       # Width of the panel
            border_style="red",             # Adding border panel
            padding=(1,2)                   # Space between tables
        )
        bot_on = True
        # Clear console
        rc.clear()
        # Print the tables
        with Live(pan, refresh_per_second=60) as live:
            while bot_on:
                next_step = str(input("Do you wish to recheck the camera battery? (Y/n) :")).lower()

                if next_step == "y":
                    live.update(pan)
                    time.sleep(5)
                else:
                    bot_on=False


class location():
    """
    Location details
    """

    #def place(self)

class mileage_logger:
    def __init__(self, img_path):
        self.img_path = img_path
        self.text = ''

    def image_parser(self):
        """Parse image for the numbers/mileage"""
        # Open Image
        all_text = []

        for root, dirs, filenames in os.walk(self.img_path):
            for filename in filenames:
                try:
                    img = Image.open(self.img_path + filename)
                    all_text.append(image_to_string(img))
                    # Deleting the files scanned
                    send2trash.send2trash(img_path + filename)
                except:
                    continue

        text = str('\n'.join(all_text))
        return text


    def number_parse(self):
        """Parse mileage number from the image"""
        # Regex code
        distance_regex = re.compile(r'''(
            ((\s|-|\.)                                  # seperator
            (\d{6})                                     # 6 digits
        )''', re.VERBOSE)

        matches = []
        mileage = ''

        # Extract and Arrange Phone Numbers
        for groups in distance_regex.findall(self.text):
            mileage = ''.join([groups[3], groups[5]])
            matches.append(mileage)
        
        return matches

    def update_mileage(self):
        """Update the database after ride"""
        db_query.run(
        "UPDATE travel_diary.vehicles SET mileage = @self.mileage WHERE name = @self.vehicle;"
        )

    def run(self):
        self.text.join(self.image_parser())
        self.matches = self.number_parse()
        if len(self.matches) > 0:
            distinct_matches = list(dict.fromkeys(self.matches))

            if len(self.matches)!=len(distinct_matches):
                rc.log(str(len(self.matches) - len(distinct_matches)) + ' Duplicates Removed')
            else:
                rc.log('No duplicates found!')

            pyperclip.copy('\n'.join(distinct_matches))

            self.update_mileage()

            rc.log('CopieD to clipboard')
        else:
            rc.log('No mileage number found!!')
