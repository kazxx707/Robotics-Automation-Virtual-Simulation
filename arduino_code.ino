// Simple pick-and-place style sweep for a single-servo demo.
// Extend with multiple Servo objects for shoulder/elbow/gripper.

#include <Servo.h>
Servo arm;

const int SERVO_PIN = 9;

void setup() {
  arm.attach(SERVO_PIN);
  Serial.begin(9600);
  delay(500);
  Serial.println("Arm Ready");
}

void smoothMove(int fromDeg, int toDeg, int stepDelay) {
  if (toDeg >= fromDeg) {
    for (int pos = fromDeg; pos <= toDeg; pos += 2) {
      arm.write(pos);
      delay(stepDelay);
    }
  } else {
    for (int pos = fromDeg; pos >= toDeg; pos -= 2) {
      arm.write(pos);
      delay(stepDelay);
    }
  }
}

void loop() {
  // Example sequence
  smoothMove(0, 60, 20);   // approach pick
  delay(200);
  smoothMove(60, 120, 20); // move to place
  delay(200);
  smoothMove(120, 30, 15); // return
  delay(500);
}