s=list(input().split(' '))
for i in s:
    c=list(i)
    a=[]
    for j in c:
        if ord(j)>=97 and ord(j)<=122:
            a.append(j)
    a.sort()
    d=0
    for j in range(0,len(c)):
        if c[j] not in a:
            print(c[j],end='')
        else:
            print(a[d],end='')
            d+=1
    print(end=' ')