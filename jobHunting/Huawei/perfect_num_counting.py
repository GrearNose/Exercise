import traceback
from itertools import product

def primes_sifting(n):
    if None == n or n <2:
        return None
    primes = []
    sift = [True]*(n+1)
    i = 2
    while i**2 <= n:
        for j in range(i**2,n+1,i):
            sift[j] = False
        primes.append(i)
        i += 1
        while not sift[i] and i <= n:
            i += 1
    for j in range(i,n+1):
        if sift[j]:
            primes.append(j)
    return primes

def lower_b(arr,val):
    if None == arr or None == val or 0 == len(arr):
        return None
    if val < arr[0]:
        return None
    if val >= arr[-1]:
        return len(arr)-1
    if val == arr[0]:
        return 0
    l,h = 0, len(arr)-1
    while l <= h:
        m = (l+h) >> 1 # (l+h) // 2
        if val > arr[m]:
            l = m + 1
        elif val < arr[m]:
            h = m - 1
        else:
            return m
    return h # the greatest lower bound.

try:
    while True:
        n = int(input().strip())
        primes = primes_sifting(n)
        cnt_perfect = 0          # counter of the perfect number.
        for i in range(6,n+1):
            ix = lower_b(primes,i)
            if primes[ix] == i: # i is a prime,
                continue        # then it is not a perfect num.
            fac_prime = []
            fac_occ = []
            for p in primes[:ix+1]: # find the prime factors.
                if 0 == i % p:
                    occ = 0
                    t = i
                    while t > 0 and 0 == t % p:
                        occ += 1
                        t //= p
                    fac_prime.append(p)
                    fac_occ.append(list(range(occ+1)))
            fac = []
            # print(fac_occ)
            # break
            for exps in product(*fac_occ):
                f = 1
                for j in range(len(fac_occ)):
                    f *= fac_prime[j]**exps[j]
                fac.append(f)
            # print(i, fac_prime, fac_occ, fac)
            # break
            # now, fac contains all factors of i, including 1 and i itself.
            if sum(fac) - i == i:
                cnt_perfect += 1
        print(cnt_perfect)
except EOFError:
    pass
except Exception as e:
    traceback.print_exc(e)