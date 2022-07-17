t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    b=list(set(a))
    b.sort()
    r=b[0]
    l=0
    for j in b:
        if a.count(j)>l:
            l=a.count(j)
            res=j
    print(res)