a=input()
a=list(a)
e=[]
d=[]
for i in a:
    if i not in e:
        e.append(i)
for i in e:
    if i in "aeiouAEIOU":
        d.append(i)
if d==" ":
    print(-1)
else:
    print(*d)