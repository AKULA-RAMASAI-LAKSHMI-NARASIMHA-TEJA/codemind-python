v="aeiou"
s=list(input().lower())
a=b=0
for i in range(len(s)):
    if s[i] in v:
        b=0
        for j in range(i,len(s)):
            if s[j] in v:
                b+=1
            else:
                break
    if(a<=b):
        a=b
print(a)