li=[1,5,21,30,15,9,30,24]
i=0
list=[]
while i<len(li):
    if li[i]%5==0:
        list.append(li[i])
    i=i+1
print(sum(list))