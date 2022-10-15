s=list(input())
o,e=[],[]
for i in s:
    if i>='0' and i<='9':
        if int(i)%2==0:
            e.append(i)
        else:
            o.append(i)
if(len(e)==0):
    print(-1)
else:
    e=list(sorted(set(e)))
    o=list(sorted(set(o)))
    l=e[0]
    e.remove(l)
    f=list(reversed(sorted(o+e)))
    f.append(l)
    print(*f,sep='')