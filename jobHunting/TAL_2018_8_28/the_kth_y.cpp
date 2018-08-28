#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm> 
using namespace std;

int main(int argc, char const *argv[])
{
    int t, x, y, k;
    scanf("%d",&t);
    for (int i = 0; i < t; ++i)
    {
        scanf("%d %d",&x,&k);
        int cnt = 0;
        y = 1;
        while (cnt < k)
        {
            while ((x+y) != (x|y))
                y += 1;
            cnt += 1;
            if (cnt == k)
                break;
            y += 1;
            // print(cnt,':', y)
        }
        printf("%d\n",y);
    }
    return 0;
}