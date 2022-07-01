n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in l:
    if i>=a and i<=b:
        c.append(i)
if c==[]:
    print('-1')
else:
    print(min(c))