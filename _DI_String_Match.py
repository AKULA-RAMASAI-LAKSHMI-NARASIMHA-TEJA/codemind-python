s=list(input())
a=[]
b,c=0,len(s)
for i in s:
    if i=='I':
        a.append(b)
        b+=1
    else:
        a.append(c)
        c-=1
for i in range(b,c+1):
    if i not in a:
        a.append(i)
print(*a)