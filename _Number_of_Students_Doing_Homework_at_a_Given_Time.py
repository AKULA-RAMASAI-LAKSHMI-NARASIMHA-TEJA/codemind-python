m=int(input())
a=list(map(int,input().split()))
n=int(input())
b=list(map(int,input().split()))
c=int(input())
d=0
for i in range(len(a)):
    if a[i]<=c and c<=b[i]:
        d+=1
print(d)