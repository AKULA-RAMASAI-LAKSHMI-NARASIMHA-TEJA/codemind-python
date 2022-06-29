n=int(input())
a=list(map(int,input().split()))
b=a.count(0)
c=a.count(1)
if b+c==n:
    print('True')
else:
    print('False')