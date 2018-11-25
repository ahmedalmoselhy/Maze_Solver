#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11);
String data = "";


void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);

}

void loop() {
  if(mySerial.available()){
    data = mySerial.readStringUntil('\n');
    Serial.println(data);  
  }

  if(Serial.available()){
    data = Serial.readStringUntil('\n');
    mySerial.println(data);  
  }

}
