t=int(input())
for i in range(t):
    s=input()
    for k in s:
        if k>='0' and k<='9':
            print("Yes")
            break
    else:
        print("No")