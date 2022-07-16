a=input()
b=input()
a,b=a.lower(),b.lower()
a,b=list(a),list(b)
c=0
a,b=set(a),set(b)
for i in a:
    if i==' ':
        continue
    if i in b:
        c+=1
print(c)