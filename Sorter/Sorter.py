#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import random
import time

class Sorter:
    def largeRandomArray(self,number):
        A=[]
        for i in range(0,number):
            A.append(int(random.random()*number))
        return A
    
    def insertionSort(self,A):
        i=0
        while i<len(A):
            key=A[i]
            j=i-1
            while j>=0 and A[j]>key:
                A[j+1]=A[j]
                j=j-1
            A[j+1]=key
            i=i+1
        return A
 
    def merge(self,A,B):
        index_1=len(A)
        index_2=len(B)
        pointer_1=0
        pointer_2=0
        R=[]
        while pointer_1<index_1 and pointer_2<index_2:
            if A[pointer_1] <= B[pointer_2]:
                R.append(A[pointer_1])
                pointer_1+=1
            else:
                R.append(B[pointer_2])
                pointer_2+=1
        if pointer_1 == index_1:
            R.extend(B[pointer_2:len(B)])
        else:
            R.extend(A[pointer_1:len(A)])
        return R

    def mergeSort(self,A):
        if len(A) != 1 :
            l=self.mergeSort(A[0:len(A)/2])
            r=self.mergeSort(A[len(A)/2:len(A)])
            R=self.merge(l,r)
            return R
        else:
            return A

    def heapSort(self,A):
        from Heap import Heap
        h = Heap(A)
        i = len(A)
        while i >= 2:
            j = h.heap[1]  
            h.heap [1] = h.heap[i]
            h.heap [i] = j
            h.heapsize = h.heapsize - 1
            h.maxHeapify(h.heap,1)
            i = i-1
        return h.heap[1:len(h.heap)]

if __name__=="__main__":
    import profile
    s=Sorter()
    l=s.largeRandomArray(100)
    print ("================PROFILE=================")
    print ("Insertion Sort:")
    profile.run("s.insertionSort(l)")
    print ("Merge Sort:")
    profile.run("s.mergeSort(l)")
    print ("Heap Sort:")
    profile.run("s.heapSort(l)")
