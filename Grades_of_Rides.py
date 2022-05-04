hurl,spin,speed=map(int,input().split(' '))
if(hurl>50 and spin>60 and speed>100):
    print("10")
elif hurl>50 and spin>60 :
    print("9")
elif spin>60 and speed>100 :
    print("8")
elif hurl>50 and speed>100 :
    print("7")
elif hurl>50 or spin>60 or speed>100 :
    print("6")
else:
    print("5")