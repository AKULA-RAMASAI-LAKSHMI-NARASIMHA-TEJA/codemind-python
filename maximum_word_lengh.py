s=input()
max=0
for i in s.split():
    if(max<len(i)):
        max=len(i)
print(max)