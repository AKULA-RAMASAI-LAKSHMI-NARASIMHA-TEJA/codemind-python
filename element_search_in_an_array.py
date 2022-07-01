n=int(input())
a=list(map(int,input().split()))
b=int(input())
if a.count(b)!=0:
    print('True')
else:
    print('False')