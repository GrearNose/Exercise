# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        f,_ = self.BitreeBalance(pRoot)
        return f
    def BitreeBalance(self,r):
        if None == r:
            return True,0
        fl,dl = self.BitreeBalance(r.left)
        if not fl:
            return False,1+dl
        fr,dr = self.BitreeBalance(r.right)
        return (fr and abs(dl-dr)<=1), max(dl,dr)+1