# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if None == num or len(num) < size or size < 1:
            return []
        window = Counter(num[:size])
        mx = [max(window.keys())]
        for i in range(size,len(num)):
            if 1 == window[num[i-size]]:
                del window[num[i-size]]
            if num[i] in window:
                window[num[i]] += 1
            else:
                window[num[i]] = 1
            mx.append(max(window.keys()))
        return mx