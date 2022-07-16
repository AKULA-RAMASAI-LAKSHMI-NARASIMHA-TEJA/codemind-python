s=input()
s=s.split()
for i in range(len(s)):
    s[i]=s[i][::-1]
s=s[::-1]
print(*s)