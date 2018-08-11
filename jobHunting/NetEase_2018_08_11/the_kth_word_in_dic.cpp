#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;


template <typename T>
void myReverse(T*from,T*to) // an simple implementation of reverse.
{
    // cout << (to-from)/sizeof(T) << endl;
    while(from<to) {
        T tmp = *from;
        *(from++) = *to;
        *(to--) = tmp;
    }
}

bool the_kth_word(char*perm,int num,int k)
{
    for (int cnt = 1; cnt < k; ++cnt)
    {
        int i, j; // find out the last ix that starts a ascending order.
        for (i = num-2; (i >= 0) && perm[i]>=perm[i+1]; --i);
        if (i < 0)
            return false;
        // to find the smallest num perm[j] satisfying perm[j] > perm[i]:
        // As perm[i:] is in descending order, just to find the first
        // one from the rear.
        j = i + 1;
        // printf("i,j,str:%d,%d,%s\n", i,j,perm);
        swap(perm[i],perm[j]);
        // myReverse(perm+i+1,perm+num-1); // for the one defined in this file.
        if(i+2 < num)
            reverse(perm+i+2,perm+num); // for the one from STL.
        // printf("str:%s\n", perm)
    }
    return true;
}


int main(int argc, char const *argv[])
{
    int n, m, k;
    while (cin >> n >> m >> k)
    {
        char *str = new char[n+m];
        memset(str,'a',n);
        memset(str+n,'z',m);
        // printf("n,m,k,str: %d,%d %d,%s\n",n,m,k,str);
        if(the_kth_word(str,n+m,k))
            printf("%s\n", str);
        else
            printf("-1\n");
        delete(str);
    }
    return 0;
}