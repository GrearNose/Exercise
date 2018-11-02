# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if None == numbers or 0 == len(numbers):
            return False
        n = sorted(numbers)
        ix = 0
        while 0 == n[ix]: ix += 1
        if (n[-1]-n[ix] or ix == len(n)-1) and ((n[-1] - n[ix]+1) - (len(n)-ix)) <= ix:
            return True
        return False