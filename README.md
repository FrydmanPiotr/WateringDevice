# WateringDevice
Projekt urządzenia do automatycznego nawadniania roślin.

Urządzenie jest oparte na komputerze jednopłytkowym (SBC) Raspberry Pi model 3B+. 
Oprogramowanie dla RPi jest napisane w języku Python.

Spis treści:
1) Raspberry Pi - czujnik DHT
2) Graficzny interfejs uzytkowanika (GUI)
3) Zapisywanie danych w arkuszu kalkulacyjnym
4) Import do bazy danych MySQL

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

Import do bazy danych 
===============================================================================
Dane zapisane w arkuszu kalulacyjnym na dysku lokalnym są automatycznie eksportowane 
do bazy danych MySQL.
