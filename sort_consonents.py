s=list(input().split(' '))
v=['a','e','i','o','u']
for i in s:
    x=list(i)
    arr=[]
    for j in x:
        if j not in v:
            arr.append(j)
    arr.sort()
    d=0
    for k in range(0,len(x)):
        if x[k] in v:
            print(x[k],end='')
        else:
            print(arr[d],end='')
            d+=1
    print(end=' ')