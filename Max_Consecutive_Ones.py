n=int(input())
a=list(map(int,input().split()))
c,m=0,0
for i in a:
    if i==1:
        c+=1
    else:
        if c>m:
            m=c
        c=0
if c>m:
    m=c
print(m)