#include <iostream>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
    int n = 0, m = 0;
    int a[100000], q[100000];
    long long acc[100000], total = 0;
    // input n
    cin >> n;
    cout << "stacks: ";
    for(int i = 0; i < n; ++i)
    {
        cin >> a[i];
        total += a[i];
        acc[i] = total;
        cout << a[i] << " ";
    }
    cout << endl << "acc: ";
    for (int i = 0; i < n; ++i)
        cout << acc[i] <<" ";
    cout << endl;

    // input q
    cin >> m;
    cout << "queries: ";
    for(int i = 0; i < m; ++i)
    {
        cin >> q[i];
        cout << q[i] << " ";
    }

    // algorithm
    for(int i = 0; i < m; ++i)      // the m-th question
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