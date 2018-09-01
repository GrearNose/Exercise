from random import seed, randint
from time import time

def first_repeat_decimal(n, m, mx_trials=1000, debug=False):
    """
    Given two integers, n and m, judge whether n/m has repeating decimals,
    and if it does, return the starting position of repeating decimal
    (after the  decimal point), and the length of the repeating decimal
    digits, if not, return None.
    ==== Args ====
    n,m: the two integers to judge,
    mx_trials: the maximum number of decimals digits to try.
    return: position of the first repeating decimal digit and the length of
    the repeating decimal digits.
    """
    if None == n or None == m:
        return None

    n,m = abs(int(n)),abs(int(m)) # make sure they are positive integers.
    n %= m # only get the remainder, in case that n > m

    remainder, decimals = [],[]
    while n * 10 < m:      # get the proceeding 0s.
        decimals.append(0) # redcord the decimal digits.
        n *= 10
    num_pred_0 = len(decimals)

    for _ in range(mx_trials):
         if 0 == n: break # non-reapeating decimal
         if n in remainder:
             ix  = remainder.index(n)
             ln  = len(remainder)-ix
             pos = ix+1
             if debug:
                print('remainder:', remainder)
                print('decimals:', decimals)
             return num_pred_0 + pos, ln
         remainder.append(n) # record the remainder
         decimals.append((10*n)//m)
         n = (10*n) % m # update the new remainder.
    return None,None # exceed the max trials


# solu by other guy.
def rp_dcml(m,n,debug=False):
    m       %= n
    result  = []
    i, flag = 0,0
    while( m % n != 0):
        if m in result:
            ix = result.index(m)
            print('ix,ln:', 1+ix,i-ix)
            if debug: print(result,m)
            flag = 1
            break
        result.append(m)
        m = m * 10 % n
        i += 1
    if flag == 0:
        # print(i,0)
        print('ix,ln:', None,None)
 
def test():
    test_num = 13
    mn,mx = 3, 99
    seed(time())
    for _ in range(test_num):
        # n = 123479
        # m = 999
        # m = 999*1e3
        n,m = randint(mn,mx),randint(mn,mx)
        print('%d/%d = %.33f' %(n,m,n/m))

        # pos,ln = first_repeat_decimal(n,m,1000,True)
        pos,ln = first_repeat_decimal(n,m,1000)
        print('ix,ln:',pos,ln)

        rp_dcml(n,m)
 
if __name__=='__main__':
     test()