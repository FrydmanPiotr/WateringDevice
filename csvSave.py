"""
Zapisywanie danych na dysku lokalnym w arkuszu kalkulacyjnym.
Autor: Piotr Frydman
"""
from tkinter import *
from datetime import date
from dhtRead import dhtRead
import csv
import os
import time

class csvSaver:
    def __init__(self):
        self.today = date.today()
        self.year = date.today().year
        self.month = date.today().month
        self.dir_name = "temp_hum"
        self.filename = f"{self.today}_temp_hum.ods"
        self.dir_path = os.path.join("/home/pi/Desktop", self.dir_name, str(self.year), str(self.month))
        self.file_path = os.path.join(self.dir_path, self.filename)
        self.header = ["Czas odczytu", "Wilg. pow.", "Temp. pow."]

    def getSurveys(self):
        surveys = []
        #czas odczytu
        read_time = time.localtime()
        current_time = time.strftime("%H:%M:%S", read_time) 
        humidity, temperature = dhtRead()
        surveys.append(current_time)
        surveys.append(humidity)
        surveys.append(temperature)
        self.save_to_csv(surveys)
    
    #tworzenie nowego pliku
    def save_to_csv(self, surveys):
        if os.path.isfile(self.file_path):
            os.chdir(self.dir_path)
            #zapis danych
            with open(self.filename, 'a',newline="") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(surveys)
            file.close()

        else:
            #tworzenie ścieżki do nowego katalogu
            os.makedirs(self.dir_path)
            #przejście do innego katalogu
            os.chdir(self.dir_path)

            with open(self.filename, 'w', newline="") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(self.header)
            file.close()

csv_save = csvSaver()
csv_save.getSurveys()
