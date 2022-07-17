n=int(input())
a=list(map(int,input().split()))
b=int(input())
for i in a:
    if i+b>=max(a):
        print('True',end=' ')
    else:
        print('False',end=' ')