f1=open(file="呸.jpg",mode="rb")
f2=open(file="E:\python1\呸.jpg",mode="wb")
data=f1.readline()
f2.write(data)

f2.close()
f1.close()