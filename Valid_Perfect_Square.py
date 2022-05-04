a=int(input())
for i in range(1,a+1,1):
    n=int(input())
    for j in range(1,n+1):
        if(n==j*j):
            print(True)
            break
    else:
        print(False)