#include <Servo.h>

Servo myServo;
int pos =90;

void setup() {
  myServo.attach(9);
  myServo.write(90);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    int data = Serial.parseInt();
    Serial.print("Received: ");
    Serial.println(data);
    if(data<-50){
      pos +=1;
      pos = max(pos,0);
      myServo.write(pos);
      delay(1);
    }
    if(data>50){
      pos -=1;
      pos = min(pos,180);
      myServo.write(pos);
      delay(1);
    }
  }
}
