a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=0
c=0
for i in range (len(a)):
    if a[i]>b[i]:
        d=d+1
    if a[i]<b[i]:
        c=c+1
print(d,c)