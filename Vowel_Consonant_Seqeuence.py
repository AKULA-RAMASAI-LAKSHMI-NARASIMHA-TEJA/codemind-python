vow=['a','e','i','o','u']
a=list(input())
b=[a[0]]
c=0
for i in range(1,len(a)):
    if(b[c] in vow)and(a[i] in vow):
        continue
    elif(b[c] not in vow)and(a[i] not in vow):
        continue
    else:
        b.append(a[i])
        c+=1
s=''
for i in b:
    if i in vow:
        s+='V'
        continue
    s+='C'
print(s)