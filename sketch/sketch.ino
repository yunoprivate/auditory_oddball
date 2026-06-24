const int standardPin = 2;
const int targetPin = 3;

void setup() {
  pinMode(standardPin, OUTPUT);
  pinMode(targetPin, OUTPUT);

  digitalWrite(standardPin, LOW);
  digitalWrite(targetPin, LOW);

  Serial.begin(115200);
}

void pulse(int pin) {
  digitalWrite(pin, HIGH);
  delayMicroseconds(5000);
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
