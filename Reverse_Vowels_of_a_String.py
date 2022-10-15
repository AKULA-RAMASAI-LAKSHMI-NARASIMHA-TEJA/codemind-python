v=['a','e','i','o','u','A','E','I','O','U']
s=input()
a=[]
for i in s:
    if i in v:
        a.append(i)
a.reverse()
b=0
for i in s:
    if i in a:
        i=a[b]
        b+=1
    print(i,end='')