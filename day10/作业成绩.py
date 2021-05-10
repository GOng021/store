
f=open(file="scores.txt",mode="r+",encoding="utf-8")
f1=open(file="sumscores.txt",mode="w+",encoding="utf-8")
sum=f.readlines()
for i in sum:
    a=i.replace("\n","").split(",")
    print(a)
    f1.write(a[0])
    del a[0]
    num=0
    for i in a:
        i=int(i)
        num=num+i
    f1.write(str(num))
f1.close()
f.close()












