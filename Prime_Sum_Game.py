def fun(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    return 0
a,b,c,d=map(int,input().split())
for i in range(a,b+1):
    e=0
    for j in range(c,d+1):
        if fun(i+j):
            break
        if j==d:
            print('Takahashi')
            e=1
            break
    if e==1:
        break
else:
    print('Aoki')