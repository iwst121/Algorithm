import math

class Heap:
    def __init__(self,A):
        self.heapsize = len(A)
        self.heap = self.expeandArray(A)
        self.buildMaxHeap(self.heap)

    def __str__(self):
        return str(self.heap[1:len(self.heap)])

    def buildMaxHeap(self,A):
        i =int(math.floor(len(A)/2))
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
    
    def getList(self):
        return self.heap

if __name__=="__main__":
    A=[4,1,3,2,16,9,10,14,8,7]
    H=Heap(A)
