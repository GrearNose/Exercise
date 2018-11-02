# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        if None == pNode:
            return None
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        if None == pNode.next:
            return None
        else:
            while pNode.next:
                if pNode == pNode.next.left: # left child of its parent
                    return pNode.next
                pNode = pNode.next
            return None