#include <Servo.h>  
Servo servoRight;  
Servo servoLeft;
String text;

int leftBias = 0;
int rightBias = 0;

void setup()
{
  Serial.begin(115200);
  servoRight.attach(12);
  servoLeft.attach(13);
  servoRight.write(1500 + rightBias);
  servoLeft.write(1500 + leftBias);
}

void loop()
{
  if(Serial.available()){
    text = Serial.readStringUntil('\n');
    Serial.println(text);
    
    if(text == "forward"){
      forward(200);
    }else if(text == "back"){
      back(200);
    }else if(text == "left"){
      left(200);
    }else if(text == "right"){
      right(200);
    }else if(text == "stop"){
      beStop(200);
    }
  }
}

void left(int spd){
  servoRight.write(1500);
  servoLeft.write(1300);
}

void right(int spd){
  servoRight.write(1700);
  servoLeft.write(1500);
}

void back(int spd){
  servoRight.write(1300);
  servoLeft.write(1700);
}

void forward(int spd){
  servoRight.write(1700);
  servoLeft.write(1300);
}

void beStop(int spd){
  servoRight.write(1500);
  servoLeft.write(1500);
}
