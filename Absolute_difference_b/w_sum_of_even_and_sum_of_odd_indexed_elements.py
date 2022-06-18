n=int(input())
a=list(map(int,input().split()))
e,o=0,0
for i in range(len(a)):
    if i%2==0:
        e+=a[i]
    else:
        o+=a[i]
print(abs(e-o))