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
b=''
for i in a:
    b+=i
print(b)