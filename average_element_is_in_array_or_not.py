n=int(input())
a=list(map(int,input().split()))
s=sum(a)
avg=s//n
if avg in a:
    print("True")
else:
    print("False")