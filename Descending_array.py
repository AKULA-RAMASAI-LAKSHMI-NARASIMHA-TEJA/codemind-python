n=int(input())
a=list(map(int,input().split()))
b=a
c=b[::-1]
a.sort()
for i in range(len(a)):
    if a[i]!=c[i]:
        print("no")
        break
else:
    print("yes")