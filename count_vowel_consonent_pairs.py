s=input()
vow=['a','e','i','o','u','A','E','I','O','U']
s1=s[0:len(s)//2]
s2=s[len(s)//2:len(s)]
s2=s2[::-1]
a=0
for i in range(min(len(s1),len(s2))):
    if s1[i]==' ' or s2[i]==' ':
        continue
    elif (s1[i] in vow and s2[i] not in vow)or(s1[i] not in vow and s2[i] in vow):
        a+=1
print(a)