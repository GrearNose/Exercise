# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix or not rows or not cols or not path: return False
        if rows<=0 or cols<=0 or rows*cols != len(matrix): return False
        if not isinstance(matrix,str) or not isinstance(path,str): return False
        loc_start = [] # locations
        m = [matrix[i*cols:(i+1)*cols] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if path[0] == m[i][j]:loc_start.append((i,j))
        visited = [[False]*cols for _ in range(rows)]
        for start_point in loc_start:
            if self.dfs(m,visited,path,0,start_point): return True
        return False

    def dfs(self,m,visited,p,ix,cur):
        assert isinstance(m,(list,tuple))
        assert isinstance(visited,list)
        assert isinstance(p,str)
        assert 0<=ix and ix<len(p)
        assert isinstance(cur,(list,tuple))
        i,j = cur
        if m[i][j]!=p[ix] or visited[i][j]: return False
        if ix+1 == len(p): return True
        visited[i][j] = True # visited the current node.
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        for d in directions:
            i,j = cur[0] + d[0], cur[1] + d[1]
            if 0<=i and i<len(m) and 0<=j and j<len(m[0]):
                if self.dfs(m,visited,p,ix+1,(i,j)): return True
        i,j = cur
        visited[i][j] = False # recover to the previous status.
        return False