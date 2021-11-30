#include <Servo.h>  
Servo servoRight;  
Servo servoLeft;           
void setup() 
{ 
  servoRight.attach(12);   
  servoLeft.attach(13);   
  Serial.begin(115200); 
}  

void loop()
{ 
  char c;              
  // 讀取串列阜資料
  String inputSpeed = "";
  if(Serial.available()){
    c = Serial.read();
    while (c != '\n') 
    {
        inputSpeed += c;
    delay(5);
        c = Serial.read();
    }
    int SPEED;
    sscanf(inputSpeed.c_str(),"%c_%d",&c,&SPEED);
    switch (c)  
    {    
       case '1':
            forward(100,SPEED); //呼叫前進的副程式
            break;
       case '2':
           trunLeft(100,SPEED);     //呼叫左轉的副程式
           break;
       case '3':
           trunRight(100,SPEED);    //呼叫右轉的副程式
           break;
       case '4':
           backward(100,SPEED);     //呼叫後退的副程式  
           break;
       case '8':
           bestop();    //呼叫停止的副程式
    } 
    while(Serial.read() >= 0){}
  }
}
void forward(int time,int SPEED){       //前進的副程式
    servoRight.writeMicroseconds(1500 - SPEED);
    servoLeft.writeMicroseconds(1500 + SPEED);
      }
void trunLeft(int time,int SPEED){
    servoRight.writeMicroseconds(1500);
    servoLeft.writeMicroseconds(1500 + SPEED);
      }    
void trunRight(int time,int SPEED){     //右轉的副程式
    servoRight.writeMicroseconds(1500 - SPEED);
    servoLeft.writeMicroseconds(1500);
       }
void backward(int time,int SPEED){      //後退的副程式
    servoRight.writeMicroseconds(1500 + SPEED);
    servoLeft.writeMicroseconds(1500 - SPEED);
      }
void bestop(){      //停止的副程式
    servoRight.write(1500);
    servoLeft.write(1500);
}
