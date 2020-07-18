#include <avr/wdt.h>
#include <Stepper.h>

#define STOP 0
#define SEND_COMP 1
#define TRACK_ON 2
#define TRACK_OFF 3

#define SPD_RANGE_UPPER 256
#define SPD_RANGE_LOWER 100

#define LEFT_F_PIN 9
#define LEFT_B_PIN 10
#define RIGHT_F_PIN 3
#define RIGHT_B_PIN 5

#define CONVEYOR_PIN 11

#define STEP1 5
#define STEP2 4
#define STEP3 3
#define STEP4 2
#define STEP_REV 2000

#define NORMAL_SPD 50
#define TURN_OFFSET 25

Stepper track(STEP_REV, STEP1, STEP2, STEP3, STEP4); 
char Data = 0;
char spR = 0;
char spL = 0;

bool isTrackOn = false;

void setup() {
  Serial.begin(9600);
  delay(500);
  Serial.write("s");

  motorStop();

  //wdt_disable();
}

void loop() {

  if (Serial.available())
  {
    Data = Serial.read();
    if (Data >= 'a' && Data <= 'f')
    {
      delay(200);
      Serial.write("s");
      delay(200);
    }
  }
  else
    Data = 'a';

  // No ball was found
  if(Data == 'a')
  {
    spL = NORMAL_SPD;
    spR = NORMAL_SPD;
  }
  // Ball found (left to right is mapped to 1-5 respectivly)
  else
  {
    spL = NORMAL_SPD + (Data > 'd') * TURN_OFFSET 
                     + (Data > 'e') * TURN_OFFSET;
    
    spR = NORMAL_SPD + (Data < 'd') * TURN_OFFSET 
                     + (Data < 'c') * TURN_OFFSET;

    if (!isTrackOn)
    {
      analogWrite(CONVEYOR_PIN, 100);
      isTrackOn = true;
      //wdt_enable(WDTO_8S);
    }
  }

  motorsOn();
}

void motorsOn()
{
  analogWrite(LEFT_F_PIN, spL);
  analogWrite(RIGHT_F_PIN, spR);
}

void motorStop()
{
  analogWrite(LEFT_F_PIN, 0);
  analogWrite(LEFT_B_PIN, 0);
  analogWrite(RIGHT_F_PIN, 0);
  analogWrite(RIGHT_B_PIN, 0);
}
