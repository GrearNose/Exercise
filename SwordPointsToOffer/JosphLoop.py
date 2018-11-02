# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if None == n or None == m or n <= 0:
            return -1
        s = list(range(n))
        ix = 0
        while len(s)>1:
            ix += m-1 if m else 0
            ix %= len(s)
            del s[ix]
        return s[0]