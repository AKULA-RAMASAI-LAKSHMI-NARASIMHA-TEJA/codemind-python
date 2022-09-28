s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
a=[]
for i in s1:
    if i==' ':
        continue
    if i not in s2 and i not in a:
        a.append(i)
for i in s2:
    if i not in s1 and i not in a:
        a.append(i)
print(len(a))