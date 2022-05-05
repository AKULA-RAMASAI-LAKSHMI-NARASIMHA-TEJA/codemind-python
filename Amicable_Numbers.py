m=int(input())
n=int(input())
m1=0
for i in range(1,n):
    if n%i==0:
        m1+=i
n1=0
for j in range(1,m):
    if m%j==0:
        n1+=j
if n1==n and m1==m:
    print("Amicable")
else:
    print("Not Amicable")