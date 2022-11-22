
#include <Servo.h>
Servo x;
Servo y;
int xnew = 90;
int ynew = 90;
int xpos = 90;
int ypos = 90;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  x.attach(3);
  y.attach(5);
  x.write(xpos);
  y.write(ypos);
}

void loop() {
  // put your main code here, to run repeatedly:
  
    while (Serial.available() > 0)
  {
    
    int Degree = Serial.read(); 
    if (Degree >= 128)
    {
      xnew = round(Degree*1.40625 - 180);
      xnew = (xnew - 180) / -1;
      while (xpos != xnew)
      {
        if (xpos > xnew)
        {
          xpos = xpos - 1;
          x.write(xpos);
        }
        if (xpos < xnew)
        {
          xpos = xpos + 1;
          x.write(xpos);
        }
        delay(1);
      }
    }
    if (Degree < 128)
    {   
      ynew = round(Degree*1.40625);
      while (ypos != ynew)
      {
        if (ypos > ynew)
        {
          ypos = ypos - 1;
          y.write(ypos);
        }
        if (ypos < ynew)
        {
          ypos = ypos + 1;
          y.write(ypos);          
        }
        delay(1);
      }
    }
    
  }
}
