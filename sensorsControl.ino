/*
Nazwa projektu: WateringDevice
Autor: Piotr Frydman
Opis: Odbieranie danych z czujników i komunikacja z Raspberry Pi
      (przesyłanie danych i sterowanie pompą wody)
*/
#include <SimpleDHT.h>
#define TRIG_PIN 12
#define ECHO_PIN 11
#define SENSOR_PIN A0
String receivedData;

const int pinDHT11 = 5; //czujnik wilgoci i temperatury powietrza
SimpleDHT11 dht11;

void setup() {
  pinMode(3, OUTPUT); //zasilanie pompy
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Serial.begin(115200);
}

void loop() { 
  int waterLevel = getWaterLevel();
  double soilHum =  getSoilHumidity();

  //odbieranie danych z Raspberry Pi
  if (Serial.available() > 0){
    receivedData = Serial.readStringUntil('\n');
  
  if (receivedData == "1-on"){
    while (waterLevel > 20 && soilHum < 10)
      digitalWrite(3, HIGH);
    digitalWrite(3, LOW);
  }
  if (receivedData == "0-off"){
    digitalWrite(3, LOW); }
  }
  else {
  //wysyłanie danych do Raspberry Pi
  Serial.println(String(soilHum) + " " + String(waterLevel));
  } 
}

//odczytuje poziom wody w zbiorniku
int getWaterLevel() {
  long duration, distance;
  
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  duration = pulseIn(ECHO_PIN, HIGH);
  distance = duration / 58;
  int d = (10 - distance)*10;
  return d;
}

//odczytuje poziom wilgotności gleby
double getSoilHumidity() {
  double soilHumidityValue = analogRead(SENSOR_PIN);
  double soilHum = (1024/soilHumidityValue)*10;
  return soilHum;
}
