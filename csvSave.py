"""
Saving data in CSV file.
Author: Piotr Frydman
"""

from dhtRead import dhtRead
from atmegaSerial import atmegaSerial
import csv
import os
import time

class csvSave():
    def __init__(self):
        current_time = time.strftime('%d_%m_%Y', time.localtime())
        self.filename = time.strftime(f"{current_time}_readings.ods")
        self.dir_path = time.strftime(f"/home/pi/Desktop/readings/"/
                                      "%Y/%m/", current_time)                             
        
    def fetch_readings(self):
        readings = []
        read_time = time.strftime("%H:%M", time.localtime()) 
        humidity, temperature = dhtRead()
        sensors = atmegaSerial()
        readings.append(read_time)
        readings.append(humidity)
        readings.append(temperature)
        readings.append(sensors[0])
        self.save_to_csv(readings)
    
    def save_to_csv(self, readings):
        if os.path.isfile(self.file_path):
            os.chdir(self.dir_path)
            
            with open(self.filename, 'a',newline="") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(readings)
            file.close()

        else:
            os.makedirs(self.dir_path)
            os.chdir(self.dir_path)
            
            header = ["Reading time", "Air hum.", "Air temper.", "Soil hum.(1)"]
            with open(self.filename, 'w', newline="") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(header)
            file.close()
