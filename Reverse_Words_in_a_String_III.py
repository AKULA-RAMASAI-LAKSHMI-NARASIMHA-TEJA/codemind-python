s=input()
s=s.split()
a=list(s)
b=[]
for i in a:
    b.append(i[::-1])
print(*b)