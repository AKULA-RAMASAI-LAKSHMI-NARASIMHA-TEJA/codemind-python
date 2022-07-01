n=int(input())
a=list(map(int,input().split()))
p=1
for i in range(n):
    for j in range(n):
        if a[i]==a[j]:
            pass
        else:
            p*=a[j]
    print(p,end=' ')
    p=1