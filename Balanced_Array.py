t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        if sum(a[0:(i)])==sum(a[i+1:]):
            print('YES')
            break
    else:
        print('NO')