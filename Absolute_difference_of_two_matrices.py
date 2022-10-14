n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
b=[]
for i in range(n):
    b.append(list(map(int,input().split())))
r=[[abs(a[i][j]-b[i][j]) for j in range(n)]for i in range(n)]
for i in r:
    print(*i)