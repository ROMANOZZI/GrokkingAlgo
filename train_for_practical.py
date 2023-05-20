
##bubble sort
def bubble_Sort(unsorted):
    for i,Round in enumerate(unsorted):
        for j,item in enumerate(unsorted):
            if j<len(unsorted)-1 and item > unsorted[j+1]:
                unsorted[j],unsorted[j+1]=unsorted[j+1],unsorted[j]
    return unsorted
##print(bubble_Sort([8,2,3,6,9,4]))

## quick sort
def Quicky(unsorted):
    if len(unsorted)<=1:
        return unsorted
    pivot=unsorted[0]
    return Quicky([i for i in unsorted if i < pivot ])+[pivot] +Quicky([i for i in unsorted if i > pivot ])
##print(Quicky([8,2,3,6,9,4]))
## merge sort 
def mergy(unsorted):
   if len(unsorted)>1:
      middy=len(unsorted)//2
      left= unsorted[:middy ]
      right= unsorted[middy:]
      mergy(left)
      mergy(right)
      i=j=k=0
      while i<len(left) and j<len(right):
          if left[i]<right[j]:
              unsorted[k]= left[i]
              i+=1
          else:
              unsorted[k]= right[j]
              j+=1
          k+=1
      while i<len(left):
              unsorted[k]= left[i]
              i+=1
              k+=1
      while j<len(right):
          unsorted[k]= right[j]
          j+=1
          k+=1
      print(unsorted)
##mergy([8,2,3,6,9,4])
graph1={
    's': ['A' , 'B' , 'D'] , 
    
    'A': ['C'] , 
    
    'B': ['D'] , 
    
    'C': ['D' , 'G'] ,
    
    'D': ['G'],
    
    'G': []
    
}
from collections import deque
def BFS(graph,start,goal):
    queue=deque()
    queue.append((start,[start]))
    visited=set()
    visited.add(start)
    while queue:
        node,path=queue.popleft()
        if node==goal:
            return path
        else:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor,path+[neighbor]))
    return None

##print(BFS(graph1,"G","s"))

##print(findSmallest([50,2,64,2,6,12]))

def selectionSort(arr):
    if len(arr)<2:
        return arr
    smallest = min(arr)
    i=arr.index(smallest)
    
    return [smallest] +selectionSort(arr[i+1:]+arr[:i])
##print(selectionSort([1,1,2,5,1,3,4,9,2]))
def binarySearch(arr,goal):
    high=len(arr)-1
    low=0
    while high >=low:
        mid= (low+high)//2
        
        if arr[mid]==goal:
            return mid
        elif arr[mid]>goal:
            high=mid-1
        else:
            low=mid+1
    return -1
##print(binarySearch([1,2,3,4,62,100,151],100))


def removeDuplicate(word):
    if len(word)<2:
        return word
    if word[0]==word[1]:
        return removeDuplicate(word[1::])
    return word[0]+removeDuplicate(word[1::])
##print(removeDuplicate("HHBBO"))

def factorial(num):
    if num <2:
        return num
    return num *factorial(num-1)
print(factorial(5))