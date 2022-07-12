n,x=map(int,input().split())
a=list(map(int,input().split()))
c,d=0,0
for i in a:
    if i<=x:
        c+=1
    elif d==1:
        break
    else:
        d+=1
print(c)