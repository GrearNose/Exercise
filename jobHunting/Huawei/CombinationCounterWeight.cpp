#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int sum_cnt(const int addens[], const int num[], const int len)
{
    if (NULL == addens || NULL == num || len <= 0)
        return 0;
    // records the different sum of a certain combination of addens.
    set<int> com;
    // initialize with 0, as 0 is a possible combination.
    com.insert(0);

    // put the first type of addens into the set.
    for(int i = 1; i <= num[0]; i++)
        com.insert(i * addens[0]);

    // for each of the rest n-1 types of addens.
    for(int i = 1; i < len; i++)
    {
        vector<int> sum_new;
        for(int s : com) // based on each of the existing combination,
        {
            // make a new combinition by adding j addens of the i-th type.
            for(int j = 1; j <= num[i]; j++) 
            {
                int trial = s + j * addens[i];
                // if this new combination yields a new sum, write it down.
                if(com.end() == com.find(trial))
                    sum_new.push_back(trial);
            }
        }
        if (sum_new.size() > 0)
        {
            for(int s: sum_new)
                com.insert(s);
        }
    }
    return com.size();
}


int main()
{
     int n;               // number of counterweight.
     int weight[10] = {0};// weight of each type of counterweight
     int num[10] = {0};   // number of each type of counterweight.
     while( cin >> n )
     {
        for(int i = 0; i < n; i++)
            cin >> weight[i];
        for(int i = 0; i < n; i++)
            cin >> num[i];
        cout << sum_cnt(weight,num,n) << endl;
     }
}