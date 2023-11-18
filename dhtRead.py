"Odczyt wilgotności i temperatury powietrza"

import Adafruit_DHT

sensor_pin = 4
sensor_type = Adafruit_DHT.DHT11

def dhtRead():
    sensor_pin = 4
    sensor_type = Adafruit_DHT.DHT11
    humidity, temperature = Adafruit_DHT.read_retry(sensor_type, sensor_pin)
    return humidity, temperature

