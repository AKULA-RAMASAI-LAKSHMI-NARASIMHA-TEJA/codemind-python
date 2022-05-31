def countoddsum(arr,n):
    res=0
    for i in range(n):
        val=0
        for j in range(i,n):
            val=val+arr[j]
            if(val%2!=0):
                res+=1
    return res
a=int(input())
b=int(input())
arr=[]
for i in range(a,b+1):
    arr.append(i)
print(countoddsum(arr,len(arr)))