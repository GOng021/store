import time
class oldphone:
    __color = ""
    __brand = ""

    def setColor(self,color):
        self.__color = color
    def getColor(self):
        return self.__color

    def setbrand(self,brand):
        self.__brand = brand
    def getbrand(self):
        return self.__brand

    def call(self,callnum):
        print(self.__brand,"正在给",callnum,"打电话！")
        for i in range(3):
            time.sleep(1)
            print(".",end="")


class newphpne(oldphone):
    def call(self,callnum):
        super().call(callnum)
        print("语音拨号中")
        for i in range(3):
            time.sleep(1)
            print(".",end="")
        print("品牌为：",self.getbrand(), "的手机很好用")

a = newphpne()
a.setbrand("诺基亚")
a.call(1258963)
