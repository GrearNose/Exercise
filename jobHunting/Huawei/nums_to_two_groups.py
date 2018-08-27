import traceback
from collections import Counter
def has_a_sum(arr,s_cur,s_tar):
    if s_cur == s_tar:
        return True
    if None == arr or len(arr) < 1:
        return False
    if s_cur + arr[0] > s_tar:
        return False
    if has_a_sum(arr[1:],s_cur+arr[0],s_tar) or has_a_sum(arr[1:],s_cur,s_tar):
        return True
    return False


def equal_divide(nums):
    """
        Devide a set of numbers into two group such that them have equal sum
        and all numbers that can be divided exactly by 5 should be put in one
        group and all numbers that can be divided exactly by 3 should be put
        the other group.
    """
    g1,g2 = 0,0
    others = []
    for n in nums:
        if 0 == n % 3: g1 += n
        elif 0 == n % 5: g2 += n
        else:
            others.append(n)
    print('others:', others)
    # cnt = Counter(others)
    # others = []
    # for k in cnt:
    #     if 0 != cnt[k] % 2:
    #         others.extend([k]*cnt[k])
    others.sort()
    print('others',others)
    print('dif of g1 and g2:', g1-g2)
    tmp = (sum(others) + abs(g1-g2))
    print('tmp:',tmp)
    if 0 != tmp % 2:
        return False
    sm = tmp // 2
    rslt = 'true' if has_a_sum(others,0,sm) or has_a_sum(others,0,-sm) else 'false'
    if False == rslt and 20 == len(nums):
        print(g1,g2,tmp,others)
    return rslt

def test():
    # nums = [-2,0,-3,3,-3,-4,-3,1,3,3,-2,0,3,2,2,-5,1,-2,-3,-5]
    # nums = [1,-5,5,3,2,1,-2,-5,-2]
    nums = [2,-1,2,-4,-3,0,2,-5,-5,-4,5,-2,2,2,5,-5,-4,-1,-2,-1,-4,-3]
    rslt = equal_divide(nums)
    print(rslt)

if __name__ == '__main__':
    test()

# try:
#     while True:
#         input()
#         nums = [int(x) for x in input().split()]
#         print(rslt)
# except EOFError:
#     pass
# except Exception as e:
#     traceback.print_exc(e)