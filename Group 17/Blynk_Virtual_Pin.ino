#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

#define BLYNK_PRINT Serial
#define trigPin 0
#define echoPin 2

BlynkTimer timer;
const char auth[] = "5489c195b16345fabf7b3ab2cdb80aac", ssid[] = "RedWheel_Barrow", pass[] = "31@reyalp";
int calb;
float fc = 35;      //minimum capacity to measure

BLYNK_WRITE(V2)
{
  calb = param.asInt();
}

void cal_dist()
{
  double duration, distance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration=pulseIn(echoPin, HIGH);
  distance =((duration/2)*0.0343);
  fc = (calb)?distance:fc;
  if(distance <= fc)
  {
    double adj = (fc > 60.49)?20:6;
    Blynk.virtualWrite(V0, distance);
    Blynk.virtualWrite(
      V1, 100-((distance-adj)/(fc-adj))*100);
  }
  else
    Blynk.notify("Please Caliberate Position!!");
}

void setup()
{
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);  
  Blynk.begin(auth, ssid, pass);
  timer.setInterval(10L, cal_dist);
}

void loop()
{
  Blynk.run();
  timer.run();
}
