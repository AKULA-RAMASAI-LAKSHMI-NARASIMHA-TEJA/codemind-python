n=int(input())
s=0
sq=n*n
while sq:
    d=sq%10
    s+=d
    sq//=10
if s==n:
    print('Neon Number')
else:
    print("Not Neon Number")