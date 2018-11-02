# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        if not threshold or not rows or not cols or threshold<=0: return 0
        m = [[False]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if sum([int(x) for x in str(i)]) + sum([int(x) for x in str(j)]) <= threshold:
                    m[i][j] = True
        directions = ((0,-1),(0,1),(-1,0),(1,0))
        s = [(0,0)]
        cnt = 1
        m[0][0] = False
        while len(s):
            cur = s.pop()
            for d in directions:
                i,j = cur[0]+d[0],cur[1]+d[1]
                if 0<=i and i<rows and 0<=j and j<cols and m[i][j]:
                    s.append((i,j))
                    m[i][j] = False
                    cnt += 1
        return cnt