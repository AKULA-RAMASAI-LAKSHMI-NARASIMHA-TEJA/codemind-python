n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    b.append(len(str(i)))
d=max(b)
for i in a:
    if len(str(i))==d:
        c.append(i)
print(*c)