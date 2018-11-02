# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if None == array or None == tsum:
            return []
        i,j = 0,len(array)-1
        while i < j:
            n,m = array[i],array[j]
            if n+m == tsum:
                return [n,m]
            elif n+m < tsum:
                i += 1
            else:
                j -= 1
        return []