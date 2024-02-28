#include <SoftwareSerial.h>

SoftwareSerial bluetooth(10, 11); // RX, TX

void setup() {
  Serial.begin(9600);
  bluetooth.begin(9600);
}

void loop() {
  byte nitrogen_val, phosphorus_val, potassium_val;

  nitrogen_val = nitrogen();
  delay(250);
  phosphorus_val = phosphorous();
  delay(250);
  potassium_val = potassium();
  delay(250);

  bluetooth.print("N:");
  bluetooth.print(nitrogen_val);
  bluetooth.print(",P:");
  bluetooth.print(phosphorus_val);
  bluetooth.print(",K:");
  bluetooth.println(potassium_val);

  delay(2000);
}

byte nitrogen(){
  // Implement the nitrogen function here
  return 0;
}

byte phosphorous(){
  // Implement the phosphorous function here
  return 0;
}

byte potassium(){
  // Implement the potassium function here
  return 0;
}
