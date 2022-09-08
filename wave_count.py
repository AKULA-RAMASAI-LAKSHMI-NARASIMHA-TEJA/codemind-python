n=int(input())
a=list(map(int,input().split()))
b,c=0,0
for i in range(0,n-2,2):
    c+=1
    if(a[i+1]>a[i] and a[i+1]>a[i+2]):
        b+=1
if c==b:
    print(b)
else:
    print(-1)