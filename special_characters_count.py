s=input()
c=0
for i in s:
    if ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122 or ord(i)==32:
        continue
    c+=1
print(c)