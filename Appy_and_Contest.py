def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    c=gcd(a,b)
    lcm=(a*b)//c
    d=n//a+n//b-2*n//lcm
    if d>=k:
        print('Win')
    else:
        print('Lose')