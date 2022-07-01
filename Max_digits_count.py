n=int(input())
a=list(map(int,input().split()))
b=max(a)
c=len(str(b))
d=0
for i in a:
    if len(str(i))==c:
        d+=1
print(d)