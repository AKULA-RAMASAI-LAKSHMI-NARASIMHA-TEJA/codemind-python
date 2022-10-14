a,b=map(int,input().split())
d=0
for i in range(0,a):
    c=list(map(int,input().split()))
    e=sorted(c)
    if(e==c or e==c[::-1]):
        d+=1
print(d)