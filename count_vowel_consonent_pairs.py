s=input()
v=['a','e','i','o','u','A','E','I','O','U']
x=s[0:len(s)//2]
y=s[len(s)//2:len(s)]
y=y[::-1]
c=0
for i in range(min(len(x),len(y))):
    if x[i]==' ' or y[i]==' ':
        continue
    if(x[i] in v and y[i] not in v) or (x[i] not in v and y[i] in v):
        c+=1
print(c)