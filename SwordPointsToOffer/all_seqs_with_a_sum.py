# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        # return []
        seqs = []
        for a1 in range(1,(tsum+1)//2):
            n = 1
            while True:
                s = (2*a1+n)*(n+1)
                if s > 2*tsum:
                    break
                elif s == 2*tsum:
                    seqs.append(list(range(a1,a1+n+1)))
                n += 1
        return seqs