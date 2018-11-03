# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        """ Given a set of numbers, connect them head to tail yielding a new
            number, try to find out the min of these yieled numbers.
        """
        if None == numbers or 0 == len(numbers):
            return ''
        n = [str(x) for x in numbers]
        sc = max([len(x) for x in n]) # to get the max length
        # append with the first char to get keys with same length,
        # in this way, the key of '3,32,321' are '333,323,321',
        # sort them according to these keys, the result is '321,32,3',
        # then concatenated together, they yield the minimum number:
        #      321323
        n.sort(key=lambda x: x+x[0]*(sc-len(x)))
        n = ''.join(n)
        n = int(n)
        return n

def test():
    n = [3,32,321]
    solu = Solution()
    m = solu.PrintMinNumber(n)
    print(n,m)

if __name__ == '__main__':
    test()