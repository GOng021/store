list = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
lis=set(list)
for i in lis:
    b=list.count(i)
    print("数字",i,"出现了：",b,"次")