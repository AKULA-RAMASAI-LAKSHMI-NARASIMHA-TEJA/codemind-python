n=int(input())
for i in range (n):
    a=int(input())
    rev=0
    temp=a
    while a:
        d=a%10
        rev=rev*10 +d
        a=a//10
    if(temp==rev):
        print("True")
    else:
        print("False")