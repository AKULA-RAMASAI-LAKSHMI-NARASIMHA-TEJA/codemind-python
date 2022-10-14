s=input()
a=[]
for i in s:
    if i.isalpha():
        a.append(i)
a.sort()
j=0
for i in s:
    if i.isalpha():
        i=a[j]
        j+=1
    print(i,end='')