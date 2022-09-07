t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]+a[j] in a:
                c+=1
    if c==0:
        print(-1)
    else:
        print(c)