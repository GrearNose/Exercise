# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if None == data or 0 == len(data):
            return 0
        if k == data[0]:
            lb = 0
        else:
            l,h = 0,len(data)
            while l + 1 < h:
                m = (l+h) >> 1
                if k <= data[m]: # k <= data[h] always true
                    h = m
                elif data[m] < k: # data[l] < k always true
                    l = m
            # when l+1 == h, lower bouder found,
            # otherwise l+1 > h, k is not in data
            if l+1 > h:
                return 0
            lb = h
        if k == data[-1]:
            ub = len(data)-1
        else:
            l,h = 0,len(data)
            while l + 1 < h:
                m = (l+h) >> 1
                if k < data[m]: # k < data[h] always true
                    h = m
                elif data[m] <= k: # data[l] <= k always true
                    l = m
            assert l + 1 == h
            ub = l
        return ub-lb+1