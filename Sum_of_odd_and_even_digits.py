n=int(input())
a=list(map(int,input().split()))
o,e=0,0
for i in range(n):
    if i%2==0:
        o+=a[i]
    else:
        e+=a[i]
if e-o==0:
    print('YES')
else:
    print('NO')