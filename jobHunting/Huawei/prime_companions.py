import traceback
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

def prime_companion(odds,evens,primes):
    if None == odds or 0 == len(odds) or None == evens or 0 == len(evens):
        return 0
    mx = 0
    odd = odds[0]
    for j in range(len(evens)):
        cnt = (odd + evens[j] in primes)
        if len(odds) > 1:
            evens_n = evens[:j] + evens[j+1:]
            cnt += prime_companion(odds[1:],evens_n,primes)
        mx = max(mx,cnt)
    return mx

def cnt_prime_companions(nums):
    if None == nums or 0 == len(nums):
        return 0
    odds  = [x for x in nums if 1 == x%2]
    evens = [x for x in nums if 0 == x%2]
    print('len(odds):',len(odds))
    print('len(evens):',len(evens))
    primes = primes_sifting(max(nums)*2)
    print('len(primes):',len(primes))
    cnt = prime_companion(odds,evens,primes)
    return cnt

def test():
    # nums = [2,5,6,13]
    nums = [9360, 2272, 15078, 15571, 4734, 18667, 10392, 17796, 12207, 14591, 8380, 10126, 11627, 1288, 24523, 568, 15754, 8400, 11280, 20964, 15482, 28433, 26109, 11147, 9628, 12296, 8500, 21628, 22561, 5532, 8830, 13253, 3231, 15580, 27278, 4824, 19217, 16038, 10091, 21071, 19587, 10243, 8786, 15529, 23644, 13228, 21503, 22706, 13546, 2937, 24488, 19924, 16138, 13815, 22460, 4122, 26823, 2987, 25011, 25469, 27224, 16237]
    cnt = cnt_prime_companions(nums)
    print(cnt)

if __name__ == '__main__':
    test()

# try:
#     while True:
#         input()
#         s = [int(x) for x in input().split()]
#         cnt = cnt_prime_companions(s)
#         print(cnt)
# except Exception as e:
#     # traceback.print_exc(e)
#     pass