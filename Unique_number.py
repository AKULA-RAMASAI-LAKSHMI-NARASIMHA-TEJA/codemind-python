n=input()
for i in n:
    if n.count(i)>1:
        print('Not Unique Number')
        break
else:
    print("Unique Number")