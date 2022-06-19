n=int(input())
for i in range(1,n):
    if i*(i+1)==n:
        print('YES')
        break
else:
    print('NO')