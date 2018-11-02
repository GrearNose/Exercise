# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if None == array or 0 == len(array):
            return []
        num = []
        cnt = Counter(array)
        for k in cnt.keys():
            if 1 == cnt[k]:
                num.append(k)
                if 2 == len(num):
                    return num
        return num
