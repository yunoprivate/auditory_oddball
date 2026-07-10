const int standardPin = 2;
const int targetPin = 3;

void setup() {
  pinMode(standardPin, OUTPUT);
  pinMode(targetPin, OUTPUT);

  digitalWrite(standardPin, LOW);
  digitalWrite(targetPin, LOW);

  Serial.begin(115200);
  Serial.write(0xFF); // ready
}

void pulse(int pin) {
  digitalWrite(pin, HIGH);
  delayMicroseconds(100000);
  digitalWrite(pin, LOW);
}

void loop() {
  if (Serial.available()) {
    char code = Serial.read();

    if (code == '1') {
      pulse(standardPin);
    } else if (code == '2') {
      pulse(targetPin);
    }
  }
}
