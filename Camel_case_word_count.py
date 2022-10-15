s=input()
c=0
for i in range(1,len(s)-1):
    if ord(s[i])>64 and ord(s[i])<91:
        c+=1
print(c+1)