/*
    Problem Description
    Given an array of integers A, build up another array B,
    such that B[i] = A[0]*A[1]*...A[i-1]*A[i]*...A[n-1],
    N.B. DO NOT use division.
*/

class Solution {
public:
    vector<int> multiply(const vector<int>& A) {
    vector<int> B;
     int cur = 1;
     for(int i =0; i < A.size(); i++)
     {
         B.push_back(cur);
         cur *= A[i];
     }
     cur = 1;
     for(int i =A.size()-1; i>=0 ; i--)
     {
         B[i] *= cur;
         cur *= A[i];
     }
     return B;
    }
};