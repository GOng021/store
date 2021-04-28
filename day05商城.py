shop=[
    ["螺蛳粉",80],
    ["猕猴桃",60],
    ["榴莲",200],
    ["超大芒果",222],
    ["《莲》",1388],
    ["张艺兴签名",888],
    ["辣条",100],
    ["火鸡面",15],
    ["彩虹糖",99],
    ["iPhone",5000],
    ["星黛露家族",1999],
    ["lenovo 电脑",5000]
]
a=()
panduan=()
mycart=[]
dicount1=[]
d="恭喜获得辣条半折优惠券"
e="恭喜获得电脑半折优惠券"

zonghuafei=[]
import random
dicount=random.randint(1,2)
if dicount==1:
    print(d)
    dicount1.append(d)
else:
    print(e)
    dicount1.append(e)
salary = int(input("请输入您的薪资："))
panduan=input("是否使用优惠券:")
if panduan=="是":
        while True:
            for index, value in enumerate(shop):
                print(index, " ", value)
            num = input("请输入您要买的商品编号：")
            if num.isdigit():
                num = int(num)
                if num > len(shop) - 1:
                    print("商品不存在！请重新输入！")
                elif  num==6:
                    if d in dicount1:
                        mycart.append(shop[num])
                        salary = int(salary - (shop[num][1] * 0.5))
                        print("辣条",shop[num][1] * 0.5)
                        zonghuafei.append(shop[num][1] * 0.5)
                        print("成功添加到购物车！！余额为：", salary)
                    else:
                        mycart.append(shop[num])
                        salary = int(salary - (shop[num][1] ))
                        print("辣条", shop[num][1])
                        zonghuafei.append(shop[num][1])
                        print("成功添加到购物车！！余额为：", salary)
                elif num==11:
                        if e in dicount1:
                            mycart.append(shop[num])
                            salary = salary - (shop[num][1] * 0.5)
                            print("电脑",shop[num][1] * 0.5)
                            zonghuafei.append(shop[num][1] * 0.5)
                            print("成功添加到购物车！！余额为：", salary)
                        else:
                            mycart.append(shop[num])
                            salary = salary - (shop[num][1])
                            print("电脑", shop[num][1])
                            zonghuafei.append(shop[num][1])
                            print("成功添加到购物车！！余额为：", salary)
                else:
                    if salary >= shop[num][1]:
                        mycart.append(shop[num])
                        salary = salary - shop[num][1]
                        zonghuafei.append(shop[num][1])
                        print("成功添加到购物车！！余额为：", salary)
                    else:
                        print("您的余额不足！")
            elif num == "Q" or num == "q":
                print("---------欢迎下次再来---------")
                break
            else:
                print("输入非法！请重新输入！！")
elif panduan=="否":
    while True:
        for index, value in enumerate(shop):
            print(index, " ", value)
        num = input("请输入您要买的商品编号：")
        if num.isdigit():
            num = int(num)
            if num <= len(shop) - 1:

                if salary >= shop[num][1]:
                    mycart.append(shop[num])
                    print(mycart)
                    salary = salary - shop[num][1]
                    zonghuafei.append(shop[num][1])
                    print("成功添加到购物车！！余额为：", salary)

                else:
                    print("您的余额不足！")
            else:
                print("商品不存在！请重新输入！")
        elif num == "Q" or num == "q":
            print("---------欢迎下次再来---------")
            break
else:
    print("输入非法字符，请重新输入")
print("您本次购物商品如下：")
for index,value in enumerate(mycart):
        print(index," ",value)
print("您的余额为：",salary)
print("本次积分：",sum(zonghuafei)//10)
print("总花费：",sum(zonghuafei))




