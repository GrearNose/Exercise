# -*- coding:utf-8 -*-
from random import randint
class Solution:
    def Add(self, num1, num2):
        if None == num1 or None == num2:
            return None
        if 0 == num1: return num2
        if 0 == num2: return num1

        n1,n2 = num1,num2
        if n1<n2: n1,n2 = n2,n1
        print('n1,n2:',n1,n2)
        s = n1
        ad = 1
        carry = 0
        while ad <= n2<<1 or carry:
            print('s,ad,c:',s,ad,carry,end='; ')
            if ((n2 & ad) or carry):
                if (n2 & ad):
                    carry_new = ((ad&s) | (s&carry) | (ad&carry))<<1 # use s before it's updated
                    s = s^ad^carry
                else:
                    carry_new = (s&carry)<<1 # use s before it's updated
                    s = s^carry
                carry = carry_new
            print('s,ad,c:',s,ad,carry)
            ad <<= 1
        s ^= carry
        return s

def adder(n,m,bit_len=32):
    if None == n or None == m: return None
    if not n or not m: return m if not n else n
    truncate = 2**bit_len-1
    print(bin(truncate))
    while m:
        n,m = n^m, (n&m)<<1
        n,m = n&truncate, m&truncate
    return n^m

def test():
    n_test = 13
    l,h    = -13,19
    solu   = Solution()
    passed = True
    for _ in range(n_test):
        n,m = randint(l,h),randint(l,h)
    # for n,m in [(2,3),(3,-4),(3,-5)]:
        print(n,m,end=' ')
        # s = solu.Add(n,m)
        s = adder(n,m)
        print(s)
        if n+m != s:
            passed = False
    print('Passed all tests: ', passed)

if __name__ == '__main__':
    test()