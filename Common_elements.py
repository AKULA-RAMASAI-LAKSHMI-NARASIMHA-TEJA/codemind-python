m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in a:
    if i not in c:
        c.append(i)
for i in c:
    if i in b:
        print(i,end=' ')