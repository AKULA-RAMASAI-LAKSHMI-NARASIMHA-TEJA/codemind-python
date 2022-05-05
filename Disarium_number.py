n=int(input())
temp=n
rev=0
while n:
    d=n%10
    rev=rev*10 + d
    n=n//10
sum=0
i=1
while rev:
    d=rev%10
    sum+=d**i
    i+=1
    rev=rev//10
if(sum==temp):
    print("True")
else:
    print("False")