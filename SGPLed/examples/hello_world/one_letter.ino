#include <FastLED.h>

#define LED_PIN 7
#define LED_BRAND WS2812B

// CONSTANTS
const int no_rows = 8;
const int no_columns = 28;

// ENUMS
enum Orientation {
  Left, Right
};
enum Colours {
    Black, Red
};

// GLOBALS
CRGB strip[(no_columns * no_rows)];
int fast_index = 0;
int local[no_rows][no_columns];
Orientation orientation;
Colour temp;

// shift board
void shift(const Colours matrix[no_rows][no_columns]) {
  for (int i = 0; i < no_rows; i++) {
    for (int j = 1; j < no_columns; j++) {
      temp = matrix[i][j];
      matrix[i][j - 1] = temp;
    }
  }

  for (int j = 1; j < no_rows; j++) {
    matrix[j][no_columns - 1] = Black;
  }
}

// draw the matrix [in actual LED]
void draw() {
  orientation = Left;
  for (int row = 0; row < no_rows; row++) {
    if (orientation == Left) {
      // left <-- right
      for (int col = no_columns - 1; col > -1; col--) {
        if (local[row][col] == Colours::Red) {
          strip[fast_index] = CRGB::Red;
        }
        fast_index += 1;
        orientation = Right;
      }
    } else {
      // left --> right
      for (int col = 0; col < no_columns; col++) {
        if (local[row][col] == Colours::Red) {
          strip[fast_index] = CRGB::Red;
        }
        fast_index += 1;
        orientation = Left;
      }
    }
  }
  FastLED.show();
  fast_index = 0;
}

void setup() {
    FastLED.addLeds<LED_BRAND, LED_PIN, GRB>(strip, (no_columns * no_rows));
    FastLED.setBrightness(50);

    for (int i = 2; i < no_rows - 2; i++) {
        local[i][no_columns - 2] = Colours::Red;
    }

    for (int i = no_columns - 6; i < no_columns - 2; i++) {
        local[1][i] = Colours::Red;
        local[no_rows - 2][i] = Colours::Red;
    }

    for (int i = 1; i < no_rows - 1; i++) {
        local[i][no_columns - 7] = Colours::Red;
    }
}

void loop() {
    draw();
    shift(local);
}
