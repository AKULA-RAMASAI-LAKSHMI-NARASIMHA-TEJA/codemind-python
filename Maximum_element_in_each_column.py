n,m=map(int,input().split())
a=list()
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    max=0
    for j in range(m):
        if a[j][i]>max:
            max=a[j][i]
    print(max)