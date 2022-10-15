for _ in range(int(input())):
    _=int(input())
    s=input()
    for i in s:
        if s.count(i)==1:
            print(i)
            break
    else:
        print(-1)