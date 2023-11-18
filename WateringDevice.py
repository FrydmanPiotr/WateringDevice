"""
Nazwa projektu: WateringDevice
Autor: Piotr Frydman
Opis: Projekt urządzenia do automatycznego nawadniania roślin
"""
import tkinter as tk
from tkinter import ttk
from dhtRead import dhtRead

class WateringDevice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nawadnianie roślin")
        self.geometry("600x400")
        
        #rozmieszczenie widgetów
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=3)       
        self.create_widgets()
        self.update_data()
    
    def create_widgets(self):
        self.airHumidity = tk.Label(self,
                        text=f"Wilgotność powietrza: ")
        self.airHumidity.grid(row=0,column=0)
    
        self.temperature = tk.Label(self,
                    text=f"Temperatura powietrza: ")
        self.temperature.grid(row=1,column=0)

    def update_data(self):
        humidity, temperature = dhtRead()
        self.airHumidity.config(text=f"Wilgotność powietrza: {humidity} %")
        self.temperature.config(text=f"Temperatura powietrza: {temperature} *C")
        
        self.after(1000, self.update_data)

menu = WateringDevice()
menu.mainloop()
