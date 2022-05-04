n=int(input())
s=0
temp=n
while n:
    d=n%10
    s+=d
    n=n//10
if(temp%s==0):
    print("True")
else:
    print("False")