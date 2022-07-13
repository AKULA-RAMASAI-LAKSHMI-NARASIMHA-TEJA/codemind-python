t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    while True:
        b.append(max(a))
        a.remove(max(a))
        if len(a)==0:
            break
        b.append(min(a))
        a.remove(min(a))
        if len(a)==0:
            break
    print(*b)