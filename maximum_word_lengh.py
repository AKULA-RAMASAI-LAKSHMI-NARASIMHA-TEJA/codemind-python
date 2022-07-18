s=input()
s=s.split()
a=[]
for i in s:
    a.append(len(i))
print(max(a))