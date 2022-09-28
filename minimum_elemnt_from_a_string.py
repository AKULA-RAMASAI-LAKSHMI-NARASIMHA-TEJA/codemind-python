s=input()
s=s.split(' ')
a=s[-1]
b=min(a)
if b.lower() in a:
    print(b.lower())
else:
    print(b)