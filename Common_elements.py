m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
for i in a:
    if i not in c:
        c.append(i)
for i in c:
    if i in b:
        d.append(i)
print(*d)