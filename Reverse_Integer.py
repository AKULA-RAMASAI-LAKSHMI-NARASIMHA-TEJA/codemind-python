n=int(input())
rev=0
s=0
if n>0:
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    print(rev)
else:
    s=abs(n)
    while s:
        d=s%10
        rev=rev*10+d
        s//=10
    print(-rev)