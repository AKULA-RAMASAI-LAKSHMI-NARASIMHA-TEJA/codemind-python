h,m=map(int,input().split(':'))
if h==12:
    h=0
if m==60:
    m=0
ha=0.5 * (h * 60 + m) 
ma=6 * m
a=abs(ha-ma)
a=min(360-a,a)
print(a)