a=int(input())
b=int(input())
def pal(n):
    temp=n
    r=0
    while n:
        d=n%10
        r=r*10+d
        n=n//10
    if temp==r:
        return True
    else:
        return False
for i in range(a,b,1):
    if(pal(i)):
        print(i,end=' ')