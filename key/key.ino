#include <EEPROM.h>
#include <Adafruit_NeoPixel.h>

uint32_t myTimer1, myTimer2, myTimer3, myTimer4;
#define BTN_PIN_1 12
#define BTN_PIN_2 11
#define BTN_PIN_3 10
#define BTN_PIN_4 9
#define BTN_PIN_5 8
#define BTN_PIN_6 7
#define BTN_PIN_7 6
#define BTN_PIN_8 5
#define LED_PIN 2 // номер порта к которому подключен модуль
#define count_led 8 // количество светодиодов 
String data = "";

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(count_led, LED_PIN, NEO_GRB + NEO_KHZ800); //first number change does distance between colors


void setup() {
  Serial.begin(9600);
  pinMode(BTN_PIN_1, INPUT_PULLUP);
  pinMode(BTN_PIN_2, INPUT_PULLUP);
  pinMode(BTN_PIN_3, INPUT_PULLUP);
  pinMode(BTN_PIN_4, INPUT_PULLUP);
  pinMode(BTN_PIN_5, INPUT_PULLUP);
  pinMode(BTN_PIN_6, INPUT_PULLUP);
  pinMode(BTN_PIN_7, INPUT_PULLUP);
  pinMode(BTN_PIN_8, INPUT_PULLUP);
  pixels.begin();
  pixels.show();
}

void loop() {
  if (millis() - myTimer1 >= 100) {   // таймер на 500 мс (2 раза в сек)
    myTimer1 = millis();
    if (digitalRead(BTN_PIN_1) == LOW) {
      Serial.println("BTN_PIN_1");
      myTimer3 = millis();
      led_on(1);
    }
    if (digitalRead(BTN_PIN_2) == LOW) {
      Serial.println("BTN_PIN_2");
      myTimer3 = millis();
      led_on(2);
    }
    if (digitalRead(BTN_PIN_3) == LOW) {
      Serial.println("BTN_PIN_3");
      myTimer3 = millis();
      led_on(3);
    }
    if (digitalRead(BTN_PIN_4) == LOW) {
      Serial.println("BTN_PIN_4");
      myTimer3 = millis();
      led_on(4);
    }
    if (digitalRead(BTN_PIN_5) == LOW) {
      Serial.println("BTN_PIN_5");
      myTimer3 = millis();
      led_on(5);
    }
    if (digitalRead(BTN_PIN_6) == LOW) {
      Serial.println("BTN_PIN_6");
      myTimer3 = millis();
      led_on(6);
    }
    if (digitalRead(BTN_PIN_7) == LOW) {
      Serial.println("BTN_PIN_7");
      myTimer3 = millis();
      led_on(7);
    }
    if (digitalRead(BTN_PIN_8) == LOW) {
      Serial.println("BTN_PIN_8");
      myTimer3 = millis();
      led_on(8);
    }
    else {
      led_off();
    }
  }
  if (millis() - myTimer2 >= 10) {   // таймер на 500 мс (2 раза в сек)
    myTimer2 = millis();
    if (Serial.available()) {
      data = Serial.readStringUntil('$');
      int len_data = data.length();
      if (len_data == 5) {
        if (data == "led_1") {
          led_on(1);
          myTimer3 = millis();
        }
        if (data == "led_2") {
          led_on(2);
          myTimer3 = millis();
        }
        if (data == "led_3") {
          led_on(3);
          myTimer3 = millis();
        }
        if (data == "led_4") {
          led_on(4);
          myTimer3 = millis();
        }
        if (data == "led_5") {
          led_on(5);
          myTimer3 = millis();
        }
        if (data == "led_6") {
          led_on(6);
          myTimer3 = millis();
        }
        if (data == "led_7") {
          led_on(7);
          myTimer3 = millis();
        }
        if (data  == "led_8") {
          led_on(8);
          myTimer3 = millis();
        }
      }
      else if (len_data == 16) {
        int led_pins = data.substring(3).toInt() - 1;
        EEPROM.write(led_pins * 12, data.substring(5, 8).toInt());
        EEPROM.write(led_pins * 12 + 3, data.substring(9, 12).toInt());
        EEPROM.write(led_pins * 12 + 6, data.substring(13, 16).toInt());
        int r = EEPROM.read(led_pins * 12);
        int g = EEPROM.read(led_pins * 12 + 3);
        int b = EEPROM.read(led_pins * 12 + 6);
        pixels.setPixelColor(led_pins, pixels.Color(r, g, b));
        pixels.show();
        myTimer3 = millis();
      }
    }
  }
}

void led_on(int pins) {
  pins -= 1;
  int r = EEPROM.read(pins * 12);
  int g = EEPROM.read(pins * 12 + 3);
  int b = EEPROM.read(pins * 12 + 6);
  pixels.setPixelColor(pins, pixels.Color(r, g, b));
  pixels.show();
}


void led_off() {
  if (millis() - myTimer3 > 500) {   // таймер на 500 мс (2 раза в сек)
    for (int i = 0; i <= count_led; i++) {
      pixels.setPixelColor(i, 0, 0, 0);
      pixels.show();
    }
  }
}
