a=0
s1=(input().lower()).split(' ')
s2=(input().lower()).split(' ')
for i in s1:
    for j in s2:
        if i==j:
            a+=1
print(a)