# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if None == pHead: return None
        if not pHead.next: return pHead
        h,last,p,q = None,None,pHead,pHead.next
        while q:
            if p.val == q.val:
                while q.next and p.val == q.val:
                    q = q.next
                if q.next: # q is not the end, thus p.val != q.val
                    p,q = q,q.next
                else: # q is the end, but not sure whether p.val != q.val
                    if last:
                        last.next = q if p.val != q.val else None
                    else:
                        h = q if p.val != q.val else None
                    break
            else:
                if last:
                    last.next = p
                    last = p
                else:
                    h = last = p
                p,q = q,q.next
        return h