#ifndef CharMap_H
#define CharMap_H

#define NO_ASCII 128
#include <string.h>

class CharMap {
    public:
        // overloading [] returns string (reference)
        String& operator [](char in_char) {
            return array[(int)in_char];
        }
        
    private:
        String array[NO_ASCII];

};

#endif // CharMap_H
