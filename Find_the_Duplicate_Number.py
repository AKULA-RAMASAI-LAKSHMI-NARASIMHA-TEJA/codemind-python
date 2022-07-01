n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if a.count(i)>1:
        print(i)
        break