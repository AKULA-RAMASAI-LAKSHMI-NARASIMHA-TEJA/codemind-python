a=int(input())
b=list(map(int,input().split()))
c,d=0,0
for i in b:
    if(i%2==0):
        c+=1
    else:
        d+=1
print(c,d)