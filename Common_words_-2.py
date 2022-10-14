a=0
s1=(input().lower()).split(' ')
s2=(input().lower()).split(' ')
for i in s1:
    for j in s2:
        if i==j and s1.count(i)==1 and s2.count(j)==1:
            a+=1
print(a)