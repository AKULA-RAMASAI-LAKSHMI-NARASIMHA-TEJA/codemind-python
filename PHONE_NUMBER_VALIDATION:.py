a=int(input())
temp=a
rev=0
c=0
while a:
    d=a%10
    c+=1
    rev=rev*10+d
    a//=10
while rev:
    d=rev%10
    break
if c<10 or c>10 and d==0:
    print("Invalid")
else:
    print("Valid")