s=input()
a=[]
for i in s:
    if i.isalpha():
        a.append(i)
a.sort()
c=0
for i in s:
    if i.isalpha():
        i=a[c]
        c+=1
    print(i,end='')