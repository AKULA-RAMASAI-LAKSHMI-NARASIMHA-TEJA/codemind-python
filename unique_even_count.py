n=input()
a=list(map(int,input().split()))
b=set(a)
c=0
for i in b:
    if i%2==0:
            c+=1
print(c)