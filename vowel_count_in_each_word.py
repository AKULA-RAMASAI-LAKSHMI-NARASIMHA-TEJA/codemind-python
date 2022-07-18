s=input()
s=s.lower()
s=s.split()
a=[]
c=0
for i in s:
    c=0
    for j in i:
        if j in 'aeiou':
            c+=1
    a.append(c)
print(*a)