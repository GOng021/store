import pymysql
con=pymysql.connect(host="localhost",user="root",password="",database="资产")
cursor=con.cursor()
users=[]
f=open(file="资产.txt",mode="r+",encoding="utf8")
num=f.readlines()

for i in num:
    user=i.replace("\n","").split(",")
    users.append(user)
for k in users:
    sql="insert into 个人资产 values(%s,%s,%s) "
    param = [k[0],k[1],k[2]]
    cursor.execute(sql,param)
    con.commit()
sql2="select sum(money) from 个人资产"
cursor.execute(sql2)
data=cursor.fetchall()
print("总资产为：",data[0])
cursor.close()
con.close()



