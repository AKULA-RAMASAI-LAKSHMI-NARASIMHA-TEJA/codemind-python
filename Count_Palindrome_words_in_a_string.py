s=input()
s=s.lower()
c=0
for i in s.split():
    if i==i[::-1]:
        c+=1
print(c)