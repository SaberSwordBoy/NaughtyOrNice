//Bryce Casamento 2021

//Pins
int buttonPin = 2;
int greenLed = 6;
int redLed = 9;
int statusLedPin = 5;

//Other Vars
int buttonState1 = 0;
bool buttonPressed = false;
int naughtyOrNice = 0;

void onButtonPressed() {
  buttonPressed = true;
  naughtyOrNice = random(0,11);
  if (naughtyOrNice < 5) {
    buildupSequence();
    Serial.println("nice");
    delay(500);
    greenLedOn();
  }
  if (naughtyOrNice > 6) {
    buildupSequence();
    Serial.println("naughty");
    delay(500);
    redLedOn();
  }
  buttonPressed = false;
}

void buildupSequence() {
  Serial.println("buildup");
  delay(1000);
  for (int i=0; i < 35; i++) {
    digitalWrite(redLed, HIGH);
    delay(100);
    digitalWrite(redLed, LOW);
    digitalWrite(greenLed, HIGH);
    delay(100);
    digitalWrite(greenLed, LOW);
  }
}
void redLedOn() {
  digitalWrite(redLed, HIGH);
  digitalWrite(greenLed,LOW);
  delay(5000);
  digitalWrite(redLed, LOW);
}
void greenLedOn() {
  digitalWrite(greenLed, HIGH);
  digitalWrite(redLed, LOW);
  delay(5000);
  digitalWrite(greenLed, LOW);
}

void setup() {
  // put your setup code here, to run once:
  pinMode(greenLed, OUTPUT);
  pinMode(redLed, OUTPUT);
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  buttonState1 = digitalRead(buttonPin);
  Serial.println(buttonState1);
  if (buttonState1 == HIGH) {
    if (!buttonPressed) {
      digitalWrite(statusLedPin, LOW);
      buttonPressed = true;
      onButtonPressed();
    }
  } else {
    digitalWrite(statusLedPin, HIGH);
  }
  delay(100);
} 
