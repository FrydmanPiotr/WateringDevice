"""
Title: WateringDevice
Author: Piotr Frydman
"""

import tkinter as tk
from tkinter import ttk
#from dhtRead import dhtRead
#from atmegaSerial import atmegaSerial

class WateringDevice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Plants irrigation")
        self.geometry("600x400")
        #self.update_data()
        self.load_menu()
    
    def load_menu(self):
        airHum = tk.Label(self, text=f"Air humidity: ").place(x=20,y=20)
        airTemper = tk.Label(self, text=f"Air temperature: ").place(x=20,y=60)
        soilHum =tk.Label(self, text="Soil humidity [1]: 0 %").place(x=20,y=100)
        waterLev = tk.Label(self, text="Water level: 0 %").place(x=20,y=140)
        
        tk.Button(self, text="Database save",bd=3,
                  command=self.save_data).place(x=20,y=180)

    def save_data(self):
        save_win = tk.Toplevel()
        save_win.title("Database save")
        save_win.geometry('250x100+500+250')
        save_win.focus()

        ttk.Label(save_win, text="Save time (min)").place(x=10,y=30)
        #set saving frequency
        save = ttk.Spinbox(save_win, from_=1,to=10)
        
        ttk.Button(save_win, text="OK").place(x=50,y=60)
        ttk.Button(save_win, text="Cancel",
                   command=save_win.destroy).place(x=130,y=60)

    def update_senors_readings(self):
        #fetch data from DHT11 sensor
        humidity, temperature = dhtRead()
	#communicate with Atmega
        sensors = atmegaSerial()
        self.airHum.config(text=f"Air humidity: {humidity} %")
        self.airTemper.config(text=f"Air temperature: {temperature} *C")
        self.soilHum.config(text=f"Soil humidity [1]: {sensors[0]} %")
        self.waterLev.config(text=f"Water level: {sensors[1]}")
        self.after(1000, self.update_senors_readings)

if __name__=="__main__":
    menu = WateringDevice()
    menu.mainloop()
