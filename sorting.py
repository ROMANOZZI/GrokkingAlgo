


def kthSmallestElement(arr,number):
    removed=[]
    for i in range(1,max(arr)+number+1):
        if i not in arr:
            removed.append(i)
    return removed[number-1]
##print(kthSmallestElement([1,3],4))
def chooseKarray(arr,k):
 arr=sorted(arr)
 i=1
 res=max(arr[0:3])-min(arr[0:3])
 temp=0
 window=[]
 while i+k <len(arr):
     window=arr[i:i+k]
     temp=max(window)-min(window)
     if temp <res:
         res=temp
     i+=1
 return res
##print(chooseKarray([10,100,300,200,1000,20,30],3))


def sortAfterApply(arr,A,B,C):
    return sorted(map(lambda x: ((A*(x**2))+(B*x)+C),arr))
print(sortAfterApply([-1,0,1,2,3,4],-1,2,-1))    