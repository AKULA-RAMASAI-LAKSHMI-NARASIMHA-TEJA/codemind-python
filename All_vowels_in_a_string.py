s=input()
a=['a','e','i','o','u']
c=0
for i in a:
    if i in s:
        c+=1
if c==5:
    print('True')
else:
    print('False')