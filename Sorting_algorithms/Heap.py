import math
import util

class Heap:
    """
        This is a heap implementation using python.
        One thing to notice here is for consistency with the CLRS book, the
        heap here index form 1 instead of 0.
    """
    def __init__(self,A):
        self._heapsize = len(A)
        self._heap = self.expandArray(A)
        self.buildMaxHeap()

    def __str__(self):
        return str(self._heap[1:len(self._heap)])
    
    def __getitem__(self,i):
        self._testIndex(i)  
        return self._heap[i]

    def __setitem__(self,i,value):
        """
            This method may violate the heap's property, use it carefully.
        """
        self._testIndex(i)
        self._heap[i] = value  

    @property
    def heapsize(self):
        return self._heapsize;
    
    @heapsize.setter
    def heapsize(self,value):
        if valuse < 0:
            raise Exception("Heapsize cannot be less then 0")
        self._heapsize = value

    @property
    def heap(self):
        return self._heap
    
    @heap.setter
    def heap(self,A):
        self._heap = self.expandArray(A)
        self.buildMaxHeap()

    def buildMaxHeap(self):
        i = int(math.floor(len(self._heap)/2))
        while(i >= 1):
            self.maxHeapify(i)
            i-=1

    def maxHeapify(self,i):
        l = self.Left(i)
        r = self.Right(i)
        if l <= self.heapsize and self._heap[l] > self._heap[i]:
            largest = l;
        else:
            largest = i;
        if r <= self.heapsize and self._heap[r] > self._heap[largest]:
            largest = r;
        if largest != i:
            self._heap[i],self._heap[largest] = util.swap(self._heap[i],self._heap[largest])
            self.maxHeapify(largest)

    def expandArray(self,A):
        R=[0]
        for i in range(0,len(A)):
            R.append(A[i])
        return R

    def _testIndex(self,i):
        if i < 1 or i > self._heapsize:
            raise Exception("Heap index error!")

    def Parent(self,i):
        self._testIndex(i)
        return int(math.floor(i/2))

    def Left(self,i):
        self._testIndex(i)
        return i*2

    def Right(self,i):
        self._testIndex(i)
        return i*2+1
    
    def append(self,val):
        """
            This may violate the heap property, use it carefully.
        """
        self._heapsize += 1
        self._heap.append(val)

if __name__=="__main__":
    A=[4,1,3,2,16,9,10,14,8,7]
    H=Heap(A)
    print H
