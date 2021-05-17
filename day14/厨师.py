class chushi:
    __name = ""
    __age = 0

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

    def make(self,guo):
        print("厨师正在用",guo,"蒸饭")

class chushi2(chushi):
    def make(self,guo):
        super().make(guo)

    def make2(self,guo2):
        print("厨师正在用",guo2,"炒菜")

class chushi3(chushi2):
    def make2(self, guo2):
        print("厨师正在用",guo2,"炒菜")
        print("年龄为",self.getAge(),"的厨师",self.getName(),"正在做饭")

a=chushi3()
a.setName("李四")
a.setAge(52)
a.make("电饭煲")
a.make2("炒锅")