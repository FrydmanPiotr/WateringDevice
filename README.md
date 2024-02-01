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
4) Zapisywanie danych w arkuszu kalkulacyjnym
5) Import do bazy danych MySQL

Arduino i czujniki
=============================================================================
Arduino odbiera dane z czujników tj.:
 -> ultradźwiękowy czujnik odległości HC-SR04                                     
 -> czujnik wilgotności gleby

Raspberry Pi - czujnik DHT
=============================================================================
Raspberry Pi jest połączone z czujnikiem DHT11. Umożliwia on odczyt 
temperatury i wilgotności powietrza w otoczeniu.
Wyniki pomiaru są wyświetlane w interfejsie użytkownika. 

W celu zapewnienia prawidłowego działania czujnika DHT należy zainstalować 
bibliotekę Adafruit. W terminalu należy wykonać następujące komendy:

$ git clone https://github.com/adafruit/Adafruit_Python_DHT.git
$ cd Adafruit_Python_DHT
$ sudo python setup.py install

Raspberry Pi - graficzny interfejs użytkownika (GUI)
===============================================================================
Interfejs użytkownika w postaci okienkowej został napisany w bibliotece 
standardowej języka Python o nazwie Tkinter. Wyświetla dane odczytane z czujnika DHT11.

Zapisywanie danych w pliku w formacie .ods
==============================================================================
Dane odczytane z czujnika DHT11 są zapisywane w pliku w arkuszu kalkulacyjnym w 
formacie .ods (Linux) / .csv (Windows). 

Import do bazy danych MySQL
===============================================================================
Dane zapisane w arkuszu kalulacyjnym na dysku lokalnym są automatycznie eksportowane 
do bazy danych MySQL.
