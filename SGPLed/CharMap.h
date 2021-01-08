#ifndef CharMap_H
#define CharMap_H

#define NO_ASCII 75
#include <string.h>
#include <Arduino.h>

class CharMap {
    public:
        // overloading [] returns string (reference)
        String& operator [](char in_char) {
            return array[((int)in_char - 48)];
        }
        
    private:
        String array[NO_ASCII];

};

#endif // CharMap_H
