s=input()
s=s.lower()
s=list(s)
a=[]
for i in s:
    if i==' ':
        continue
    else:
        if i not in a:
            a.append(i)
print(len(a))