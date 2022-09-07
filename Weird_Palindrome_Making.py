t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for j in a:
        c+=j%2
    print(c//2)