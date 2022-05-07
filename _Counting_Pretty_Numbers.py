n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=0
    for j in range (a,b+1):
        while j:
            d=j%10
            if d==2 or d==3 or d==9:
                c+=1
            break
    print(c)