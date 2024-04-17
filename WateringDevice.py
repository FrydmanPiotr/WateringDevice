"""
Title: WateringDevice
Author: Piotr Frydman
"""

import tkinter as tk
from tkinter import ttk
from dhtRead import dhtRead
from atmegaSerial import atmegaSerial

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
        
        tk.Button(self, text="Saving data",bd=3,
            command=self.save_data).place(x=20,y=180)

    def save_data(self):
        save_win = tk.Toplevel()
        save_win.title("Saving data")
        save_win.geometry('220x100+500+250')
        save_win.focus()

        ttk.Label(save_win, text="CSV").place(x=10,y=30)
        #save frequency settings
        csv = ttk.Spinbox(save_win, from_=1,to=10)
        #csv.set("Recording frequency")
        csv.place(x=40,y=30)
        ttk.Button(save_win, text="OK").place(x=40,y=60)
        ttk.Button(save_win, text="Cancel",
                   command=save_win.destroy).place(x=120,y=60)

    def update_data(self):
        #fetch data from DHT11 sensor
        humidity, temperature = dhtRead()
	#communicate with Atmega
        sensors = atmegaSerial()
        self.airHum.config(text=f"Air humidity: {humidity} %")
        self.airTemper.config(text=f"Air temperature: {temperature} *C")
        self.soilHum.config(text=f"Wilgotność gleby(1): {sensors[0]} %")
	self.waterLev.config(text=f"Ilość wody: {sensors[1]}")
        self.after(1000, self.update_data)

if __name__=="__main__":
    menu = WateringDevice()
    menu.mainloop()
