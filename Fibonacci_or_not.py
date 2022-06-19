n=int(input())
a=0
b=1
for i in range(1,n+1):
    c=a+b
    a=b
    b=c
    if(c==n):
        print("True")
        break
else:
    print("False")