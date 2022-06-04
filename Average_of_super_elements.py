n=input()
a=list(map(int,input().split()))
b=set(a)
c=[]
d=0
for i in b:
    if a.count(i)==i:
        c.append(i)
        d+=1
if d==0:
    print("-1")
else:
    print('{0:.2f}'.format(sum(c)/len(c)))