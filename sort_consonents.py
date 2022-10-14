s=list(input().split(' '))
vow=['a','e','i','o','u']
for i in s:
    c=list(i)
    a=[]
    for j in c:
        if j not in vow:
            a.append(j)
    a.sort()
    d=0
    for j in range(0,len(c)):
        if c[j] in vow:
            print(c[j],end='')
        else:
            print(a[d],end='')
            d+=1
    print(end=' ')