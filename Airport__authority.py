c=[]
n=int(input())
for i in range(n):
    a=int(input())
    c.append(a)
d=int(input())
b=0
e=0
for i in c:
    if i>d:
        b=b+1
    else:
        e=e+1
print(2*b+e)