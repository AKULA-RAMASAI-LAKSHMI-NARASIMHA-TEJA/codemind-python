m=int(input())
a=list(map(int,input().split()))
n=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(len(a)):
    c.insert(b[i],a[i])
print(*c)