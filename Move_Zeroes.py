n=int(input())
a=list(map(int,input().split()))
b=[]
c=a.count(0)
for i in a:
    if i!=0:
        b.append(i)
for i in range(c):
    b.append(0)
print(*b)