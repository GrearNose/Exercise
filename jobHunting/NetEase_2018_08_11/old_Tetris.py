"""
Problem Description
Here is an old Tetris game. Each time one cubic will falls at a random
position on the ground. If there are already some cubic on the ground
at the position to fall at, the new cubic will fall on the top of them.
when these fallen cubics on the ground fill up a row, then this row
will vanish and the player gets one score. Given the sequence of such
cubics falling cubics, figure out the final score.

Input
1st line: two integers, n and m, indicating the number of cubics to fall,
    and the length of a row.
2nd line: n integers, the position on the ground these cubics.

Output
one integer, the final score.
"""


n,m = [int(x) for x in input().split()]
boxes = [int(x) for x in input().split()]

scores = 0
cnt = 0
appear = [0] * (n+1)
for bx in boxes:
    appear[bx] += 1
    if 1 == appear[bx]:
        cnt += 1
        if cnt == n:
            scores += 1
            appear = [x-1  for x in appear]
            cnt = 0
            for x in appear:
                if x > 0: cnt += 1
print(scores)