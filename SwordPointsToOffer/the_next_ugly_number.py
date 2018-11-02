# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if 0 == index: return 0
        ugly_num = [1]
        fac = [2,3,5]
        for i in range(1,index):
            candidates = []
            for f in fac:
                for u in ugly_num:
                    can = f*u
                    if can > ugly_num[-1]:
                        candidates.append(can)
                        break
            nxt = min(candidates) # the next ulgly_number
            if i == index:
                return nxt
            while ugly_num[0]*fac[-1] < nxt:
                del ugly_num[0]
            ugly_num.append(nxt)
        return ugly_num[-1]

def test():
    solu = Solution()
    for n in range(30):
        u = solu.GetUglyNumber_Solution(n)
        print(n,u)

if __name__ == '__main__':
    test()