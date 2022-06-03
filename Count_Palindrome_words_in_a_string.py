s=input()
s=s.lower()
c=0
for word in s.split():
    if word==word[::-1]:
        c+=1
print(c)