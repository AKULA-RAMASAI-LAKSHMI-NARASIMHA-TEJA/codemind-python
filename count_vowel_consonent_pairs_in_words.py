s=input().split(' ')
vow=['a','e','i','o','u','A','E','I','O','U']
a=0
for i in s:
    s1=i[0:len(i)//2]
    s2=i[len(i)//2:len(i)]
    s2=s2[::-1]
    for j in range(min(len(s1),len(s2))):
        if (s1[j] in vow and s2[j] not in vow)or(s1[j] not in vow and s2[j] in vow):
            a+=1
print(a)