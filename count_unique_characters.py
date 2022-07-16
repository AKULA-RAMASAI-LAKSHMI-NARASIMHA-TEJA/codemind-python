s=input()
s=s.lower()
s=list(s)
a=[]
for i in s:
    if i==' ':
        continue
    else:
        if s.count(i)==1:
            a.append(i)
a.sort()
b=0
for i in a:
    b+=1
print(b)