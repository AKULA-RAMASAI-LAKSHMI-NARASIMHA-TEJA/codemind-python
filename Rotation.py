t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=[]
    k=k%n
    for j in range(n):
        if j<k:
            b.append(a[n+j-k])
        else:
            b.append(a[j-k])
    print(*b)