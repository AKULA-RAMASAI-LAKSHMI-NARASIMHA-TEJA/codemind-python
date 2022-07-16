s=input()
s=s.lower()
s=list(s)
a=[]
c=0
for i in s:
    if i==' ':
        continue
    else:
        if s.count(i)==1:
            print(i)
            c=1
            break
if c==0:
    print(-1)