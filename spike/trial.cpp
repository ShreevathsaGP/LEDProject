#include <iostream>
#include <string>

using namespace std;

const int no_rows = 8;
const int no_columns = 28;

enum Orientation {
    Left, Right
};
Orientation orientation; 
int fast_index;

int main() {
    orientation = Left; // starting orientation
    fast_index = 0;
    for (int row = 0; row < no_rows; row ++) {
        if (orientation == Left) {
            for (int col = no_columns - 1; col > -1; col --) {
                cout << "[" << row << "]" << "[" << col << "]";
                fast_index += 1;
            }
            cout << endl;
            orientation = Right;
        } else {
            for (int col = 0; col < no_columns; col ++) {
                cout << "[" << row << "]" << "[" << col << "]";
                fast_index += 1;
            }
            cout << endl;
            orientation = Left;
        }
    }
}
