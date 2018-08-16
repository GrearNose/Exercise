/*
Problem Description
Wallis is gather up sundries in his room. There are some dumplings and each
consists of four articles. Each article comes with a position (a,b) and the
turning point (x,y), and can be roted 90 degrees counterclockwise. A dumpling
is tidy if its four articles form a square with an positive area. For each
dumpling, figure out the minimum rotation it takes to be tidy, if no possible
way, output -1.

Input
1st line: one integer n, the number of dumplings;
next 4*n lines: each line is the a,b,x,y of one article, and each four
        articles form a dumpling.
Output
n lines, each line one integer indicating the min rotations.

Remarks
This solution is fetched online.
*/



#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;
    for (int i = 0; i != n; ++i) {
        vector<vector<pair<int, int>>>edge(4, vector<pair<int, int>>(4, { 0,0 }));
        for (int j = 0; j != 4; ++j) {
            int a, b, x, y;
            cin >> a >> b >> x >> y;
            edge[j][0] = { a,b };
            for (int k = 1; k != 4; ++k)
                edge[j][k] = { x + y - edge[j][k - 1].second, y - x + edge[j][k - 1].first };
        }
        int mincost = 0x7FFFFFFF;
        for (int a = 0; a != 4; ++a)
            for (int b = 0; b != 4; ++b) 
                for (int c = 0; c != 4; ++c) 
                    for (int d = 0; d != 4; ++d) {
                        vector<pair<int, int>>temp{ edge[0][a],edge[1][b],edge[2][c],edge[3][d] };
                        sort(temp.begin(), temp.end());
                        if (temp[0].first == temp[1].first&&temp[0].second == temp[2].second&&
                            temp[1].second - temp[0].second != 0&&
                            temp[1].second - temp[0].second == temp[2].first - temp[0].first&&
                            temp[3].first == temp[2].first&&temp[3].second == temp[1].second)
                            mincost = min(mincost, a + b + c + d);
                    }
        cout << (mincost == 0x7FFFFFFF ? -1 : mincost) << endl;
    }
    return 0;
}