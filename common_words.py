a=input()
a=a.lower()
a=a.split(' ')
b=input()
b=b.lower()
b=b.split(' ')
for i in b:
    if i in a:
        print(i,end=' ')