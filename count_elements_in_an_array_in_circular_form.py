n=int(input())
a=list(map(int,input().split()))
b=a
b.append(a[0])
b.append(a[1])
c=0
for i in range(1,n+1):
    if(b[i-1]%2==0 and b[i+1]%2!=0) or (b[i-1]%2!=0 and b[i+1]%2==0):
        c+=1
print(c)