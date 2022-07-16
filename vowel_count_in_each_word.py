s=input()
s=s.lower()
s=s.split()
b=[]
c=0
a=['a','e','i','o','u']
for i in s:
    c=0
    i=list(i)
    for j in i:
        if j in a:
            c+=1
    b.append(c)
print(*b)