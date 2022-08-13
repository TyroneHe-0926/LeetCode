#using a min and max heap
from heapq import heappush, heappop, heapify
import math

minHeap=[]
heapify(minHeap)
maxHeap=[]
heapify(maxHeap)

def insertHeaps(num):
    heappush(maxHeap,-num)                ### Pushing negative element to obtain a minHeap for
    heappush(minHeap,-heappop(maxHeap))    ### the negative counterpart
   
    if len(minHeap) > len(maxHeap):
        heappush(maxHeap,-heappop(minHeap))
     
def getMedian():
    if len(minHeap)!= len(maxHeap):
        return -maxHeap[0]
    else:
        return (minHeap[0]- maxHeap[0])/2
   
 
if __name__== '__main__':
    A= [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
    n= len(A)
    for i in range(n):
        insertHeaps(A[i])
        print(math.floor(getMedian()))