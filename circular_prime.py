n=int(input())
temp=n
r=0
while n:
    d=n%10
    r=r*10+d
    n=n//10
n=temp
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
            break
    else:
        return True

if prime(n) and prime(r):
    print("circular prime")
elif prime(n) and not prime(r):
    print("prime but not a circular prime")
else:
    print("not prime")