s=input()
s=s.split(' ')
for i in s:
    a=[]
    b=list(i)
    for i in b:
        if ord(i)>=97 and ord(i)<=122:
            a.append(i)
    a.sort()
    d=0
    for j in range(0,len(b)):
        if b[j] not in a:
            print(b[j],end='')
        else:
            print(a[d],end='')
            d+=1
    print(end=' ')