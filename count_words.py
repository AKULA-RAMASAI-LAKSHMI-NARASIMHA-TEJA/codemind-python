s=input()
s=s.lower()
s=s.split()
s=list(s)
a='aeiou'
c=0
for i in s:
    if i[0] in a:
        if i[len(i)-1] not in a:
            c+=1
print(c)