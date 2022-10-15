def sub(b,o,a):
    for a in range(a+1,len(o)):
            b.append(o[a])
def arrange(b,e,o):
    m=min(len(e),len(o))
    for i in range(m):
        b.append(e[i])
        b.append(o[i])
        a=i
    if(len(o)>len(e)):
        sub(b,o,a)
    else:
        sub(b,e,a)
s=input()
c=0
e,o=[],[]
for i in range(0,len(s)):
    if((ord(s[i])>32 and ord(s[i])<=47)or(ord(s[i])>=58 and ord(s[i])<=64)or(ord(s[i])>=91 and ord(s[i])<=96)or(ord(s[i])>=123 and ord(s[i])<=126)):
        c+=1
    if(s[i]>='0' and s[i]<='9'):
        if int(s[i])%2==0:
            e.append(s[i])
        else:
            o.append(s[i])
b=[]
if c%2==0:
   arrange(b,e,o)
else:
    arrange(b,o,e)
print(*b,sep='')