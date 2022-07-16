s=input()
s=list(s)
for i in s:
    if i==' ':
        s.remove(i)
print(min(s),s.count(min(s)),end=' ')
print(max(s),s.count(max(s)),end=' ')