n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    c.append(i)
    c.append(a.count(i))
print(*c)