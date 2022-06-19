n=int(input())
def prime(n):
    for i in range(2,int(n**0.5)+1,1):
        if n%i==0:
            return False
            break
    else:
        return True
if prime(n):
    print("0")
else:
    i=n+1
    while True:
        if prime(i):
            np=i
            break
        i+=1
    for i in range(n-1,0,-1):
        if prime(i):
            pp=i
            break
    if n-pp<np-n:
        print(n-pp)
    else:
        print(np-n)