s=input()
s=s.split()
x,y=0,0
for i in s:
    x=ord(max(i))
    y=ord(min(i))
    print(abs(x-y),end=' ')