n=int(input())
p,s=0,0
for i in range(n):
    a=list(map(int,input().split()))
    p+=a[i]
    s+=a[n-i-1]
print('Principal Diagonal',p,sep=':')
print('Secondary Diagonal',s,sep=':')