import serial

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.reset_input_buffer()

surveys = []

    surveys.append(current_time)
    surveys.append(humidity)
    surveys.append(temperature)

def atmegaSerial():   
    #odbieranie danych z mikrokontrolera 
    if ser.in_waiting > 0:
        receiver = ser.readline().strip().decode('utf-8')
        dat = receiver.split()
        rv = f"Wilgotność gleby [1]: {dat[0]} %\nIlość wody: {dat[1]} %\n"
        readVal.config(text=rv)
        data.append(dat[0])
        data.append(dat[1])
        dat.clear()
