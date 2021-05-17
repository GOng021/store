class people:
    __name=""
    __age=""
    __sex=""

    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age

    def sefSex(self,sex):
        self.__sex=sex
    def getSex(self):
        return self.__sex

class worker(people):

    def work(self):
        print(self.getName(),"正在干活")

class student(people):
    __account=""
    def setAccount(self,account):
        self.__account=account
    def getAccount(self):
        return self.__account

    def sing(self):
        print(self.getName(),"在唱歌")

    def study(self):
        print(self.getName(),"在学习")

a=student()
a.setName("张三")
a.sing()
a.study()

