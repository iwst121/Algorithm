from Heap import Heap
import util

class PQueue:
    """This is a priority queue implementation"""
    def __init__(self,A):
        self._heap = Heap(A)

    def __str__(self):
        return str(self._heap.heap[1:])

    def peekMax(self):
        return self._heap[1]
    
    def extractMax(self):
        if self._heap.heapsize < 1:
            raise Exception("Heap underflow!")
        _max = self._heap[1]
        self._heap[1] = self._heap[self._heap.heapsize]
        self._heap.heapsize -= 1
        self._heap.maxHeapify(1)
        return _max
    
    def increaseKey(self,i,key):
        if key < self._heap[i]:
            raise Exception("New key is smaller than current key")
        self._heap[i] = key
        while i > 1 and self._heap[self._heap.Parent(i)] < self._heap[i]:
            self._heap[i],self._heap[self._heap.Parent(i)] = self._heap[self._heap.Parent(i)],self._heap[i]
            i = self._heap.Parent(i)
    
    def insert(self,key):
        pass

if __name__=="__main__":
    A=[4,1,3,2,16,9,10,14,8,7]
    P=PQueue(A)
    print P
    print P.peekMax()
    P.increaseKey(2,100)
    print P
