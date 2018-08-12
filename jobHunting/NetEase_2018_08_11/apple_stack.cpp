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

template<typename T>
void print_array(T*arr,int n, string msg)
{
    cout << msg;
    for (int i = 0; i < n; ++i)
        cout << arr[i] << " ";
    cout << endl;
}

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

    print_array(a, n, "stacks:");
    print_array(acc, n, "acc:");
    print_array(q, m, "queries:");

    // queries.
    for(int i = 0; i < m; ++i)
    {
        if(q[i] > total || q[i] < 0)
        {
            cout << -1 << endl;
            continue;
        }
        cout << endl;
        int l = 0, h = n-1, mid;
        int cnt = 0;
        cout << "query: " << q[i] << endl;
        while(l <= h)
        {
            ++ cnt;
            if (cnt > n)
            {
                cout << "deap loop " << endl;
                break;
            }
            mid = (l + h) >> 1;
            printf("l,h,m: %d, %d, %d\n", l,h,mid);
            if ((acc[mid-1] < q[i]) && (q[i] <= acc[mid]))
            {
                printf("%d\n",mid+1);
                break;
            }
            else if ((mid > 0) && (q[i] < acc[mid-1]))
                h = mid-1;
            else if ((acc[mid] < q[i]) && (mid < n))
                l = mid +1;
        }
    }

    return 0;
}