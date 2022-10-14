a,b=map(int,input().split())
d=0
for _ in range(0,a):
    v=list(map(int,input().split()))
    k=sorted(v)
    if(k==v or k==v[::-1]):
        d+=1
print(d)