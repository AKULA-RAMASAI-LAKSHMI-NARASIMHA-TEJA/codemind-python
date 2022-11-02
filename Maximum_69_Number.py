num=int(input())
g=''
h=len(str(num))
d=(10**h)-1
e=d-num
f=len(str(e))
num=list(str(num))
num[-f]=9
for i in num:
    g+=str(i)
print(g)
            