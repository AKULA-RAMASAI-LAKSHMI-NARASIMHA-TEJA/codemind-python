n=int(input())
a=list(map(int,input().split()))
b,c,d=[],[],[]
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
e,f=len(b),len(c)
g=min(e,f)
h=max(e,f)-g
for i in range(g):
    d.append(b[i])
    d.append(c[i])
for i in range(h):
    if e>f:
        d.append(b[g+i])
    else:
        d.append(c[g+i])
if len(d)%2!=0:
    d.append(0)
print(*d)