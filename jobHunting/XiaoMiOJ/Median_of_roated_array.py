def solution(line):
    """
        Given a str of comma separated numbers of a rotated array,
        find out its meidan. N.B. length rotated array is odd and
        all elements are unique.
    """
    nums = [int(x) for x in line.split(',')]
    # print('nums:', nums)
    if 1 == len(nums):
        return nums[0]
    if nums[0] < nums[-1]:
        n = nums[len(nums)>>1]
        r = str(n)
        return r
    ix = 0
    i,j = 0,len(nums)-1
    while i < j:
        if 1 == j - i:
            ix = j
            break
        m = (i+j) >> 1
        # print(i,j,m)
        if nums[m] >= nums[i]:
            i = m
        elif nums[m] <= nums[j]:
            j = m
    ln1,ln2 = ix, len(nums)-ix
    # print('ix',ix,'min', nums[ix])
    # print('ln1,ln2',ln1,ln2)
    if ln1 > ln2:
        ix = (ln1-ln2)>>1
    elif ln1 < ln2:
        ix = len(nums) - ((ln2-ln1)>>1) - 1
    # print('ix',ix)
    r = str(nums[ix])
    return r

def test():
    s = ['1', '1,2,3', '4,5,6,7,0,1,2', '12,13,14,5,6,7,8,9,10', '8,9,1,2,3,4,5,6,7','1,2,3,4,5,6,7']
    for l in s:
        r = solution(l)
        print(l,r,sep='\n')
if __name__ == '__main__':
    test()