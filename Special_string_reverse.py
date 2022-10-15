v=input()
r,re=[],[]
for k in range(0,len(v)):
    if((ord(v[k])>32 and ord(v[k])<=47)or(ord(v[k])>=58 and ord(v[k])<=64)or(ord(v[k])>=91 and ord(v[k])<=96)or(ord(v[k])>=123 and ord(v[k])<=126)or(v[k]>='0' and v[k]<='9')):
        r.append(k)
    else:
        re.append(v[k])
re=re[::-1]
vk,a='',0
for i in range(len(v)):
    if i not in r:
        vk+=re[a]
        a+=1
        continue
    vk+=v[i]
print(*vk,sep='')