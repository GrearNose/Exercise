#include <stdlib.h>
#include <iostream>
using namespace std;

class Solution {
public:
    bool match(char* str, char* pattern)
    {
        if (NULL == str or NULL == pattern)
            return false;
        if( str[0] == pattern[0] )
        {
            if( '\0' == pattern[0] )
                return true;
            if ('*' == pattern[1])  // match no char, one or more.
                return match(str,pattern+2) or match(str+1,pattern+2) or match(str+1,pattern);
            return match(str+1,pattern+1);
        }
        else
        {
            if ('\0' == str[0])
                return '*' == pattern[1]? match(str,pattern+2):false;
            if ('\0' == pattern[0])
                return false;
            if('*' == pattern[1])
            {
                if ('.' == pattern[0]) // match no char, one or more.
                    return match(str,pattern+2) or match(str+1,pattern+2) or match(str+1,pattern); 
                return match(str,pattern+2); // match no char.
            }
            if('.' == pattern[0])
                return match(str+1,pattern+1); // '.' match any char
            return false;
        }
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    char str[] = {"abc"};
    char p1[] = ".*bd";
    char p2[] = ".*b";
    char p3[] = ".*c";
    cout << s.match(str,p1) << endl;
    cout << s.match(str,p2) << endl;
    cout << s.match(str,p3) << endl;
    return 0;
}