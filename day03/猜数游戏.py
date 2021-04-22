import random
num =random.randint(1,101)
count = 0
money = 20
while True:
    count = count + 1
    num1 = input("请输入您要输入的数:")
    num1 = int(num1)
    if num1 > num:
        print("大了,花费金币:",count*money)
    elif num1 < num:
        print("小了,花费金币:",count*money)
    else:
        print("恭喜您猜对了！！！本次中奖号码为:",num,"你本次猜了",count,"次!共花费金币:",count*money)
        break
    if  count>=7:
        print("游戏被锁定!共花费金币:",count*money)
        break


