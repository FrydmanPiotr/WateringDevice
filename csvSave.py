"""
Zapisywanie danych na dysku lokalnym w pliku w formacie CSV.
Autor: Piotr Frydman
"""
from tkinter import *
from datetime import date
from dhtRead import dhtRead
from atmegaSerial import atmegaSerial
import csv
import os
import time

class csvSave:
    def __init__(self):
        self.today = date.today()
        self.year = date.today().year
        self.month = date.today().month
        self.dir_name = "readings"
        self.filename = f"{self.today}_readings.ods"
        self.dir_path = os.path.join("/home/pi/Desktop", self.dir_name,
                                     str(self.year), str(self.month))
        self.file_path = os.path.join(self.dir_path, self.filename)
        self.header = ["Czas odczytu", "Wilg. pow.", "Temp. pow.",
                       "Wilg.gl(1)"]

    def getSurveys(self):
        surveys = []
        #czas odczytu
        read_time = time.localtime()
        current_time = time.strftime("%H:%M:%S", read_time) 
        humidity, temperature = dhtRead()
        sensors = atmegaSerial()
        surveys.append(current_time)
        surveys.append(humidity)
        surveys.append(temperature)
        surveys.append(sensors[0])
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

csv_save = csvSave()
csv_save.getSurveys()
