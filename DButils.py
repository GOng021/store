import pymysql
host="localhost"
user="root"
password=""
database="中国工商银行"
# 针对增、删、改
con=pymysql.connect(host=host,user=user,password="",database=database)
cursor=con.cursor()

def update(sql,param):
    cursor.execute(sql, param)
    con.commit()
# 针对查询
def select(sql,param):
    cursor.execute(sql, param)
    con.commit()
    return cursor.fetchall()
    # 关闭
def close():
    cursor.close()
    con.close()