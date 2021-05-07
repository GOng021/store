import random
from DButils import update
from DButils import select
from DButils import close
# 2.银行的名称写死
bank_name = "中国工商银行的昌平支行"

# 打印欢迎页面
def welcome():
    print("---------------------------------")
    print("-     中国工商银行账户管理系统V2.0     -")
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
    sql = "select count(*)from 用户信息"
    data = select(sql,[])
    if data[0][0] >= 100:
        return 3
    # 判断是否存在
    sql1="select * from 用户信息 where account=%s"
    data=select(sql1,account)
    if len(data)!=0:
        return 2
    # 正常开户
    sql2="insert into 用户信息 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param=[account,username,password,country,province,street,door,0,bank_name]
    update(sql2,param)
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
        info="""
        ------------账户信息------------
        账号：%s
        姓名：%s
        密码：%s
        地址：
         国家：%s
         省份：%s
         街道：%s
         门牌号：%s
        账户余额：%s
        注册银行名：%s
       ------------------------------- 
        """
        print(info % (account,name,password,country,province,street,door,0,bank_name))

    elif status == 2:
          print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")
# 用户存钱逻辑
def bank_savemoney(account,money):
    sql = "select * from 用户信息 where account=%s "
    data=select(sql,account)
    if len(data) != 0:
        sql1 = "update 用户信息 set money = money + %s  where account = %s;"
        update(sql1,[money,account])
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
    sql = "select * from 用户信息 where account=%s  "
    date = select(sql,account)
    if len(date) != 0:
        sql2 = "select account from 用户信息 where mima=%s"
        date = select(sql2,password)
        if len(date) != 0:
                sql4="select money from 用户信息 where money>%s"
                date = select(sql4,getmoney)
                if len(date)!=0:
                    sql3="update 用户信息 set money = money - %s  where account = %s"
                    update(sql3, [getmoney, account])
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
        print("恭喜你，取款成功!" )
    elif money1 == 1:
        print("账号不存在！")
    elif money1 == 2:
        print("密码错误！")
    elif money1 == 3:
        print("你的钱不够！")

# 转账逻辑
def bank_transfer(outaccount,inaccount,password,outmoney):
    sql = "select * from 用户信息 where account=%s  "
    data = select(sql, outaccount)
    if len(data)!=0:
        sq2 = "select * from 用户信息 where account=%s  "
        data = select(sq2, inaccount)
        if len(data)!=0:
            sql3 = "select account from 用户信息 where account=%s and mima=%s"
            data=select(sql3, [outaccount,password])
            if len(data) != 0:
                sql4 = "select money from 用户信息 where money>%s"
                data=select(sql4, outmoney)
                if len(data)!=0:
                    sql5="update 用户信息 set money=money-%s where account = %s "
                    update(sql5, [outmoney, outaccount])
                    sql6 = "update 用户信息 set money=money+%s where account = %s "
                    update(sql6, [outmoney, inaccount])
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
        print("转账成功！成功转出")
    elif outmoney1==1:
        print("账户不存在！")
    elif outmoney1==2:
        print("密码错误！")
    elif outmoney1==3:
        print("你的钱不够！")
# 查询逻辑
def bank_inquriy(account,password):
    sql = "select * from 用户信息 where account=%s  "
    data = select(sql, account)
    if len(data) != 0:
        sql2 = "select account from 用户信息 where mima=%s"
        data = select(sql2, password)
        if len(data) != 0:
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
        sql = "select * from 用户信息 where account=%s  "
        date = select(sql, account)
        if len(date) != 0:
            print("账号：",date[0][0],
                  "账户名",date[0][1],
                  "密码：",date[0][2],
                  "居住地址：",date[0][3],date[0][4],date[0][5],date[0][6],
                  "余额：", date[0][7],
                  "当前账户开户行：",date[0][8])
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
            close()
            break
        else:
            print("输入非法！请重新输入！！！")
    else:
        print("您输入非法！请重新输入！！！")



