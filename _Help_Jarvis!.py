t=int(input())
for i in range(t):
    a=input()
    b=[]
    for i in a:
        b.append(int(i))
    if min(b)+3==max(b):
        print('YES')
    else:
        print('NO')