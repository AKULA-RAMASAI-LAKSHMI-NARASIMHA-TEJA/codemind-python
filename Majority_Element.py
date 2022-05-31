n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    c=a.count(i)
    b.append(c)
for i in a:
    if a.count(i)==max(b):
        print(i)
        break