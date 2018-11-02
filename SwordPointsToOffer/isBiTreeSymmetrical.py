# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if None == pRoot:
            return True
        l,r = pRoot.left,pRoot.right
        s = [(l,r)]
        while len(s):
            l,r = s.pop()
            if ((not l) != (not r)): # one None and one not None
                return False
            if not l: continue # both are None
            if (l.val != r.val) or ((not l.left) != (not r.right)) or ((not l.right) != (not r.left)):
                return False
            s.append((l.left,r.right))
            s.append((l.right,r.left))
        return True

# A BiTree is symmetrical if and only if it's the same as its mirror.
# Thus None or one node tree is symmetrical;
# it has two children if it has any, and they must be each other's mirror