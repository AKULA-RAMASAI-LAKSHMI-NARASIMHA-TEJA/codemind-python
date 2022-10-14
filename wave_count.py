n=int(input())
l=list(map(int,input().split()))
a=b=0
for i in range(0,len(l)-2,2):
    b+=1
    if(l[i+1]>l[i] and l[i+1]>l[i+2]):
        a+=1
if(a==b):
    print(a)
else:
    print(-1)