n=input()
a=list(map(int,input().split()))
sum=0
for i in a:
    if i**0.5==int(i**0.5):
        sum+=i
print(sum)