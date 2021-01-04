#include <iostream>
#include <string>

using namespace std;

int main() {
    string something = "Something";
    cout << something.length() << endl;
    something += ' ';

    cout << something.length() << endl;
}
