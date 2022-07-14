n=int(input())
a=list(map(int,input().split()))
b,c,d=[],[],[]
while True:
    b.append(max(a))
    a.remove(max(a))
    if len(a)==0:
        break
    c.append(max(a))
    a.remove(max(a))
    if len(a)==0:
        break
while True:
    if len(c)!=0:
        d.append(max(c))
        c.remove(max(c))
    d.append(max(b))
    b.remove(max(b))
    if len(b)==0:
        break
print(*d)