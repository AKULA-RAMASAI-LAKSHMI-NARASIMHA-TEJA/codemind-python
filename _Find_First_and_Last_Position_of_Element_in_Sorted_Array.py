n=int(input())
a=list(map(int,input().split()))
t=int(input())
f,l=-1,-1
for i in range(n):
    if t!=a[i]:
        continue
    if f==-1:
        f=i
    l=i
print(f,l)