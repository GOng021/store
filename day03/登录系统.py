name="root"
password="admin"
count=0
while True:
    count=count+1
    name=input("用户名:")
    password=input("密码：")
    if name=="root" and password=="admin":
        print("登录成功！")
        break
    if password!="admin" and name=="root":
        print("输入密码错误")
    if count>=3:
        print("账户被锁定")
        break


