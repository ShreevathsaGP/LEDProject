#ifndef GLOBALS_H
#define GLOBALS_H

#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <unordered_map>

// matrix specs
const int no_rows = 8;
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
    std::queue<std::string> instructions;
    std::string current_instruction;
    int instruction_index;
};

#endif // GLOBALS_H
