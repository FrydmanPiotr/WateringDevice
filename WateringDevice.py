"""
Nazwa projektu: WateringDevice
Autor: Piotr Frydman
Opis: Projekt urządzenia do automatycznego nawadniania roślin.
      Okno główne aplikacji.
"""

import tkinter as tk
from tkinter import ttk
from dhtRead import dhtRead
from atmegaSerial import atmegaSerial

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
        self.rowconfigure(2, weight=3)
        self.create_widgets()
        self.update_data()
    
    def create_widgets(self):
        self.airHumidity = tk.Label(self,
                        text=f"Wilgotność powietrza: ")
        self.airHumidity.grid(row=0,column=0)
    
        self.temperature = tk.Label(self,
                    text=f"Temperatura powietrza: ")
        self.temperature.grid(row=1,column=0)
        
        self.readValues = tk.Label(self, text="Wilgotność gleby[1]: 0%\n"\
                                   "Ilość wody: 0%")
        self.readValues.grid(row=2,column=0)
        
        self.saveCsv = tk.Button(self, text="Zapis danych",
                                 command=self.save_data)
        self.saveCsv.grid(row=0,column=1)

    def save_data(self):
        #ustawienia zapisu odczytów
        save_win = tk.Toplevel()
        save_win.title("Zapis danych")
        save_win.geometry('300x200')
        save_win.focus()

        #rozmieszczenie elementów
        self.columnconfigure(0,weight=2)
        self.columnconfigure(1,weight=2)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=3)
        self.rowconfigure(2, weight=3)

        #częstotliwość zapisu odczytów
        vlist = ["1 min", "10 min", "30 min", "1 godz"]
 
        csv = ttk.Combobox(save_win, values = vlist, state="readonly")
        csv.set("Częstotliwość zapisu")
        csv.grid(row=0,column=1)

        ttk.Label(save_win, text="CSV").grid(row=0,column=0)
        ttk.Label(save_win, text="SQL").grid(row=1,column=0)
        
        sql = ttk.Combobox(save_win, values = vlist, state="readonly")
        sql.set("Częstotliwość zapisu")
        sql.grid(row=1,column=1)
        
        save = ttk.Button(save_win, text="OK", command=save_win.destroy)
        close = ttk.Button(save_win, text="Anuluj", command=save_win.destroy)
        save.grid(row=2,column=0)
        close.grid(row=2,column=1)

    def update_data(self):
        #pobieranie odczytów z czujnika DHT11
        humidity, temperature = dhtRead()
	#odbieranie odczytów z czujników (Atmega)
        sensors = atmegaSerial()
        self.airHumidity.config(text=f"Wilgotność powietrza: {humidity} %")
        self.temperature.config(text=f"Temperatura powietrza: {temperature} *C")
        self.readValues.config(text=f"Wilgotność gleby(1): {sensors[0]}%\n"\
			f"Ilość wody: {sensors[1]}")
        
        self.after(1000, self.update_data)
if __name__=="__main__":    
	menu = WateringDevice()
	menu.mainloop()
