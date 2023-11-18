"""
Zapisywanie danych do bazy danych MySQL.
Autor: Piotr Frydman
"""
from tkinter import *
from tkinter import ttk
import pandas as pd
import mysql.connector as msql
from mysql.connector import Error
from datetime import date

today = date.today()
databaseName = "wd_tem_hum"
tableName = "tem_hum_" + str(today)
file_path = "/home/pi/Desktop/{today}_temp_hum.ods"

class dbSave():
    def __init__(self, databaseName="wd_temp_hum", tableName=None):
        self.databaseName = databaseName
        self.tableName = tableName

    def connectDB(self):
        wdData = pd.read_csv(file_path, index_col=False, delimiter=';')

        # połączenie do bazy danych
        try:
            conn = msql.connect(host="localhost", user="root", password="")
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.databaseName}")
                cursor.execute(f"USE {self.databaseName};")
                self.saveSQL(cursor, conn, wdData)

        except Error as e:
            print("Error:", e)

        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

    def saveSQL(self, cursor, conn, wdData):
        # utworzenie tabeli w bazie danych
        create_table = f'CREATE TABLE IF NOT EXISTS {self.tableName}(' \
                        'read_time TIME, air_hum FLOAT, air_temp FLOAT, soil_hum FLOAT);'
        cursor.execute(create_table)

        insert_query = f'INSERT INTO {self.tableName} (read_time, air_hum, air_temp, soil_hum) VALUES (%s, %s, %s, %s)'
        for i, row in wdData.iterrows():
            cursor.execute(insert_query, tuple(row))
            conn.commit()

db_saver = dbSave(databaseName, tableName)
db_saver.connectDB()                 
