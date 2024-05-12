"""
Saving data in database.
Author: Piotr Frydman
"""

from dhtRead import dhtRead
from atmegaSerial import atmegaSerial
import sqlite3 as db
import time

class dbSave():
    def __init__(self):
        self.current_date=time.strftime('%d_%m_%Y', time.localtime())
        self.table_name = f"sensors_{self.current_date}"
        self.conn = db.connect("wat_dev.sqlite")
        self.cur = self.conn.cursor()                              

    def connect_to_database(self):
        self.conn = db.connect("imgw.sqlite")
        self.cur = self.conn.cursor()

    def close_database_connection(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
    
    def create_table(self):
        self.connect_to_database()
        query = f'''CREATE TABLE IF NOT EXISTS {self.table_name}
            (Hour TIME,
            Air_humidity FLOAT,
            Air_temperature FLOAT,
            Soil_humidity(1) FLOAT)'''
        self.cur.execute(query)
        self.save_to_database()
        
    def save_to_database(self):
        reading_time = time.strftime("%H:%M:%S", time.localtime()) 
        humidity, temperature = dhtRead()
        sensors = atmegaSerial()
                
        query = f'''INSERT INTO {self.table_name}
        (Hour, Air_humidity, Air_temperature,
        Soil_humidity) VALUES (?, ?, ?, ?, ?)'''
        
        self.cur.execute(query, (reading_time, humidity, temperature, sensors))
        self.conn.commit()
        self.close_database_connection()

            
