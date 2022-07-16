s=input()
s=s.lower()
s=s.split()
c=0
a=['a','e','i','o','u']
for i in s:
    if i[0] in a and i[-1] not in a:
        c+=1
print(c)