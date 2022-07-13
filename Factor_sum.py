def fun(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
    return s
a=list(map(int,input().split(',')))
b=[]
for i in a:
    if fun(i) in a:
        b.append(i)
b.sort()
if len(b)==0:
    print('-1')
else:
    print(*b)