n=int(input())
a=list(map(int,input().split()))
c,d=0,0
for i in range(n):
    if a[i]%2==0 and i%2==0:
        c+=1
    if a[i]%2==0:
        d+=1
if c==d:
    print("True")
else:
    print("False")