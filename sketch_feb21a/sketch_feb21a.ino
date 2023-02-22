#include <LedControl.h>

const int DIN_PIN = 12;
const int CS_PIN = 10;
const int CLK_PIN = 11;
const int NUM_DEVICES = 1;

LedControl lc = LedControl(DIN_PIN, CLK_PIN, CS_PIN, NUM_DEVICES);

int row = 0;
int col = 0;
int row2 = 0;
int col2 = 0;

void setup() {
  lc.shutdown(0, false);
  lc.setIntensity(0, 1);
  lc.clearDisplay(0);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() >= 4) {
    row = Serial.read();
    col = Serial.read();
    row2 = Serial.read();
    col2 = Serial.read();
    lc.setLed(0, row, col, true);
    lc.setLed(0, row2, col2, true);
    delay(7000);
    lc.setLed(0, row, col, false);
    lc.setLed(0, row2, col2, false);
    delay(1000);
  }
}
