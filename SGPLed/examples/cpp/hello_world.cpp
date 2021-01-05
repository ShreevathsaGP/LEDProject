#include <SGPLed.h>

using namespace std;

//------ GLOBALS -----------------------------------------------------------------------------------------------------
State current_state = State();
Writer writer = Writer(current_state);
Colours temp;
bool running = true;
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

//------ CPP ---------------------------------------------------------------------------------------------------------

void show(const Colours matrix[no_rows][no_columns]) {
    for (int i = 0; i < no_rows; i++) {
        cout << "[ ";
        for (int j = 0; j < no_columns; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << "]" << endl;
    }
}
void render(State &current_state) {
    show(current_state.board);
    cout << endl;
    shift(current_state.board);
}

//------ CPP ---------------------------------------------------------------------------------------------------------

void setup() {
    current_state.instruction_index = 0;
    current_state.current_instruction.clear();
    writer.write("hello world");
}

void loop() {
    // check for instruction update
    if (current_state.instruction_index > (int)current_state.current_instruction.length() - 1) {
        if (current_state.instructions.empty()) {
            running = false; return;
        }
        current_state.instruction_index = 0;
        current_state.current_instruction = current_state.instructions.front();
        current_state.instructions.pop(); 
    }
    
    // execute the instructions
    for (int i = current_state.instruction_index; i < current_state.current_instruction.length(); i++) {
        current_state.instruction_index += 1;
        if (current_state.current_instruction[i] == ' ') {break;}
        /* cout << current_state.current_instruction[i] - '0'; */
        current_state.board[(current_state.current_instruction[i]) - '0'][no_columns - 1] = Red;
    }

    render(current_state);
}

int main() {
    setup();
    while (running) {
        loop();
    }

    return 0;
}

