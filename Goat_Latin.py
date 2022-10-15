s=list(input().split(' '))
v="aeiouAEIOU"
a=1
res=''
for i in s:
    if i[0] in v:
        res+=str(i)
    else:
        res+=str(i[1:len(i)])
        res+=str(i[0])
    res+='ma'
    res+=a*'a'
    if(a==len(s)):
        break
    res+=' '
    a+=1
print(res)