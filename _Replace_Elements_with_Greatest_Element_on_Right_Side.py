n=int(input())
a=list(map(int,input().split()))
b=list()
for i in range(n-1):
    c=max(a[i+1:n+1])
    b.append(c)
b.append(-1)
print(*b)