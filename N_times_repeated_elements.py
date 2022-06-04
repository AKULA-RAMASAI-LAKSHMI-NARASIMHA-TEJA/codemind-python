n=int(input())
a=list(map(int,input().split()))
c=int(input())
b=set(a)
d=[]
e=0
for i in b:
    if a.count(i)==c:
        e+=1
        d.append(i)
if e==0:
    print("-1")
else:
    for i in range (len(d)):
        print(d[i],end=' ')