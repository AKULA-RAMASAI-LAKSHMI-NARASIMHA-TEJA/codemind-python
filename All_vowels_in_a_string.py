s=input()
s=list(s)
a=['a','e','i','o','u']
for i in a:
    if i in s:
        continue
    else:
        print('False')
        break
else:
    print('True')