a = input("请输入三角形的边长a:")
a = int(a)
b = input("请输入三角形的边长b:")
b = int(b)
c = input("请输入三角形的边长c:")
c = int(c)
if a+b<=c or a+c<=b or b+c<=a  or a==0 or b==0 or c==0:
    print("不能构成三角形")
elif a==b==c:
    print("等边三角形")
elif a==b or b==c or a==c:
    print("等腰三角形")
elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
    print("直角三角形")
else:
    print("普通三角形")




