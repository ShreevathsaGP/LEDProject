#include "globals.h"
#include "writing.h"

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
    letter_width = 5;
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

    for (int i = 2; i < (no_rows - 2); i++) {
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
    for (int i = 2; i < (no_rows - 2); i++) {
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

    // J
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
        sample_string += ' ';
    }
    sample_string = sample_string.substr(0, sample_string.size() - 1);
    add_space(NO_SPACES, sample_string);
    letter_map['j'] = sample_string;

    // K
    sample_string.clear();
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int _ = 0; _ < (letter_width - 3); _++) {
        sample_string += to_string(no_rows / 2);
        sample_string += ' ';
    }

    sample_string += to_string((no_rows / 2) - 1);
    sample_string += to_string((no_rows / 2) + 1);
    sample_string += ' ';

    for (int i = 1; i < (no_rows - 1); i++) {
        if (i != (no_rows /2) && i != (no_rows /2) + 1 && i != (no_rows/2) - 1) {
            sample_string += to_string(i);
        }
    }
    add_space(NO_SPACES, sample_string);
    letter_map['k'] = sample_string;

    // L
    sample_string.clear();
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int _ = 0; _ < (letter_width - 1); _++) {
        sample_string += to_string(no_rows - 2);
        sample_string += ' ';
    }
    sample_string = sample_string.substr(0, sample_string.size() - 1);
    add_space(NO_SPACES, sample_string);
    letter_map['l'] = sample_string;

    // M
    sample_string.clear(); 
    temp = 2;
    no_flat = 0;
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    middle = (letter_width - 2);
    if (middle % 2 == 0) {
        for (int i = 0; i < (middle / 2); i++) {
            sample_string += to_string(temp);   
            sample_string += ' ';
            if (temp < (no_rows / 2)) {temp += 1;} else {no_flat += 1;}
        }
        for (int i = 0; i < no_flat; i++) {
            sample_string += to_string(no_rows / 2);
            sample_string += ' ';
        }
        temp -= 1;
        for (int i = 0; i < (middle / 2) - no_flat; i++) {
            sample_string += to_string(temp);
            sample_string += ' ';
            if (temp > 1) {temp -= 1;}
        }
    } else {
        for (int i = 0; i < (middle / 2); i++) {
            sample_string += to_string(temp);   
            sample_string += ' ';
            if (temp < (no_rows / 2)) {temp += 1;} else {no_flat += 1;}
        }
        sample_string += to_string(temp);
        temp -= 1;
        sample_string += ' ';
        for (int i = 0; i < no_flat; i++) {
            sample_string += to_string(no_rows / 2);
            sample_string += ' ';
        }
        for (int i = 0; i < (middle / 2) - no_flat; i++) {
            sample_string += to_string(temp);
            sample_string += ' ';
            if (temp > 1) {temp -= 1;}
        }
    }
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    add_space(NO_SPACES, sample_string);
    letter_map['m'] = sample_string;

    // N
    sample_string.clear();
    temp = 2;
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int i = 0; i < (letter_width - 2); i++) {
        sample_string += to_string(temp);
        sample_string += ' ';
        if (temp < (no_rows - 2)) {temp += 1;}
    }
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    add_space(NO_SPACES, sample_string);
    letter_map['n'] = sample_string;
    
    // O
    sample_string.clear();
    for (int i = 2; i < (no_rows - 2); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int i = 0; i < letter_width - 2; i++) {
        sample_string += '1';
        sample_string += to_string(no_rows - 2);
        sample_string += ' ';
    }
    for (int i = 2; i < (no_rows - 2); i++) {
        sample_string += to_string(i);
    }
    add_space(NO_SPACES, sample_string);
    letter_map['o'] = sample_string;

    // P
    sample_string.clear();
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int i = 0; i < letter_width - 2; i++) {
        sample_string += '1';
        sample_string += to_string(no_rows / 2);
        sample_string += ' ';
    }
    for (int i = 1; i < (no_rows / 2) + 1; i++) {
        sample_string += to_string(i);
    }
    add_space(NO_SPACES, sample_string);
    letter_map['p'] = sample_string;

    // Q
    sample_string.clear();
    for (int i = 2; i < (no_rows - 2); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int i = 0; i < (letter_width - 4); i++) {
        sample_string += '1';
        sample_string += to_string(no_rows - 2);
        sample_string += ' ';
    }
    sample_string += '1';
    sample_string += to_string(no_rows - 4);
    sample_string += to_string(no_rows - 2);
    sample_string += ' ';
    sample_string += '1';
    sample_string += to_string(no_rows - 3);
    sample_string += ' ';
    for (int i = 2; i < (no_rows - 3); i++) {
        sample_string += to_string(i); 
    }
    sample_string += to_string(no_rows - 2);
    add_space(NO_SPACES, sample_string);
    letter_map['q'] = sample_string;

    // R
    sample_string.clear();
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int _ = 0; _ < (letter_width - 2); _++) {
        sample_string += '1';
        sample_string += to_string(no_rows / 2);
        sample_string += ' ';
    }
    for (int i = 1; i < (no_rows - 1); i++) {
        if (i != (no_rows /2)) {
            sample_string += to_string(i);
        }
    }
    add_space(NO_SPACES, sample_string);
    letter_map['r'] = sample_string;
    
    // S
    sample_string.clear();
    for (int i = 2; i < (no_rows / 2); i++) {
        sample_string += to_string(i);
    }
    sample_string += to_string(no_rows - 2);
    sample_string += ' ';
    for (int i = 0; i < (letter_width - 2); i++) {
        sample_string += '1';
        sample_string += to_string(no_rows / 2);
        sample_string += to_string(no_rows - 2);
        sample_string += ' ';
    }
    for (int i = no_rows - 3; i > (no_rows / 2); i--) {
        sample_string += to_string(i);
    }
    sample_string += '1';
    add_space(NO_SPACES, sample_string);
    letter_map['s'] = sample_string;

    // T
    sample_string.clear();
    for (int i = 0; i < (letter_width / 2); i++) {
        sample_string += '1';
        sample_string += ' ';
    }
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int i = 0; i < ((letter_width - 1) - (letter_width / 2)); i++) {
        sample_string += '1';
        sample_string += ' ';
    }
    add_space(NO_SPACES - 1, sample_string);
    letter_map['t'] = sample_string;

    // U
    sample_string.clear();
    for (int i = 1; i < (no_rows - 2); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    for (int i = 0; i < (letter_width - 2); i++) {
        sample_string += to_string(no_rows - 2);
        sample_string += ' ';
    }
    for (int i = 1; i < (no_rows - 2); i++) {
        sample_string += to_string(i);
    }
    add_space(NO_SPACES, sample_string);
    letter_map['u'] = sample_string;

    // V
    sample_string.clear();
    for (int i = 1; i < (no_rows - 3); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    sample_string += to_string(no_rows - 3);
    sample_string += ' ';
    for (int i = 0; i < (letter_width - 4); i++) {
        sample_string += to_string(no_rows - 2);
        sample_string += ' ';
    }
    sample_string += to_string(no_rows - 3);
    sample_string += ' ';
    for (int i = 1; i < (no_rows - 3); i++) {
        sample_string += to_string(i);
    }

    add_space(NO_SPACES, sample_string);
    letter_map['v'] = sample_string;
    
    // W
    sample_string.clear(); 
    temp = (no_rows - 3);
    no_flat = 0;
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    sample_string += ' ';
    middle = (letter_width - 2);
    if (middle % 2 == 0) {
        for (int i = 0; i < (middle / 2); i++) {
            sample_string += to_string(temp);
            sample_string += ' ';
            if (temp > (no_rows / 2)) {temp -= 1;} else {no_flat += 1;}
        }
        for (int i = 0; i < no_flat; i++) {
            sample_string += to_string(no_rows / 2);
            sample_string += ' ';
        }
        temp += 1;
        for (int i = 0; i < (middle / 2) - no_flat; i++) {
            sample_string += to_string(temp);
            sample_string += ' ';
            if (temp < (no_rows - 2)) {temp += 1;}
        }
    } else {
        for (int i = 0; i < (middle / 2); i++) {
            sample_string += to_string(temp);
            sample_string += ' ';
            if (temp > (no_rows / 2)) {temp -= 1;} else {no_flat += 1;}
        }
        sample_string += to_string(temp);
        temp += 1;
        sample_string += ' ';
        for (int i = 0; i < (middle / 2) - no_flat; i++) {
            sample_string += to_string(temp);
            sample_string += ' ';
            if (temp < (no_rows - 2)) {temp += 1;} 
        }
    }
    for (int i = 1; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    add_space(NO_SPACES, sample_string);
    letter_map['w'] = sample_string;
    
    // X
    sample_string.clear();
    top = no_rows / 4;
    bottom = (top + letter_width) - 1;

    for (int i = 0; i < letter_width; i++) {
        if (i == 0) {
            for (int i = 1; i < top; i++) {
                sample_string += to_string(i);
            }
            for (int i = no_rows - 2; i > bottom; i--) {
                sample_string += to_string(i);
            }
        } else if (i == (letter_width - 1)) {
            for (int i = 1; i < bottom; i++) {
                sample_string += to_string(i);
            }
            for (int i = no_rows - 2; i > top; i--) {
                sample_string += to_string(i);
            }
        }
        sample_string += to_string(top);
        sample_string += to_string(bottom);
        sample_string += ' ';
        top += 1;
        bottom -= 1;
    }
    add_space(NO_SPACES - 1, sample_string);
    letter_map['x'] = sample_string;
    
    // Y
    sample_string.clear(); 
    temp = 1;
    no_flat = 0;
    middle = letter_width;
    if (letter_width % 2 == 0) {middle += 1;}
    for (int i = 0; i < (middle / 2); i++) {
        sample_string += to_string(temp);   
        sample_string += ' ';
        if (temp < (no_rows / 2)) {temp += 1;} else {no_flat += 1;}
    }
    for (int i = temp; i < (no_rows - 1); i++) {
        sample_string += to_string(i);
    }
    temp -= 1;
    sample_string += ' ';
    for (int i = 0; i < no_flat; i++) {
        sample_string += to_string(no_rows / 2);
        sample_string += ' ';
    }
    for (int i = 0; i < (middle / 2) - no_flat; i++) {
        sample_string += to_string(temp);
        sample_string += ' ';
        if (temp > 1) {temp -= 1;}
    }
    add_space(NO_SPACES - 1, sample_string);
    letter_map['y'] = sample_string;

    // Z
    letter_map['z'] = letter_map['s'];

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
        current_state.instructions.push(letter_map[(char)tolower(in_string[i])]);
    }
}
