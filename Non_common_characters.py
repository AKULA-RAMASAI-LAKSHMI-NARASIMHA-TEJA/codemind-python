a=input()
b=input()
a,b=a.lower(),b.lower()
a,b=list(a),list(b)
c=[]
a,b=set(a),set(b)
for i in a:
    if i==' ':
        continue
    if i not in b:
        c.append(i)
for i in b:
    if i==' ':
        continue
    if i not in a:
        c.append(i)
print(len(c))