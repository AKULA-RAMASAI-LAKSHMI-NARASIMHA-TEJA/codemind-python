n=int(input())
s=0
p=1
while n:
    d=n%10
    s+=d
    p*=d
    n=n//10
print(p-s)