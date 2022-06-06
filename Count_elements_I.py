m,n=input().split()
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
c=0
for i in a:
    if i in b:
        c+=1
print(c)