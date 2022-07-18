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
print(len(a))