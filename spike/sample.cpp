#include <FastLED.h>

// fill this in
#define NO_LEDS 224
#define LED_PIN 7
#define LED_BRAND WS2812B
#define DELAY 200

// declarations
CRGB strip[NO_LEDS];
unsigned long previous_time = 0;
int current_index = 0;
bool state = false; // false => turning on, true = turning off

// setup strip
void setup() {
    Serial.begin(9600);
    FastLED.addLeds<LED_BRAND, LED_PIN, GRB>(strip, NO_LEDS);
    FastLED.setBrightness(50);
}

// timed animation
void loop() {
    unsigned long current_time = millis();
    if (current_time - previous_time > DELAY) {
        Serial.print("timing works");
        previous_time = current_time;
        if (!state) {
            Serial.print("on");
            state = true;
            strip[current_index] = CRGB::Red;
            FastLed.show();

        } else {
            Serial.print("off");
            state = false;
            // increment index
            strip[current_index] = CRGB::Black;
            current_index += 1;

            // reset the index
            if (current_index >= NO_LEDS) {
                current_index -= NO_LEDS;
            }
        }
    }
}

// old code
/* // animate strip */
/* void loop() { */
/*     // forward pass */
/*     for (int i = 0; i < NO_LEDS; i++) { */
/*         strip[i] = CRGB::Red; */
/*         FastLED.show(); */
/*         delay(DELAY); */
/*         strip[i] = CRGB::Black; */
/*     } */

/*     // backward pass */
/*     for (int i = NO_LEDS - 1; i >= 0; i--) { */
/*         strip[i] = CRGB::Red; */
/*         FastLED.show(); */
/*         delay(DELAY); */
/*         strip[i] = CRGB::Black; */
/*     } */
/* } */
