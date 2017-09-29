
void setup() {
  // put your setup code here, to run once:
  Serial.begin(57600);
  Serial3.begin(57600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial3.available()) {
    byte b = Serial3.read();
    Serial.print((char)b);
  }
  while(Serial.available()) {
    byte b = Serial.read();
    Serial3.write(b);
  }
}
