names=("一一","二二","三三","四四","五五","六六","七七","八八","九九","十十")
import random
while True:
    print("1:随机点名   2：随机处罚")
    num=input("请输入编号:")
    if num.isdigit():
        num=int(num)
        if num==1:
            rannum=random.randint(0,len(names)-1)
            print(names[rannum])
        elif num==2:
            a=random.randint(0,100)
            print("恭喜您！被处罚",a,"遍！")
        else:
            print("你输入的字符非法！")
    elif num=="q" or num=="Q":
        print("欢迎下次再来！")
        break
    else:
        print("你输入的字符非法！")



