# WateringDevice
Projekt urządzenia do automatycznego nawadniania roślin.

Urządzenie jest oparte na komputerze jednopłytkowym (SBC) 
Raspberry Pi model 3B+ oraz platformie rozwojowej Arduino
Uno Rev 3 (Atmega 328p). Oprogramowanie dla RPi jest napisane 
w języku Python, natomiast dla Arduino w języku C++. Komunikacja 
pomiędzy mikrokontrolerem i komputerem jest nawiązywana przez 
interfejs UART (port USB).

Spis treści:
1) Arduino i czujniki
2) Raspberry Pi - czujnik DHT
3) Raspberry Pi - graficzny interfejs uzytkowanika (GUI)

Arduino i czujniki
=============================================================================
Arduino odbiera dane z czujników tj.:
 -> ultradźwiękowy czujnik odległości HC-SR04                                     
 -> czujnik wilgotności gleby

Raspberry Pi - czujnik DHT
=============================================================================
Raspberry Pi jest połączone z czujnikiem DHT11. Umożliwia on odczyt 
temperatury i wilgotności powietrza w otoczeniu.
Wyniki pomiaru są wyświetlane w oknie głównym interfejsu użytkownika. 

W celu zapewnienia prawidłowego działania czujnika DHT należy zainstalować 
bibliotekę Adafruit. W terminalu należy wykonać następujące komendy:

$ git clone https://github.com/adafruit/Adafruit_Python_DHT.git
$ cd Adafruit_Python_DHT
$ sudo python setup.py install

Raspberry Pi - graficzny interfejs użytkownika (GUI)
===============================================================================
Interfejs użytkownika w postaci okienkowej został napisany w bibliotece 
standardowej języka Python o nazwie Tkinter. Są w nim wyświetlane dane odczytane 
z czujnika DHT11 oraz wyniki pomiarów odebrane z czujników wilgotności gleby i 
poziom wody w zbiorniku połączonych z Arduino. Wyniki pomiarów są automatycznie 
aktualizowane.
