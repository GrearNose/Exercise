# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        assert isinstance(tinput,(list,tuple))
        assert isinstance(k,int)
        if None == tinput or k <= 0:
            return []
        if k > len(tinput):
            return []
        heap = tinput[:k]
        print(heap)
        for i in reversed(range(k//2)):
            self.adjust_heap(heap,i,k)
        print(heap)
        for i in range(k,len(tinput)):
            if tinput[i] < heap[0]:
                heap[0] = tinput[i]
                self.adjust_heap(heap,0,k)
        # return heap
        for i in range(k-1):
            print(i,heap)
            heap[0],heap[k-i-1] = heap[k-i-1],heap[0]
            print(i,heap)
            self.adjust_heap(heap,0,k-i-1)
        return heap

    def adjust_heap(self,heap,ix,len_heap):
        if None == heap or 2*ix+1 >= len_heap: # None or has no child
            return
        if 2*ix+2 < len_heap: # has two children
            if heap[ix] >= max(heap[2*ix+1],heap[2*ix+2]): return # no need to adjust
            if heap[2*ix+1] > heap[2*ix+2]: # swap with the left child
                heap[ix],heap[2*ix+1] = heap[2*ix+1],heap[ix]
                self.adjust_heap(heap,2*ix+1,len_heap)
            else:
                heap[ix],heap[2*ix+2] = heap[2*ix+2],heap[ix]
                self.adjust_heap(heap,2*ix+2,len_heap)
        else: # has one child
            if heap[ix] >= heap[2*ix+1]: return # no need to adjust
            heap[ix],heap[2*ix+1] = heap[2*ix+1],heap[ix]
            self.adjust_heap(heap,2*ix+1,len_heap)
def test():
    # arr,k = [4,5,1,6,2,7,3,8],4
    arr,k = [4,5,1,6,2,7,3,8],8
    sulo = Solution()
    min_k = sulo.GetLeastNumbers_Solution(arr,k)
    print(arr,k)
    print(min_k)

if __name__ == '__main__':
    test()