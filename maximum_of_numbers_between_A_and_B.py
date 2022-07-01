n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
b=[]
for i in a:
    if i>=x and i<=y:
        b.append(i)
if b==[]:
    print('-1')
else:
    print(max(b))