s=input()
s=s.lower()
s=list(s)
a=['a','e','i','o','u']
b=0
for i in s:
    if i in a:
        b+=1
print(b)