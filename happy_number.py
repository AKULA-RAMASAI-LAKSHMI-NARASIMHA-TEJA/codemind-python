n=int(input())
r=0
while n:
    d=n%10
    n=n//10
    r+=d*d
    if n==0 and r>9:
        n=r
        r=0
if r==1 or r==7:
    print("True")
else:
    print("False")