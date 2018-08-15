# Problem Description
# There are n stack apples, and the i-th has the number of Ai.
# Given a query q, figure out which stack the q-th apple belongs to.
# input:
# the 1st row, an integer n, the number of apple stacks;
# the 2nd row, n integers, the amount of each stacks;
# the 3rd row, an integer m, the number of queries;
# the 4th row, m integers, the queries.
# outputs:
# m rows, each for the answer to the corresponding queires.


n = int(input())
A = [int(x) for x in input().split()]
m = int(input())
q = [int(x) for x in input().split()]


acc = []
s = 0
for x in A:
    s += x
    acc.append(s)

for a in q:
    if a < 0 or a > acc[-1]:
        print(-1)
        continue

    l,h = 0,n-1
    while l <= h:
        mid = (l+h) >> 1
        if a > acc[mid]:
            l = mid + 1
        elif a < acc[mid]:
            h = mid - 1
        else:
            l = mid
            break
    print(l+1) # acc[l] is the lest upper bound.