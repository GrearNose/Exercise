class Solution {
public:
    bool isNumeric(char* string)
    {
        /* state  definition:
            0: initial state
            1: interal part
            2: radix point '.'
            3: decimal part
            4: 'E/e'
            5: exponent part
            6: final state
        */
        int s = 0;
        for(int i = 0; i <= strlen(string); ++i)
        {
            char c = string[i];
            switch(s)
            {
                case 0:
                    if ('+' == c or '-' == c or ('0' <= c and c <= '9'))
                        s = 1;
                    else
                        return false;
                    break;
                case 1:
                    if ('0' <= c and c <= '9')
                        s = 1;
                    else if ('.' == c)
                        s = 2;
                    else if ('e' == c or 'E' == c)
                        s = 4;
                    else if ('\0' == c)
                        return true;
                    else
                        return false;
                    break;
                case 2:
                    if ('0' <= c and c <= '9')
                        s = 3;
                    else
                        return false;
                    break;
                case 3:
                    if ('0' <= c and c <= '9')
                        s = 3;
                    else if ('e' == c or 'E' == c)
                        s = 4;
                    else if ('\0' == c)
                        return true;
                    else
                        return false;
                    break;
                case 4:
                    if ('+' == c or '-' == c or ('0' <= c and c <= '9'))
                        s = 5;
                    else
                        return false;
                    break;
                case 5:
                    if ('0' <= c and c <= '9')
                        s = 5;
                    else if ('\0' == c)
                        return true;
                    else
                        return false;
            }
        }
        return false;
    }

};