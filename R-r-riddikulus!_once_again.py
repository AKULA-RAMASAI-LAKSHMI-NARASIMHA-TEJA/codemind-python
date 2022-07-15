def fun(a,n,d):
    d=d%n
    return a[d:]+a[:d]
n,d=map(int,input().split())
a=list(map(int,input().split()))
b=fun(a,n,d)
print(*b)