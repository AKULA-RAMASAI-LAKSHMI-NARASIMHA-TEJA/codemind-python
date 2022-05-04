n=int(input())
e=0
c=0
o=0
while n:
    d=n%10
    if(d%2==0):
        e+=1
    else:
        o+=1
    c+=1
    n=n//10
if(c==e):
    print("Even")
elif(c==o):
    print("Odd")
else:
    print("Mixed")