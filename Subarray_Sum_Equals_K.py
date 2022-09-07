n,k=map(int,input().split())
a=list(map(int,input().split()))
s=0
for i in range(n):
    for j in range(i+1,n+1):
        b=sum(a[i:j])
        if b==k:
            s+=1
print(s)