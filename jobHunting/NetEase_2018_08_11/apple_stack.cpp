#include <iostream>
#include <string>
using namespace std;

/*
Problem Description
There are n stack apples, and the i-th has the number of Ai.
Given a query q, figure out which stack the q-th apple belongs to.
input:
the 1st row, an integer n, the number of apple stacks;
the 2nd row, n integers, the amount of each stacks;
the 3rd row, an integer m, the number of queries;
the 4th row, m integers, the queries.
outputs:
m rows, each for the answer to the corresponding queires.
*/

int main(int argc, char* argv[])
{
    int n = 0, m = 0;
    int a[100000], q[100000];
    long long acc[100000], total = 0;

    // input the apple stacks
    cin >> n;
    for(int i = 0; i < n; ++i)
    {
        cin >> a[i];
        total += a[i];
        acc[i] = total;
    }
    // input the quries.
    cin >> m;
    for(int i = 0; i < m; ++i)
        cin >> q[i];
    // queries.
    for(int i = 0; i < m; ++i)
    {
        if(q[i] > total || q[i] < 0)
        {
            cout << -1 << endl;
            continue;
        }
        int l = 0, h = n-1, mid;
        while(l <= h)
        {
            mid = (l + h) >> 1;
            if (q[i] < acc[mid])
                h = mid - 1;
            else if (q[i] > acc[mid])
                l = mid + 1;
            else
            {
                l = mid;
                break;
            }
        }
        // acc[l] is the least uppper bound.
        cout << l + 1 << endl;
    }

    return 0;
}