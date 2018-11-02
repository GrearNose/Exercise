# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if None == pHead1 or None == pHead2:
            return None
        assert isinstance(pHead1,ListNode)
        assert isinstance(pHead2,ListNode)
        ln1 = self.list_len(pHead1)
        ln2 = self.list_len(pHead2)
        #p = ListNode(ln1)
        #q = ListNode(ln2)
        #p.next = q
        #return p
        p,q = (pHead1,pHead2) if ln1 < ln2 else (pHead2,pHead1)
        s = set()
        while p:
            s.add(p)
            p = p.next
        while q:
            if q in s:
                return q
            q = q.next
        return q

    def list_len(self,pHead):
        if None == pHead:
            return 0
        assert isinstance(pHead,ListNode)
        ln = 0
        p = pHead
        while p:
            ln += 1
            p = p.next
        return ln
