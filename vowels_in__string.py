s=input()
v=['a','e','i','o','u','A','E','I','O','U']
a=[]
for i in s:
    if i in v and i not in a:
        a.append(i)
if len(a)==0:
    print(-1)
else:
    print(*a)