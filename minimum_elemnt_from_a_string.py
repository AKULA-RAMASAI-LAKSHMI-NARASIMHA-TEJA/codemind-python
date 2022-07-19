s=input()
s=s.split()
a=list(s[-1])
a.sort()
b=a[0]
if b.lower() in a:
    print(b.lower())
else:
    print(b)