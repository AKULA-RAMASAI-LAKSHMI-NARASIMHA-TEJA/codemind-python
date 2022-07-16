s=input()
s=s.split()
for i in range(len(s)):
    if i%2==0:
        s[i]=s[i][::-1]
print(*s)