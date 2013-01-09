import Heap
class PQueue:
    """This is a priority queue implementation
    """
    def __init__(self,A):
        self.heap = Heap.Heap(A)
    
    def maximum(self):
        return self.heap.heap[1]
    
    def extractMax(self):
        if self.heap.heapsize < 1:
            raise Exception("Heap underflow!")
        maxofQueue = self.heap.heap[1]
        self.heap.heap[1] = self.heap.heap[self.heap.heapsize]
        self.heap.heapsize-=1
        self.heap.maxHeapify(self.heap.heap,1)
        return maxofQueue

if __name__=="__main__":
    A=[4,1,3,2,16,9,10,14,8,7]
    P=PQueue(A)
    print P.maximum()
    while P.heap.heapsize > 1:
        print P.extractMax()
