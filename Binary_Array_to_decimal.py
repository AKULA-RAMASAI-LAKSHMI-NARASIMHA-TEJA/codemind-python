n=int(input())
a=list(map(int,input().split()))
p=0
for i in a:
    n-=1
    p+=i*(2**n)
print(p)