/*
Nazwa projektu: WateringDevice
Autor: Piotr Frydman
Opis: Odbieranie danych z czujników i komunikacja z Raspberry Pi
      (przesyłanie danych)
*/
#define TRIG_PIN 12
#define ECHO_PIN 11
#define SENSOR_PIN A0

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Serial.begin(115200);
}

void loop() { 
  int waterLevel = getWaterLevel();
  double soilHum =  getSoilHumidity();

  if (Serial.available() > 0){
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
