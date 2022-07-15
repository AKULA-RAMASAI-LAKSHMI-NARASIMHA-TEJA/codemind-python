m=int(input())
n=int(input())
s=0
for i in range(m):
    s+=sum(list(map(int,input().split())))
print(s)