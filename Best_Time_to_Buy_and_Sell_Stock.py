n=int(input())
a=list(map(int,input().split()))
min=a[0]
for i in range(n):
    if min>a[i]:
        min=a[i]
        break
max=max(a[i:n])
print(max-min)