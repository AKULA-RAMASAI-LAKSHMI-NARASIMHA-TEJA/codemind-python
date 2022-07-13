n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    c=0
    for j in range(n):
        if a[i]>a[j]:
            c+=1
    b.append(c)
print(*b)