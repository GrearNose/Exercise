# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if None == s or 0 == len(s):
            return -1
        occurence = {}
        keys = []
        for i,c in enumerate(s):
            if c in occurence:
                occurence[c] += 1
            else:
                occurence[c] = 1
                keys.append((c,i))
        for k,ix in keys:
            if 1 == occurence[k]:
                return ix
        return -1

def test():
    solu = Solution()
    strings = 'asldjaifas','asekhwenas','asnkabjmd'
    for s in strings:
        ix = solu.FirstNotRepeatingChar(s)
        print(s,ix,s[ix])

if __name__ == '__main__':
    test()