n=int(input())
s=''
a=list(map(int,input().split()))
for i in a:
    s+=str(i)
s=int(s)
s+=1
s=str(s)
for i in s:
    print(i,end=' ')