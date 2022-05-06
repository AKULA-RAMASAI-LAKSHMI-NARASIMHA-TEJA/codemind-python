n=int(input())
for i in range(1,n,1):
    x=2**i
    if n<x:
        break
l=2**(i-1)
u=2**(i)
if n==x:
    print("0")
elif n-l>u-n:
    print(u-n)
else:
    print(n-l)