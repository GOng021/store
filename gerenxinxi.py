name=input("请输入姓名：")
num=input("请输入身份证编号:")
age=input("请输入年龄：")
sex=input("请输入性别：")
height=input("请输入身高:")
address=input("请输入地址：")
info = '''
    ------------个人信息----------
    姓名:%s
    身份证编号:%s
    年龄:%s
    性别:%s
    身高:%s
    地址：%s
    -----------------------------
'''
print(info % (name,num,age,sex,height,address,))



