n=int(input())
a=list(map(int,input().split()))
c,d=0,0
for i in range(0,n-2):
    if  (a[i]<a[i+1] and a[i+1]>a[i+2]) or (a[i]>a[i+1] and a[i+1]<a[i+2]):
        pass
    else:
        c=1
        break
if c==1:
    print('no')
else:
    print('yes')