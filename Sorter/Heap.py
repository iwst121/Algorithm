import math

class Heap:
    def __init__(self,A):
        self._heapsize = len(A)
        self._heap = self.expeandArray(A)
        self.buildMaxHeap(self._heap)

    def __str__(self):
        return str(self._heap[1:len(self._heap)])

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
        self._heap = self.expeandArray(A)
        self.buildMaxHeap(self._heap)

    def buildMaxHeap(self,A):
        i = int(math.floor(len(A)/2))
        while(i >= 1):
            self.maxHeapify(A,i)
            i-=1

    def maxHeapify(self,A,i):
        l = self.Left(i)
        r = self.Right(i)
        if l <= self.heapsize and A[l] > A[i]:
            largest = l;
        else:
            largest = i;
        if r <= self.heapsize and A[r] > A[largest]:
            largest = r;
        if largest != i:
            j = A[i]
            A[i] = A[largest]
            A[largest] = j
            self.maxHeapify(A,largest) 

    def expeandArray(self,A):
        R=[0]
        for i in range(0,len(A)):
            R.append(A[i])
        return R

    def Parent(self,i):
        return int(math.floor(i/2))

    def Left(self,i):
        return i*2

    def Right(self,i):
        return i*2+1

if __name__=="__main__":
    A=[4,1,3,2,16,9,10,14,8,7]
    H=Heap(A)
    print H
