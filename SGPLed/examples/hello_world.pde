#include <SGPLed.h>
#include <FastLED.h>

#define DELAY 30
#define LED_PIN 7
#define LED_BRAND WS2812B

//------ GLOBALS -----------------------------------------------------------------------------------------------------

CRGB strip[no_columns * no_rows]

unsigned long previous_time = 0;
unsigned long current_time = 0;
State current_state = State();
Writer writer = Writer(current_state);
Colours temp;
int fast_index = 0;
enum Orientation {
  Left, Right;
}
Orientation orientation ;

//------ GLOBALS -----------------------------------------------------------------------------------------------------

//------ BOARD -------------------------------------------------------------------------------------------------------

void shift(Colours matrix[no_rows][no_columns]) {
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

//------ BOARD -------------------------------------------------------------------------------------------------------

//------ ARDUINO -----------------------------------------------------------------------------------------------------

// show matrix [in serial output]
void show(Colours matrix[no_rows][no_columns]) {
  for (int i = 0; i < no_rows; i++) {
    Serial.print("[ ")
    for (int j = 0; j < no_columns; j++) {
      Serial.print(matrix[i][j]);
      Serial.print(" ");
    }
    Serial.print("]");
    Serial.print("\n");
  }
}

// render the matrix [in actual LED]
void render() {
  orientation = Left;
  for (int row = 0; row < no_rows; row++) {
    if (orientation == Left) {
      // left <-- right
      for (int col = no_columns - 1; col > -1; col--) {
        if (current_state.board[row][col] == Colours::Red) {
          strip[fast_index] = CRGB::Red;
        }
        fast_index += 1;
        orientation = Right;
      }
    } else {
      // left --> right
      for (int col = 0; col < no_columns; col++) {
        if (current_state.board[row][col] == Colours::Red) {
          strip[fast_index] = CRGB::Red;
        }
        fast_index += 1;
        orientation = Left;
      }
    }
  }
  FastLed.show();
  shift(matrix);

  fast_index = 0;
}

//------ ARDUINO -----------------------------------------------------------------------------------------------------

void setup() {
  // ARDUINO
  Serial.begin(9600);
  FastLED.addLeds<LED_BRAND, LED_PIN, GRB>(strip, (no_columns * no_rows));
  FastLED.setBrightness(50);
  // ARDUINO

  current_state.instruction_index = 0;
  current_state.current_instruction.clear();
  writer.write("HELLO WORLD");
}

void loop() {
  current_time = millis();
  if (current_time - previous_time > DELAY) {
    previous_time = current_time; 
    // check for instruction update 
    if (current_state.instruction_index > (int)current_state.current_instruction.length() - 1) {
      if (current_state.instructions.empty()) {
        return;
      }
      current_state.instruction_index = 0;
      current_state.current_instruction = current_state.instructions.front();
      current_state.instructions.pop(); 
    }

    // execute the instructions
    for (int i = current_state.instruction_index; i < current_state.current_instruction.length(); i++) {
      current_state.instruction_index += 1;
      if (current_state.current_instruction[i] == ' ') {break;}
      current_state.board[(current_state.current_instruction[i]) - '0'][no_columns - 1] = Colours::Red;
    }

    render(current_state);
  }
}
