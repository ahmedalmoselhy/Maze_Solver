
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

// Speed
int SpeedLeft = 100;
int SpeedRight = 105;

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
  moveStop();
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
  if(DistanceFw > 10.0){
    moveForward();
    delay(500);
  }
  else if(DistanceRi > 10.0){
    turnRight();
    delay(300);
    moveForward();
    delay(500);
  }
  else if(DistanceLe > 10.0){
    turnLeft();
    delay(300);
    moveForward();
    delay(500);
  }
  else if(DistanceLe < 10.0 && DistanceRi < 10.0 && DistanceFw < 10.0){
    turnLeft();
    delay(300);
  }
}

void moveStop(){
  digitalWrite(RightMotorForward, LOW);
  digitalWrite(LeftMotorForward, LOW);
  digitalWrite(RightMotorBackward, LOW);
  digitalWrite(LeftMotorBackward, LOW);
}

void turnLeft(){
  moveBackward();
  moveStop();
  digitalWrite(RightMotorBackward, LOW);
  digitalWrite(LeftMotorForward, LOW);
  
  analogWrite(RightMotorForward, SpeedRight);
  analogWrite(LeftMotorBackward, SpeedLeft);
}

void turnRight(){
  moveBackward();
  moveStop();
  digitalWrite(LeftMotorBackward, LOW);
  digitalWrite(RightMotorForward, LOW);
  
  analogWrite(LeftMotorForward, SpeedLeft);
  analogWrite(RightMotorBackward, SpeedRight);
}

void moveForward(){
  digitalWrite(RightMotorBackward, LOW);
  digitalWrite(LeftMotorBackward, LOW);
  
  analogWrite(RightMotorForward, SpeedRight);
  analogWrite(LeftMotorForward, SpeedLeft);
}

void moveBackward(){
  moveStop();
  digitalWrite(RightMotorForward, LOW);
  digitalWrite(LeftMotorForward, LOW);

  analogWrite(RightMotorBackward, SpeedRight);
  analogWrite(LeftMotorBackward, SpeedLeft);
  delay(40);
}
