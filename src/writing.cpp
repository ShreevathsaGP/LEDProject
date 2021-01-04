#include "globals.h"
#include "writing.h"
#define NO_SPACES 2

using namespace std;

// constructor (initializer list for &current_state)
Writer::Writer(State &in_state): current_state(in_state) {
    init_mappings(); 
}

void Writer::add_space(int no, string &in_string) {
    for (int _ = 0; _ < no; _++) {
        in_string += ' ';
    }
}

// initialize letter-mappings
bool Writer::init_mappings() {
    // board landmarks
    letter_width = no_columns / 5;
    if (letter_width <= 3) {return false;} // board not wide enough
    if (no_rows <= 4) {return false;} // board not long enough
   
    // [ ] (Space)
    sample_string.clear();
    sample_string += ' ';
    sample_string += ' ';
    sample_string += ' ';
    letter_map[' '] = sample_string;

    // A
    sample_string.clear();
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int i = 0; i < (letter_width - 2); i++) {
        sample_string += '1';
        sample_string += to_string((no_rows / 2));
        sample_string += ' ';
    }
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    add_space(NO_SPACES, sample_string);
    letter_map['a'] = sample_string;

    // B
    sample_string.clear();
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';

    for (int _ = 0; _ < (letter_width - 2); _++) {
        sample_string += '1';
        sample_string += to_string(no_rows / 2);
        sample_string += to_string(no_rows - 2);
        sample_string += ' ';
    }

    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    add_space(NO_SPACES, sample_string);
    letter_map['b'] = sample_string;

    // C
    sample_string.clear();
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int i = 0; i < (letter_width - 1); i++) {
        sample_string += '1';
        sample_string += to_string(no_rows - 2);
        sample_string += ' ';
    }
    sample_string = sample_string.substr(0, sample_string.size() - 1);
    add_space(NO_SPACES, sample_string);
    letter_map['c'] = sample_string;

    // D
    sample_string.clear(); 
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int i = 0; i < (letter_width - 2); i++) {
        sample_string += '1';
        sample_string += to_string(no_rows - 2);
        sample_string += ' ';
    }
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    add_space(NO_SPACES, sample_string);
    letter_map['d'] = sample_string;

    // E
    sample_string.clear();
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int i = 0; i < (letter_width - 1); i++) {
        sample_string += '1';
        sample_string += to_string(no_rows / 2);
        sample_string += to_string(no_rows - 2);
        sample_string += ' ';
    }
    sample_string = sample_string.substr(0, sample_string.size() - 1);
    add_space(NO_SPACES, sample_string);
    letter_map['e'] = sample_string;

    // F
    sample_string.clear();
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int i = 0; i < (letter_width - 1); i++) {
        sample_string += '1';
        sample_string += to_string(no_rows / 2);
        sample_string += ' ';
    }
    sample_string = sample_string.substr(0, sample_string.size() - 1);
    add_space(NO_SPACES, sample_string);
    letter_map['f'] = sample_string;
    
    // G
    sample_string.clear();
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int i = 0; i < (letter_width / 2) / 2; i++) {
        sample_string += '1';
        sample_string += to_string(no_rows - 2);
        sample_string += ' ';
    }
    for (int i = 0; i < (letter_width - ((letter_width / 2) / 2) - 2); i++) {
        sample_string += '1';
        sample_string += to_string(no_rows / 2);
        sample_string += to_string(no_rows - 2);
        sample_string += ' ';
    }
    sample_string += '1';
    for (int i = (no_rows / 2); i < no_rows - 1; i++) {
        sample_string += to_string(i);
    } 
    add_space(NO_SPACES, sample_string);
    letter_map['g'] = sample_string;
      
    // H
    sample_string.clear();
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int i = 0; i < (letter_width - 2); i++) {
        sample_string += to_string(no_rows / 2);
        sample_string += ' ';
    }
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    add_space(NO_SPACES, sample_string);
    letter_map['h'] = sample_string;

    // I
    sample_string.clear();
    for (int i = 0; i < (letter_width - 1) / 2; i++) {
        sample_string += '1';
        sample_string += to_string(no_rows - 2);
        sample_string += ' ';
    }
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int i = 0; i < (letter_width - ((letter_width - 1) / 2)) - 1; i++) {
        sample_string += '1';
        sample_string += to_string(no_rows - 2);
        sample_string += ' ';
    }
    sample_string = sample_string.substr(0, sample_string.size() - 1);
    add_space(NO_SPACES, sample_string);
    letter_map['i'] = sample_string;

    return true;
}

// write animation
void Writer::write(string in_string) {
    // reset board
    current_state.current_process = Writing;
    for (int i = 0; i < no_rows; i++) {
        for (int j = 0; j < no_columns; j++) {
            current_state.board[i][j] = Black;
        }
    }

    // letter-wise instructions
    for (int i = 0; i < in_string.length(); i++) {
        current_state.instructions.push(letter_map[in_string[i]]);
    }
}
