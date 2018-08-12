#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int max_elem(int* arr, int l, int r)
{
    int max_e = arr[l];
    for(int i = l; i < r; ++i)
    {
        if(arr[i] > max_e)
        {
            max_e = arr[i];
        }
    }
    return max_e;
}

int min_elem(int* arr, int l, int r)
{
    int min_e = arr[l];
    for(int i = l; i < r; ++i)
    {
        if(arr[i] < min_e)
        {
            min_e = arr[i];
        }
    }
    return min_e;
}


int main(int argc, char* argv[])
{
    int n = 0;
    int a[100000], b[100000];

    // input
    cin >> n;
    for(int i = 0; i < n; ++i)
        cin >> a[i];
    for(int i = 0; i < n; ++i)
        cin >> b[i];

    // algorithm
    int maxA = 0, minB = 0;
    int count = 0;
    for(int l = 0; l < n; ++l)
    {
        for(int r = l; r < n; ++r)
        {
            maxA = max_elem(a, l, r);
            minB = min_elem(b, l, r);

            if(maxA < minB)
                ++count;
        }
    }

    // output
    cout << count << endl;

    return 0;
}