#include <algorithm>
#include <ctime>
#include <cassert>
#include <vector>
#include <iostream>
#define N 52
using namespace  std;

template <typename T>
bool has_a_sum(T*arr, unsigned len, int sum_cur,\
    int sum_target, vector<int> &nums, int depth=0)
{
    if( len < 1 || sum_cur > sum_target)
        return false;

    if (sum_cur == sum_target)
    {
        // cout << "depth = " << depth << ": ";
        // for (unsigned i = 0; i < nums.size(); ++i)
        //     cout << nums[i] << " ";
        // cout << endl;
        return true;
    }

    if(sum_cur+arr[0] > sum_target) // impossible to find feasible num in the rest part.
        return false;
    // choose arr[0]
    nums.push_back(arr[0]);
    if(has_a_sum(arr+1, len-1, sum_cur+arr[0], sum_target, nums, depth+1))
        return true;
    // not choose arr[0]
    nums.pop_back();
    return has_a_sum(arr+1, len-1, sum_cur, sum_target, nums, depth+1);
}

template <typename T>
bool has_a_sum_enumerate(T*arr, unsigned len, int sum)
{
    if( len < 1)
        return false;
    // choose arr[0]
    if (sum-arr[0] == 0)
        return true;
    else if (has_a_sum_enumerate(arr+1, len-1, sum-arr[0]))
        return true;
    // not choose ar[0]
    if(has_a_sum_enumerate(arr+1, len-1, sum))
        return true;
    return false;
}


int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; ++i)
    {
        cin >> arr[i];
    }
    // sort(arr,arr+n);
    // for (int i = 0; i < n; ++i)
    // {
    //     printf("%d ", arr[i]);
    // }
    // printf("\n");
    int sum;
    cin >> sum;
    std::vector<int> nums;
    // if (has_a_sum(arr,n,0,sum,nums))
    if (has_a_sum_enumerate(arr, n, sum))
        cout << 1 << endl;
    else
        cout << 0 << endl;
    return 0;
}