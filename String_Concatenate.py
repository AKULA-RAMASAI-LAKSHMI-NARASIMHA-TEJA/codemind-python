a=input()
b=input()
a+=b
a=list(a)
a.sort()
c=''
for i in a:
    c+=i
print(c)