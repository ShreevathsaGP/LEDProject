#ifndef WRITING_H
#define WRITING_H

#include "globals.h"

class Writer {
    public:
        // constructor
        Writer(State &in_state);

        // write animation
        void write(std::string in_string);

        // space (between letters)
        void add_space(int no, std::string &in_string);


    private:
        // initialize letter-mappings
        bool init_mappings();
        
        // variables
        State &current_state;
        std::string sample_string;
        int letter_width;
        int temp;
        int middle;
        int no_flat;

        int top;
        int bottom;
        int constraint;
        
        // letter-mappings (column wise operations)
        std::unordered_map<char, std::string> letter_map;
        

};

#endif // WRITING_H
