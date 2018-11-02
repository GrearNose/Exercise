from random import randint,seed
from time import time

def occurence_of_k(m,k):
    """
    Given a positve integer m and a digit 0<=k<=9, figure out
    the occurence of k in all numbers in range [1,m].
    N.B. k might appear more than once in a certain number, in
    this case, evry occurence of k in this number count.
    """
    assert m > 0
    assert 0 <= k and k <= 9
    cnt = 0
    k = str(k)
    for i in range(1,m+1):
        cnt += sum([x==k for x in str(i)])
    return cnt

def occurence_of_k_divide(m,k):
    assert m > 0
    assert 0 <= k and k <= 9
    s   = str(m)
    ln  = len(s)
    # --------------- for the first(highest) digit --------------
    if 0 == k: # high digits cannot be 0.
        cnt = 0
    else:
        if int(s[0]) < k:    # the first digit is smaller than k.
            cnt = 0
        elif int(s[0]) == k: # the first digit is exactly k.
            cnt = int(s[1:])+1 if ln > 1 else 1
        else:                # the first digit is larger than k.
            cnt = 10**(ln-1)
    # -------------- for the 2nd ~ n-th digits -----------------
    for i in range(1,ln):
        l = int(s[:i])   # combination of digits in the left
        r = 10**(ln-i-1) # combination of digts in the right
        cnt += l*r if k else (l-1)*r # xx..k..xx
        if k < int(s[i]): # A0A1..k..xx
            cnt += r
        elif k == int(s[i]): # A0A1..k..An-1An
            cnt += int(s[i+1:])+1 if i+1<ln else 1
    return cnt

def test():
    seed(time())
    k = randint(0,9)
    n_test = 13
    testCase=[(randint(1,1000),k) for _ in range(n_test)]
    # testCase.append((99,1))
    # testCase.append((90,0))
    # testCase.append((1,0))
    passed = True
    for n,k in testCase:
        cnt1 = occurence_of_k(n, k)
        cnt2 = occurence_of_k_divide(n,k)
        print('[%5d,%d]: %5d vs %5d'%(n,k,cnt1,cnt2))
        if cnt1 != cnt2: passed = False
    if passed:
        print('Passed all tests!')
    else:
        raise('Did not pass all tests!')
if __name__ == '__main__':
    test()