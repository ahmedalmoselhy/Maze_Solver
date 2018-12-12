
//Left Motor
const int LeftMotorForward = 5;
const int LeftMotorBackward = 3;
//Right Motor
const int RightMotorForward = 9;
const int RightMotorBackward = 6;

//UltraSonicForward
const int UltraFwTrig = 10;
const int UltraFwEcho = 11;
//UltraSonicLeft
const int UltraLeTrig = 13;
const int UltraLeEcho = 12;
//UltraSonicRight
const int UltraRiTrig = 8;
const int UltraRiEcho = 7;

//Additonal Needs
float DistanceFw;
float DistanceLe;
float DistanceRi;

//Time Variables
float TimeFw;
float TimeLe;
float TimeRi;

void setup() {
  //Motors Pins
  pinMode(LeftMotorForward,OUTPUT);
  pinMode(LeftMotorBackward,OUTPUT);
  pinMode(RightMotorForward,OUTPUT);
  pinMode(RightMotorBackward,OUTPUT);

  //UltraSonic Pins
  pinMode(UltraFwEcho,INPUT);
  pinMode(UltraFwTrig,OUTPUT);
  pinMode(UltraLeEcho,INPUT);
  pinMode(UltraLeTrig,OUTPUT);
  pinMode(UltraRiEcho,INPUT);
  pinMode(UltraRiTrig,OUTPUT);

}

void loop() {
  //Forward
  digitalWrite (UltraFwTrig,LOW);
  delayMicroseconds(3);
  digitalWrite (UltraFwTrig,HIGH);
  delayMicroseconds(10);
  digitalWrite (UltraFwTrig,LOW);
  TimeFw=pulseIn(UltraFwEcho,HIGH);
  DistanceFw=float(TimeFw)/58.8 ;
  delay(100);

  //Left
  digitalWrite (UltraLeTrig,LOW);
  delayMicroseconds(3);
  digitalWrite (UltraLeTrig,HIGH);
  delayMicroseconds(10);
  digitalWrite (UltraLeTrig,LOW);
  TimeLe=pulseIn(UltraLeEcho,HIGH);
  DistanceLe=float(TimeLe)/58.8 ;
  delay(100);

  //Right
  digitalWrite (UltraRiTrig,LOW);
  delayMicroseconds(3);
  digitalWrite (UltraRiTrig,HIGH);
  delayMicroseconds(10);
  digitalWrite (UltraRiTrig,LOW);
  TimeRi=pulseIn(UltraRiEcho,HIGH);
  DistanceRi=float(TimeRi)/58.8 ;
  delay(100);

  //Movement Conditions
  if(DistanceLe > 15.0){
    turnLeft();
    delay(300);
  }
  else if(DistanceRi > 15.0){
    turnRight();
    delay(300);
  }
  if(DistanceRi < 5.0 && DistanceLe < 5.0 && DistanceFw <5.0){
    turnLeft();
    delay(300);
  }
  if(DistanceRi > 170.0){
    turnLeft();
    delay(300);
  }
  if(DistanceLe > 170.0){
    turnRight();
    delay(300);
  }

  

  moveForward();
  delay(700);
  moveStop();
}

void moveStop(){
  digitalWrite(RightMotorForward, LOW);
  digitalWrite(LeftMotorForward, LOW);
  digitalWrite(RightMotorBackward, LOW);
  digitalWrite(LeftMotorBackward, LOW);
}

void turnLeft(){
  moveStop();
  digitalWrite(RightMotorBackward, LOW);
  digitalWrite(LeftMotorForward, LOW);
  
  analogWrite(RightMotorForward, 128);
  analogWrite(LeftMotorBackward, 128);
}

void turnRight(){
  moveStop();
  digitalWrite(LeftMotorBackward, LOW);
  digitalWrite(RightMotorForward, LOW);
  
  analogWrite(LeftMotorForward, 128);
  analogWrite(RightMotorBackward, 128);
}

void moveForward(){
  moveStop();
  digitalWrite(RightMotorBackward, LOW);
  digitalWrite(LeftMotorBackward, LOW);
  
  analogWrite(RightMotorForward, 128);
  analogWrite(LeftMotorForward, 128);
}
