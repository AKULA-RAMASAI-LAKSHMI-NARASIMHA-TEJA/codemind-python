x=0
for _ in range(int(input())):
    y=input()
    if '++' in y:
        x+=1
    elif '--' in y:
        x-=1
print(x)