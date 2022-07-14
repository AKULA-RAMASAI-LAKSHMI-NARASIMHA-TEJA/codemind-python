n=int(input())
a=list(map(int,input().split()))
b=set(a)
c=0
for i in b:
    c+=(a.count(i))//2
print(c)