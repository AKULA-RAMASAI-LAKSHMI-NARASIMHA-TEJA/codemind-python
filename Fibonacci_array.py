n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n-3):
    if a[i]+a[i+1]==a[i+2]:
        c+=1
if c==n-3:
    print('yes')
else:
    print('no')