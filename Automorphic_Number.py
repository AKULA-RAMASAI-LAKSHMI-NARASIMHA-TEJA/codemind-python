n=int(input())
temp=n
sq=n*n
c=0
while n:
    n=n//10
    c+=1
r=0
while c:
    d=sq%10
    r=r*10+d
    sq=sq//10
    c-=1
res=0
while r:
    d=r%10
    res=res*10+d
    r=r//10
if temp==res:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")