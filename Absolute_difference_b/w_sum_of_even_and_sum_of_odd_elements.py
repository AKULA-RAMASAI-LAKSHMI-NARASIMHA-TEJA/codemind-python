n=int(input())
a=list(map(int,input().split()))
e,o=0,0
for i in a:
    if i%2==0:
        e+=i
    else:
        o+=i
print(abs(e-o))