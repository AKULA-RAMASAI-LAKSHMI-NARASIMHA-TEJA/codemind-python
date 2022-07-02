n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,n,2):
    for j in range(a[i+1]):
        b.append(a[i])
print(*b)