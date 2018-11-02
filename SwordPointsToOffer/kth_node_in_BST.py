# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if None == pRoot or k < 1:
            return None
        rslt,_ = self.kth_node_in_BST(pRoot,k)
        return rslt
    def kth_node_in_BST(self,r,k):
        if None == r or k < 1:
            return None,0
        cnt_node_left,cnt_node_right = 0,0
        if r.left:
            rslt,cnt_node_left = self.kth_node_in_BST(r.left,k)
            if rslt: return rslt,None # the second val will not be used when the node is found.
            if cnt_node_left+1 == k: return r,None
        if r.right:
            # search the the r-subtree, there are k-1-cnt_node_left nodes in l-subtree and root.
            rslt,cnt_node_right = self.kth_node_in_BST(r.right,k-1-cnt_node_left)
            if rslt: return rslt,None
        if 1 + cnt_node_left + cnt_node_right == k:
            return r,None
        return None, 1 + cnt_node_left + cnt_node_right