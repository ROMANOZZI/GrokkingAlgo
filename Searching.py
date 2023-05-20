## 1) Subarray wwith given sum

def SubArr(N,s,arr):
     left=right=0
     windowRes=arr[0]
     while right <len(arr):
          if windowRes < s:
               right+=1
               windowRes+=arr[right]
          elif windowRes==s:
               return [left+1,right+1]
          else:
               while windowRes > s:
                    windowRes-=arr[left]
                    left+=1
                    
##print(SubArr(5,12,[1,2,2,7,5]))
          
## 2) Missing number 
def MissingNum(n,arr):
   desiredres=0
   for i in range(1,n+1):
        desiredres+=i
   res=sum(arr)
   return desiredres-res
##print(MissingNum(5,[1,2,3,5]))
## 3) kth smallest number        
def kthSmallestElement(n,arr):
     arr=sorted(arr)
     return arr[n-1]
##print(kthSmallestElement(3,[7,10,4,3,20,15]))
## 4) O(Logn)
     