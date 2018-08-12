#include <iostream>
#include <string>

using namespace std;

/*
Given a string with length of 4*n,
print it as a square such that the
upper base of the square is the first
n chars of the string, and the rest 3
sides in clock-wise are the 2nd, 3rd and
4th n chars of the string.
*/

int main(int argc, char* argv[])
{
    // input strting
    std::string str;
    cin >> str;

    // verify the length of this string
    int len = str.length();

    if((len % 4 != 0)) {
        return -1;
    }
    int k = len / 4;

    // algorithm
    std::string result = "";

    // upper line 
    for(int i = 0; i < k+1; ++i)
        result += str[i];
    // middle line
    for(int i = 0; i < k-1; ++i) {
        result += str[4*k - 1 - i];
        for(int j = 1; j < k; ++j) {
            result += ' ';
        }
        result += str[k + 1 + i];
    }
    // lower line
    for(int i = 0; i < k+1; ++i) {
        result += str[3*k - i];
    }

    // print
    for(int i = 0; i < k+1; ++i) {
        for(int j = 0; j < k+1; ++j) {
            cout << result[i*(k+1) + j];
        }
        cout << endl;
    }
    return 0;
}