class Sorter:
    
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

if __name__=="__main__":
    s = Sorter()
    B=s.insertionSort([5,3,1,6,4,2,9,7])
    print B
