# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if None == pRoot:
            return []
        traversal = []
        s = [[pRoot]]
        while len(s):
            layer_cur,layer_next = s.pop(),[]
            traversal.append([n.val for n in layer_cur])
            for n in layer_cur:
                if n.left:  layer_next.append(n.left)
                if n.right: layer_next.append(n.right)
            if len(layer_next): s.append(layer_next)
        return traversal