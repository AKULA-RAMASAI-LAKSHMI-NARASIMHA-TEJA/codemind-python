a=input()
b=input()
a=list(a)
for i in a:
    if i==b:
        print(True)
        print(a.index(i))
        break
else:
    print(False)