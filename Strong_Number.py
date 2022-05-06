n=int(input())
temp=n
p=1
s=0
while n:
    d=n%10
    for i in range(1,d+1):
        p=p*i
    s+=p
    n=n//10
    p=1
n=temp
if s==n:
    print("The number {0} is a strong number".format(n))
else:
    print("The number {0} is not a strong number".format(n))