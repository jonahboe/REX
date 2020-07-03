#define STOP 0
#define SEND_COMP 1
#define TRACK_ON 2
#define TRACK_OFF 3

#define SPD_RANGE_UPPER 256
#define SPD_RANGE_LOWER 100

#define LEFT_F_PIN 11
#define LEFT_B_PIN 10
#define RIGHT_F_PIN 9
#define RIGHT_B_PIN 6

#define STEP1 5
#define STEP2 4
#define STEP3 3
#define STEP4 2
#define STEP_REV 2000

#include <Stepper.h>

Stepper track(STEP_REV, STEP1, STEP2, STEP3, STEP4); 
char data = 0;
bool isTrackOn = false;
bool isNewData = false;

void setup() {

}

void loop() {

  if(isNewData)
    decodeData();
  
  if (isTrackOn)
    track.step(10);
}

void decodeData()
{
   switch (data)
  {
    case 0: 
      motorsstop();
    break;
    case 1: 
      sendcompass();
    break;
    case 2: 
      isTrackOn = true;
    break;
    case 3: 
      isTrackOn = false;
    break;
    case 4: 
      //AVAILABLE TASK 1
    break;
    case 5:
      //AVAILABLE TASK 2
    break;
    case 6: 
      //AVAILABLE TASK 3
    break;
    case 7: 
      //AVAILABLE TASK 4
    break;
    default:
      setMotorSpeed();
    break;
  }
}

void motorsstop()
{
  analogWrite(LEFT_F_PIN, 0);
  analogWrite(LEFT_B_PIN, 0);
  analogWrite(RIGHT_F_PIN, 0);
  analogWrite(RIGHT_B_PIN, 0);
}

void sendcompass()
{
  //INSERT SERIAL SEND COMPASS DATA
}

// Motor Speed Code Ranges
// Left [8,131]
//   Forward [8,69]
//   Backward [70, 131]
//
// Right [132, 255]
//   Forward [132,193] 
//   Backward [194, 255]
void setMotorSpeed()
{
  char spd;
  if(data>=131) //left motor
  {
    if (data >= 69) //left forward
    {
      spd = map(data, 8, 69, SPD_RANGE_LOWER, SPD_RANGE_UPPER);
      analogWrite(LEFT_F_PIN, spd); 
      analogWrite(LEFT_B_PIN, 0);     
    }
    else  //left backward
    {
      spd = map(data, 70, 131, SPD_RANGE_LOWER, SPD_RANGE_UPPER);
      analogWrite(LEFT_F_PIN, 0);
      analogWrite(LEFT_B_PIN, spd);
    }
  }
  else  //right wire
  {
      if (data >= 193) //right forward
    {
      spd = map(data, 132, 193, SPD_RANGE_LOWER, SPD_RANGE_UPPER);
      analogWrite(RIGHT_F_PIN, spd);
      analogWrite(RIGHT_B_PIN, 0); 
    }
    else  //right backward
    {
      spd = map(data, 193, 255, SPD_RANGE_LOWER, SPD_RANGE_UPPER);
      analogWrite(RIGHT_F_PIN, 0);
      analogWrite(RIGHT_B_PIN, spd);
    }
  }
}
