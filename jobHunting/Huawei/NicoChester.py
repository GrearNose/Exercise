from time import time
from random import randint, seed

def NicoChester(m):
    """
        NicoChester Theorem
        Any positive integer m, its cubic is the sum of m consective odds.
        Give an positive m, try to figure out all these odds
        that sum up to its cubic.
    """
    if None == 0 or m < 0:
        return None
    n = m ** 3
    base = (n - m*(m-1)) // m
    itms = [str(base+2*i) for i in range(m)]
    return itms


def test():
    test_num = 10
    mn,mx = 1, 33
    seed(time())
    for _ in range(test_num):
        m = randint(mn,mx)
        itms = NicoChester(m)
        s = '%d ** 3 = '%m + '+'.join(itms)
        print(s)
if __name__ == '__main__':
    test()