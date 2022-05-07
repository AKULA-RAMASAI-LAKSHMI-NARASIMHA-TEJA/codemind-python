n=int(input())
sqn=n*n
temp=n
rn=0
while n:
    d=n%10
    rn=rn*10+d
    n=n//10
sqr=rn*rn
rr=0
while sqr:
    d=sqr%10
    rr=rr*10+d
    sqr=sqr//10
if sqn==rr:
    print(True)
else:
    print(False)