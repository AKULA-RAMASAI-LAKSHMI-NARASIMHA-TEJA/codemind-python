n=int(input())
a=list(map(str,input().split()))
c=0
for i in a:
    if len(i)%2==0:
        c+=1
print(c)