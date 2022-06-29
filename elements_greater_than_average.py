n=int(input())
a=list(map(int,input().split()))
avg=sum(a)//n
c=0
for i in a:
    if i>=avg:
        c+=1
print(c)