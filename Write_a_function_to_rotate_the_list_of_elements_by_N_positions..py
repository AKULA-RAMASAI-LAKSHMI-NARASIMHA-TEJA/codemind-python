n=int(input())
a=list(map(int,input().split()))
r=int(input())
for i in range(r):
    b=a[-1]
    for j in range(n-1,0,-1):
        a[j]=a[j-1]
    a[0]=b
print(*a)