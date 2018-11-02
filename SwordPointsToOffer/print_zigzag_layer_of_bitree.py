# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        if None == pRoot: return []
        traversal = []
        in_seq = True
        s = [[pRoot]]
        while len(s):
            layer_cur = s.pop()
            if not len(layer_cur): continue
            layer_next = []
            for n in layer_cur:
                if n.left:  layer_next.append(n.left)
                if n.right: layer_next.append(n.right)
            s.append(layer_next)

            if not in_seq: layer_cur = reversed(layer_cur)
            traversal.append([n.val for n in layer_cur])
            in_seq = not in_seq
        return traversal