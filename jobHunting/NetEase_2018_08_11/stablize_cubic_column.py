"""
Problem Description
There are some columns of cubics with different height, while all the cubics
forming them are of the same side length of 1. Define the instable index s as
the height difference of the highest one and the shortest one. To stablize
them (decrease s), Cubics can be moved from one column to another one at a
time. Given the maximum times k of such move, figure out the final value of s,
and the actual times it takes to move, and the two columns involved in each
move.

Algorithm
Use Greedy strategy: each time pick the highest one and the shortest one,
then each move will have the max possibility to lower the s value(as there
might be more than one such columns), so at last s will reach the least value.

Input
1st line: two integer n and k, indicating the number of columns
           and the maximum moves;
2nd line: n integers, height of each columns.

Output
1st line: two integers s and m, the smallest s value and the actual moves;
next m lines: the two columns involed in each move.
"""

n,k = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]

def indx_max(arr):
    ix = [0]
    for i,v in enumerate(arr[1:]):
        # print('ix,i,v', ix,i,v)
        if v > arr[ix[0]]:
            # print('replace')
            ix = [i+1]
        elif v == arr[ix[0]]:
            # print('append')
            ix.append(i+1)
    return ix

def indx_min(arr):
    ix = [0]
    for i,v in enumerate(arr[1:]):
        if v < arr[ix[0]]: ix = [i+1]
        elif v == arr[ix[0]]: ix.append(i+1)
    return ix

# print('n,k',n,k)
# print('h:', h)

ix_max = indx_max(h)
ix_min = indx_min(h)
moves = []
i = -1
for i in range(k):
    t = h[ix_max[0]] - h[ix_min[0]]
    # print('ix_max:',ix_max)
    # print('ix_min:',ix_min)
    # print('t:', t)
    if 0 == t:
        s = 0
        break
    ixM = ix_max.pop()
    ixm = ix_min.pop()
    h[ixM] -= 1
    h[ixm] += 1
    moves.append((ixM+1,ixm+1))
    if len(ix_max) == 0:
        ix_max = indx_max(h)
    if len(ix_min) == 0:
        ix_min = indx_min(h)
m = i + 1
s = h[ix_max[0]] - h[ix_min[0]]
print(s,m)
for mv in moves:
    print(mv[0],mv[1])
