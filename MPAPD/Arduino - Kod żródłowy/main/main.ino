// github.com/mateuszpiela
#include "DHT.h"
#define pin 2
#define type DHT11
DHT dht(pin, type);
void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600);
   dht.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
      delay(20);
      float t = dht.readTemperature();
      Serial.print(t);
      Serial.print("\n");
  }
}
