n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
if len(b)==0:
    print(-1)
else:
    print(max(b))