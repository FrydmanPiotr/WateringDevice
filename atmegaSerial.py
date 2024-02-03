import serial

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.reset_input_buffer()

def atmegaSerial():   
    #odbieranie danych z mikrokontrolera 
    if ser.in_waiting > 0:
        receiver = ser.readline().strip().decode('utf-8')
        sensors = receiver.split()
        return sensors
        sensors.clear()
