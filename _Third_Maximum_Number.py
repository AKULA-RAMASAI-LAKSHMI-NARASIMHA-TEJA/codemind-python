n=int(input())
a=list(map(int,input().split()))
a=set(a)
a=list(a)
a.sort()
if n==1 or n==2:
    print(max(a))
else:
    print(a[-3])