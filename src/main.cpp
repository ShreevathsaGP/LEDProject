#include <iostream>
#include <queue>
#include <unordered_map>
/* #include "FastLED.h" */

#define ROWS 5
#define COLUMNS 10

using namespace std;

int current_state[ROWS][COLUMNS] = {0};

void show(int matrix[ROWS][COLUMNS]) {

    for (int i = 0; i < ROWS; i++) {
        cout << "[ ";
        for (int j = 0; j < COLUMNS; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << "]" << endl;
    }
}

int main() {
    show(current_state);
}
