n=int(input())
sq=n**2
temp=sq
s=0
while sq:
    d=sq%10
    s+=d
    sq=sq//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")