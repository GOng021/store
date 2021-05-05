import random
# 1. 空的银行的库 ： 100个
users = {}

# 2.银行的名称写死
bank_name = "中国工商银行的昌平支行"

# 打印欢迎页面
def welcome():
    print("---------------------------------")
    print("-     中国工商银行账户管理系统V1.0     -")
    print("---------------------------------")
    print("-   1.开户                       -")
    print("-   2.存钱                       -")
    print("-   3.取钱                       -")
    print("-   4.转账                       -")
    print("-   5.查询                       -")
    print("-   6.Bye!                       -")
    print("----------------------------------")
# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door):
    # 判断是否已满
    if len(users) >= 100:
        return 3
    # 判断是否存在
    if account in users:
        return 2
    #正常开户
    users[account] = {
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "bank_name":bank_name
    }
    return 1

# 用户开户方法
def addUser():
    # 随机获取账号
    li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "q", "a", "z", "w", "s", "x", "e", "d", "c", "r", "f", "v",
          "t", "g", "b", "y", "h", "n", "u", "j", "m", "i", "k", "o", "l", "p"]
    account = ""
    for i in range(8):
        index = random.randint(0, len(li) - 1)
        account = account + li[index]
    name = input("请输入用户名：")
    password = input("请输入您的密码（6位数字）：")
    print("接下来要输入您的地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street =  input("\t输入街道：")
    door = input("\t输入门牌号：")
    # 余额不允许第一次输入，需要存钱

    status = bank_addUser(account,name,password,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！")
        info = '''
            ------------个人信息----------------
            账号：%s,
            用户名：%s,
            取款密码：%s,
            地址信息：
                国家：%s,
                省份：%s,
                街道：%s,
                门牌号：%s,
            余额：%s,
            开户行：%s
            -----------------------------------
        '''
        print(info % (account,name,password,country,province,street,door,users[account]["money"],bank_name))

    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")
# 用户存钱逻辑
def bank_savemoney(account,money):
    if account in users:
        users[account]["money"]= users[account]["money"]+int(money)
        return 1
    else:
        return False
# 存钱方法
def savemoney():
    account=input("请输入账号：")
    money=input("请输入存款金额：")
    money1=bank_savemoney(account,money)
    if money1==1:
        print("存款成功！")
    else:
        print("用户不存在！")

# 用户取钱的逻辑
def bank_getmoney(account,password,getmoney):
    if account in users:
        if password==users[account]["password"]:
            getmoney = int(getmoney)
            if users[account]["money"] >= getmoney:
                users[account]["money"] = users[account]["money"] - getmoney
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1
# 取钱方法：
def getmoney():
    account=input("请输入账号：")
    password=input("请输入密码：")
    money=input("请输入您要取的金额：")
    money1= bank_getmoney(account, password, money, )
    if money1 == 0:
        print("恭喜你，取款成功，余额为", users[account]["money"])
    elif money1 == 1:
        print("账号不存在！")
    elif money1 == 2:
        print("密码错误！")
    elif money1 == 3:
        print("你的钱不够！")

# 转账逻辑
def bank_transfer(outaccount,inaccount,password,outmoney):
    if outaccount in users:
        if inaccount in users:
            if password==users[outaccount]["password"]:
                if users[outaccount]["money"] >= int(outmoney):
                    users[outaccount]["money"]=users[outaccount]["money"]-int(outmoney)
                    users[inaccount]["money"]=users[inaccount]["money"]+int(outmoney)
                    return 0
            else:
                return 3
        else:
            return 2

    else:
        return 1
# 转账方法
def transfer():
    outaccount=input("请输入转出账户:")
    inaccount=input("请输入转入账户：")
    password=input("请输入转出账户密码：")
    outmoney=input("请输入转出金额：")
    outmoney1=bank_transfer(outaccount,inaccount,password,outmoney)
    if outmoney1==0:
        print("转账成功！成功转出",outmoney,"账户余额为",users[outaccount]["money"])
        print("到账",outmoney,"账户余额为",users[inaccount]["money"])
    elif outmoney1==1:
        print("账户不存在！")
    elif outmoney1==2:
        print("密码错误！")
    elif outmoney1==3:
        print("你的钱不够！")
# 查询逻辑
def bank_inquriy(account,password):
    if account in users:
        if password==users[account]["password"]:
            return 0
        else:
            return 2
    else:
        return 1
# 查询方法
def inquiry():
    account=input("请输入账户：")
    password=input("请输入密码：")
    account1= bank_inquriy(account,password)
    if account1==0:
        print("账号：",account,
              "密码：",password,
              "余额：",users[account]["money"],
              "居住地址：",users[account]["country"],users[account]["province"],users[account]["street"],users[account]["door"],
              "当前账户开户行：",bank_name)
    elif account1==1:
        print("账户不存在！")
    elif account1==2:
        print("密码错误！")
while True:
    welcome()
    num = input("请输入您的业务编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            addUser()
        elif num == 2:
            savemoney()
        elif num == 3:
            getmoney()
        elif num == 4:
            transfer()
        elif num == 5:
            inquiry()
        elif num == 6:
            print("欢迎下次光临！！！")
            break
        else:
            print("输入非法！请重新输入！！！")
    else:
        print("您输入非法！请重新输入！！！")



