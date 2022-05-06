n=int(input())
temp=n
rev=0
while(n):
    d=n%10
    rev=rev*10+d
    n=n//10
if temp==rev:
    print("True")
else:
    print("False")