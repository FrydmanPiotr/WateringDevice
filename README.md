## WateringDevice
Design of a device for automatic plant irrigation.

The device is based on a single board computer (SBC)
Raspberry Pi model 3B+ and the Arduino development platform
Uno Rev 3 (Atmega 328p). The software for the RPi is written
in Python, and for Arduino in C++. Communication
between the microcontroller and the computer is established by
UART interface (USB port).

## Table of contents:
1) Arduino and sensors
2) Raspberry Pi - DHT sensor
3) Raspberry Pi - graphical user interface (GUI)

Arduino and sensors
==================================================================
Arduino receives data from sensors, i.e.:
 * HC-SR04 ultrasonic distance sensor
 * soil moisture sensor

Raspberry Pi - DHT sensor
=================================================================
Raspberry Pi is connected to the DHT11 sensor. It allows reading
ambient air temperature and humidity.
The measurement results are displayed in the main window of the user interface.

A DHT sensor must be installed to ensure proper operation
Adafruit library. In the terminal, execute the following commands:

```
$ git clone https://github.com/adafruit/Adafruit_Python_DHT.git
$ cd Adafruit_Python_DHT
$ sudo python setup.py install
```

Raspberry Pi - graphical user interface (GUI)
================================================================= 
The windowed user interface was written in the library
standard Python language called Tkinter. It displays the read data
from the DHT11 sensor and measurement results received from soil moisture sensors and
water level in the tank connected to Arduino. Measurement results are automatic
updated.
