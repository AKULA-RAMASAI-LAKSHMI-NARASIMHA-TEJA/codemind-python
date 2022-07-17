n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i>0:
        b.append(i)
b.sort()
for i in range(1,max(b)+2):
    if i not in b:
        print(i)
        break