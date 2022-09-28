s=input()
s=s.split(' ')
v=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in s:
    a=i[0:len(i)//2]
    b=i[len(i)//2:len(i)]
    b=b[::-1]
    for j in range(min(len(a),len(b))):
        if(a[j] in v and b[j] not in v) or (a[j] not in v and b[j] in v):
            c+=1
print(c)