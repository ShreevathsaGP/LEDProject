#ifndef SGPLed_H
#define SGPLed_H

//------ INCLUDES ----------------------------------------------------------------------------------------------------

#include <Queue.h>
#include <string.h>
#include <CharMap.h>

#include <Arduino.h>

//------ INCLUDES ----------------------------------------------------------------------------------------------------

//------ GLOBALS -----------------------------------------------------------------------------------------------------

// matrix specs 
const int no_rows = 8; // SHOULD NOT BE MORE THAN 10 [Writing Lib Will Fail]
const int no_columns = 28;

// colours
enum Colours {
    Black, Red, Green, Blue, Yellow, Orange, Purple, Pink
};

// processes
enum Processes {
    Writing, Tetris, Pong, Watch, Nothing
};

// led-matrix state
struct State {
    Colours board[no_rows][no_columns];
    Processes current_process;
    Queue<String> instructions;
    String current_instruction;
    int instruction_index;
};

//------ GLOBALS -----------------------------------------------------------------------------------------------------

//------ WRITING -----------------------------------------------------------------------------------------------------

#define NO_SPACES 2
class Writer {
    public:
        // constructor
        Writer(State &in_state);

        // write animation
        void write(String in_string);

        // space (between letters)
        void add_space(int no, String &in_string);


    private:
        // initialize letter-mappings
        bool init_mappings();
        
        // variables
        State &current_state;
        String sample_string;
        int letter_width;
        int temp;
        int middle;
        int no_flat;

        int top;
        int bottom;
        int constraint;
        
        // letter-mappings (column wise operations)
        CharMap letter_map;
};

//------ WRITING -----------------------------------------------------------------------------------------------------

#endif // SGPLed_H
