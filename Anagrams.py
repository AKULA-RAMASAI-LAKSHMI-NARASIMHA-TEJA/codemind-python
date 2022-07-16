a=input()
b=input()
a,b=a.lower(),b.lower()
a,b=list(a),list(b)
c=0
if len(a)==len(b):
    for i in a:
        if i in b:
            c+=1
    if c==len(a):
        print('True')
    else:
        print('False')
else:
    print('False')