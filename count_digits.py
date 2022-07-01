n=int(input())
a=list(map(int,input().split()))
for i in a:
    print(len(str(abs(i))),end=' ')